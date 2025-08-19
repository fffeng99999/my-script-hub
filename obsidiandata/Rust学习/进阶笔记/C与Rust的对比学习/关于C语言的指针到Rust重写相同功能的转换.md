### 从代码的整体功能出发
---
不能逐字逐句地将C指针 `*` 直接换成Rust的某个语法，而是要问：“==C代码在这里使用指针是为了做什么？==”

---

### 1. 用于函数参数，以只读方式访问数据（不可变借用）

这种指针的意图是避免复制大型数据，同时保证函数不会修改原始数据。

**C 语言:**

```C
void print_sum(const int* array, size_t len) {
    long sum = 0;
    for (size_t i = 0; i < len; ++i) {
        sum += array[i]; // 只读取数据
    }
    printf("Sum: %ld\n", sum);
}
```

Rust 实现:

在Rust中，我们使用 不可变引用 (Immutable Reference) &T 和 切片 (Slice) &[T]。切片是一个“视图”，它同时包含了指向数据的指针和长度信息，因此更安全。

```Rust
// 参数 `&[i32]` 代表一个i32类型的切片引用，它既安全又高效。
fn print_sum(array: &[i32]) {
    let sum: i64 = array.iter().sum(); // 使用迭代器，更地道、更安全
    println!("Sum: {}", sum);
}

fn main() {
    let my_vec = vec![1, 2, 3, 4, 5];
    let my_array = [10, 20, 30];

    print_sum(&my_vec);      // Vec可以被借用为切片
    print_sum(&my_array);    // 数组也可以
}
```

**转换核心**：`const int*` + `size_t len` -> `&[i32]`

---

### 2. 用于函数参数，以修改传入的数据（可变借用）

这种指针的意图是让函数能够修改其调用者作用域内的数据。

**C 语言:**

```C
void add_one(int* num) {
    *num += 1; // 修改指针指向的值
}
```

Rust 实现:

在Rust中，我们使用 可变引用 (Mutable Reference) &mut T。Rust的借用检查器会确保在任何时候，对一个变量要么只有一个可变引用，要么有多个不可变引用，但不能同时存在。这从根本上杜绝了数据竞争。

```Rust
fn add_one(num: &mut i32) {
    *num += 1; // 同样使用解引用操作符*
}

fn main() {
    let mut x = 5;
    println!("Before: {}", x);
    add_one(&mut x); // 必须传入一个可变引用
    println!("After: {}", x);
}
```

**转换核心**：`int*` (用于修改) -> `&mut i32`

---

### 3. 指向动态分配的内存（所有权与智能指针）

在C中，`malloc` 返回一个指针，你必须手动调用 `free` 来释放它。这很容易导致内存泄漏或悬垂指针。

**C 语言:**

```C
struct Point { int x; int y; };

struct Point* create_point(int x, int y) {
    struct Point* p = (struct Point*)malloc(sizeof(struct Point));
    p->x = x;
    p->y = y;
    return p;
}

// ... 之后必须手动 free(p);
```

Rust 实现:

在Rust中，最直接的等价物是 Box<T>，一个拥有所有权的智能指针。当Box离开作用域时，它所指向的内存会自动被释放，无需手动管理。

```Rust
struct Point { x: i32, y: i32 }

// 函数直接返回一个拥有所有权的Point实例。
// 调用者可以选择是否要把它放到堆上。
fn create_point(x: i32, y: i32) -> Point {
    Point { x, y }
}

fn main() {
    // 如果需要显式地在堆上分配
    let p1 = Box::new(create_point(10, 20));
    println!("Point on heap: ({}, {})", p1.x, p1.y);

    // p1离开作用域时，内存会自动被释放，没有free()
}
```

**转换核心**：`malloc` / `free` -> `Box<T>`

---

### 4. 可能为空的指针（Nullable Pointers）

C语言使用 `NULL` 来表示一个指针是无效的或不指向任何东西。忘记检查 `NULL` 是导致程序崩溃的常见原因。

**C 语言:**

```C
// 这个函数可能返回一个指针，也可能返回NULL
struct Node* find_node(...) { ... }

struct Node* node = find_node(...);
if (node != NULL) {
    // 对 node 进行操作
}
```

Rust 实现:

Rust在语言层面通过 Option<T> 枚举来处理可能缺失的值。Option<T> 有两个变体：Some(value) 表示值存在，None 表示值不存在（等同于NULL）。Rust编译器会强制你处理 None 的情况，从而彻底消除空指针解引用错误。

```Rust
struct Node { /* ... */ }

// 函数签名明确表示它可能不会返回一个Node
fn find_node(...) -> Option<Node> {
    // ... 逻辑 ...
    if found {
        Some(Node { /* ... */ })
    } else {
        None // 使用None代替NULL
    }
}

fn main() {
    // 必须处理Option
    match find_node(...) {
        Some(node) => {
            println!("Node found!");
            // 在这里安全地使用node
        }
        None => {
            println!("Node not found.");
        }
    }
}
```

**转换核心**：`T*` (可能为 `NULL`) -> `Option<Box<T>>` 或 `Option<&T>`

---

### 5. 需要C指针的场景（裸指针）

当你需要与C库交互（FFI）或者在极少数情况下构建不安全的高级抽象时，Rust也提供了C风格的指针，称为 **裸指针 (Raw Pointers)**：`*const T` (不可变) 和 `*mut T` (可变)。

但是，解引用裸指针必须在 **`unsafe`** 块中进行。这相当于你向编译器保证：“我知道这里的操作可能不安全，但我自己负责保证它的正确性。” 在编写纯粹的Rust程序时，你应该极力避免使用它。

```Rust
let mut num = 5;

// 从引用创建裸指针是安全的操作
let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;

unsafe {
    // 解引用裸指针必须在unsafe块内
    println!("r1 is: {}", *r1);
    *r2 = 10;
    println!("r2 is now: {}", *r2);
}
```

### 总结

下表总结了转换的核心思想：

|C 指针用途|Rust 中对应的安全工具|核心思想|
|---|---|---|
|**只读访问** (`const T*`)|**不可变引用** (`&T`, `&[T]`)|借用检查器保证数据在你读取时不会被修改。|
|**修改数据** (`T*`)|**可变引用** (`&mut T`, `&mut [T]`)|借用检查器保证同一时间只有一个地方能修改数据。|
|**动态内存** (`malloc`/`free`)|**智能指针** (`Box<T>`)|RAII机制（资源获取即初始化），自动管理内存生命周期。|
|**空指针** (`NULL`)|**`Option<T>` 枚举**|将可能为空的概念纳入类型系统，强制在编译时处理。|
|**与C库交互/底层代码**|**裸指针** (`*const T`, `*mut T`)|作为逃生舱口，在 `unsafe` 块中进行手动内存管理。|