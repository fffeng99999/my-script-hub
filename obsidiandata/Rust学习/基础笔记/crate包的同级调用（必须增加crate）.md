
[[use和mod的区别以及使用场景#^f3f5a9]]

如果是 **`foo` 模块调用同级的 `bar` 模块**，思路是一样的，只不过模块的可见性和导入方式要注意。

我假设还是以下结构（同级模块）：

```
src/
 ├─ main.rs
 ├─ foo.rs
 └─ bar.rs
```

---

## 1️⃣ 基本做法

在 `foo.rs` 里调用 `bar.rs` 的函数：

### main.rs

```rust
mod foo;
mod bar;

fn main() {
    foo::test();
}
```

### bar.rs

```rust
pub fn world() {
    println!("World from bar!");
}
```

### foo.rs

```rust
// 声明外部模块
use crate::bar; // 引入 bar 模块

pub fn test() {
    println!("foo 调用了 bar");
    bar::world(); // 调用 bar 的函数
}
```

---

### 2️⃣ 关键点

1. **模块路径从 crate 根开始**
    
    - 在 `foo.rs` 里，要访问 `bar`，用 `crate::bar`
        
    - `crate` 相当于项目的根（这里就是 `main.rs`）
        
2. **被调用的函数必须 `pub`**
    
    - 否则 `foo` 看不到 `bar::world()`
        

---

## 3️⃣ 子目录模块场景

如果你用子目录：

```
src/
 └─ utils/
      ├─ mod.rs
      ├─ foo.rs
      └─ bar.rs
```

`mod.rs` 内容：

```rust
pub mod foo;
pub mod bar;
```

- `foo.rs` 调用 `bar.rs`：
    

```rust
use crate::utils::bar;  // 从 crate 根开始访问

pub fn test() {
    println!("foo 调用了 bar");
    bar::world();
}
```

---

### 4️⃣ 小结

- **同级模块互相调用**，用 `crate::` 从根开始引用即可
    
- 子目录也一样，只是路径更长，例如 `crate::utils::bar`
    
- 确保函数或类型 `pub` 才能跨模块访问
    

---
