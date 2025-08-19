
---

## 1️⃣ 定义

`Option<T>` 是 Rust 标准库定义的一个枚举：

```rust
pub enum Option<T> {
    None,
    Some(T),
}
```

- **`Some(T)`**：有值，存了一个 `T`
    
- **`None`**：没有值
    
- **`T`** 可以是任何类型
    

> 设计目的：**安全地表示可选值，避免空指针（null）**。

---

## 2️⃣ 基本用法

```rust
fn main() {
    let a = Some(42);        // Option<i32>，有值
    let b: Option<i32> = None; // Option<i32>，无值

    println!("{:?} {:?}", a, b); // Some(42) None
}
```

---

## 3️⃣ 配合模式匹配

Rust 提供了 **穷尽匹配** 来处理 `Option`：

```rust
fn main() {
    let x = Some(10);

    match x {
        Some(v) => println!("拿到值: {}", v),
        None => println!("没有值"),
    }
}
```

常用的简化方式是 `if let`：

```rust
if let Some(v) = x {
    println!("值是 {}", v);
}
```

---

## 4️⃣ 常用方法

`Option<T>` 实现了很多方法，支持 **函数式链式操作**。

### 🔹1. 提取值

- `unwrap()`：直接拿值，`None` 会 **panic**
    
- `unwrap_or(default)`：`None` 时给默认值
    
- `unwrap_or_else(func)`：`None` 时调用函数生成默认值
    
- `expect(msg)`：`None` 时 panic 并输出自定义错误
    

```rust
let x = Some(5);
println!("{}", x.unwrap());           // 5
println!("{}", x.unwrap_or(0));       // 5

let y: Option<i32> = None;
println!("{}", y.unwrap_or(0));       // 0
```

---

### 🔹2. 转换方法

- `map`：对 `Some` 里的值做映射
    
- `and_then` / `flat_map`：返回另一个 `Option`，可链式
    
- `filter`：条件不满足就变 `None`
    

```rust
let x = Some(2);

let doubled = x.map(|v| v * 2);           // Some(4)
let even = x.filter(|v| v % 2 == 0);      // Some(2)
let odd = x.filter(|v| v % 2 != 0);       // None
```

---

### 🔹3. 组合方法

- `or` / `or_else`：`None` 时返回另一个 `Option`
    
- `and`：只有当前和另一个都 `Some` 才返回后者
    
- `xor`：只有一个是 `Some` 才返回 `Some`
    

```rust
let a = Some(1);
let b = None;

println!("{:?}", a.or(b)); // Some(1)
println!("{:?}", b.or(a)); // Some(1)
```

---

### 🔹4. 转换为 `Result`

- `ok_or(err)`：`Some(v)` → `Ok(v)`，`None` → `Err(err)`
    
- `ok_or_else(func)`
    

```rust
let x: Option<i32> = None;
let r: Result<i32, &str> = x.ok_or("没有值");
println!("{:?}", r); // Err("没有值")
```

---

## 5️⃣ 内存与优化

Rust 的 `Option<T>` **没有额外开销**，因为编译器做了优化：

- 如果 `T` 类型本身有无效状态（niche），`Option<T>` 可以零成本表示
    
- 比如 `Option<&T>` 只占一个指针大小，`None` 用空指针表示
    

举例：

```rust
use std::mem::size_of;

fn main() {
    println!("{}", size_of::<Option<&i32>>()); // 8
    println!("{}", size_of::<Option<i32>>());  // 8
}
```

即便 `Option` 是枚举，它的内存布局依旧高效。

---

## 6️⃣ 使用场景

1. **函数返回可能失败的值**
    
    - 没找到就返回 `None`，找到了返回 `Some(v)`
        
2. **替代空指针**
    
    - 比如链表尾巴 `next` 字段用 `Option<Box<Node>>`
        
3. **简化条件逻辑**
    
    - 配合 `map`、`filter`、`and_then`，可以写出优雅的链式调用
        

---

## 7️⃣ 小结

- `Option<T>` = `Some(T)` + `None`
    
- 编译器零开销，安全替代 `null`
    
- 丰富的方法链让逻辑更简洁
    

---
## 用法思维导图
![[Rust `Option_T_` 方法结构图.png]]