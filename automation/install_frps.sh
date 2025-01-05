#!/bin/bash

# 脚本开始
set -e

echo "全自动安装 frps 开始..."

# 检查是否具有 root 权限
if [ "$(id -u)" -ne 0 ]; then
  echo "请使用 root 权限运行该脚本。"
  exit 1
fi

# 定义变量
BIN_DIR="/usr/bin"
CONFIG_DIR="/etc/frps"
CONFIG_FILE="${CONFIG_DIR}/frps.toml"
SYSTEMD_FILE="/etc/systemd/system/frps.service"
TOKEN="cyberfeng"
LATEST_RELEASE_URL="https://api.github.com/repos/fatedier/frp/releases/latest"

# 获取最新版本号
echo "获取 frps 最新版本信息..."
FRP_VERSION=$(curl -s ${LATEST_RELEASE_URL} | grep '"tag_name":' | sed -E 's/.*"v([0-9.]+)".*/\1/')

if [ -z "$FRP_VERSION" ]; then
  echo "无法获取最新版本信息，请检查网络连接或 GitHub API。"
  exit 1
fi

FRP_TAR="frp_${FRP_VERSION}_linux_amd64.tar.gz"
DOWNLOAD_URL="https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/${FRP_TAR}"

echo "最新版本为 frps ${FRP_VERSION}，准备下载..."

# 安装依赖
echo "安装必要的依赖..."
apt update -y && apt install -y wget tar curl

# 下载并解压 frps
DOWNLOAD_PATH="/tmp/${FRP_TAR}"

if [ -f "$DOWNLOAD_PATH" ]; then
  echo "发现已存在的文件 $DOWNLOAD_PATH，正在删除..."
  rm -f "$DOWNLOAD_PATH"
fi

echo "下载 frps..."
wget --show-progress -O "$DOWNLOAD_PATH" "$DOWNLOAD_URL"

# 验证文件完整性
echo "下载完成，验证文件完整性..."
if ! tar -tzf "$DOWNLOAD_PATH" >/dev/null 2>&1; then
  echo "文件解压失败，可能已损坏。请检查网络连接或 GitHub 资源。"
  exit 1
fi

echo "解压 frps..."
mkdir -p /tmp/frps_install
tar -xzf "$DOWNLOAD_PATH" -C /tmp/frps_install --strip-components=1

# 移动文件到指定目录
echo "复制 frps 可执行文件到 ${BIN_DIR}..."
cp /tmp/frps_install/frps ${BIN_DIR}/frps

echo "创建配置目录 ${CONFIG_DIR}..."
mkdir -p ${CONFIG_DIR}

# 配置 frps.toml
echo "生成 frps 配置文件 (TOML 格式)..."
cat > ${CONFIG_FILE} <<EOF
[common]
bind_port = 7000
token = "${TOKEN}"

# Web 管理页面配置
dashboard_port = 7500
dashboard_user = "admin"
dashboard_pwd = "admin"
EOF

# 设置 systemd 服务
echo "创建 frps systemd 服务文件..."
cat > ${SYSTEMD_FILE} <<EOF
[Unit]
Description=Frp Server Service
After=network.target

[Service]
Type=simple
ExecStart=${BIN_DIR}/frps -c ${CONFIG_FILE}
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

# 设置权限并启用服务
echo "设置权限并启用 frps 服务..."
chmod 644 ${SYSTEMD_FILE}
systemctl daemon-reload
systemctl enable frps
systemctl start frps

# 检查服务状态
echo "检查 frps 服务状态..."
systemctl status frps --no-pager

echo "frps 安装完成！"
echo "版本：${FRP_VERSION}"
echo "默认端口：7000"
echo "Web 管理页面：7500"
echo "Web 管理页面用户名：admin"
echo "Web 管理页面密码：admin"
echo "Token：${TOKEN}"
echo "配置文件路径：${CONFIG_FILE}"
