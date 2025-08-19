
# 原理

- mermaid由node.js驱动，使用npm安装，可用于前端网络设计。
- 在前端中，通过以下方式使用：
```javascript
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>
```
浏览网页的时候，表格代码被渲染为`svg`图片。



# basic demo


---

## Flowchart
---
```mermaid
graph TD;
	A --> C;
	A --> B;
	B --> D;
	C --> D;
```

> `graph TD;`起始，按照缩进分级，每一段以`;`结尾。

## SequenceDiagram
---
```mermaid
sequenceDiagram
	participant Mike
	participant Niko
	Mike ->> Timi: Where are you?
	loop Thinking
		Timi ->> Timi: Should I tell the Truth?
	end
	Note left of Timi: Can't tell the truth!
	Timi -->> Mike: Home!
	Timi ->> Niko: Help me cheating Mike!
	Niko ->> Timi: Never!
	Alice -->> Mike: sad!
	Alice -->> Niko: good!
	Alice -->> Timi: What f?
```

```mermaid
quadrantChart
    title 编程语言特性 (性能 vs. 易用性)
    x-axis Low --> High
    y-axis Low --> High
    quadrant-1 LL
    quadrant-2 LH
    quadrant-3 HL
    quadrant-4 HH
    Go: [0.8, 0.7]
    C#: [0.7, 0.6]
    Java: [0.7, 0.5]
    Rust: [0.95, 0.2]
    C++: [0.9, 0.1]
    Python: [0.2, 0.9]
    JavaScript: [0.3, 0.8]
    Ruby: [0.15, 0.85]
```

```mermaid
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    Campaign A: [0.3, 0.6]
    Campaign B: [0.45, 0.23]
    Campaign C: [0.57, 0.69]
    Campaign D: [0.78, 0.34]
    Campaign E: [0.40, 0.34]
    Campaign F: [0.35, 0.78]

```

### [XY Chart](https://mermaid.js.org/syntax/xyChart.html)

```mermaid
xychart-beta
    title "Sales Revenue"
    x-axis [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    y-axis "Revenue (in $)" 4000 --> 11000
    bar [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
    line [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]

```
> 轴刻度根据所取范围自动分化


# 编辑器基础

## Maikdown链接演示
---
[![](https://mermaid.ink/img/pako:eNpFkcFOhDAQhl-FnZMmLJTCttCDibrJXj14Ujx0aaEk0JJSVNzl3S2osXPo_Pmn33TaC1RGSGDQWD6o4PlY6sCv-9cnbt38Fuz3d9eTdEFvtJyvwcPNyQSjMsPQ6ma3u_2phtAfbwUwZycZQi9tz1cJl9UvwSnZyxKYT2tj5ehKCH-dTayGkl1ngg9jO1FCqRfPHLh-Mab_w1ozNQpYzbvRq2kQ3Mljy_3F_0ukFtI-mkk7YGQjALvAJ7CMoChPaZHmFGWU5lkIM7CEkihFGaYFLjKMfCwhfG09UXQg6IAKhNftQKjHdYZ7_EqsjK7bZs0m2_lBlXPDyOK4aUcXNa1T0zmqTB-PrVD-IdV7QWKCSc5xKglN-SFNRXVOirzGWVILihLMwfd287B9hsfAsnwD7jN-tw?type=png)](https://mermaid.live/edit#pako:eNpFkcFOhDAQhl-FnZMmLJTCttCDibrJXj14Ujx0aaEk0JJSVNzl3S2osXPo_Pmn33TaC1RGSGDQWD6o4PlY6sCv-9cnbt38Fuz3d9eTdEFvtJyvwcPNyQSjMsPQ6ma3u_2phtAfbwUwZycZQi9tz1cJl9UvwSnZyxKYT2tj5ehKCH-dTayGkl1ngg9jO1FCqRfPHLh-Mab_w1ozNQpYzbvRq2kQ3Mljy_3F_0ukFtI-mkk7YGQjALvAJ7CMoChPaZHmFGWU5lkIM7CEkihFGaYFLjKMfCwhfG09UXQg6IAKhNftQKjHdYZ7_EqsjK7bZs0m2_lBlXPDyOK4aUcXNa1T0zmqTB-PrVD-IdV7QWKCSc5xKglN-SFNRXVOirzGWVILihLMwfd287B9hsfAsnwD7jN-tw)

## 美化
---
```mermaid
---
config:
  look: handDrawn
  theme: neutral
---
flowchart LR
  A[Start] --> B{Decision}
  B -->|Yes| C[Continue]
  B -->|No| D[Stop]

```

```mermaid
---
config:
  theme: neutral
  layout: elk
  elk:
    mergeEdges: true
    nodePlacementStrategy: LINEAR_SEGMENTS
---
flowchart LR
  A[Start] --> B{Choose Path}
  B -->|Option 1| C[Path 1]
  B -->|Option 2| D[Path 2]
```

```mermaid
---
config:
  layout: dagre
  look: classic
  theme: default
---

flowchart LR
A[Start] --> B{Choose Path}
B -->|Option 1| C[Path 1]
B -->|Option 2| D[Path 2]
```

```mermaid
---
config:
  layout: dagre
  look: classic
  theme: forest
---

flowchart LR
A[Start] --> B{Choose Path}
B -->|Option 1| C[Path 1]
B -->|Option 2| D[Path 2]
```

> 以下样例包含常用的颜色设置，图形形状以及结构。
```mermaid
---
config:
  theme: 'base'
  themeVariables:
    primaryColor: '#BB2528'
    primaryTextColor: '#fff'
    primaryBorderColor: '#7C0000'
    lineColor: '#F8B229'
    secondaryColor: '#006100'
    tertiaryColor: '#fff'
---
        graph TD
          A[Christmas] -->|Get money| B(Go shopping)
          B --> C{Let me think}
          B --> G[/Another/]
          C ==>|One| D[Laptop]
          C -->|Two| E[iPhone]
          C -->|Three| F[fa:fa-car Car]
          subgraph section
            C
            D
            E
            F
            G
          end

```

更多自定义主题设置：
[Theme Settings](https://mermaid.js.org/config/theming.html)