> C语言中可变数组在Rust中的代替

### ✅ 方法1：用 `Vec`（最常用）

```rust
use std::os::raw::c_char;

fn main() {
    let n = read_module::run(&*String::new());
    let mut flags: Vec<c_char> = vec![0; n]; // 初始化 n 个 0

    // 访问时像数组一样用
    flags[0] = 1;
}
```

- `Vec` 支持运行时长度
    
- 可以通过 `.as_mut_ptr()` 获取原生指针给 FFI
    

---

### ✅ 方法2：用堆上切片 `Box<[T]>`

如果你希望有点接近 C 的静态数组感觉，可以用 `Box<[T]>`：

```rust
use std::os::raw::c_char;

fn main() {
    let n = read_module::run(&*String::new());
    let mut flags: Box<[c_char]> = vec![0; n].into_boxed_slice();

    // 使用类似数组的索引
    flags[0] = 1;

    // 获取裸指针给 C 调用
    let ptr: *mut c_char = flags.as_mut_ptr();
}
```

`Box<[T]>` 的好处是固定长度，一旦创建不能再扩容。

---

### ✅ 方法3：如果长度很小且可用最大值

如果你知道长度最大值，可以用**定长大数组 + 切片**：

```rust
use std::os::raw::c_char;

fn main() {
    let n = read_module::run(&*String::new());
    let mut buffer: [c_char; 1024] = [0; 1024]; // 预分配最大可能长度
    let flags = &mut buffer[..n];               // 用切片访问前 n 个元素
}
```

---
