__Overview of Computation Theory__

_ict chapter 1&2_

Intriguing questions
---
- What problems can be solved by computers?
  - What can not?
- How to evaluate the difficulty of a problem?
- How to evaluate a computer's capability?
- Two approaches:
  - Experimental methods
  - *Mathematical models*


Machines and languages
---
- The mathematical models developed in computation theory are called *machines*
- Algorithms are developed to solve problems
  - the *languages* used to write algorithms are computer programs
  - we focus on the form or structure of the languages instead of their semantics
    - so they are called *formal languages*
- The capability of a machine now can be interpreted in the languages it can understand or *accept*
- Three types of machines and their languages
  - Finite automata and regular languages
  - Pushdown automata and context-free languages
  - Turing machines and general languages


Prerequisites for computation theory
---
- Mathematical logic
- Set theory
- Mathematical proof


Formal languages
---
- A formal language $L$ is a set of strings
  - An empty language $Φ$ has no strings
  - can be finite or infinite
- A string or word is a sequence of symbols or letters from an alphabet $Σ$
  - An empty string $Λ$ or $ϵ$ has no symbols
- An alphabet $Σ$ is a finite set of symbols


🍎 Example
---
- A simple formal language $L$ defined over alphabet $Σ = \{a\}$
  - $L=\{ a, aa, aaa, ⋯ \}$ in list or 
  - $L=\{ a^n | n ∈ N ∩ n>0 \}$ in description


❓ Question
---
- How many strings of length less than 10 in the above language?
  - the *length* of a string $w$ is the number of symbols it has, denoted as $|w|$
    - $|ϵ|=0$
  - How about in $L_2=\{ a^{2n+1} | n ∈ N \}$?
  - and, in $L_3=\{ a^{2n} | n ∈ N \}$?
- Is the empty string in the above language?
  - No.



💡 Demo
---
- Type mathematics
  - use equation editor in [Canvas](https://lx.uts.edu.au/collections/building-your-canvas-course/resources/canvas-math-editor/)
  - [write equations in Word](https://support.microsoft.com/en-us/office/write-an-equation-or-formula-1d01cabc-ceb1-458d-bc70-7f9737722702)
  - use [$\LaTeX$](https://en.wikibooks.org/wiki/LaTeX) on website [Overleaf](https://www.overleaf.com/)
  - Further reference [The Not So Short Introduction to $\LaTeX$ 2ε](https://mirror.mwt.me/ctan/info/lshort/english/lshort.pdf)


String concatenation
---
- the *concatenation* of string $a$ and $b$ is $ab$
  - $ϵw=wϵ=w$
  - concatenation is NOT communicative
- the $k^{th}$ *power* of a string $a$ is concatenating $a$ $k$ times
  - $a^0 = ϵ$ 
    - ⚠️ Don't be confused with the mathematical power of 0
  - $a^k = a^{k-1}a$
- given a string $w=xyz$,
  - $x$ is a *prefix* of $w$,
  - $z$ is a *suffix* of $w$,
  - $y$ is a *subword, substring, index* or *factor* of $w$


💡 Demo
---
- Given $w=dog$, find all its prefixes, suffixes and factors
  - prefixes: $\{ϵ, d, do, dog\}$
  - suffixes: $\{ϵ, g, og, dog\}$
  - factors: $\{ϵ,d, do, g, og,dog \}$


The power operation on languages
---
- given two languages $L_1, L_2$, 
  - $L_1L_2$ denotes the language $L_3$ formed by concatenating any word in $L_1$ with any word in $L_2$
  - $L_3$ can be called the *Cartesian product* of $L_1$ and $L_2$
- the $k^{th}$ *power* of a language $L$ is cartesian-multiplying $L$ $k$ times
  - $L^0 = ∅ = \{ϵ\}$
    - ⚠️ Don't be confused with the mathematical power of 0
  - $L^k = L^{k-1}L$
- $L^*$, denotes the *closure of the power operation*, is defined as
  - $\displaystyle L^* = L^0∪L^1∪L^2∪⋯ = ∪_{k=0}^∞L^k$
- $L^+ = L^*-\{ϵ\}$, i.e. $L^*$ without the empty string


💡 Demo
---
- Given $L=\{a,ϵ\}$, find $L^k$ for k=0,1,2,3
- When will $L^* = L^+$?
  - ans: when $ϵ ∉ L$
- Is $L^* = (L^*)^* = L^{**}$ true for any language $L$?
  - ans: Yes. It is a theorem



💡 Demo
---
- Prove $L^* = (L^*)^* = L^{**}$ holds for any language $L$?
- prove by construction
  - any word in $L^{**}$ is concatenated from words in $L^*$
    - $L^*$ contains all concatenations of its own words
    - so, $L^{**} ⊆ L^*$
  - any word in $L^*$ is a factor of at least one word of $L^{**}$
    - so, $L^* ⊆ L^{**}$
- therefor, $L^* = L^{**}$


📝 Practice
---
- Given $L=\{x,y\}$, find $L^k$ for k=0,1,2,3
- Given $L=\{u,v,ϵ\}$, find $L^k$ for k=0,1,2,3


❓ Questions
---
- Find the number of words in the following languages
  - $A^*$ where $A=\{ϵ\}$
    - Ans: 1
  - $B^*$ where $B=\{b\}$ where $b≠ϵ$
    - Ans: ∞


Closure of an alphabet
---
- the universal set of all languages defined on the alphabet $Σ$
  - denoted as $Σ^*$
    - includes $ϵ$
  - this notation is also called the *Kleene star*
  - usually listed in *lexicographic* order



📝 Practice
---
- Find the Kleene closures for the following alphabets
  - $Σ=\{0,1\}$
  - $Σ=\{u\}$
  - $Σ=\{a,b,c\}$
  - $Σ=\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$
  - $Σ=∅$
    - ans: $Σ^* = \{ϵ\}$


String reverse and palindrome
---
- the reverse of a string has the same symbols but in reversed order
- a palindrome is a string that equals its reverse
- the language *PALINDROME* over a alphabet $Σ$ has
  - all the palindromes in $Σ^*$


💡 Demo
---
- Given $Σ = \{a,b\}$, find all palindromes of length 0,1,2,3,4,5
