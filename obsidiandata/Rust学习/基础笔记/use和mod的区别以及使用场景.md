

# use和mod的区别

---

## 1️⃣ `mod`：声明模块（告诉编译器“我有这个文件/模块”）

- **功能**：把源文件或子模块 **加入当前 crate**
    
- **本质**：编译时扫描文件、生成模块树
    
- **不会** 自动把内容引入作用域
    

例子：

```
src/
 ├─ main.rs
 ├─ foo.rs
```

### main.rs

```rust
mod foo; // 声明模块 foo.rs
fn main() {}
```

> 这时 Rust 知道有 `foo` 模块了，但你还不能直接用 `foo::something`，  
> 如果 `foo` 里有函数，要么写全路径 `foo::func()`，要么配合 `use`。

---

## 2️⃣ `use`：把模块/类型引入当前作用域（方便访问）

- **功能**：在当前作用域创建一个**短名字**
    
- **本质**：相当于 C++ 的 `using` 或 Python 的 `import as`
    
- **不能** 创建模块，必须在模块已经存在后使用
    

例子：

```rust
mod foo;

use crate::foo::hello; // 让 hello 可以直接用，不用 foo::hello

fn main() {
    hello();
}
```

`use` **不会** 自动生成模块，它只是把已有路径搬进作用域。

---

## 3️⃣ 直观类比

|关键字|作用|类比|
|---|---|---|
|`mod`|**声明模块**，让编译器知道去找文件/子模块|C 的 `#include` 文件定义|
|`use`|**引入符号到作用域**，简化路径|Python 的 `from xxx import`|

> 也可以理解为：
> 
> - `mod` = 注册模块
>     
> - `use` = 创建本地别名
>     

---

## 4️⃣ 常见组合写法

最常见模式是 **`mod` + `use` 配合**：

```
src/
 ├─ main.rs
 ├─ foo.rs
 └─ bar.rs
```

### foo.rs

```rust
pub fn hello() {
    println!("hello");
}
```

### main.rs

```rust
mod foo;             // 声明模块
use crate::foo::hello; // 引入函数到当前作用域

fn main() {
    hello();         // 可以直接用
}
```

如果不用 `use`，就得写全路径：

```rust
mod foo;

fn main() {
    foo::hello();
}
```

---

### 5️⃣ 记忆口诀

- **`mod`**：我告诉 Rust，“我有个模块”
    
- **`use`**：我告诉 Rust，“我想在这里用它，最好用短名字”
    

---


# 使用场景一：同级模块无法使用mod，必须使用use的原因

^f3f5a9

[[crate包的同级调用（必须增加crate）]]

这个问题问得很到位，涉及 **Rust 模块系统的工作原理**。

核心原因是：

> **`mod` 是声明模块（定义模块），不是导入别的模块作用域的工具**。  
> 模块定义完成后，互相调用必须通过 **路径访问**，而 `use` 只是简化路径。


假设目录结构：

```
src/
 ├─ main.rs
 ├─ foo.rs
 └─ bar.rs
```

`main.rs`：

```rust
mod foo;
mod bar;

fn main() {
    foo::call_bar();
}
```

`foo.rs`：

```rust
pub fn call_bar() {
    println!("foo 调用 bar");
    // 这里想调用 bar::hello()
}
```

`bar.rs`：

```rust
pub fn hello() {
    println!("Hello from bar!");
}
```

---

### 1️⃣ 直接写 `mod bar` 在 foo.rs 不行

```rust
mod bar; // ❌ 错误
```

原因：

1. **`mod bar;` 的含义是“声明一个新的子模块 bar”**
    
2. ==Rust 会在 `src/foo/bar.rs` 或 `src/foo/bar/mod.rs` 找文件==
    
3. 它不会去找**同级目录下的 bar.rs**，也不会重用已经在 `main.rs` 声明的 `bar`
    

所以 `mod` 不能用来**导入同级兄弟模块**，它只会创建子模块。

---

### 2️⃣ 正确方式：用绝对路径 + `use`

在 `foo.rs` 里：

```rust
use crate::bar; // 从 crate 根开始找到 bar 模块

pub fn call_bar() {
    println!("foo 调用 bar");
    bar::hello();
}
```

或者不 `use`，直接写全路径：

```rust
pub fn call_bar() {
    crate::bar::hello();
}
```

---

### 🔹 总结原因

1. **`mod` 是声明模块，不是导入模块**
    
    - 在兄弟模块里写 `mod bar;` 相当于“在 foo 下创建一个新的子模块 bar”
        
    - Rust 不会自动重用外面声明过的 `bar`
        
2. **兄弟模块访问要么用绝对路径，要么用 use**
    
    - `crate::bar::func()`
        
    - 或 `use crate::bar;` 然后 `bar::func()`
        

---
