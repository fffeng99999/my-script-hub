
C语言可以使用双目运算符号简化判定赋值：
```C
char demo = (if flag == true) ? 'Option0' : 'Option1';
```

Rust没有'?'双目运算符的写法，采用以下写法实现相同的功能：
```Rust
let expected1: char = if flag % 2 == 0 { 'R' } else { 'B' };
```