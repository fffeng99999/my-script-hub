在 **Ubuntu 22.04 (ub22)** 中将 SMB（即 Windows 共享）挂载到本地目录，你可以通过以下步骤完成：

---

## ✅ 一、安装挂载所需工具

```bash
sudo apt update
sudo apt install cifs-utils -y
```
---

## ✅ 二、创建本地挂载点

```bash
sudo mkdir -p /mnt/smb_share
```
你可以自定义目录，比如 `/mnt/share_docs`、`/home/yourname/share` 等。

---

## ✅ 三、挂载 SMB 共享目录（命令行方式）

### 方式 1：使用明文用户名和密码

```bash
sudo mount -t cifs //192.168.1.100/shared_folder /mnt/smb_share \   -o username=your_username,password=your_password,uid=$(id -u),gid=$(id -g),iocharset=utf8
```
### 参数说明：

- `//192.168.1.100/shared_folder`：SMB 服务端的 IP 和共享目录名。
    
- `your_username`：访问共享时用的用户名。
    
- `your_password`：访问共享时的密码（注意明文风险）。
    
- `uid=$(id -u)` & `gid=$(id -g)`：挂载的文件归属当前用户。
    
- `iocharset=utf8`：支持中文文件名。
    

---

## ✅ 四、使用认证文件避免明文密码（推荐）


1. 创建一个认证文件：
```bash
sudo nano /etc/smb-credentials
```

内容如下：
```ini
username=your_username
password=your_password
```

2. 设置权限：
```bash
sudo chmod 600 /etc/smb-credentials
```

3. 使用认证文件挂载：
```bash
sudo mount -t cifs //192.168.1.100/shared_folder /mnt/smb_share -o credentials=/etc/smb-credentials,uid=$(id -u),gid=$(id -g),iocharset=utf8
```

> 换行输入加入反斜杠
```bash
sudo mount -t cifs //192.168.58.124/douyin /mnt/smb_share \
  -o credentials=/etc/smb-credentials,uid=$(id -u),gid=$(id -g),iocharset=utf8

```
---

## ✅ 五、自动挂载（写入 `/etc/fstab`）

编辑：

```bash
sudo nano /etc/fstab
```

添加这一行：
```ini
//192.168.1.100/shared_folder /mnt/smb_share cifs credentials=/etc/smb-credentials,uid=1000,gid=1000,iocharset=utf8 0 0
```

然后挂载测试：
```bash
sudo mount -a
```
---

## ✅ 六、卸载 SMB 挂载

```bash
sudo umount /mnt/smb_share
```
---

## 🔍 常见问题排查

|问题|解决方式|
|---|---|
|`mount error(13): Permission denied`|用户名密码错误、权限不足|
|中文乱码|加上 `iocharset=utf8` 选项|
|无法访问共享|确保 SMB 服务开启、防火墙放行端口（445）|
