__Regular expressions__

_ict chapter 4_

Regular expression (re) of a language
---
- denoted by boldface letters
- represents any word generally in the language
- e.x.
  - Let $S=\{x\} \text{ and } L_0=S^* = \{x\}^*$, i.e. $L_0=\{ϵ, x, xx, xxx, ⋯\}$
    - plain description: a language of any string of x's
  - define a re on $L_0$ as $\mathbf{x^*}$, which means
    - $\mathbf{x^*} = ϵ ∨ x ∨ x^2 ∨ x^3 ∨ ⋯ = x^n, (n \in \mathcal{N})$
    - rewrite $L_0=language \{\mathbf{x^*}\}=L(\mathbf{x^*})$


💡 Demo
---
- Describe $L_1=\{a, ab, abb, abbb, ⋯\}$ with
  - plain description: 
    - a language whose words are composed of one a and zero or more b's
  - re:
    - $L_1=L(\mathbf{ab^*})$
    - ⚠️ $\mathbf{ab^*}$ is different from $\mathbf{(ab)^*}$
      - i.e. power has higher precedence than concatenation
      - $\mathbf{(ab)^*}=(ab)^n, n∈\mathcal{N}$
- Describe $L_2=\{a, aa, aaa, aaaa, ⋯\}$ with
  - plain description: 
    - a language whose words are composed of one or more a's
  - re:
    - $L_2=L(\mathbf{aa^*})$
      - $\mathbf{a^+}=a^n, n∈\mathcal{N^+}$


❓ Question
---
1. Are these re equivalent?
   - $\mathbf{aa^*, a^*a, aa^*a^*, a^*aa^*, a^+a^*, a^*a^+,a^*a^*a^*aa^*, a^+a^*a^*a^+}$
     - ans: yes. all define the language $a^+$ except $\mathbf{a^+a^*a^*a^+}$ defines all words of at least two a's
2. Given languages defined by each of the res $\mathbf{xy^*x, x^*y^*, (xy)^*, x^*y^*x^*}$,
   1. Describe each language in plain English
   2. List the shortest 5 words of each language
3. ans to 2:
   1. $\mathbf{xy^*x}$: all words of  y's between two x's
      1. $L(\mathbf{xy^*x})=\{xx,xyx,xyyx,xyyyx,xyyyyx,⋯\}$
   2. $\mathbf{x^*y^*}$: all words of x's preceding y's
      1. $L(\mathbf{x^*y^*})=\{ϵ, x,y,xx,xy,yy,xxx,xxy,xyy,yyy,⋯\}$
   3. $\mathbf{(xy)^*}$: all words of pairs of xy
      1. $L(\mathbf{(xy)^*})=\{ϵ, xy, xyxy, xyxyxy, xyxyxyxy, ⋯\}$
   4. $\mathbf{x^*y^*x^*}$: (x's)(y's)(x's)
      1. $L(\mathbf{x^*y^*x^*})=\{ϵ, x, y, xx, xy, yx, yy, xxx,xxy,xyx,xyy,yxx,yyx,yyy,⋯\}$:


💡 Demo
---
Given $Σ=\{a,b,c\}$,
- $L_3=\{a,c,ab,cb,abb,cbb, abbb,cbbb, ⋯\}$, it can be described in  
  - re: $L_3 = L(\mathbf{ab^*+cb^*}) = L(\mathbf{(a+c)b^*})$
  - plain English: $L_3=$language{either a or c followed by some b's}
- $L_4=\{aaa,aab,aba,abb,baa,bab,bba,bbb\}$, it can be described in
  - re: $L_4=L(\mathbf{(a+b)(a+b)(a+b)})=L(\mathbf{(a+b)^3})$
  - plain description: set of all three letters of a's and b's


❓ Questions
---
Given $Σ=\{a,b\}$, 
- describe the languages defined by the following re's in plain description
- list the first shortest 10 words of each language if it has
  - $\mathbf{(a+b)^*, (a+b)^5, a(a+b)^*, a(a+b)^*b}$
    - $\mathbf{(a+b)^*}$ are *all possible strings* can be generated from $Σ$
      - including the empty string ϵ


The recursive definition of REs
---
The set of REs over $Σ$ is defined by
- Rule 1 (seeds): 
  - Every letter in $Σ$ by making it **boldface**
  - The empty string $\mathbf{ϵ}$ or $\mathbf{Λ}$
- Rule 2 (generators):
  - if $\mathbf{r_1}$ and $\mathbf{r_2}$ are REs, then so are
    - $\mathbf{(r_1), r_1r_2, r_1+r_2, r_1^*}$
      - the parentheses are used for precedence and clarity
        - not a requirement for RE
      - the `+` is for union `∪`
- Languages defined by REs are called *regular languages*


👁️ Clarity
---
- `a` could mean
  - the letter in $Σ$ or the word in $Σ^*$
- `{a}`is the language of one word `a` and its re is $\mathbf{a}$
- ⚠️ $\mathbf{Φ}$ is the RE for the *null language* $Φ$ with properties
  - $\mathbf{r+Φ=r}$
  - $\mathbf{Φr=Φ}$


👁️ Clarity
---
- `+` in the REs means union, not algebraic plus, so the REs below are meaningful
  - $\mathbf{a^* = a^*+a^*}$
  - $\mathbf{a^* = a^*+a^*+a^*}$
  - $\mathbf{a^* = a^*+aa+ aaaa}$
- That two REs equal means they represent the same set of language


❓ Questions
---
Describe the languages defined by the following REs:

- $\mathbf{(a+b)^*a(a+b)^*}$
  - the set of all words over the alphabet $Σ=\{a,b\}$ that have a factor `a`
    - does not have word $ϵ=b^0$ or b's, i.e. all words without a
      - the RE is $\mathbf{b^*}$
  - all words = (all words with an a) + (all words without an a)
    - $\mathbf{(a+b)^* = (a+b)^*a(a+b)^* + b^*}$
- $\mathbf{b^*ab^*a(a+b)^*}$
  - (any b's)(a)(any b's)(a)(all words)
- $\mathbf{(a+b)^*ab(a+b)^*+b^*a^*}$
  - all words of a's and b's
    - $\mathbf{(a+b)^*ab(a+b)^*}$: all words containing substring ab
  - $\mathbf{b^*a^*}$: all words  NOT containing substring ab, i.e.
    - all a's, or all b's or b's followed by a's, or ϵ
- It is a challenge to describe the language defined by RE at most of the time
  - $\mathbf{(ϵ+ba^*)(ab^*a+ba^*)^*b(a^*+b^*a)bab^*}$


💡 Demo
---
Represent the  language of all words that have at least one `a` and at least one `b`:
- wrong: $\mathbf{(a+b)^*a(a+b)^*b(a+b)^*}$
  - (any words)(a)(any words)(b)(any words)
  - how about word `ba`, `bbbaaa`, etc.?
- right: $\mathbf{(a+b)^*a(a+b)^*b(a+b)^*+(a+b)^*b(a+b)^*a(a+b)^*}$, or
  - $\mathbf{(a+b)^*a(a+b)^*b(a+b)^*+bb^*aa^*}$

Extension: all words do not contain both an a and a b in them are
- (all a's) + (all b's) + ϵ
- so, $\mathbf{(a+b)^* = (a+b)^*a(a+b)^*b(a+b)^*+bb^*aa^* + a^*+b^*}$


❓ Questions
---
Represent the languages below with REs

- The language of all words that have two b's any where in the word
  - (any words)(b)(any words)(b)(any words)
    - Does this include words with b at the head or tail of the word?
  - $\mathbf{(a+b)^*b(a+b)^*b(a+b)^*}$
- The language of all words that have two b's together any where in the word
  - (any words)(bb)(any words)
  - $\mathbf{(a+b)^*bb(a+b)^*}$
- The language of all words that have two b's together at the beginning the word
  - (bb)(any words)
  - $\mathbf{bb(a+b)^*}$
- All words with at least two a's
  - $\mathbf{(a+b)^*ab^*ab^*}$, or
  - $\mathbf{b^*a(a+b)^*ab^*}$
  - Are they equivalent?
- All words with exactly two a's
  - $\mathbf{b^*ab^*ab^*}$
- The language of words that are all b's or an a followed by some b's
  - $\mathbf{b^++ab^+ = (ϵ+a)b^+}$


Regular languages
---
The regular language $L(\mathbf{r})$ associated with RE $\mathbf{r}$ over alphabet $Σ$ is defined recursively:
- seeds:
  - $L(\mathbf{Φ}) = Φ$
  - $L(\mathbf{ϵ})=\{ϵ\}$
  - $∀ a∈Σ: L(\mathbf{a})=\{a\}$
- generators:
  - $\mathbf{r=r_1+r_2} → L(\mathbf{r})=L(\mathbf{r_1})+L(\mathbf{r_2})$
  - $\mathbf{r=r_1r_2} → L(\mathbf{r})=L(\mathbf{r_1})L(\mathbf{r_2})$
  - $L(\mathbf{r^*}) → L(\mathbf{r})^*$


䷼ Theorem
---
- Every finite language $L=\{w_1,w_2,⋯,w_n\}$ is a regular language, i.e. it can be defined by a RE
  - $\mathbf{w_1+w_2+⋯+w_n}$
- ⚠️ There are languages can NOT be defined by RE


Review *,+ and ?
---
Given language $L=\{w_1,w_2,⋯, w_n\}$ and alphabet $Σ=\{a_1,a_2,\cdots,a_n\}$:

- $\displaystyle L^* = L^0∪L^1∪L^2∪⋯ = ∪_{k=0}^∞L^k$ in REs
  - $\displaystyle \mathcal{R}(L^0)=\mathbf{ϵ}$
  - $\displaystyle \mathcal{R}(L^1)=\mathcal{R}(L)=\mathbf{w_1+w_2+⋯+w_n}$
  - $\displaystyle \mathcal{R}(L^2)=\mathbf{(w_1+w_2+⋯+w_n)(w_1+w_2+⋯+w_n)=(w_1+w_2+⋯+w_n)^2}$
  - $\displaystyle \mathcal{R}(L^n)=\mathcal{R}(L)=\mathbf{(w_1+w_2+⋯+w_n)^n}$
  - $\displaystyle \mathcal{R}(L^*)=\mathbf{Σ_{i=0}^∞}\mathcal{R}(L^n)=\mathbf{Σ_{i=0}^∞(w_1+w_2+⋯+w_n)^n}$
- $\displaystyle \mathcal{R}(L^+)=\mathbf{Σ_{i=1}^∞}\mathcal{R}(L^n)=\mathbf{Σ_{i=1}^∞(w_1+w_2+⋯+w_n)^n}$
  - $\displaystyle \mathcal{R}(L^*)=\mathcal{R}(L^+)+\mathcal{R}(L^0)=\mathcal{R}(L^+)+\mathbf{ϵ}$
  - $\displaystyle \mathcal{R}(L^?)=\mathcal{R}(L^1)+\mathcal{R}(L^0)=\mathcal{R}(L)+\mathbf{ϵ}$
- $\displaystyle Σ^* = Σ^0∪Σ^1∪Σ^2∪⋯ = ∪_{k=0}^∞Σ^k$ in REs
  - $\displaystyle \mathcal{R}(Σ^0)=\mathbf{ϵ}$
  - $\displaystyle \mathcal{R}(Σ^1)=\mathcal{R}(Σ)=\mathbf{a_1+a_2+⋯+a_n}$
  - $\displaystyle \mathcal{R}(Σ^2)=\mathbf{(a_1+a_2+⋯+a_n)(a_1+a_2+⋯+a_n)=(a_1+a_2+⋯+a_n)^2}$
  - $\displaystyle \mathcal{R}(Σ^n)=\mathcal{R}(Σ)=\mathbf{(a_1+a_2+⋯+a_n)^n}$
  - $\displaystyle \mathcal{R}(Σ^*)=\mathbf{Σ_{i=0}^∞}\mathcal{R}(Σ^n)=\mathbf{Σ_{i=0}^∞(a_1+a_2+⋯+a_n)^n}$
- $\displaystyle \mathcal{R}(Σ^+)=\mathbf{Σ_{i=1}^∞}\mathcal{R}(Σ^n)=\mathbf{Σ_{i=1}^∞(a_1+a_2+⋯+a_n)^n}$
  - $\displaystyle \mathcal{R}(Σ^*)=\mathcal{R}(Σ^+)+\mathcal{R}(Σ^0)=\mathcal{R}(Σ^+)+\mathbf{ϵ}$
  - $\displaystyle \mathcal{R}(Σ^?)=\mathcal{R}(Σ^1)+\mathcal{R}(Σ^0)=\mathcal{R}(Σ)+\mathbf{ϵ}$


RE laws
---
- Two REs are equivalent if their regular languages are equal
  - $L(\mathbf{r_1})=L(\mathbf{r_2}) → \mathbf{r_1}=\mathbf{r_2}$
- Denote $L(\mathbf{r_1})⊆L(\mathbf{r_2})$  with $\mathbf{r_1≤r_2}$

| law | equation |
|:--:|:--:|
| simple | $\mathbf{r+Φ = r}$<br>$\mathbf{r+r=r}$<br>$\mathbf{ϵr=rϵ=r}$<br>$\mathbf{Φr=rΦ=Φ}$<br>$\mathbf{rr^*=r^*r=r^+}$<br>$\mathbf{ϵ+r^+=r^*}$ <br> $\underbrace{\mathbf{rr⋯r}}_{n\mathbf{r}'s}=\mathbf{r^n}$ <br>$\mathbf{r^0=ϵ}$ <br> $\mathbf{(r^*)^*=r^*r^*=r^*}$ |
| communication | $\mathbf{r_1+r_2=r_2+r_1}$ |
| association | $\mathbf{r_1+(r_2+r_3)=(r_1+r_2)+r_3}$<br>$\mathbf{r_1(r_2r_3)=(r_1r_2)r_3}$ |
| distribution | $\mathbf{r_1(r_2+r_3)=r_1r_2+r_1r_3}$<br>$\mathbf{(r_1+r_2)r_3=r_1r_3+r_2r_3}$ |
| subset | $\mathbf{r_1≤r_2 → r_1+r_2=r_2}$ <br> $\mathbf{r_2+r_1r_3≤r_3→r_1^*r_2≤r_3}$<br>$\mathbf{r_2+r_3r_1≤r_3→r_2r_1^*≤r_3}$ |
| derived | $\mathbf{(r_1r_2)^*r_1=r_1(r_2r_1)^*}$<br>$\mathbf{(r_1^*r_2)^*r_1^*=(r_1+r_2)^*}$ <br> $\mathbf{r_1^*(r_2r_1^*)^*=(r_1+r_2)^*}$<br>$\mathbf{(r_1^*r_2^*)^*=(r_1+r_2)^*}$<br>$\mathbf{(ϵ+r)^*=r^*}$ |


Simplify REs
---
- L={aa,ab,ba,bb}
  - $\mathbf{aa+ab+ba+bb=(a+b)(a+b)}$
- L={ϵ,x,xx,xxx,xxxx,xxxxx}
  - $\mathbf{ϵ+x+xx+xxx+xxxx+xxxxx=(ϵ+x)(ϵ+x)(ϵ+x)(ϵ+x)(ϵ+x)=(ϵ+x)^5}$
- It is still unknown whether there exists  a set of algebraic rules can be used to reduce a RE to another equivalent one


Complex REs
---
🍎 Example 1

- $\mathbf{r_1=(a+b)^*(aa+bb)(a+b)^*}$
  - (arbitrary)(double letter)(arbitrary)
  - strings containing a double letter
- $\mathbf{(ϵ+b)(ab)^*(ϵ+a)}$
  - strings not containing a double letter, e.x.
  - ϵ,a,b,ab,ba,aba,bab,abab,baba,...
- combine together
  - $\mathbf{(a+b)^*(aa+bb)(a+b)^* + (ϵ+b)(ab)^*(ϵ+a)=(a+b)^*}$

🍎 Example 2

- $\mathbf{r_2=(a+b)^*a(a+b)^*(a+ϵ)(a+b)^*a(a+b)^*}$
  - break from the middle using distribution
  - =❶ $\mathbf{(a+b)^*a(a+b)^*a(a+b)^*a(a+b)^*}$
    - all words contain at least 3 a's
  - +❷ $\mathbf{(a+b)^*a(a+b)^*ϵ(a+b)^*a(a+b)^*}$
- ❷ $\mathbf{(a+b)^*a(a+b)^*ϵ(a+b)^*a(a+b)^*}$
  - = $\mathbf{(a+b)^*a(a+b)^*a(a+b)^*}$
    - all words contain at least 2 a's
- therefor, ❶⊆❷, so ❶+❷⊆❷, i.e.
  - $\mathbf{r_2=(a+b)^*a(a+b)^*a(a+b)^*}$

🍎 Example 3

- $\mathbf{(a+b)^*=(a^*+b)^*=(a+b^*)^*=(a^*+b^*)^*}$
- $\mathbf{(aa+ab^*)^*≠(aa+ab)^*}$
  - the right RE cannot have words with a double b
- $\mathbf{(a^*b^*)^*=(a+b)^*}$
- $\mathbf{(a^*b^*)^*≠a^*b^*≠(ab)^*}$

🍎 Example 4

- EVEN-EVEN: $\mathbf{[aa+bb+(ab+ba)(aa+bb)^*(ab+ba)]^*}$
  - all words of even number of a's and even number of b's
  - the number of a's and b's do not have to be the same
- first several words
  - {ϵ, aa, bb, aaaa, aabb,abab, abba, baab, baba, bbaa,bbbb, aaaaaa,aaaabb,aaabab, ⋯}

# References
- [regex simplifier](https://ivanzuzak.info/noam/webapps/regex_simplifier/)