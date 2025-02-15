# LuckPerms权限组 教程

## 目录

1. [LuckPerms 简介](#1-luckperms-简介)
2. [基础命令](#2-基础命令)
3. [权限节点与继承](#3-权限节点与继承)
4. [上下文与服务器作用域](#4-上下文与服务器作用域)
5. [元数据与聊天格式](#5-元数据与聊天格式)
6. [权限检查与调试](#6-权限检查与调试)

---

## 1. LuckPerms 简介

LuckPerms 是一款高性能的 Minecraft 权限管理插件，支持 Bukkit/Spigot、BungeeCord、Velocity 等平台，功能包括：

- **权限分配**：控制玩家或组的命令/功能访问权限。
- **组管理**：通过组继承简化权限配置。
- **上下文控制**：根据世界、服务器、时间等条件动态调整权限。
- **元数据支持**：设置前缀、后缀、权重等。

### 步骤 1：安装插件

1. 下载对应版本的 LuckPerms。
2. 将 `.jar` 文件放入服务器的 `plugins` 文件夹。
3. 重启服务器，生成默认配置文件。

### 步骤 2：选择数据库（可选）

默认使用本地文件存储，如需 MySQL 或 MongoDB：

1. 修改 `config.yml`：

    ```yaml
    storage-method: mysql
    # 填写数据库信息
    data:
       address: localhost:3306
       database: minecraft
       username: root
       password: "123456"
    ```yaml

    ```

2. 重启服务器生效。

---

## 2. 基础命令

### 基础权限

| 命令 | 说明 | 示例 |
|------|------|------|
| `/lp user <玩家> permission set <权限> [true/false]` | 给玩家添加权限 | `/lp user Notch permission set minecraft.command.gamemode true` |
| `/lp user <玩家> permission unset <权限>` | 移除玩家的权限 | `/lp user Notch permission unset minecraft.command.gamemode` |
| `/lp group <组名> permission set <权限>` | 给组添加权限 | `/lp group admin permission set minecraft.command.*` |

### 组管理

| 命令 | 说明 | 示例 |
|------|------|------|
| `/lp creategroup <组名>` | 创建新组 | `/lp creategroup vip` |
| `/lp deletegroup <组名>` | 删除组 | `/lp deletegroup vip` |
| `/lp user <玩家> parent add <组名>` | 将玩家加入组 | `/lp user Notch parent add admin` |
| `/lp group <组名> parent add <父组>` | 设置组继承 | `/lp group admin parent add mod` |

### 查看信息

| 命令 | 说明 | 示例 |
|------|------|------|
| `/lp user <玩家> info` | 查看玩家权限 | `/lp user Notch info` |
| `/lp group <组名> info` | 查看组权限 | `/lp group admin info` |
| `/lp listgroups` | 列出所有组 | `/lp listgroups` |

---

## 3. 权限节点与继承

### 常用的权限节点

| 权限 | 说明 |
|------|------|
| `minecraft.command.help` | 使用 `/help` 命令 |
| `minecraft.command.gamemode` | 切换游戏模式 |
| `essentials.fly` | 允许飞行（需 EssentialsX） |
| `luckperms.*` | 所有 LuckPerms 权限 |

### 继承与权重

- **继承**：子组自动拥有父组权限。

  ```bash
  /lp group admin parent add mod
  ```

- **权重**：数字越大优先级越高，覆盖低权重组的权限。

  ```bash
  /lp group admin setweight 100
  ```

---

## 4. 上下文与服务器作用域

根据条件限制权限生效范围：

- 仅在地图 `world_nether` 生效：

  ```bash
  /lp user Notch permission set minecraft.command.gamemode true server=survival world=world_nether
  ```

- 临时权限（1小时后过期）：

  ```bash
  /lp user Notch permission set essentials.fly true expires=1h
  ```

---

## 5. 元数据与聊天格式

### 设置前缀和后缀

```bash
/lp user <玩家> meta setprefix 100 "&a[VIP] "
/lp user <玩家> meta setsuffix 100 "&e"
```

- **权重值**：决定优先级（数字越大越优先）。
- **颜色代码**：使用 `&` 符号（如 `&a` 为绿色）。

### 集成聊天插件

确保安装 Vault 和 EssentialsX Chat，并在配置文件中启用：

```yaml
# config.yml
vault-server: global
vault-include-global: true
```

---

## 6. 权限检查与调试

### 检查玩家权限

```bash
/lp user <玩家> permission check <权限>
```

### 调试权限问题

```bash
/lp verbose on  # 开启调试模式
/lp verbose off # 关闭
```
