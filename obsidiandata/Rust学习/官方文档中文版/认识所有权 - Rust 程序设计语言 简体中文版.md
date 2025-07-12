---
title: "认识所有权 - Rust 程序设计语言 简体中文版"
source: "https://kaisery.github.io/trpl-zh-cn/ch04-00-understanding-ownership.html"
author:
published:
created: 2025-07-09
description:
tags:
  - "clippings"
---
所有权（系统）是 Rust 最为与众不同的特性，对语言的其他部分有着深刻含义。它让 Rust 无需垃圾回收（garbage collector）即可保障内存安全，因此理解 Rust 中所有权如何工作是十分重要的。本章，我们将讲到所有权以及相关功能：借用（borrowing）、slice 以及 Rust 如何在内存中布局数据。