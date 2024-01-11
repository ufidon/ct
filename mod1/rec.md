__Recursive Definition and Proof__

_ict chapter 3_

Define the set of even numbers $E$ *recursively*
---
- Rule 1: 
  - Basic elements: $0 ∈ E$
  - seed elements
- Rule 2:
  - Recursive step: if $n ∈ E$, then $n±2 ∈ E$
  - construct other elements in the set from the basic elements
- Rule 3:
  - The elements in $E$ can only be produced through the recursive step from the basic elements
  - this rule is redundant and usually omitted


An alternative construction of $E$
---
- Basic elements: $2 ∈ E$
- Recursive step: if $m,n ∈ E$, then $m±n ∈ E$
- To prove an element belongs to a set defined recursively
  - prove by construction, i.e.
  - show the element can be constructed using the rules


💡 Demo
---
- Prove that $20 ∈ E$ using definition 1
  - Start from rule 1 then apply rule 2 ten times
- Prove that $20 ∈ E$ using definition 2
  - What is minimum number of steps used to construct 20?
- ☠ Challenge: prove or disprove $n ∈ E$
    - find the minimum number of steps


📝 Practice
---
- Define the following sets recursively
  - the set of natural numbers $N$
    - the set of positive integers $N^+$ 
  - the set of integers $Z$
  - the set of odd numbers
  - the set of positive real numbers $R^+$


💀 Define the set of real numbers $R$ recursively
---
- Does the following two rules work?
  - Rule 1: $1 ∈ R$
  - Rule 2: $a,b \in R → a+b ∈ R, a-b ∈ R, a×b∈R, a÷b∈R$
- What numbers are defined by the two rules exactly?


Define the set of polynomials of variable $x$ recursively
---
- Let's denote this set as $P_x$
- Formal definition:
  - A polynomial is a finite sum of terms
  - Each term is of the form a real number times a power of $x$
- Recursive definition:
  - Rule 1 (seeds): 
    - $a ∈ R → a∈ P_x$, i.e. any number is in $P_x$
    - $x ∈ P_x$
  - Rule 2 (generators): $p, q∈P_x → p+q, p-q, (p), pq ∈ P_x$


💡 Demo
---
- Show $x^2+3x -7 ∈ P_x$
- ☠️ Prove all polynomials are differentiable


💡 Some interesting recursive definitions
---
- Adam's family tree $T$ 
  - Rule 1: Adam is in $T$
  - Rule 2: $p∈T → p$'s children $∈ T$
- the federal executive branch of government $F$
  - Rule 1: the president $∈ F$
  - Rule 2: $p∈F$ and $e$ works for $p → e∈F$
- factorial
  - Rule 1: $0!= 1$
  - Rule 2: $n! = n×(n-1)!$


💡 Recursive definitions for languages
---
- Positive decimal integers $D$
  - Rule 1: $1,2,3,4,5,6,7,8,9 ∈ D$
  - Rule 2: $i∈D → i0,i1,i2,i3,i4,i5,i6,i7,i8,i9 ∈ D$
- Kleene closure of language $L$
  - Rule 1:
    - $w∈L → w∈L^*$
    - $ϵ ∈ L^*$
  - rule 2:
    - $a,b ∈ L^* → ab ∈ L^*$
- Some special languages constructed from word $w$
  - $w^+=\{w,ww,www,⋯ \}$
    - Rule 1: $w∈w^+$
    - Rule 2: $x∈w^+ → wx∈w^+$
  - $w^*=\{ϵ,w,ww,www,⋯\}$
    - rule 1: $ϵ,w∈w^*$
    - rule 2: $x∈w^* → wx∈w^*$
  - $w^{odd} = \{w, www, wwwww, ⋯\}$
    - rule 1: $w∈w^{odd}$
    - rule 2: $x∈w^* → wwx∈w^*$


Arithmetic expressions (AEs)
---
- Let $E$ denote the set of AEs
- Rule 1: any number is $∈ E$
- Rule 2: 
  - $x∈E → (x), ❶±x ∈ E$ 
    - $x$ is not started with $±$ at ❶
  - $x,y∈E → ❷x±y, x*y, x/y, x**y∈E$
    - $y$ is not started with $±$ at ❷


🍎 Examples
---
- valid AEs
  - $3*(2+1)*5$
- valid but ambiguous AEs
  - $3+(2+1)*5$
  - $10/5/2$
    - can be resolved with extra parenthesis, operator precedence and associativity
  - these are problems of semantic not syntax



Recursive proof
---
- Computation theory is also called *recursive theory*
- statements on *recursive structures* can be proved or disproved recursively
- prove or disprove the following statements
  1. There exist AEs contain the character not shown in the definition such as `?,>, @`, etc.
  2. There exist AEs begin or end with symbol `*` or `/`
  3. There exist AEs begin ith symbol `+` or `-`
  4. There exist AEs end with symbol `+` or `-`
  5. No AE can contain the substring `//`


☠️ Well-formed formulas (WFFs)
---
- Let $W$ denotes the set of WFFs
- Investigated in sentential calculus or propositional calculus
- defined over $Σ=\{¬, →, ∨, ∧, (,)\} ∪$ `{Latin letters}` by
  - Rule 1: any single Latin letter is a WFF
  - Rule 2: 
    - $p∈W → (p),¬p ∈ W$
    - $p,q∈W → p→q, p∨q, p∧q∈ W$
- the parentheses in WFFs are balanced