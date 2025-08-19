```mermaid
%% 双链表插入节点四步图
%% 假设在节点 B 与节点 C 之间插入新节点 X

%% 第 0 步：设置方向与主题
%% LR 表示从左到右
%% TD 表示从上到下
%% 这里用 TD，四张子图上下排布
%% 如需横向，改成 LR 即可
%% 选用暗黑主题，可改成 default、forest、neutral 等
%% 节点样式用 classDef 统一
%% 使用 subgraph 把每一步包起来，便于整体控制

%% 全局配置
%% direction TD 已写在 subgraph 里
%% 如需统一节点样式，可取消注释
%% classDef node fill:#1e1e1e,stroke:#fff,stroke-width:1px,color:#fff

%% 第 1 步：初始双链表
subgraph Step1 [步骤 1：初始双链表]
    direction LR
    A1["<pre>  A  </pre>"]
    B1["<pre>  B  </pre>"]
    C1["<pre>  C  </pre>"]
    D1["<pre>  D  </pre>"]

    A1 --> B1
    B1 --> C1
    C1 --> D1
    D1 --> C1
    C1 --> B1
    B1 --> A1
end

%% 第 2 步：创建新节点 X
subgraph Step2 [步骤 2：创建新节点 X]
    direction LR
    A2["<pre>  A  </pre>"]
    B2["<pre>  B  </pre>"]
    C2["<pre>  C  </pre>"]
    D2["<pre>  D  </pre>"]
    X2["<pre>  X  </pre>"]:::new

    A2 --> B2
    B2 --> C2
    C2 --> D2
    D2 --> C2
    C2 --> B2
    B2 --> A2
end

%% 第 3 步：修改 4 个指针
subgraph Step3 [步骤 3：修改 4 个指针]
    direction LR
    A3["<pre>  A  </pre>"]
    B3["<pre>  B  </pre>"]
    C3["<pre>  C  </pre>"]
    D3["<pre>  D  </pre>"]
    X3["<pre>  X  </pre>"]:::new

    A3 --> B3
    D3 --> C3
    C3 --> X3        %% 修改 C 的前驱
    X3 --> C3        %% X 的后继
    B3 --> X3        %% 修改 B 的后继
    X3 --> B3        %% X 的前驱
end

%% 第 4 步：完成插入
subgraph Step4 [步骤 4：完成插入]
    direction LR
    A4["<pre>  A  </pre>"]
    B4["<pre>  B  </pre>"]
    X4["<pre>  X  </pre>"]:::new
    C4["<pre>  C  </pre>"]
    D4["<pre>  D  </pre>"]

    A4 --> B4
    B4 --> X4
    X4 --> C4
    C4 --> D4
    D4 --> C4
    C4 --> X4
    X4 --> B4
    B4 --> A4
end

%% 样式：高亮新节点
classDef new fill:#ff6b6b,stroke:#fff,stroke-width:2px,color:#fff
```
