#!/bin/bash

# 自动挂载块设备到 /mnt/<块名称> 的脚本
set -e

# 提示用户输入块设备名称
read -p "请输入块设备名称（如 mmcblk1p1）： " blk_name

# 检查块设备是否存在
if [ ! -b "/dev/$blk_name" ]; then
    echo "错误：块设备 /dev/$blk_name 不存在，请检查后重试！"
    exit 1
fi

# 获取块设备的 UUID
uuid=$(blkid -s UUID -o value "/dev/$blk_name")
if [ -z "$uuid" ]; then
    echo "错误：无法获取 /dev/$blk_name 的 UUID，请检查设备或文件系统！"
    exit 1
fi

# 创建挂载点目录
mnt_dir="/mnt/$blk_name"
if [ ! -d "$mnt_dir" ]; then
    echo "创建挂载点目录：$mnt_dir"
    sudo mkdir -p "$mnt_dir"
fi

# 检查 /etc/fstab 是否已存在该 UUID 的挂载配置
if grep -q "$uuid" /etc/fstab; then
    echo "警告：UUID=$uuid 已存在于 /etc/fstab，跳过配置。"
else
    # 添加挂载配置到 /etc/fstab
    echo "添加挂载配置到 /etc/fstab"
    echo "UUID=$uuid $mnt_dir ext4 defaults 0 2" | sudo tee -a /etc/fstab
fi

# 测试挂载
echo "测试挂载配置..."
sudo mount -a

# 验证挂载是否成功
if mount | grep -q "$mnt_dir"; then
    echo "成功挂载 /dev/$blk_name 到 $mnt_dir"
    echo "挂载配置已完成！"
else
    echo "错误：挂载失败，请检查配置！"
    exit 1
fi

