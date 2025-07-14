在 `/etc/fstab` 中删除了系统磁盘（通常是挂载到 `/` 的根分区）那一行，系统启动时就无法自动挂载根文件系统，通常会掉到 **emergency mode（急救模式）**。

你现在处于急救模式，还可以修复。请跟着以下步骤操作：

---

### 🚑 修复步骤（在 emergency shell 里执行）：

#### 1. **重新挂载根目录为读写模式**

```bash
mount -o remount,rw /
```

#### 2. **用文本编辑器（如 `vi` 或 `nano`）打开 fstab**

```bash
vi /etc/fstab
```

或（如果你不熟悉 `vi`）：

```bash
nano /etc/fstab
```

#### 3. **添加回根分区的挂载项**

你需要知道根分区的设备名，比如是 `/dev/sda2`、UUID 或者 LVM 名称。可以用如下命令查看：

```bash
lsblk -f
```

你会看到类似这样：

```
NAME   FSTYPE LABEL UUID                                 MOUNTPOINT
sda
├─sda1 ext4         1234abcd-...                         /boot
└─sda2 ext4         abcd1234-...                         /
```

> 假设 `/dev/sda2` 是你的根分区，UUID 是 `abcd1234-...`

那么在 `/etc/fstab` 中添加如下这一行（示例）：

```fstab
UUID=abcd1234-...   /   ext4    defaults   0 1
```

或（如果你不用 UUID）：

```fstab
/dev/sda2   /   ext4    defaults   0 1
```

✅ 注意保持列之间是 **Tab** 或空格，不能乱。

#### 4. **保存并退出**

在 `vi` 中：

- 按 `ESC`
    
- 输入 `:wq` 然后回车
    

在 `nano` 中：

- 按 `Ctrl+O` 保存
    
- 按 `Ctrl+X` 退出
    

---

### 🔁 5. 重启系统

```bash
reboot
```

---

### 🧠 提示

- 最好用 `UUID`，而不是 `/dev/sdaX`，因为设备号有时会变。
    
- 如果你不知道原来那行内容，可以尝试恢复 `/etc/fstab` 的备份：
    

```bash
ls /etc/fstab*
```

如果有 `fstab.bak` 或 `fstab~`，可以用它还原：

```bash
cp /etc/fstab.bak /etc/fstab
```

---

需要帮你根据 `lsblk` 或 `blkid` 输出写回去那行的话，也可以贴出来我帮你写。