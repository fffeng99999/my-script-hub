
aria2安装目录：
**aria2由包管理器apt进行安装，安装位置为默认位置** 

安装命令：
```bash
sudo apt install aria2
```

aria2配置文件路劲：
```bash
/etc/aria2/aria2.conf
/etc/aria2/aria2.session
```
aria2.conf文件内容：
```conf
##===================================##

## 文件保存相关 ##

##===================================##

# 文件保存目录

dir=/home/userf/Downloads

# 启用磁盘缓存, 0为禁用缓存, 需1.16以上版本, 默认:16M

disk-cache=16M

# 断点续传

continue=true

#日志保存

log=aria2.log

# 文件预分配方式, 能有效降低磁盘碎片, 默认:prealloc

# 预分配所需时间: none < falloc ? trunc < prealloc

# falloc和trunc则需要文件系统和内核支持

# NTFS建议使用falloc, EXT3/4建议trunc, MAC 下需要注释此项

file-allocation=prealloc

##===================================##

## 下载连接相关 ##

##===================================##

# 最大同时下载任务数, 运行时可修改, 默认:5

max-concurrent-downloads=100

# 同一服务器连接数, 添加时可指定, 默认:1

# 官方的aria2最高设置为16, 如果需要设置任意数值请重新编译aria2

max-connection-per-server=16

# 整体下载速度限制, 运行时可修改, 默认:0（不限制）

max-overall-download-limit=0

# 单个任务下载速度限制, 默认:0（不限制）

max-download-limit=0

# 整体上传速度限制, 运行时可修改, 默认:0（不限制）

max-overall-upload-limit=0

# 单个任务上传速度限制, 默认:0（不限制）

max-upload-limit=0

# 禁用IPv6, 默认:false

disable-ipv6=false

# 最小文件分片大小, 添加时可指定, 取值范围1M -1024M, 默认:20M

# 假定size=10M, 文件为20MiB 则使用两个来源下载; 文件为15MiB 则使用一个来源下载

min-split-size=10M

# 单个任务最大线程数, 添加时可指定, 默认:5

# 建议同max-connection-per-server设置为相同值

split=16

##===================================##

## 进度保存相关 ##

##===================================##

# 从会话文件中读取下载任务

input-file=/etc/aria2/aria2.session

# 在Aria2退出时保存错误的、未完成的下载任务到会话文件

save-session=/etc/aria2/aria2.session

# 定时保存会话, 0为退出时才保存, 需1.16.1以上版本, 默认:0

save-session-interval=60

##===================================##

## RPC相关设置 ##

##此部分必须启用，否则无法使用WebUI

##===================================##

# 启用RPC, 默认:false

enable-rpc=true

# 允许所有来源, 默认:false

rpc-allow-origin-all=true

# 允许外部访问, 默认:false

rpc-listen-all=true

# RPC端口, 仅当默认端口被占用时修改

rpc-listen-port=6750

# 设置的RPC授权令牌, v1.18.4新增功能, 取代 --rpc-user 和 --rpc-passwd 选项

rpc-secret=fff99999

# 设置的RPC访问用户名, 此选项新版已废弃, 建议改用 --rpc-secret 选项

#rpc-user=

# 设置的RPC访问密码, 此选项新版已废弃, 建议改用 --rpc-secret 选项

#rpc-passwd=

# 启动SSL

# rpc-secure=true

# 证书文件, 如果启用SSL则需要配置证书文件, 例如用https连接aria2

# rpc-certificate=

# rpc-private-key=

##===================================##

## BT/PT下载相关 ##

##===================================##

# 当下载的是一个种子(以.torrent结尾)时, 自动开始BT任务, 默认:true

follow-torrent=true

# BT监听端口, 当端口被屏蔽时使用, 默认:6881-6999

listen-port=51413

# 单个种子最大连接数, 默认:55

#bt-max-peers=55

# 打开DHT功能, PT需要禁用, 默认:true

enable-dht=true

# 打开IPv6 DHT功能, PT需要禁用

enable-dht6=true

# DHT网络监听端口, 默认:6881-6999

dht-listen-port=6881-6999

# 本地节点查找, PT需要禁用, 默认:false

bt-enable-lpd=true

# 种子交换, PT需要禁用, 默认:true

enable-peer-exchange=true

# 每个种子限速, 对少种的PT很有用, 默认:50K

bt-request-peer-speed-limit=50K

# 客户端伪装, PT需要

peer-id-prefix=-TR2770-

user-agent=Transmission/2.77

# 当种子的分享率达到这个数时, 自动停止做种, 0为一直做种, 默认:1.0

seed-ratio=0

# 强制保存会话, 即使任务已经完成, 默认:false

# 较新的版本开启后会在任务完成后依然保留.aria2文件

force-save=true

# BT校验相关, 默认:true

#bt-hash-check-seed=true

# 继续之前的BT任务时, 无需再次校验, 默认:false

bt-seed-unverified=true

# 保存磁力链接元数据为种子文件(.torrent文件), 默认:false

bt-save-metadata=true

# 单个种子最大连接数, 默认:55 0表示不限制

bt-max-peers=0

# 最小做种时间, 单位:分

# seed-time = 60

# 分离做种任务

bt-detach-seed-only=true

#BT Tracker List ;下载地址：https://github.com/ngosang/trackerslist

bt-tracker=udp://tracker.coppersurfer.tk:6969/announce,udp://tracker.internetwarriors.net:1337/announce,udp://tracker.opentrackr.org:1337/announce
```

aria2启动命令：
```bash
# 通配命令
aria2c --conf-path=/path/to/aria2.conf
# 适用于cyberfengx230
aria2c --conf-path=/etc/aria2/aria2.conf
```

*并未配置aria2自启动服务*    2024.08.15

**aria2自启动服务**      2024.08.17

增加开机启动脚本
```bash
sudo vim /etc/init.d/aria2c
```
添加如下内容：

```bash
#!/bin/sh
### BEGIN INIT INFO
# Provides: aria2
# Required-Start: $remote_fs $network
# Required-Stop: $remote_fs $network
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Aria2 Downloader
### END INIT INFO
 
case "$1" in
start)
 
 echo -n "已开启Aria2c"
 sudo aria2c --conf-path=/etc/aria2/aria2.conf -D
;;
stop)
 
 echo -n "已关闭Aria2c"
 killall aria2c
;;
restart)
 
 killall aria2c
 sudo aria2c --conf-path=/etc/aria2/aria2.conf -D
;;
esac
exit

```

修改文件权限为755 (a+x)
```bash
sudo chmod 755 /etc/init.d/aria2c
```
添加aria2c服务到开机启动
```bash
sudo update-rc.d aria2c defaults
```
启动服务
```bash
sudo service aria2c start
```
查看服务状态
```bash
sudo systemctl status aria2c
```