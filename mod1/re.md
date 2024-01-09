__Regular expressions__

_ict chapter 4

Regular expression (re) of a language
---
- denoted by boldface letters
- represents any word generally in the language
- e.x.
  - Let $S=\{x\} \text{ and } L_0=S^* = \{x\}^*$, i.e. $L_0=\{ϵ, x, xx, xxx, ⋯\}$
    - plain description: a language of any string of x's
  - define a re on $L_0$ as $\mathbf{x^*}$, which means
    - $\mathbf{x^*} = ϵ ∨ x ∨ x^2 ∨ x^3 ∨ ⋯ = x^n, (n \in \mathcal{N})$
    - rewrite $L_0=language \{\mathbf{x^*}\}$


💡 Demo
---
- Describe $L_1=\{a, ab, abb, abbb, ⋯\}$ with
  - plain description: 
    - a language whose words are composed of one a and zero or more b's
  - re:
    - $L_1=language(\mathbf{ab^*})$
    - ⚠️ $\mathbf{ab^*}$ is different from $\mathbf{(ab)^*}$
      - i.e. power has higher precedence than concatenation
      - $\mathbf{(ab)^*}=(ab)^n, n∈\mathcal{N}$
- Describe $L_2=\{a, aa, aaa, aaaa, ⋯\}$ with
  - plain description: 
    - a language whose words are composed of one or more a's
  - re:
    - $L_2=language(\mathbf{aa^*})$
      - $\mathbf{a^+}=a^n, n∈\mathcal{N^+}$


❓ Question
---
1. Are these re equivalent?
   - $\mathbf{aa^* a^*  aa^*a^* a^*aa^* a^+a^* a^*a^+ a^*aa^*a^*aa^*  a^+a^*a^*a^+}$
2. Given languages defined by each of the res $\mathbf{xy^*x  x^*y^*  (xy)^*  x^*y^*x^*}$,
   1. Describe each language in plain English
   2. List the shortest 10 words of each language


💡 Demo
---
Given $Σ=\{a,b,c\}$,
- $L_3=\{a,c,ab,cb,abb,cbb, abbb,cbbb, ⋯\}$, it can be described in  
  - re: $L_3 = language(\mathbf{ab^*+cb^*}) = language(\mathbf{(a+c)b^*})$
  - plain English: $L_3=$language{either a or c followed by some b's}
- $L_4=\{aaa,aab,aba,abb,baa,bab,bba,bbb\}$, it can be described in
  - re: $L_4=language\{(a+b)(a+b)(a+b)\}=language\{(a+b)^3\}$
  - plain: set of all three letters of a's and b's


❓ Questions
---
Given $Σ=\{a,b\}$, 
- describe the languages defined by the following re's in plain
- list the first shortest 10 words of each language if it has
  - $\mathbf{(a+b)^*  (a+b)^5  a(a+b)^*  a(a+b)^*b}$
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
    - $\mathbf{(r_1)  r_1r_2  r_1+r_2  r_1^*}$
- Languages defined by REs are called *regular languages*


💡 Demo
---
- `a` could mean
  - the letter in $Σ$ or the word in $Σ^*$
- `{a} `is the language of one word `a` and its re $\mathbf{a}$
- $\mathbf{Φ}$ is the RE for the *null language* $Φ$ with properties
  - $\mathbf{r+Φ=r}$
  - $\mathbf{Φr=Φ}$