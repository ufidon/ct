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
  - No for $L_2$, yes for $L3$.



💡 Demo
---
- Type mathematics
  - use equation editor in [Canvas](https://lx.uts.edu.au/collections/building-your-canvas-course/resources/canvas-math-editor/)
  - [write equations in Word](https://support.microsoft.com/en-us/office/write-an-equation-or-formula-1d01cabc-ceb1-458d-bc70-7f9737722702)
  - use [$\LaTeX$](https://en.wikibooks.org/wiki/LaTeX) on website [Overleaf](https://www.overleaf.com/)
  - Further reference [The Not So Short Introduction to $\LaTeX$ 2ε](https://mirror.mwt.me/ctan/info/lshort/english/lshort.pdf)


💡 Demo
---
- frequently-used symbols in computation theory
- `α, β, γ, δ, ϵ, λ, σ, Σ, ≠, ≤, ≥, →, ⇒, ∧, ∨, ∈, ∩, ∪, ⊂, ⊆, ∀, ∃, N, Z, Q, R, C`



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
  - also called *Kleene closure*
- $\displaystyle L^+ = L^1∪L^2∪⋯ = ∪_{k=1}^∞L^k$
  - the plus operation is also called *positive closure*


💡 Demo
---
- Given $L=\{a,ϵ\}$, find $L^k$ for k=0,1,2,3
- Is $L^+ = L^*$?
  - ans: Yes. If $L$ contains $ϵ$
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
    - ans: $Σ^* = \{ϵ, 0, 1, 00, 01, 10, 11, 000, 001, ⋯\}$
  - $Σ=\{u\}$
    - ans: $Σ^* = \{ϵ, u, uu, uuu, ⋯\}$
  - $Σ=\{a,b,c\}$
    - ans: $Σ^* = \{ϵ, a,b,c,aa, ab, ac, ba,bb,bc, ca,cb, cc, aaa, ⋯\}$
  - $Σ=\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$
    - ans: $Σ^* = \{ϵ, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 00, 01, 02,  ⋯\}$
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

| length | palindromes |
|:---:|:---:|
| 0 | ϵ |
| 1 | a, b |
| 2 | aa, bb |
| 3 | aaa,aba, bbb, bab |
| 4 | aaaa, abba, bbbb, baab |
| 5 | aaaaa, aabaa, abbba, ababa, bbbbb, bbabb, baaab, babab |


💡 Demo: Kleene closure on languages
---
Describe the Kleene closures of the following languages in plain English
- $S_1=\{aa,b\}$
  - $S_1^* =$ {ϵ and any word including aa and b as factors}
  - = {ϵ and all strings of a's and b's where the a's occur in even groups}
  - = {ϵ, b, aa, bb, aab, baa, bbb, aaaa, aabb,baab, bbaa, bbbb, aaaab, ⋯}
- $S_2=\{a,ab\}$
  - $S_2^*=$ {ϵ and any word composed of factors of a and ab}
  - = {ϵ and all strings of a's and b's except those that start with b and those that contain a double b}
  - = {ϵ,a,aa,ab,aaa,aab,aba,aaaa,aaab,aaba, abaa,abab, aaaaa,aaaab,⋯}


Factoring of strings in $S^*$
---
- A word in $S^*$ can be written as a concatenate of words from $S$
  - e.x. `abaaba` ∈ $S_2*$ since
  - `abaaba = (ab)(a)(ab)(a)`
  - this factoring is unique
- $S_3=\{xx,xxx\}, S_3^*$=
  - {ϵ and all strings of more than one x} 
  - {$x^n$ for $n=0,2,3,4,5,⋯$}
  - {ϵ, xx, xxx, xxxx,xxxxx,xxxxxx,⋯}


💡Demo
---
- Factoring xxxxxx=$x^6 ∈ S_3^*$
  - the factoring is non-unique
    - (xx)(xx)(xx)=$x^2x^2x^2$
    - (xxx)(xxx)=$x^3x^3$
  - prove $S_3^*$ contains string of x's except one x
    - by constructive algorithm and strong induction


Special cases for Kleene closure
---
- $Σ=∅ → Σ^*=\{ϵ\}$
- $L=\{ϵ\} → L^*=\{ϵ\}$
- if two languages have identical base set of words, then their Kleene closures are equal
  - ex. $T_1=\{x,y,xy\} T_2=\{x,y,xx\} T_3=\{x,y,yy\}, T_4=\{x,y,xxxyyyx\}$
  - show that $T_1^* = T_2^* = T_3^* = T_4^*$


💡 Demo 
---
Find the Positive closure of $S=\{w_1,w_2,w_3\}$
- ans: $S^+ = \{w_1,w_2,w_3,w_1w_1, w_1w_2, w_1w_3,w_2w_1,w_2w_2,w_2w_3,w_3w_1, w_3w_2,w_3w_3,w_1w_1w_1,⋯\}$