在 Ubuntu 22.04 上，将用户名和主机名都修改为 hxh 需要几个步骤。以下是通过命令行完成此任务的方法：

⚠️ 注意事项：
修改用户名可能会影响系统登录和权限，建议提前备份重要数据。

最好使用 root 或 sudo 权限执行以下命令。

不要在当前会话中直接将正在使用的用户名改成新的用户名，可以通过其他用户或 root 来执行。

一、修改主机名为 hxh  
步骤：

```bash
sudo hostnamectl set-hostname hxh
```

还建议将 /etc/hosts 中的旧主机名替换为新主机名：

```bash
sudo sed -i "s/$(hostname)/hxh/g" /etc/hosts
```

二、修改用户名为 hxh  
假设当前用户名是 olduser，你可以按如下步骤修改：

创建一个临时管理员账号（可选但推荐）：

```bash
sudo adduser tempadmin
sudo usermod -aG sudo tempadmin
```

然后 注销并以 tempadmin 登录。

修改用户名和主目录：

```bash
sudo usermod -l hxh olduser             # 修改用户名
sudo usermod -d /home/hxh -m hxh        # 修改主目录
sudo groupmod -n hxh olduser            # 修改用户组名
```

检查是否成功：

```bash
id hxh
```

删除临时管理员账号（可选）：

```bash
sudo deluser tempadmin
sudo rm -r /home/tempadmin
```

三、重启系统：

```bash
sudo reboot
```

✅ 修改后效果：

用户名：hxh  
主目录：/home/hxh  
主机名：hxh
