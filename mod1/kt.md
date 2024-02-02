__Kleen's Theorem__

_ict chapter 7_



Theorem: Equal capability of RE,FA and TG
---
Any language that can be defined by
- regular expression, or
- finite automaton, or
- transition graph

can be defined by all three methods.

$∀L: L \coloneqq FA → L \coloneqq TG → L \coloneqq RE → L\coloneqq FA$



Proof
---
- Part ❶: $∀L: L \coloneqq FA → L \coloneqq TG$
  - Every language that can be defined by a finite automaton can also be defined by a transition graph.
- Part ❷: $∀L: L \coloneqq TG → L\coloneqq RE$
  - Every language that can be defined by a transition graph can also be defined by a regular expression.
- Part ❸: $∀L: L\coloneqq RE → L\coloneqq FA$
  - Every language that can be defined by a regular expression can also be defined by a finite automaton.


Proof of Part ❶:
---
- $∀L: L \coloneqq FA → L \coloneqq TG$
- Every FA is a TG. Done.


Proof of Part ❷:
---
- $∀L: L \coloneqq TG → L\coloneqq RE$
- prove by construction
  - construct a RE from an arbitrarily given TG and they define the same language
- the construction algorithm must
  - work for every conceivable TG
  - complete in a finite number of steps
- steps 
  - ➀ Simplify 
    - the start states to be one state without incoming edges and 
    - the final states to be one unique final state without outgoing edges
  - ➁ parallel edges are union-ed
  - ➂ eliminate states other than the start and final state
  - ➃ unite all edges from the start state to the final states


Step ➀: uniquefy start and final states
---
- Simplify the start states to be one start states *without incoming edges*
```mermaid
flowchart LR
s1((1-))-->|r1|q2((" "))-->f(("+"))
s2((2-))-->|r2|q3((" "))-->f(("+"))
s3((3-))-->|r3|q4((" "))-->f(("+"))
```
- is simplified to be
```mermaid
flowchart LR
s(("-"))-->|ϵ|s1
s-->|ϵ|s2
s-->|ϵ|s3
s1((1))-->|r1|q2((" "))-->f(("+"))
s2((2))-->|r2|q3((" "))-->f(("+"))
s3((3))-->|r3|q4((" "))-->f(("+"))
```
- ---
- Simplify the final states to be one unique final state without outgoing edges
```mermaid
flowchart LR
q1((" "))-->|r1|f1(("f1+"))
q2((" "))-->|r2|f1
q3((" "))-->|r3|f2(("f2+"))
f2-->|r4|f2
```
- is simplified to be
```mermaid
flowchart LR
q1((" "))-->|r1|f1(("f1"))
q2((" "))-->|r2|f1
q3((" "))-->|r3|f2(("f2"))
f2-->|r4|f2
f1-->|ϵ|f(("+"))
f2-->|ϵ|f(("+"))
```
- ---
- Simplify combined state and final states
```mermaid
flowchart LR
q1(("1"))-->|r1|f1(("±"))
f1-->|r2|f1
f1-->|r3|q3(("3"))
```
- is simplified to be
```mermaid
flowchart LR
q1(("1"))-->|r1|f1((" "))
f1-->|r2|f1
f1-->|r3|q3(("3"))
s(("-"))-->|ϵ|f1
f1-->|ϵ|f(("+"))
```

Step ➁: Unite  parallel edges
---
- loops on a single state
```mermaid
flowchart LR
q1((" "))-->|r1|q1
q1-->|r2|q1
q1-->|r3|q1
```
- is simplified to be
```mermaid
flowchart LR
q1((" "))-->|"r1+r2+r3"|q1
```
- ---
- unite parallel edges
```mermaid
flowchart LR
q1((" "))-->|r1|q2((" "))
q1-->|r2|q2
q1-->|r3|q2
```
- to be
```mermaid
flowchart LR
q1((" "))-->|"r1+r2+r3"|q2((" "))
```
- ---

Step ➂: eliminate states
---
- concatenate segments on a single path
```mermaid
flowchart LR
q1(("1"))-->|r1|q2(("2"))
q2-->|r2|q3(("3"))
```
- eliminate state 2
```mermaid
flowchart LR
q1(("1"))-->|r1r2|q3(("3"))
```
- ---
```mermaid
flowchart LR
q1(("1"))-->|r1|q2(("2"))
q2-->|r2|q2
q2-->|r3|q3(("3"))
```
- eliminate state 2
```mermaid
flowchart LR
q1(("1"))-->|r1r2*r3|q3(("3"))
```
- ---
```mermaid
flowchart LR
q1(("1"))-->|r1|q2(("2"))
q2-->|r2|q2
q2-->|r3|q3(("3"))
q2-->|r4|q4(("4"))
q2-->|r5|q5(("5"))
```
- eliminate state 2
```mermaid
flowchart LR
q1(("1"))-->|r1r2*r3|q3(("3"))
q1-->|r1r2*r4|q4(("4"))
q1-->|r1r2*r5|q5(("5"))
```
- ---
- eliminate a state with multiple incoming edges and outgoing edges
  - consider all passing routes
  - use cartesian product of the incoming edges and outgoing edges

```mermaid
flowchart LR
s(("-"))-->|ϵ|q1
s(("-"))-->|ϵ|q3
q1(("1"))-->|r1|q2(("2"))
q3(("3"))-->|r3|q2
q2-->|r2|q2
q2-->|r4|q4(("4"))
q2-->|r5|q5(("5"))
q4-->|ϵ|f(("+"))
q5-->|ϵ|f
```
- eliminate state 2
```mermaid
flowchart LR
s(("-"))-->|ϵ|q1(("1"))
s(("-"))-->|ϵ|q3(("3"))
q1-->|r1r2*r4|q4(("4"))
q1-->|r1r2*r5|q5(("5"))
q3-->|r3r2*r4|q4(("4"))
q3-->|r3r2*r5|q5(("5"))
q4-->|ϵ|f(("+"))
q5-->|ϵ|f
```
- ---
```mermaid
flowchart LR
q1(("1"))-->|r1|q2(("2"))
q2-->|r2|q2
q2-->|r4|q1
q3(("3"))-->|r3|q2
```
- eliminate state 2
```mermaid
flowchart LR
q1(("1"))-->|"r1r2*r4"|q1
q3(("3"))-->|"r3r2*r4"|q1
```
- ---
```mermaid
flowchart LR
q1(("1"))-->|r1|q1
q2(("2"))-->|r2|q2
q1-->|r12|q2
q2-->|r21|q1
q1-->|r13|q3(("3"))
q3-->|r31|q1
q2-->|r23|q3
q3-->|r32|q2
q3-->|r3|q3
```
- eliminate state 2
```mermaid
flowchart LR
q1(("1"))
q3(("3"))
q1-->|"r1+r12r2*r21"|q1
q1-->|"r13+r12r2*r23"|q3
q3-->|"r31+r32r2*r21"|q1
q3-->|"r3+r32r2*r23"|q3
```

- ---
```mermaid
flowchart LR
q1(("1"))-->|r12|q2(("2"))
q3(("3"))-->|r32|q2
q2-->|r2|q2
q2-->|r23|q3
q3-->|r3|q3
q3-->|r31|q1
q2-->|r24|q4(("4"))
q4-->|r4|q4
q4-->|r41|q1
q2-->|r25|q5(("5"))
```
- eliminate state 2
  - incoming edges from: 1,3
  - outgoing edges: 3,4,5
- 1 →2→ 3: r12r2*r23
- 1 →2→ 4: r12r2*r24
- 1 →2→ 5: r12r2*r25
- 3 →2→ 3: r32r2*r23
- 3 →2→ 4: r32r2*r24
- 3 →2→ 5: r32r2*r25


Step ➃: unite all edges from the start state to the final states
---
```mermaid
flowchart LR
q1(("-"))-->|r1|q2(("+"))
q1-->|r2|q2
q1-->|r3|q2
```
- becomes
```mermaid
flowchart LR
q1(("-"))-->|"r1+r2+r3"|q2(("+"))
```

The state-elimination algorithm that derives the RE from an arbitrary TG
---
- Create a unique, unenterable minus state and a unique, unleaveable plus state
- bypass and eliminate all the non - or + states in the TG
  - A state is bypassed by connecting each incoming edge with each outgoing edge
  - The label of each resultant edge is the concatenation of 
    - the label on the incoming edge with
    - the label on the loop edge if there is one and 
    - the label on the outgoing edge
- When two states are joined by more than one edge going in the same direction, unify them by adding their labels
- Finally, when all that is left is one edge from - to + , the label on that edge is a regular expression that generates the same language as was recognized by the original machine


🍎 find the REs for the following TGs
---
- Example 1
```mermaid
flowchart LR
s(("-"))
s-->|"aa,bb"|q1((1))
q1-->|"a,b"|q1
q1-->|aa|e1(("+"))
q1-->|bb|e2(("+"))
```
- is simplified to be
```mermaid
flowchart LR
s(("-"))
s-->|"aa+bb"|q1((1))
q1-->|"a+b"|q1
q1-->|aa|e1((" "))
q1-->|bb|e2((" "))
e1-->|ϵ|f(("+"))
e2-->|ϵ|f
```
- →
```mermaid
flowchart LR
s(("-"))
s-->|"aa+bb"|q1((1))
q1-->|"a+b"|q1
q1-->|"aa+bb"|f(("+"))
```
- →
```mermaid
flowchart LR
s(("-"))
s-->|"(aa+bb)(a+b)*(aa+bb)"|f(("+"))
```
- ---
- Example 2
```mermaid
flowchart LR
q1(("q1±"))-->|"ab,ba"|q2(("2"))
q1-->|"aa,bb"|q1
q2-->|"aa,bb"|q2
q2-->|"ab,ba"|q1
```
- →
```mermaid
flowchart LR
s(("-"))-->|ϵ|q1
q1(("q1"))-->|"ab+ba"|q2(("2"))
q1-->|ϵ|e(("+"))
q1-->|"aa+bb"|q1
q2-->|"aa+bb"|q2
q2-->|"ab+ba"|q1
```
- →
```mermaid
flowchart LR
s(("-"))-->|ϵ|q1(("q1"))
q1-->|ϵ|e(("+"))
q1-->|"(aa+bb)+(ab+ba)(aa+bb)*(ab+ba)"|q1
```
- →
```mermaid
flowchart LR
s(("-"))-->|"((aa+bb)+(ab+ba)(aa+bb)*(ab+ba))*"|e(("+"))
```
- ---
- Example 3
```mermaid
flowchart LR
s(("-"))-->|ϵ|q1(("q1"))
q1-->|a|q2(("2"))
q1-->|"b"|q3((3))
q2-->|b|q2
q2-->|a|e(("+"))
q2-->|a|q3
q3-->|a|q3
q3-->|b|q2
q3-->|"ϵ"|e
```
- →
```mermaid
flowchart LR
q1(("q1-"))-->|a|q2(("2"))
q1-->|"b"|q3((3))
q2-->|b|q2
q2-->|a|e(("+"))
q2-->|a|q3
q3-->|a|q3
q3-->|b|q2
q3-->|"ϵ"|e
```
- eliminate state 2
  - incoming edges: 1, 3
  - outgoing edges: 3, +
- →
```mermaid
flowchart LR
q1(("q1-"))-->|"ab*a"|e(("+"))
q1-->|"ab*a"|q3
q1-->|b|q3
q3-->|a|q3(("3"))
q3-->|"bb*a"|q3
q3-->|"bb*a"|e
q3-->|"ϵ"|e
```
- →
```mermaid
flowchart LR
q1(("q1-"))-->|"ab*a"|e(("+"))
q1-->|"b+ab*a"|q3
q3-->|"a+bb*a"|q3(("3"))
q3-->|"ϵ+bb*a"|e
```
- →
```mermaid
flowchart LR
q1(("q1-"))
e(("+"))
q1-->|"ab*a+(b+ab*a)(a+bb*a)*(ϵ+bb*a)"|e
```

📝 Practice
---
- Redo example 3 by eliminating state 3


Proof of Part ❸
---
- $∀L: L\coloneqq RE → L\coloneqq FA$
- Prove by recursive definition of RE and constructive algorithm for FA side by side
- RE is recursively generated from the seeds such as letters from an alphabet Σ and the empty string ϵ by  __addition, concatenation, and closure__
  - σ is an arbitrary letter in Σ


Step ➀: Build FAs for the seeds
---
- A FA accepts only the empty string ϵ 
```mermaid
flowchart LR
q1(("q1±"))
d(("☠️")) 
q1-->|"all σ"|d
d-->|"all σ"|d
```
- A FA accepts only the specified letter σ1∈Σ 
```mermaid
flowchart LR
q1(("q1-"))
e(("+"))
d(("☠️")) 
q1-->|"σ1"|e
q1-->|"all σ except σ1"|d
d-->|"all σ"|d
e-->|"all σ"|d
```

Step ➁: Unite FAs
---
- FA1 accepts L(r1), FA2 accepts L(r2), then there is a FA3 accepts L(r1+r2). Let's denote this as FA3 = FA1+FA2.


🍎 Example
---
Given FA1 and FA2, build FA3 = FA1+FA2.
- FA1: all words with a double a in them somewhere
```mermaid
flowchart LR
  q1(("-x1"))
  q2(("x2"))
  q3(("+x3"))

  q1-->|b|q1
  q1-->|a|q2
  q2-->|b|q1
  q2-->|a|q3
  q3-->|"a,b"|q3
```

- FA2: EVEN-EVEN
```mermaid
flowchart LR
  q1(("±y1"))
  q2((y2))
  q3((y3))
  q4((y4))
  q1-->|b|q2
  q1-->|a|q3
  q2-->|b|q1
  q2-->|a|q4  
  q3-->|a|q1
  q3-->|b|q4
  q4-->|a|q2
  q4-->|b|q3  
```

- Transition table of FA1

| state\input | a | b |
|:---:|:---:|:---:|
| -x1  | x2 | x1 |
| x2 | x3 | x1 |
| +x3 | x3 | x3 |

- Transition table of FA2

| state\input | a | b |
|:---:|:---:|:---:|
| ±y1 | y3 | y2 |
|  y2 | y4 | y1 |
| y3 | y1 | y4 |
| y4 | y2 | y3 |

- FA3 tracks the transition on both FA1 and FA2, each state in FA3 will combine the states from FA1 and FA2 based on their transitions
  - $z_{start}=x_{start} \text{ or } y_{start}$
  - $z_{next}$ after letter σ = ($x_{next}$ after letter σ) or ($y_{next}$ after letter σ) 
  - +z contains at least one final state from FA1 or FA2

- Transition table of FA3

| FA3 | FA1+FA2 | a | b |
|:---:|:---:|:---:|:---:|
| ±z1 | -x1 or ±y1 | z2 | z3 |
| z2  | x2 or y3 | z4 | z5 |
| z3  | -x1 or y2 | z6 | z1 |
| +z4 | +x3 or ±y1 | z7 | z8 |
| z5  | -x1 or y4 | z9 | z10 |
| z6  | x2 or y4 | z8 | z10 |
| +z7 | +x3 or y3 | z4 | z11 |
| +z8 | +x3 or y2 | z11 | z4 |
| z9  | x2 or y2 | z11 | z1 |
| z10 | -x1 or y3 | z12 | z5 |
| +z11| +x3 or y4 | z8 | z7 |
| +z12| x2 or ±y1 | z7 | z3 |


📝 Practice
---
P1: Find the FA3 = FA1 + FA2

- FA1: 
```mermaid
flowchart LR
  q1(("-x1"))
  q2(("x2"))
  q3(("+x3"))

  q1-->|b|q1
  q1-->|a|q2
  q2-->|b|q1
  q2-->|a|q3
  q3-->|"a,b"|q3
```
- FA2:
```mermaid
flowchart LR
  q1(("-y1"))
  q2(("+y2"))

  q1-->|a|q1
  q1-->|b|q2
  q2-->|b|q2
  q2-->|a|q1
```
- FA3:
  - -z1 = x1 or y1
  - z2 = x2 or y1
  - z3+ = x1 or y2+
  - z4+ = x3+ or y1
  - z5+ = x3+ or y2+
```mermaid
flowchart LR
  z1(("z1-"))-->|a|z2(("z2"))
  z1-->|b|z3(("z3+"))
  z2-->|b|z3
  z3-->|a|z2
  z3-->|b|z3
  z2-->|a|z4(("z4+"))
  z4-->|a|z4
  z4-->|b|z5(("z5+"))
  z5-->|b|z5
  z5-->|a|z4
```
- ---
P2: Find the FA3 = FA1 + FA2

- FA1:  all words that end in a
```mermaid
flowchart LR
  q2(("x1-"))
  q1(("x2+"))
  q1-->|a|q1
  q1-->|b|q2
  q2-->|b|q2
  q2-->|a|q1
```

- FA2: all words with an odd number of letters
```mermaid
flowchart LR
  q1(("-y1"))
  q2(("+y2"))
  q1-->|"a,b"|q2
  q2-->|"a,b"|q1
```

- FA3:  all words that either have
an odd number of letters or end in a

```mermaid
flowchart LR
  q11(("z1-=<br>x1- or y1-"))
  q22(("z2+=<br>x2+ or y2+"))
  q12(("z3+=<br>x1- or y2+"))
  q21(("z4+=<br>x2+ or y1-"))
  q11-->|a|q22
  q22-->|b|q11
  q11-->|b|q12
  q12-->|b|q11
  q12-->|a|q21
  q21-->|b|q12
  q21-->|a|q22
  q22-->|a|q21
```

- ---
P3: Find the FA3 = FA1 + FA2
- Let's solve it in two methods
  - ⓵ build new states of FA3 as needed
  - ⓶ build all FA3 states beforehand

- FA1:  all words that end in a
```mermaid
flowchart LR
  q2(("x1-"))
  q1(("x2+"))
  q1-->|a|q1
  q1-->|b|q2
  q2-->|b|q2
  q2-->|a|q1
```

- FA2: all words that end in b
```mermaid
flowchart LR
  q1(("-y1"))
  q2(("+y2"))
  q1-->|"b"|q2
  q1-->|a|q1
  q2-->|"a"|q1
  q2-->|b|q2
```

- FA3:   all words ending in a or b, that is, all words except ϵ
  - ⓵ a new state in FA3 is built when it's needed

```mermaid
flowchart LR
  q11(("z1-=<br>x1- or y1-"))
  q12(("z2+=<br>x1- or y2+"))
  q21(("z3+=<br>x2+ or y1-"))
  q11-->|b|q12
  q12-->|b|q12
  q11-->|a|q21
  q21-->|a|q21
  q12-->|a|q21
  q21-->|b|q12
```
- ---
- ⓶ All the states in FA3 can also be built beforehand as the Cartesian product of all FA1 states and all FA2 states
  - create all the transitions
  - remove all unreachable states and their edges
    - such as state z4

```mermaid
flowchart LR
  q11(("z1-=<br>x1- or y1-"))
  q12(("z2+=<br>x1- or y2+"))
  q21(("z3+=<br>x2+ or y1-"))
  q22(("z4+=<br>x2+ or y2+"))
  q11-->|b|q12
  q12-->|b|q12
  q11-->|a|q21
  q21-->|a|q21
  q12-->|a|q21
  q21-->|b|q12
  q22-->|a|q21
  q22-->|b|q12
```

Step ③: Concatenate FAs
---
- FA1 accepts L(r1), FA2 accepts L(r2), then there is a FA3 accepts L(r1r2). Let's denote this as FA3 = FA1FA2.


💡 Demo
---
What could go wrong?

Given FA1: all words with b as the second letter
```mermaid
flowchart LR
  q1(("q1-"))
  q2(("q2"))
  q3(("q3+"))
  q4(("q4"))

  q1-->|"a,b"|q2
  q2-->|b|q3
  q3-->|"a,b"|q3
  q2-->|a|q4
  q4-->|"a,b"|q4
```
and FA2: all words that have an odd number of a's
```mermaid
flowchart LR
  q1(("-"))
  q2(("+"))

  q1-->|b|q1
  q1-->|a|q2
  q2-->|b|q2
  q2-->|a|q1
```

- An intuitive but wrong construction of FA3=FA1FA2:
  - suppose we can jump somehow from q3+ to x1-
```mermaid
flowchart LR
  q1(("q1-"))
  q2(("q2"))
  q3(("q3+"))
  q4(("q4"))

  q1-->|"a,b"|q2
  q2-->|b|q3
  q3-->|"a,b"|q3
  q2-->|a|q4
  q4-->|"a,b"|q4

  q3-->|"↷"|qs1

  qs1(("x1-"))
  qs2(("x2+"))

  qs1-->|b|qs1
  qs1-->|a|qs2
  qs2-->|b|qs2
  qs2-->|a|qs1  
```

- Run the strings below on FA3
- ababbaa = (ab)(abbaa)
  - (ab) ∈ FA1, (abbaa) ∈ FA2
  - ∴ (ab)(abbaa)=ababbaa ∈ FA3
  - (ab) on FA1 stops at q3
  - then jump to x1 to run (abbaa)
  - and it is accepted
- ababbab = (abab)(bab)
  - (abab) ∈ FA1, (bab) ∈ FA2
  - ∴ (abab)(bab)=ababbab ∈ FA3
  - (ab) on FA1 stops at q3, 
  - if now we jump to FA2, (abbab) will be rejected
  - if we run (abab) on FA1, then (bab) will be accepted on FA2
- However, an FA must be deterministic without operator's choice.


💡 Demo
---
Another idea.

Given FA1: 

- all words with a double a in them somewhere
- $\mathbf{(a + b)^*aa(a + b)^*}$

```mermaid
flowchart LR
  q1(("x1-"))
  q2(("x2"))
  q3(("x3+"))

  q1-->|b|q1
  q1-->|a|q2
  q2-->|b|q1
  q2-->|a|q3
  q3-->|"a,b"|q3
```

and FA2:
- all words end in b
  - $\mathbf{(a+b)^*b}$
```mermaid
flowchart LR
  q1(("y1-"))
  q2(("y2+"))

  q1-->|a|q1
  q1-->|b|q2
  q2-->|b|q2
  q2-->|a|q1
```

FA3:
- z1- = x1-
- z2 = x2
- z3 = x3+ or y1-
- z4+ = x3+ or y1- or y2+
```mermaid
flowchart LR
  q1(("z1-"))
  q2(("z2"))
  q3(("z3"))
  q4(("z4+"))

  q1-->|b|q1
  q1-->|a|q2
  q2-->|b|q1
  q2-->|a|q3
  q3-->|"a"|q3
  q3-->|b|q4
  q4-->|a|q3
  q4-->|b|q4
```

Algorithm for constructing FA_3 = FA1FA2
---
- make a z-state for every nonfinal x-state in FA1 before hitting its final states
- for every FA1 final state, a z-state of is created = this FA1 final state or y1- in FA2, then trace the running of the remain string from there, so a z-state is
  - in one and only one x-somestate or a set of y-somestates
- the accepted string must stop at a FA2 final state
  - so a z-final state must contain a y-final state


📝 Practice
---
Given FA1 and FA2 below, find FA3=FA1FA2

- FA1: all words that start with b
- all words start with b
  - $\mathbf{b(a+b)^*}$
```mermaid
flowchart LR
  q1(("x1-"))
  q2(("x2"))
  q3(("x3+"))

  q1-->|a|q2
  q1-->|b|q3
  q2-->|"a,b"|q2
  q3-->|"a,b"|q3
```

- FA2: all words that end with b
- all words end in b
  - $\mathbf{(a+b)^*b}$
```mermaid
flowchart LR
  q1(("y1-"))
  q2(("y2+"))

  q1-->|a|q1
  q1-->|b|q2
  q2-->|b|q2
  q2-->|a|q1
```
- FA3 = FA1FA2: all words begin with b and end with b
  - z1 = x1-
  - z2 = x2
  - z3 = x3 or y1
  - z4 = x3 or y1 or y2

```mermaid
flowchart LR
  q1(("z1-"))
  q2(("z2"))
  q3(("z3"))
  q4(("z4+"))

  q1-->|b|q3
  q1-->|a|q2
  q2-->|"a,b"|q2
  q3-->|"a"|q3
  q3-->|b|q4
  q4-->|a|q3
  q4-->|b|q4
```

- FA3' = FA2FA1: all words with a double b in them
- z1- = y1-
- z2 = y2 or x1-
- z3 = y1- or x2
- z4 = y2+ or x1- or x3+
- z5 = y2+ or x1- or x2
- z6 = y1- or x2 or x3+
- z7 = y2 or x1- or x2 or x3+
 
```mermaid
flowchart LR
  q1(("z1-"))
  q2(("z2"))
  q3(("z3"))
  q4(("z4+"))
  q5(("z5"))
  q6(("z6+"))
  q7(("z7+"))

  q1-->|b|q2
  q1-->|a|q1
  q2-->|"b"|q4
  q2-->|a|q3
  q3-->|"a"|q3
  q3-->|b|q5
  q5-->|a|q3
  q5-->|b|q7
  q4-->|a|q6
  q4-->|b|q4
  q6-->|b|q7
  q6-->|a|q6
  q7-->|a|q6
  q7-->|b|q7
```

📝 Practice
---
Given FA1 and FA2 below, find FA3=FA1FA2

- FA1: all words that do not contain the substring aa.

```mermaid
flowchart LR
  q1(("x1±"))
  q2(("x2+"))
  q3(("x3"))

  q1-->|b|q1
  q1-->|a|q2
  q2-->|b|q1
  q2-->|a|q3
  q3-->|"a,b"|q3
```
- FA2:  all words with an odd number of letters
```mermaid
flowchart LR
  q1(("y1-"))
  q2(("y2+"))
  q1-->|"a,b"|q2
  q2-->|"a,b"|q1
```
- FA3 = FA1FA2:  all words but ϵ
```mermaid
flowchart LR
  q1(("x1±"))
  q2(("x2+"))
  q3(("x3"))

  q1-->|b|q1
  q1-->|a|q2
  q2-->|b|q1
  q2-->|a|q3
  q3-->|"a,b"|q3
```


Step ④: Star-close FAs
---
- FA1 accepts L(r), then there is a FA2 accepts L(r*). Let's denote this as FA2 = FA1*.