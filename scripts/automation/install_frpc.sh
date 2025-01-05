#!/bin/bash

# 脚本开始
set -e

echo "全自动安装 frpc 开始..."

# 检查是否具有 root 权限
if [ "$(id -u)" -ne 0 ]; then
  echo "请使用 root 权限运行该脚本。"
  exit 1
fi

# 定义变量
BIN_DIR="/usr/bin"
CONFIG_DIR="/etc/frpc"
CONFIG_FILE="${CONFIG_DIR}/frpc.toml"
SYSTEMD_FILE="/etc/systemd/system/frpc.service"
LATEST_RELEASE_URL="https://api.github.com/repos/fatedier/frp/releases/latest"
TOKEN="cyberfeng"  # 默认 token

# 获取当前设备的架构
ARCHITECTURE=$(uname -m)

# 根据架构选择合适的版本
case $ARCHITECTURE in
  "x86_64")
    FRP_ARCH="amd64"
    ;;
  "aarch64"|"arm64")
    FRP_ARCH="arm64"
    ;;
  "armv7l"|"armv6l")
    FRP_ARCH="arm"
    ;;
  *)
    echo "不支持的架构：$ARCHITECTURE"
    exit 1
    ;;
esac

# 获取最新版本号
echo "获取 frpc 最新版本信息..."
FRP_VERSION=$(curl -s ${LATEST_RELEASE_URL} | grep '"tag_name":' | sed -E 's/.*"v([0-9.]+)".*/\1/')

if [ -z "$FRP_VERSION" ]; then
  echo "无法获取最新版本信息，请检查网络连接或 GitHub API。"
  exit 1
fi

FRP_TAR="frp_${FRP_VERSION}_linux_${FRP_ARCH}.tar.gz"
DOWNLOAD_URL="https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/${FRP_TAR}"

echo "最新版本为 frpc ${FRP_VERSION}，准备下载 ${FRP_ARCH} 架构的版本..."

# 安装依赖
echo "安装必要的依赖..."
apt update -y && apt install -y wget tar curl

# 下载并解压 frpc
DOWNLOAD_PATH="/tmp/${FRP_TAR}"

if [ -f "$DOWNLOAD_PATH" ]; then
  echo "发现已存在的文件 $DOWNLOAD_PATH，正在删除..."
  rm -f "$DOWNLOAD_PATH"
fi

echo "下载 frpc..."
wget --show-progress -O "$DOWNLOAD_PATH" "$DOWNLOAD_URL"

# 验证文件完整性
echo "下载完成，验证文件完整性..."
if ! tar -tzf "$DOWNLOAD_PATH" >/dev/null 2>&1; then
  echo "文件解压失败，可能已损坏。请检查网络连接或 GitHub 资源。"
  exit 1
fi

echo "解压 frpc..."
mkdir -p /tmp/frpc_install
tar -xzf "$DOWNLOAD_PATH" -C /tmp/frpc_install --strip-components=1

# 移动文件到指定目录
echo "复制 frpc 可执行文件到 ${BIN_DIR}..."
cp /tmp/frpc_install/frpc ${BIN_DIR}/frpc

echo "创建配置目录 ${CONFIG_DIR}..."
mkdir -p ${CONFIG_DIR}

# 手动输入参数
echo "请输入 frps服务器 的 IP 地址:"
read FRPS_IP
echo "请输入 frps服务器 的端口 (如 7000):"
read FRPS_PORT
echo "请输入 frps服务器 的 token (如 token):"
read TOKEN
echo "请输入远程服务器用户名 (如 root):"
read USERNAME
echo "请输入 frpc客户端网页端口:"
read FRPC_PORT
# echo "请输入主机的名称 (如 my-server):"
# read CONFIG_NAME
echo "请输入 SSH 远程端口号 (例如 6000):"
read REMOTE_PORT
echo "请输入 Web 服务的远程端口号 (例如 7501):"
read REMOTE_WEB_PORT

# 询问是否加密和是否压缩
echo "是否启用加密? (true/false):"
read ENCRYPTION
echo "是否启用压缩? (true/false):"
read COMPRESSION

# 配置 frpc.toml
echo "生成 frpc 配置文件 (${CONFIG_FILE})..."
cat > ${CONFIG_FILE} <<EOF
# frpc.toml
serverAddr = "${FRPS_IP}"
serverPort = ${FRPS_PORT}
auth.method = "token"
auth.token = "${TOKEN}"
user = "${USERNAME}"

webServer.addr = "127.0.0.1"
webServer.port = ${FRPC_PORT}
webServer.user = "admin"
webServer.password = "admin"

[[proxies]]
name = "ssh"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = ${REMOTE_PORT}
transport.useEncryption = ${ENCRYPTION}
transport.useCompression = ${COMPRESSION}

[[proxies]]
name = "dashboard"
type = "tcp"
localIP = "127.0.0.1"
localPort = ${FRPC_PORT}
remotePort = ${REMOTE_WEB_PORT}
EOF

# 设置 systemd 服务
echo "创建 frpc systemd 服务文件..."
cat > ${SYSTEMD_FILE} <<EOF
[Unit]
Description=Frp Client Service
After=network.target

[Service]
Type=simple
ExecStart=${BIN_DIR}/frpc -c ${CONFIG_FILE}
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

# 设置权限并启用服务
echo "设置权限并启用 frpc 服务..."
chmod 644 ${SYSTEMD_FILE}
systemctl daemon-reload
systemctl enable frpc
systemctl start frpc

# 检查服务状态
echo "检查 frpc 服务状态..."
systemctl status frpc --no-pager

echo "frpc 安装完成！"
echo "版本：${FRP_VERSION}"
echo "frps 地址：${FRPS_IP}"
echo "配置名称：${CONFIG_NAME}-ssh"
echo "远程服务器：${REMOTE_ADDRESS}"
echo "SSH 隧道远程端口：${REMOTE_PORT}"
echo "Web 管理页面远程端口：${REMOTE_WEB_PORT}"
echo "Web 管理页面名称：${DASHBOARD_NAME}"
echo "远程服务器用户名：${USERNAME}"
echo "加密：${ENCRYPTION}"
echo "压缩：${COMPRESSION}"
echo "配置文件路径：${CONFIG_FILE}"

