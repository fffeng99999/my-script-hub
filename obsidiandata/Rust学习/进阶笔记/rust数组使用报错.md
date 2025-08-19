
```Rust
let mut n = 0;  
n = read_module::run(&*String::new());  
let mut flags: [c_char; n] = ......
```

上面这个写法在 Rust 里无效，是因为==数组类型的长度必须在**编译期就能确定**==，这里用的 `n` 是**运行时计算出来的值**。Rust 原生数组 `[T; N]` 的 `N` 必须是 `const`。

也就是说，这里：

```rust
let mut n = 0;
n = read_module::run(&*String::new());
let mut flags: [c_char; n] = ...
```

- `n` 是运行时才知道的
    
- Rust 原生数组不能用运行时值当长度
    [[可变与可变#^62de23 | 可变与可变-原生数组与可变]]

---

## 1️⃣ 原因分析

- Rust 的数组 `[T; N]` 是固定长度类型
    
- 长度 `N` 是类型的一部分，例如 `[i32; 3]` 和 `[i32; 4]` 是不同类型
    
- 运行时值不能决定类型，所以编译直接报错
    

如果想用运行时决定长度，你必须用**堆分配的动态数组**（`Vec` 或 `Box<[T]>`），而不是栈上固定数组。

---

## 2️⃣ 解决方法

[[Rust的“可变数组”]]

---
## 🔹推荐方案

大多数情况下，用 `Vec<c_char>` 最灵活，尤其是你在做 [[C FFI是什么 | C FFI]] 时：

```rust
let mut flags: Vec<c_char> = vec![0; n];
let ptr = flags.as_mut_ptr(); // 给C函数用
```

---

