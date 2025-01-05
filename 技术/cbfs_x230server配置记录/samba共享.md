samba安装目录：
**samba由包管理器apt进行安装，安装位置为默认位置** 

安装命令：
```bash
sudo apt install samba
```

samba配置文件路劲：
```bash
/etc/samba/smb.conf
```

smb.conf文件内容：
```bash
# 省略默认内容

# 添加共享目录
[calibre_data]
   comment = Calibre Data
   path = /mnt/sda1/calibre_data
   browsable = yes
   guest ok = yes
   read only = no
   create mask = 0755
```

