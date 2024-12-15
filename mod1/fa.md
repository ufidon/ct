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

![a⁺](./img/s20.png)

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

![conv1](./img/c1.png)

- convention 2

![conv2](./img/c2.png)

- convention 3

![conv3](./img/c3.png)

- or simply,

![conv4](./img/c4.png)

- Run the FA with `aaaabba, bbaabbbb`
- This FA accepts $`\mathbf{(a+b)^*b(a+b)^*}`$

🍎 Building FAs given REs or languages
---
- $\mathbf{(a+b)^+}$
  - the set of all strings except $\mathbf{ϵ}$

![abp](./img/abp.png)

- ---
- $\mathbf{(a+b)^*}$
  - `±` means the state is both initial and final

![all](./img/all.png)


---

Two types of FAs that accept NO languages
---
- FAs that have no final states
 ![no1](./img/no1.png)
- FAs whose final states cannot be reached from the start sate
 ![no21](./img/no21.png)
 ![no22](./img/no22.png)

- ---
- all words over alphabet $Σ=\lbrace a,b\rbrace$ with even number of letter

  ![even](./img/even.png)

- ---
- $\mathbf{a(a+b)^*}$
  - all words begin with $a$

![aall](./img/aall.png)

- or with two final states

![two finals](./img/f2.png)

- or with more final states
  - ⚠️ there is no unique FA for a given language

![four finals](./img/f4.png)

- ---
-  L = {`aaa`, `bbb`}
  - ⚠️ any finite languages can be built similarly

![a3b3](./img/a3b3.png)

- ---
- all words containing a triple letter, either `aaa` or `bbb`

![ca3b3](./img/ca3b3.png)

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

![fa1](./img/fa1.png)

- strings have a double letter in them
  - $\mathbf{(a+b)^*(aa+bb)(a+b)^*}$

- ---
- FA2

![fa2](./img/fa2.png)

- words with b as the third letter
  - $\mathbf{(aab+abb+bab+bbb)(a+b)^*}$, or
  - $\mathbf{(a+b)^2b(a+b)^*}$

- ---
- FA3

![fa3](./img/fa3.png)

- L={baa}

- ---
- FA4

![fa4](./img/fa4.png)

- L={baa,ab}

- ---
- FA5

![fa5](./img/fa5.png)

- $`\mathbf{a^*(a^*ba^*ba^*ba^*)^*(a + a^*ba^*ba^*ba^*)}`$
  - or, $\mathbf{(a + ba^*ba^*b)^+}$
  - this FA does not accept ϵ
  - to accept ϵ as well, use the FA below
    - $`\mathbf{(a^*ba^*ba^*ba^*)^*}`$

![fa5p](./img/fa5p.png)

- ---
- FA6

![fa6](./img/fa6.png)

- L = {ϵ}

- ---
- FA7

![fa7](./img/fa7.png)

- $\mathbf{(a+b)^*a}$
  - has no ϵ

- ---
- FA8

![fa8](./img/fa8.png)

- all words not end in b
  - $\mathbf{(a+b)^*a+ϵ}$

- ---
- FA9

![fa9](./img/fa9.png)

- all words with an odd number of a 's
  - $`\mathbf{b^*ab^*(ab^*ab^*)^*}`$

- ---
- FA10

![fa10](./img/fa10.png)

- all words with a double a in them somewhere
  - $`\mathbf{(a + b)^*aa(a + b)^*}`$

- ---
- FA11

![fa11](./img/fa11.png)

- all words that have different first and last letters
  - $\bm{a(a + b)^*b+b(a + b)^*a}$

- ---
- FA12

![fa12](./img/fa12.png)

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

![fa13](./img/fa13.png)