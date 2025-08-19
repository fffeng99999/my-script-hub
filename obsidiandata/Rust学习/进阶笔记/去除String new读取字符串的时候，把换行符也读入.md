现象：

```
r

t
```

中间出现了 **多出来的一行换行**，这是典型的 **控制台输入读取问题**，在 Rust 里常见于使用 `String::new()` + 输入函数时没有处理末尾的换行符 `\n`。

---

## 1️⃣ 常见原因

1. **`read_line` 会把换行符读进字符串**
    
    - 例如用户输入 `r` 然后回车
        
    - 读取到的字符串实际上是 `"r\n"`
        
    - 如果你取第一个字符或打印原始字符串，就会出现多余换行
        
2. **你在循环里多次创建 `String::new()`**
    
    - `read_module::input_char(&*String::new())` 可能内部就是用 `read_line`
        
    - 每次输入回车就会导致字符串里带 `\n`
        
    - 打印时就出现多行
        

---

## 2️⃣ 检查点

- `read_module::input_char` 的实现
    
    - 是否用 `std::io::stdin().read_line(&mut s)`
        
    - 是否 `.trim()` 或 `.trim_end()` 去掉了 `\n`
        
- 你的 `flags` 打印方式
    
    - 如果直接打印 `char` 并且包含 `'\n'`，就会换行
        

---

## 3️⃣ 解决方法

### 方法 1：`trim` 去掉换行符

假设你原本的函数是这样：

```rust
pub fn input_char(_: &str) -> char {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    s.chars().next().unwrap()
}
```

改成：

```rust
pub fn input_char(_: &str) -> char {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    s.trim().chars().next().unwrap()  // 去掉 \n \r
}
```

---

### 方法 2：在调用处手动过滤

如果你不能改 `read_module`：

```rust
let c = read_module::input_char(&*String::new());
if c != '\n' && c != '\r' {
    flags[i] = c;
}
```

但更推荐在读取函数里统一 `trim`。

---

## 4️⃣ 推荐检查流程

1. 打印 `input_char` 的返回值的 **Unicode 码点**，确认是不是 `'\n'` 或 `'\r'`
    
2. 确认输入函数是否用 `read_line`
    
3. 确认是否 `trim` 了末尾换行符
    

---

如果你愿意，我可以帮你重写一个 **`read_module::input_char`**，  
让它既能安全读取单字符，又不会引入多余换行。

你希望我帮你写吗？