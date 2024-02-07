二
---
$FA_0$
```mermaid
flowchart LR
  q1(("1±"))
  q2(("2"))
  q1-->|"a,b"|q2
  q2-->|"a,b"|q2
```
$FA_1$
```mermaid
flowchart LR
  q1(("w1-"))
  q2(("w2+"))
  q1-->|b|q1
  q1-->|a|q2
  q2-->|a|q2
  q2-->|b|q1
```
$FA_2$
```mermaid
flowchart LR
  q1(("x1-"))
  q2(("x2"))
  q3(("x3+"))
  q1-->|b|q1
  q1-->|a|q2
  q2-->|b|q3
  q2-->|a|q2
  q3-->|"a,b"|q3
```