#!/bin/bash

# 替换目标路径
OLD_PATH="/usr/local/cuda"
NEW_PATH="/usr/local/cuda-11.6"

# 查找所有 Makefile
echo "🔍 正在查找 Makefile 中的 CUDA 路径..."

find . -type f -name Makefile | while read file; do
    if grep -q "$OLD_PATH" "$file"; then
        echo "🛠️  修改: $file"
        sed -i.bak "s|$OLD_PATH|$NEW_PATH|g" "$file"
    fi
done

echo "✅ 所有路径已修改完成（已自动备份为 .bak 文件）"
