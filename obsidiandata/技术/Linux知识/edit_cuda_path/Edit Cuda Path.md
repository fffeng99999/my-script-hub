### Find Cuda Path
![[find_cuda_path.sh]]

```bash
#!/bin/bash

grep -r "cuda/bin/nvcc" Samples/ Common/

# 备用命令
grep -r "CUDA_PATH" .
```


![[edit_cuda_path.sh]]

```bash
#!/bin/bash

  
# 替换目标路径
OLD_PATH="/usr/local/cuda"
NEW_PATH="/usr/local/cuda-11.6"

# 查找所有 Makefile

echo "🔍 正在查找 Makefile 中的 CUDA 路径..."

find . -type f -name Makefile | while read file; do

    if grep -q "$OLD_PATH" "$file"; then

        echo "🛠️  修改: $file"

        sed -i.bak "s|$OLD_PATH|$NEW_PATH|g" "$file"

    fi

done

echo "✅ 所有路径已修改完成（已自动备份为 .bak 文件）"


# 还原函数

# find . -name "*.bak" | while read f; do

#     mv "$f" "${f%.bak}"

# done
```


![[restore_function.txt]]

```txt
find . -name "*.bak" | while read f; do
    mv "$f" "${f%.bak}"
done

```