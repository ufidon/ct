__Finite automata__

_ict chapter 5_


Introduction
---
- Finite automata (FA) are one of the mathematical models of computation
  - called finite state automata (FSA)
- A FA has a finite set of states
  - it transits from states to states based on the current states and inputs
  - it has one start state and zero or more end states

🍎 Demo
---
Run the FA with input strings `a, aa, aaa, aaaa` over $Σ=\lbrace a \rbrace$ separately:
```mermaid
flowchart LR
  q0(("-"))
  q1(("+"))
  q0-->|a|q1
  q1-->|a|q1
```
- `⊖` is the start state, `⊕` is the final state
- if a string $s$ runs the $FA$ into its final state we say
  - FA accepts, or recognizes $s$, denoted as $s∈FA$
  - otherwise, FA rejects the string, denoted as $s∉FA$
- if $∀s∈L: s∈FA$, we say language $L$ is defined by the $FA$, or
  - $FA$ accepts $L$
- the FA above accepts string {a,aa,aaa,⋯}, i.e. the language $a^+$


Formal definition of FA
---
A FA is a 5-tuple $(Q,Σ,q_0,A,δ)$  where

- $Q$ is a finite set of states
- $Σ$ is a finite input alphabet
- $q_0∈Q$ is the initial or start state
- $A⊆Q$ is the set of accepting states
- $δ:Q×Σ→Q$ is the transition function

The transition function $δ(q,σ)$ means

- The FA transits from state $q$ to state $q'=δ(q,σ)$ 
  - if it is in state $q∈Q$ and receives the input $σ∈Σ$
- ⚠️ For each state, every letter in $Σ$ and the next state must be specified


Related terms
---
- accepting state is also called 
  - halting state, terminal state, or final state
- FA is also called
  - finite acceptor, or language recognizer, 
  - since its sole job is to accept or recognize certain input strings and reject others
- ⚠️ FAs accept no language if 
  - they have no initial or final states, or
  - their final states cannot be reached because
    - they disconnected from other states, or
    - there are no arrows pointing at them


💡 Demo
---
Let $Σ=\lbrace a,b\rbrace, Q=\lbrace x,y,z\rbrace$, and $δ:Q×Σ→Q$ be defined in the table below

| input | a | b |
|:---:|:---:|:---:|
| `⊖` x | y | z |
| y | x | z |
| `⊕` z | z | z |

The transition function can be represented with the *transition graphs* below in three conventions:

- convention 1
```mermaid
flowchart LR
  q0(("x-"))
  q1(("y"))
  q2(("z+"))  
  
  q0-->|a|q1  
  q1-->|a|q0
  q0-->|b|q2
  q1-->|b|q2
  q2-->|"a,b"|q2
```
- convention 2
```mermaid
flowchart LR
  q0(("x"))
  q1(("y"))
  q2((("z")))  
  
  s-->q0
  q0-->|a|q1  
  q1-->|a|q0
  q0-->|b|q2
  q1-->|b|q2
  q2-->|"a,b"|q2
```
- convention 3
```mermaid
flowchart LR
  q0(("-"))
  q1((" "))
  q2(("+"))  
  
  q0-->|a|q1  
  q1-->|a|q0
  q0-->|b|q2
  q1-->|b|q2
  q2-->|"a,b"|q2
```

- Run the FA with `aaaabba, bbaabbbb`
- This FA accepts $\mathbf{(a+b)^*b(a+b)^*}$

🍎 Building FAs given REs or languages
---
- $\mathbf{(a+b)^+}$

```mermaid
flowchart LR
  q0(("-"))
  q1(("+"))
  
  q0-->|a|q1  
  q0-->|b|q1
  q1-->|"a,b"|q1
```

- ---
- $\mathbf{(a+b)^*}$
  - `±` means the state is both initial and final
```mermaid
flowchart LR
  q0(("±"))
  q0-->|"a,b"|q0
```
- ---
- all words over alphabet $Σ=\lbrace a,b\rbrace$ with even number of letter

```mermaid
flowchart LR
  q0(("±"))
  q1((" "))
  
  q0-->|"a,b"|q1  
  q1-->|"a,b"|q0
```
- ---
- $\mathbf{a(a+b)^*}$

```mermaid
flowchart LR
  q0(("-"))
  q1((" "))
  q2(("+"))  
  
  q0-->|b|q1  
  q1-->|"a,b"|q1
  q0-->|a|q2
  q2-->|"a,b"|q2
```
- or with two final states

```mermaid
flowchart LR
  q0(("-"))
  q1((" "))
  q2(("+"))
  q3(("+"))  
  
  q0-->|b|q1  
  q1-->|"a,b"|q1
  q0-->|a|q3
  q3-->|"a,b"|q2
  q2-->|"a,b"|q2
```

- or with more final states
  - ⚠️ there is no unique FA for a given language

```mermaid
flowchart LR
  q0(("-"))
  q1((" "))
  q2(("+"))
  q3(("+")) 
  q4(("+"))  
  
  q0-->|b|q1  
  q1-->|"a,b"|q1
  q0-->|a|q2
  q2-->|"a,b"|q3
  q3-->|"a,b"|q4
  q4-->|a|q3
  q4-->|b|q2
```
- ---
-  L = {`aaa`, `bbb`}
  - ⚠️ any finite languages can be built similarly

```mermaid
flowchart LR
  s(("-"))
  f(("+"))
  d((" "))
  s-->|a|a0((" "))
  a0-->|a|a1((" "))
  a0-->|b|d
  a1-->|a|f
  a1-->|b|d
  s-->|b|b0((" "))
  b0-->|b|b1((" "))
  b0-->|a|d
  b1-->|b|f
  b1-->|a|d
  f-->|"a,b"|d
  d-->|"a,b"|d
```
- ---
- all words containing a triple letter, either `aaa` or `bbb`

```mermaid
flowchart LR
  s(("-"))
  f(("+"))
  s-->|a|a0((" "))
  a0-->|a|a1((" "))
  a0-->|b|b0
  a1-->|a|f
  a1-->|b|b0
  s-->|b|b0((" "))
  b0-->|b|b1((" "))
  b0-->|a|a0
  b1-->|b|f
  b1-->|a|a0
  f-->|"a,b"|f
```

䷼ Theorem
---
- A language acceptable by a FA can be defined by REs
- The language defined by a RE can be accepted by some FAs
- There are languages are neither accepted by FAs nor defined by REs

🍎 Find the language or RE accepted by a given FA
---
- path: concatenation
- branch: union
- loop: Star closure


- FA1:
```mermaid
flowchart LR
  s(("1-"))
  f(("4+"))
  s-->|a|q2((2))
  q2-->|a|f
  s-->|b|q3((3))
  q3-->|b|f
  q2-->|b|q3
  q3-->|a|q2
  f-->|"a,b"|f
```
- strings have a double letter in them
  - $\mathbf{(a+b)^*(aa+bb)(a+b)^*}$

- ---
- FA2
```mermaid
flowchart LR
  q1(("1-"))
  q5(("5+"))

  q1-->|"a,b"|q2((2))
  q2-->|"a,b"|q3((3))
  q3-->|a|q4((4))
  q4-->|"a,b"|q4
  q3-->|b|q5
  q5-->|"a,b"|q5
```
- words with b as the third letter
  - $\mathbf{(aab+abb+bab+bbb)(a+b)^*}$, or
  - $\mathbf{(a+b)^2b(a+b)^*}$

- ---
- FA3
```mermaid
flowchart LR
  q1(("-"))
  q4(("+"))
  d((" "))
  q1-->|b|q2((" "))
  q2-->|a|q3((" "))
  q3-->|a|q4
  q1-->|a|d
  q2-->|b|d
  q3-->|b|d
  q4-->|"a,b"|d
  d-->|"a,b"|d
```
- L={baa}

- ---
- FA4
```mermaid
flowchart LR
  s(("-"))
  f1(("+"))
  f2(("+"))
  d(("☠"))
  d-->|"a,b"|d
  s-->|a|q11((" "))
  q11-->|b|f1
  q11-->|a|d
  f1-->|"a,b"|d
  s-->|b|q21((" "))
  q21-->|b|d
  q21-->|a|q22((" "))
  q22-->|a|f2
  q22-->|b|d
  f2-->|"a,b"|d
```
- L={baa,ab}

- ---
- FA5
```mermaid
flowchart LR
  q1(("1-"))
  q3(("3+"))

  q1-->|b|q2((2))
  q1-->|a|q3
  q2-->|b|q4((4))
  q2-->|a|q2
  q3-->|a|q3
  q3-->|b|q2
  q4-->|b|q3
  q4-->|a|q4
```
- $\mathbf{a^*(a^*ba^*ba^*ba^*)^*(a + a^*ba^*ba^*ba^*)}$
  - or, $\mathbf{(a + ba^*ba^*b)^+}$
  - this FA does not accept ϵ
  - to accept ϵ as well, use the FA below
    - $\mathbf{(a^*ba^*ba^*ba^*)^*}$
```mermaid
flowchart LR
  q1(("±"))
  q2((" "))
  q3((" "))

  q1-->|a|q1
  q1-->|b|q2
  q2-->|a|q2
  q2-->|b|q3
  q3-->|a|q3
  q3-->|b|q1
```
- ---
- FA6
```mermaid
flowchart LR
  q1(("±"))
  q2(("☠"))

  q1-->|"a,b"|q2
  q2-->|"a,b"|q2
```
- L = {ϵ}

- ---
- FA7
```mermaid
flowchart LR
  q1(("-"))
  q2(("+"))

  q1-->|b|q1
  q1-->|a|q2
  q2-->|a|q2
  q2-->|b|q1
```
- $\mathbf{(a+b)^*a}$
  - has no ϵ

- ---
- FA8
```mermaid
flowchart LR
  q1(("±"))
  q2((" "))

  q1-->|a|q1
  q1-->|b|q2
  q2-->|b|q2
  q2-->|a|q1
```
- all words not end in b
  - $\mathbf{(a+b)^*a+ϵ}$

- ---
- FA9
```mermaid
flowchart LR
  q1(("-"))
  q2(("+"))

  q1-->|b|q1
  q1-->|a|q2
  q2-->|b|q2
  q2-->|a|q1
```
- all words with an odd number of a 's
  - $\mathbf{b^*ab^*(ab^*ab^*)^*}$

- ---
- FA10
```mermaid
flowchart LR
  q1(("-"))
  q2((" "))
  q3(("+"))

  q1-->|b|q1
  q1-->|a|q2
  q2-->|b|q1
  q2-->|a|q3
  q3-->|"a,b"|q3
```
- all words with a double a in them somewhere
  - $\mathbf{(a + b)^*aa(a + b)^*}$

- ---
- FA11
```mermaid
flowchart LR
  q0(("-"))
  q11((" "))
  q12(("+"))
  q21((" "))
  q22(("+"))

  q0-->|a|q11
  q11-->|a|q11
  q11-->|b|q12
  q12-->|a|q11
  q12-->|b|q12
  q0-->|b|q21
  q21-->|b|q21
  q21-->|a|q22
  q22-->|b|q21
  q22-->|a|q22
```
- all words that have different first and last letters
  - $\mathbf{a(a + b)^*b+b(a + b)^*a}$

- ---
- FA12
```mermaid
flowchart LR
  q1(("1±"))
  q2((2))
  q3((3))
  q4((4))
  q1-->|b|q2
  q1-->|a|q3
  q2-->|b|q1
  q2-->|a|q4  
  q3-->|a|q1
  q3-->|b|q4
  q4-->|a|q2
  q4-->|b|q3  
```
- EVEN-EVEN: all words with  an even number of a's as well as an even number of b's
  - all words with an even number of b's will stop at state 1 and 3
  - all words with an even number of a's will stop at state 1 and 2
  - All words that end in state 1 have an even number of a's but an even number of b's
  - All words that end in state 2 have an even number of a's but an odd number of b's
  - All words that end in state 3 have an odd number of a's but an even number of b's
  - All words that end in state 4 have an odd number of a's and an odd number of b's
- $\mathbf{(aa+bb+(ab+ba)(aa+bb)^*(ab+ba))^*}$


Build a FA that can locate an English word or substring
---
- Locate dog
```mermaid
flowchart LR
  q1(("-"))
  q2((2))
  q3((3))
  q4(("4+"))

  q1-->|"all except d"|q1
  q1-->|d|q2
  q2-->|"all except d,o"|q1
  q2-->|d|q2
  q2-->|o|q3
  q3-->|d|q2
  q3-->|"all except d,g"|q1
  q3-->|g|q4
  q4-->|"any letter"|q4
```