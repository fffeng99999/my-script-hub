```bash
sudo visudo

# sudo nano(vim) /etv/sudoers
```

进入编辑状态后，在**文件最后面**（划重点：一定是在文件最后面）添加以下内容：
```bash
username ALL = (ALL) NOPASSWD: ALL
```
这里的username就是自己的用户名。

😊