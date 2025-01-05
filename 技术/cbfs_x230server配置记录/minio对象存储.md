*程序下载自minio官网*  [minio官网](https://min.io/)

**二进制文件路径：**
```bash
#mimio二进制文件的当前路径
/opt/mimio/minio

#mimio二进制文件的推荐路径
/usr/local/bin/
```

**配置文件路径：**
```bash
sudo nano /etc/default/minio

#环境变量内容
MINIO_ROOT_USER=your-access-key
MINIO_ROOT_PASSWORD=your-secret-key
MINIO_VOLUMES="/media/userf/095876e8-646e-4a40-bbda-138822faf3a3/miniodata"
MINIO_OPTS="--address :9000"
```

**Systemd服务文件**

```bash
sudo nano /etc/systemd/system/minio.service
```

```toml
#文件内容
[Unit]
Description=MinIO
Documentation=https://docs.min.io Wants=network-online.target
After=network-online.target

[Service]
EnvironmentFile=/etc/default/minio
ExecStart=/opt/mimio/minio server $MINIO_OPTS $MINIO_VOLUMES
Restart=always User=root Group=root
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```