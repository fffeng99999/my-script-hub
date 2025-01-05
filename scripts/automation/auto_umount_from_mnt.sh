#!/bin/bash

# 自动卸载块设备并清理挂载配置的脚本
set -e

# 提示用户输入块设备名称
read -p "请输入块设备名称（如 mmcblk1p1）： " blk_name

# 检查挂载点是否存在
mnt_dir="/mnt/$blk_name"
if ! mount | grep -q "$mnt_dir"; then
    echo "警告：挂载点 $mnt_dir 未找到或未挂载。"
else
    # 卸载设备
    echo "正在卸载 /mnt/$blk_name..."
    sudo umount "$mnt_dir" || { echo "错误：卸载失败，请检查挂载状态！"; exit 1; }
    echo "成功卸载 $mnt_dir"
fi

# 检查 /etc/fstab 是否存在该设备的配置
uuid=$(blkid -s UUID -o value "/dev/$blk_name" 2>/dev/null)
if [ -n "$uuid" ]; then
    if grep -q "$uuid" /etc/fstab; then
        echo "从 /etc/fstab 中移除 UUID=$uuid 的挂载配置..."
        sudo sed -i "\|UUID=$uuid|d" /etc/fstab
        echo "成功移除 /etc/fstab 中的挂载配置。"
    else
        echo "未在 /etc/fstab 中找到 UUID=$uuid 的挂载配置，无需移除。"
    fi
else
    echo "警告：未能获取 /dev/$blk_name 的 UUID，跳过 /etc/fstab 清理。"
fi

# 删除挂载点目录
if [ -d "$mnt_dir" ]; then
    echo "正在删除挂载点目录 $mnt_dir..."
    sudo rmdir "$mnt_dir" || { echo "警告：删除挂载点目录失败，可能目录不为空。"; }
    echo "挂载点目录已删除。"
else
    echo "挂载点目录 $mnt_dir 不存在，无需删除。"
fi

echo "卸载和清理操作已完成！"

