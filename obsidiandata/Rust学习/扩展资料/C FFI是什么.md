C FFI 是 **Foreign Function Interface**（外部函数接口），在 Rust 语境下通常指 **Rust 与 C 语言互相调用的接口机制**。

它是让 **不同编程语言之间** 共享函数、数据结构的桥梁。

在 Rust 里，C FFI 主要用来：

1. **调用现有的 C 库**（如 OpenSSL、libcurl、zlib）
    
2. **导出 Rust 函数给 C 调用**（写高性能库给 C/C++/Python 用）
    

---

## 1️⃣ Rust 调用 C（最常用场景）

Rust 通过 `extern "C"` 声明外部函数，并用 `unsafe` 调用。

假设有个 C 函数：

```c
// mathlib.h
int add(int a, int b);
```

在 Rust 里：

```rust
extern "C" {
    fn add(a: i32, b: i32) -> i32;
}

fn main() {
    unsafe {
        let result = add(2, 3);
        println!("2+3={}", result);
    }
}
```

- `extern "C"` 告诉编译器用 C ABI 调用函数
    
- `unsafe` 是因为 Rust 无法保证 C 代码安全
    
- 需要链接到 `.so` / `.dll` / `.a` 文件才能运行
    

---

## 2️⃣ Rust 导出函数给 C 用

如果你想把 Rust 当作动态库给 C 调用：

```rust
#[no_mangle]          // 禁止函数名被 Rust 改名（mangling）
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

编译成 `cdylib` 或 `staticlib` 后，C 可以直接用：

```c
int add(int a, int b); // 来自 Rust 库
```

---

## 3️⃣ 常用类型映射

Rust 调 C 时，通常使用 `libc` 里的类型，保证和 C ABI 对齐：

|C 类型|Rust 类型|
|---|---|
|`int`|`c_int` / `i32`|
|`char*`|`*mut c_char`|
|`const char*`|`*const c_char`|
|`void*`|`*mut c_void`|
|`size_t`|`size_t` (`usize`)|

示例：

```rust
use std::os::raw::{c_char, c_int};

extern "C" {
    fn puts(s: *const c_char) -> c_int;
}
```

---

## 4️⃣ 内存安全注意点

1. **Rust 调 C** 时必须保证：
    
    - 传递的指针有效且生命周期正确
        
    - 处理好字符串的编码和终止符（C 需要 `\0`）
        
2. **C 调 Rust** 时必须保证：
    
    - Rust 导出的函数不能 panic 跨越 FFI 边界（可能导致未定义行为）
        
    - 内存所有权和释放规则必须明确（避免 double free）
        

---

## 5️⃣ 典型用途

- 调用高性能 C 库，如 OpenSSL、SQLite
    
- 给 Python、Lua、Node.js 写扩展（通常通过 C ABI）
    
- 嵌入式或系统编程中和现有 C 驱动交互
    

---

如果你愿意，我可以帮你写一个**Rust 调用 C 函数的完整示例**，  
包括 `.c` 文件、`Cargo.toml` 配置、以及 Rust 侧调用方法。

你希望我给你写这个 FFI 示例吗？