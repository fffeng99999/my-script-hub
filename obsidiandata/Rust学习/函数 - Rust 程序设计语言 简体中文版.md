---
title: "函数 - Rust 程序设计语言 简体中文版"
source: "https://kaisery.github.io/trpl-zh-cn/ch03-03-how-functions-work.html"
author:
published:
created: 2025-07-09
description:
tags:
  - "clippings"
---
函数在 Rust 代码中非常普遍。你已经见过语言中最重要的函数之一： `main` 函数，它是很多程序的入口点。你也见过 `fn` 关键字，它用来声明新函数。

Rust 代码中的函数和变量名使用 *snake case* 规范风格。在 snake case 中，所有字母都是小写并使用下划线分隔单词。这是一个包含函数定义示例的程序：

文件名：src/main.rs

```rust
fn main() {
    println!("Hello, world!");

    another_function();
}

fn another_function() {
    println!("Another function.");
}
```

我们在 Rust 中通过输入 `fn` 后面跟着函数名和一对圆括号来定义函数。大括号告诉编译器哪里是函数体的开始和结尾。

可以使用函数名后跟圆括号来调用我们定义过的任意函数。因为程序中已定义 `another_function` 函数，所以可以在 `main` 函数中调用它。注意，源码中 `another_function` 定义在 `main` 函数 **之后** ；也可以定义在之前。**==Rust 不关心函数定义所在的位置，只要函数被调用时出现在调用之处可见的作用域内就行。==**

让我们新建一个叫做 *functions* 的二进制项目来进一步探索函数。将上面的 `another_function` 例子写入 *src/main.rs* 中并运行。你应该会看到如下输出：

```shell
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished \`dev\` profile [unoptimized + debuginfo] target(s) in 0.28s
     Running \`target/debug/functions\`
Hello, world!
Another function.
```

`main` 函数中的代码会按顺序执行。首先，打印 “Hello, world!” 信息，然后调用 `another_function` 函数并打印它的信息。

我们可以定义为拥有 **参数** （ *parameters* ）的函数，参数是特殊变量，是函数签名的一部分。当函数拥有参数（形参）时，可以为这些参数提供具体的值（实参）。技术上讲，这些具体值被称为参数（ *arguments* ），但是在日常交流中，人们倾向于不区分使用 *parameter* 和 *argument* 来表示函数定义中的变量或调用函数时传入的具体值。

在这版 `another_function` 中，我们增加了一个参数：

文件名：src/main.rs

```rust
fn main() {
    another_function(5);
}

fn another_function(x: i32) {
    println!("The value of x is: {x}");
}
```

尝试运行程序，将会输出如下内容：

```shell
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished \`dev\` profile [unoptimized + debuginfo] target(s) in 1.21s
     Running \`target/debug/functions\`
The value of x is: 5
```

`another_function` 的声明中有一个命名为 `x` 的参数。 `x` 的类型被指定为 `i32` 。当我们将 `5` 传给 `another_function` 时， `println!` 宏会把 `5` 放在格式字符串中包含 `x` 的那对花括号的位置。

在函数签名中， **必须** 声明每个参数的类型。这是 Rust 设计中一个经过慎重考虑的决定：要求在函数定义中提供类型注解，意味着编译器再也不需要你在代码的其他地方注明类型来指出你的意图。而且，在知道函数需要什么类型后，编译器就能够给出更有用的错误消息。

当定义多个参数时，使用逗号分隔，像这样：

文件名：src/main.rs

```rust
fn main() {
    print_labeled_measurement(5, 'h');
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```

这个例子创建了一个名为 `print_labeled_measurement` 的函数，它有两个参数。第一个参数名为 `value` ，类型是 `i32` 。第二个参数是 `unit_label` ，类型是 `char` 。然后，该函数打印包含 `value` 和 `unit_label` 的文本。

尝试运行代码。使用上面的例子替换当前 *functions* 项目的 *src/main.rs* 文件，并用 `cargo run` 运行它：

```shell
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished \`dev\` profile [unoptimized + debuginfo] target(s) in 0.31s
     Running \`target/debug/functions\`
The measurement is: 5h
```

因为我们使用 `5` 作为 `value` 的值， `h` 作为 `unit_label` 的值来调用函数，所以程序输出包含这些值。

函数体由一系列的语句和一个可选的结尾表达式构成。目前为止，我们提到的函数还不包含结尾表达式，不过你已经见过作为语句一部分的表达式。因为 Rust 是一门基于表达式（expression-based）的语言，这是一个需要理解的重要区别。其他语言并没有这样的区别，所以让我们看看语句与表达式有什么区别以及这些区别是如何影响函数体的。

- **语句** （ *Statements* ）是执行一些操作但不返回值的指令。
- **表达式** （ *Expressions* ）计算并产生一个值。

让我们看一些例子。

实际上，我们已经使用过语句和表达式。使用 `let` 关键字创建变量并绑定一个值是一个语句。在示例 3-1 中， `let y = 6;` 是一个语句。

文件名：src/main.rs

```rust
fn main() {
    let y = 6;
}
```

示例 3-1：包含一个语句的 `main` 函数定义

函数定义也是语句，上面整个例子本身就是一个语句。（不过，如我们将在下面看到， **调用** 函数并不是语句。）

语句不返回值。因此，不能把 `let` 语句赋值给另一个变量，比如下面的例子尝试做的，会产生一个错误：

文件名：src/main.rs

```rust
fn main() {
    let x = (let y = 6);
}
```

当运行这个程序时，会得到如下错误：

```shell
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error: expected expression, found \`let\` statement
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^
  |
  = note: only supported directly in conditions of \`if\` and \`while\` expressions

warning: unnecessary parentheses around assigned value
 --> src/main.rs:2:13
  |
2 |     let x = (let y = 6);
  |             ^         ^
  |
  = note: \`#[warn(unused_parens)]\` on by default
help: remove these parentheses
  |
2 -     let x = (let y = 6);
2 +     let x = let y = 6;
  |

warning: \`functions\` (bin "functions") generated 1 warning
error: could not compile \`functions\` (bin "functions") due to 1 previous error; 1 warning emitted
```

`let y = 6` 语句并不返回值，所以没有可以绑定到 `x` 上的值。这与其他语言不同，例如 C 和 Ruby，它们的赋值语句会返回所赋的值。在这些语言中，可以这么写 `x = y = 6` ，这样 `x` 和 `y` 的值都是 `6` ；==Rust 中不能这样写。==

表达式会计算出一个值，并且你将编写的大部分 Rust 代码是由表达式组成的。考虑一个数学运算，比如 `5 + 6` ，这是一个表达式并计算出值 `11` 。表达式可以是语句的一部分：在示例 3-1 中，语句 `let y = 6;` 中的 `6` 是一个表达式，它计算出的值是 `6` 。函数调用是一个表达式。宏调用是一个表达式。用大括号创建的一个新的块作用域也是一个表达式，例如：

文件名：src/main.rs

```rust
fn main() {
    let y = {
        let x = 3;
        x + 1
    };

    println!("The value of y is: {y}");
}
```

这个表达式：

```rust
{
    let x = 3;
    x + 1
}
```

是一个代码块，它的值是 `4` 。这个值作为 `let` 语句的一部分被绑定到 `y` 上。注意 `x + 1` 这一行在结尾没有分号，与你见过的大部分代码行不同。==表达式的结尾没有分号。==如果在表达式的结尾加上分号，它就变成了语句，而语句不会返回值。在接下来探索具有返回值的函数和表达式时要谨记这一点。

函数可以向调用它的代码返回值。我们并不对返回值命名，但要在箭头（ `->` ）后声明它的类型。在 Rust 中，函数的返回值等同于函数体最后一个表达式的值。使用 `return` 关键字和指定值，可从函数中提前返回；但大部分函数隐式的返回最后的表达式。这是一个有返回值的函数的例子：

文件名：src/main.rs

```rust
fn five() -> i32 {
    5
}

fn main() {
    let x = five();

    println!("The value of x is: {x}");
}
```

在 `five` 函数中没有函数调用、宏、甚至没有 `let` 语句 —— 只有数字 `5` 。这在 Rust 中是一个完全有效的函数。注意，也指定了函数返回值的类型，就是 `-> i32` 。尝试运行代码；输出应该看起来像这样：

```shell
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished \`dev\` profile [unoptimized + debuginfo] target(s) in 0.30s
     Running \`target/debug/functions\`
The value of x is: 5
```

`five` 函数的返回值是 `5` ，所以返回值类型是 `i32` 。让我们仔细检查一下这段代码。有两个重要的部分：首先， `let x = five();` 这一行表明我们使用函数的返回值初始化一个变量。因为 `five` 函数返回 `5` ，这一行与如下代码相同：

```rust
#![allow(unused)]
fn main() {
let x = 5;
}
```

其次， `five` 函数没有参数并定义了返回值类型，不过函数体只有单单一个 `5` 也没有分号，因为这是一个表达式，我们想要返回它的值。

让我们看看另一个例子：

文件名：src/main.rs

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
```

运行代码会打印出 `The value of x is: 6` 。但如果在包含 `x + 1` 的行尾加上一个分号，把它从表达式变成语句，我们将看到一个错误。

文件名：src/main.rs

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1;
}
```

运行代码会产生一个错误，如下：

```shell
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error[E0308]: mismatched types
 --> src/main.rs:7:24
  |
7 | fn plus_one(x: i32) -> i32 {
  |    --------            ^^^ expected \`i32\`, found \`()\`
  |    |
  |    implicitly returns \`()\` as its body has no tail or \`return\` expression
8 |     x + 1;
  |          - help: remove this semicolon to return this value

For more information about this error, try \`rustc --explain E0308\`.
error: could not compile \`functions\` (bin "functions") due to 1 previous error
```

主要的错误信息，“mismatched types”（类型不匹配），揭示了代码的核心问题。函数 `plus_one` 的定义说明它要返回一个 `i32` 类型的值，不过语句并不会返回值，使用单位类型 `()` 表示不返回值。因为不返回值与函数定义相矛盾，从而出现一个错误。在输出中，Rust 提供了一条信息，可能有助于纠正这个错误：它建议删除分号，这会修复这个错误。