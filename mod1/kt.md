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
- `:=` denotes `defined by`

Since they are sets of words,

$(FA⊆TG⊆RE⊆FA) ≡ (FA=TG=RE)$

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
  - ➀ collect the start and final states into one state for each by ε-edges
    - the start states to be one state without incoming edges and 
    - the final states to be one unique final state without outgoing edges
  - ➁ parallel edges are union-ed
  - ➂ eliminate states other than the start and final state
  - ➃ unite all edges from the start state to the final states


Step ➀: uniquefy start and final states
---
- Simplify the start states to be one start state *without incoming edges*
  - ![k1](./img/k1.png)
  - is simplified to be
  - ![k2](./img/k2.png)

- ---

- Simplify the final states to be one unique final state without outgoing edges
  - ![k3](./img/k3.png)
  - is simplified to be
  - ![k4](./img/k4.png)
- Now the TG has shape
  - ![k5](./img/k5.png)

- ---

- Simplify combined start and final states
  - ![k6](./img/k6.png)
  - is simplified to be
  - ![k7](./img/k7.png)

Step ➁: Unite  parallel edges
---
- loops on a single state
  - ![k8](./img/k8.png)
  - is simplified to be
  - ![k9](./img/k9.png)

- ---

- unite parallel edges
  - ![ka](./img/ka.png)
  - to be
  - ![kb](./img/kb.png)

- ---

Step ➂: eliminate states
---
- concatenate segments on a single path
  - ![kc](./img/kc.png)
  - eliminate state 2
  - ![kd](./img/kd.png)

- ---

- ![ke](./img/ke.png)
- eliminate state 2
- ![kf](./img/kf.png)

- ---

- eliminate a state with multiple incoming edges and outgoing edges
  - consider all passing routes
  - use cartesian product of the incoming edges and outgoing edges

- ![kg](./img/kg.png)
- eliminate state 2
- ![kh](./img/kh.png)

---

- ![kk](./img/kk.png)
- eliminate state 2
- ![kl](./img/kl.png)

---

- ![km](./img/km.png)
- eliminate state 2
- ![kn](./img/kn.png)

---

- ![ko](./img/ko.png)
- eliminate state 2
- ![kp](./img/kp.png)

---

- ![kq](./img/kq.png)
- eliminate state 2
- ![kr](./img/kr.png)

---

- ![k00](./img/k00.png)
- eliminate state 2
- ![k01](./img/k01.png)


- ---

Step ➃: unite all edges from the start state to the final states
---
- ![ki](./img/ki.png)
- becomes
- ![kj](./img/kj.png)


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
  - ![ks](./img/ks.png)

- is simplified to be
  - ![kt](./img/kt.png)

- → ![ku](./img/ku.png)

- → ![kv](./img/kv.png)

- → ![kw](./img/kw.png)

- → ![kx](./img/kx.png)

- $`\mathbf{(aa+bb)(a+b)^*(aa) + (aa+bb)(a+b)^*(bb)}`$
  - $`\mathbf{(aa+bb)(a+b)^*(aa+bb)}`$

- ---

- Example 2
  - ![ky](./img/ky.png)
- → ![kz](./img/kz.png)
- → ![kz2](./img/kz2.png)
- → ![kz3](./img/kz3.png)
- → ![kz4](./img/kz4.png)

- ---

- Example 3: eliminate the states in the order 1,2,3
  - ![k02](./img/k02.png)
  - → ![k03](./img/k03.png)
  - → ![k04](./img/k04.png)
  - → ![k05](./img/k05.png)


📝 Practice
---
- Redo example 3 by eliminating states in the order 3,2,1
  - → ![k06](./img/k06.png)
  - → ![k07](./img/k07.png)
  - → ![k08](./img/k08.png)
- Can you tell the two REs obtained are equivalent?


Proof of Part ❸
---
- $∀L: L\coloneqq RE → L\coloneqq FA$
- Prove by recursive definition of RE and constructive algorithm for FA side by side
- RE is recursively generated from the seeds such as letters from an alphabet Σ and the empty string ϵ by  __addition, concatenation, and closure__
  - Let's denote σ,σi as an arbitrary letter in Σ


Step ➀: Build FAs for the seeds
---
- A FA accepts only the empty string ϵ 
  - ![k09](./img/k09.png)
- A FA accepts only one specified letter x∈Σ 
  - ![k10](./img/k09.png)

Step ➁: Unite FAs
---
- FA1 accepts L(r1), FA2 accepts L(r2), then there is a FA3 accepts L(r1+r2). Let's denote this as FA3 = FA1+FA2.


🍎 Example
---
Given FA1 and FA2, build FA3 = FA1+FA2.
- FA1: all words with a double a in them somewhere
  - ![k11](./img/k11.png)

- Transition table of FA1

| state\input | a | b |
|:---:|:---:|:---:|
| -x1  | x2 | x1 |
| x2 | x3 | x1 |
| +x3 | x3 | x3 |

---

- FA2: EVEN-EVEN
  - ![k12](./img/k12.png)
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

- If a string traces through this machine and ends up at a final state, it means that it would also
  - end at a final state either on machine FA1 or on machine FA2 
  - Also, any string accepted by ei­ther FA1 or FA2 will be accepted by this FA3

- FA3
  - ![k13](./img/k13.png)

---

📝 Practice
---
P1: Find the FA3 = FA1 + FA2

- FA1 and FA2
  - ![k14](./img/k14.png)

- FA3:
  - -z1 = x1 or y1
  - z2 = x2 or y1
  - z3+ = x1 or y2+
  - z4+ = x3+ or y1
  - z5+ = x3+ or y2+

- ![k15](./img/k15.png)

- ---
P2: Find the FA3 = FA1 + FA2

- FA1:  all words that end in a
  - ![k16](./img/k16.png)

- FA2: all words with an odd number of letters
  - ![k17](./img/k17.png)

- FA3:  all words that either have
an odd number of letters or end in a
  - ![k18](./img/k18.png)

- ---
P3: Find the FA3 = FA1 + FA2
- Let's solve it in two methods
  - ⓵ build new states of FA3 as needed
  - ⓶ build all FA3 states beforehand

- FA1:  all words that end in a
  - ![k19](./img/k19.png)

- FA2: all words that end in b
  - ![k20](./img/k20.png)

- FA3:   all words ending in a or b, that is, all words except ϵ
  - ⓵ a new state in FA3 is built when it's needed
  - ![k21](./img/k21.png)
- ---
- ⓶ All the states in FA3 can also be built beforehand as the Cartesian product of all FA1 states and all FA2 states
  - create all the transitions
  - remove all unreachable states and their edges
    - such as state z4
  - ![k22](./img/k22.png)

Step ③: Concatenate FAs
---
- FA1 accepts L(r1), FA2 accepts L(r2), then there is a FA3 accepts L(r1r2). Let's denote this as FA3 = FA1FA2.


💡 Demo
---
What could go wrong? 

Given FA1: all words with b as the second letter

- ![k23](./img/k23.png)

and FA2: all words that have an odd number of a's

- ![k24](./img/k24.png)

- An intuitive but wrong construction of FA3=FA1FA2:
  - suppose we can jump somehow from q3+ to x1-
  - ![k25](./img/k25.png)

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
- $`\mathbf{(a + b)^*aa(a + b)^*}`$
- ![k26](./img/k26.png)

and FA2:

- all words end in b
  - $\mathbf{(a+b)^*b}$
- ![k27](./img/k27.png)

FA3:
- z1- = x1-
- z2 = x2
- z3 = x3+ or y1-
  - *Every time we hit a final state on FA1,*
    - *we jump onto the start state of FA2 to get ready to process the remained string*
    - from this point, the remained string is running on both FAs
- z4+ = x3+ or y1- or y2+
  - *pay attention to the y1- again*
- ![k28](./img/k28.png)

---

Algorithm for constructing FA3 = FA1FA2
---
- make a z-state for every nonfinal x-state in FA1 before hitting its final states
- for every hitting FA1 final state, a z-state of is created = this FA1 final state or y1- in FA2, then trace the running of the remain string from there on both FAs, so a z-state is
  - in one and only one x-somestate or a set of y-somestates
- the accepted string must stop at a FA2 final state
  - so a z-final state must contain a y-final state


📝 Practice
---
Given FA1 and FA2 below, find FA3=FA1FA2

- FA1: all words that start with b 
  - $\mathbf{b(a+b)^*}$
- and FA2: all words that end with b
  - $\mathbf{(a+b)^*b}$
- ![k29](./img/k29.png)


- FA3 = FA1FA2: all words begin with b and end with b
  - z1 = x1-
  - z2 = x2
  - z3 = x3 or y1
  - z4 = x3 or y1 or y2
- ![k30](./img/k30.png)

- ---

- FA3' = FA2FA1: all words with a double b in them
- z1- = y1-
- z2 = y2 or x1-
- z3 = y1- or x2
- z4 = y2+ or x1- or x3+
- z5 = y2+ or x1- or x2
- z6 = y1- or x2 or x3+
- z7 = y2 or x1- or x2 or x3+
- ![k31](./img/k31.png) 

---


📝 Practice
---
Given FA1 and FA2 below, find FA3=FA1FA2

- FA1: all words that do not contain the substring aa.
  - ![k32](./img/k32.png)
- FA2:  all words with an odd number of letters
  - ![k33](./img/k33.png)
- FA3 = FA1FA2:  all words but ϵ
  - if  a word w has an odd number of letters, factor it as (ϵ)(w)
    - ϵ ∈ FA1, w ∈ FA2
  - if w has an even (>0) number of letters, factor its as (first letter)(the rest)
    - first letter ∈ FA1, the rest ∈ FA2
  - ![k34](./img/k34.png)

Step ④: Star-close FAs
---
- FA1 accepts L(r), then there is a FA2 accepts L(r*). Let's denote this as FA2 = FA1*.
  - ∵ ϵ ∈ r*, ∴ FA2 must have a ㊏ state

🍎 Example
---
❶ Given the language L defined by $\mathbf{r=a^*+aa^*b}$ is all strings of only a ' s and the strings of some (not 0) a 's ending in a single b, FA1 below accepts L:

- ![k35](./img/k35.png)

- Build FA2 accepts $`\mathbf{r^*=(a^*+aa^*b)^*}`$:
  - `z1± = x1±` (**Case 1: x1 is a ± state**)
  - z2 = x4
  - z3+ = x1± or x2+
    - Note: same idea as in concatenation here
    - Every time hitting a final sate, we jump to x1 to get ready for processing the remain string
    - from then on, the remain string traces on the final state and x1
    - follow this pattern recursively
  - z4+ = x1± or x3+ or x4
  - z5+ = x1± or x2+ or x4
  - **key point 1**: each time we reach a final state it is possible that we have to
start over again at x1

![k36](./img/k36.png)

---

__Algorithm: build FA*__

Given an FA whose states are x1, x2, ... , the FA* can be built as follows:
1. Create a state for every subset of x's. Cancel any subset that contains a final x-state but does not contain the start state
2. For all the remaining nonempty states, draw an a-edge and a b-edge to the col­lection of x-states reachable in FA from the component x's by a- and b-edges  respectively
3. Call `the null subset a ± state` and connect it to whatever states the original start state is connected to by a- and b-edges, even possibly the start state itself
4. Finally, put + signs in every state containing an x-component that is a final state of FA

---

🍎 Example
---
Given an RE: $`\mathbf{r=aa^*bb^*}`$ that defines the language of all words where all the a's (of which there is at least one) come before all the b's (of which there is at least one).

One FA1 that accepts this language is

![k37](./img/k37.png)

Build an FA1* that accepts $`\mathbf{r^*=(aa^*bb^*)^*}`$ ,
- z1± = x1- (**case 2: the start state x1 has NO incoming edges**)
- z2 = x2
- z3 = x3
- z4+ = x1- or x4+
- z5 = x2 or x3
- z6+ = x1 or x3 or x4+

- ![k38](./img/k39.png)

- ---
**Case 3: For an FA NOT accepting ϵ and its x1 has incoming edges**, to build its FA*, two separate start states are needed,
- One of them will be x1 and a final state, 
- whereas the other will be x1 and a nonfinal state

🍎 Example
---
Given FA1 that accepts the language of all words with an odd number of b's

![k40](./img/k40.png)

Build FA1*, which accepts all words but not words of only a's
- z1± = x1- and a final state
- z2 = x1- and a nonfinal state
- z3+ = x1- or x2+

![k41](./img/k41.png)

- ---

❷ Find the FA* for the below FA that accepts all strings that end in a 

![k42](./img/k42.png)

- build the FA*
  - ![k43](./img/k43.png)

- **key point 2**: always begin the FA *-machine with a `special ± start state` that exists in addition to all the states that are subsets of x's
  - This start state should have exit­ing a- and b-edges going to the same x's that the old start state did
    - but has no incoming edges at all
  - The old start state, say, it was x 1 , still appears in the new machine but not as a start state, `just once as itself alone` and many times in combination with other x's

🎆 Summary
---
- Let's denote FA(r) as the FA that accepts the language defined by RE r, we can build an FA recursively for any given RE which can be disassembled recursively,
  - seeds: FA($\boldsymbol{ϵ}$), FA($\boldsymbol{σ}$)
  - generators: FA($\mathbf{r_1+r_2}$), FA($\mathbf{r_1r_2}$), FA($\mathbf{r^*}$), 

🍎 Example
---
Build FA($`\mathbf{(ab)^*a(ab + a^*)^*}`$) top-down then bottom-up
- FA($`\mathbf{(ab)^*a(ab + a^*)^*}`$) = FA1($`\mathbf{(ab)^*a}`$)FA2($`\mathbf{(ab + a^*)^*}`$)
- FA2($`\mathbf{(ab + a^*)^*}`$) = FA3($`\mathbf{(ab + a^*)}`$)*
- etc.


Nondeterministic finite automaton (NFA)
---
- A NFA is a TG with a unique start state
  - each of its edge labels is a single alphabet letter
- the regular deterministic finite automata are referred as DFAs
- A NFA can also be considered as an FA that 
  - allows arbitrarily many a- and b-edges coming out of each state
  - and it accepts a string if there exists a path to +

🍎 Example
---
Three NFAs,

![k44](./img/k44.png)

---

🍎 Example
---
One possible use of the NFA is to eliminate all loop states in a given FA:

![k45](./img/k45.png)

- after the loop is removed
  - the new state 7' introduced indicates the looping occurred
- ![k46](./img/k46.png)

---

🍎 Example
---
- An NFA accepts all words with a triple a followed by a triple b
  - ![k47](./img/k47.png)
  - ambiguity: a triple a followed by a triple b can occur at state 1, 4, 7 as well

- A more strict language: all words begin with a triple a followed by a triple b:
  - ![k48](./img/k48.png)

---

䷀ Theorem
---
For every NFA, there is some FA that accepts exactly the same language.


Proof 1:
---
Use RE as the intermediary between NFA and FA,
- convert the NFA into an RE by state bypass operations
- construct an FA that accepts the same language as the regular expression


Proof 2:
---
- Construct an FA from the NFA
- use the method of constructing an FA* from an FA in Kleene's theorem
  - the states in the target FA are collections of states from the NFA
  - The start state of the target FA is the same start state of the NFA
  - transitions in the FA follow those in the NFA
  - unspecified transitions lead to the null collection Φ —— the dead state

🍎 Examples
---
- ➀ convert the NFA below
  - ![k49](./img/k49.png)
- to an FA
  - ![k50](./img/k50.png)

- ---

- ➁ convert the NFA that accepts the language {bb,bbb}  below
  - ![k51](./img/k51.png)
  - to an FA
  - ![k52](./img/k52.png)

- ---

- ➂ convert the NFA that accepts all inputs with a bb in them below
  - ![k53](./img/k53.png)
  - to an FA
  - ![k54](./img/k54.png)

- ---

- ➃ convert the NFA that accepts all inputs with a triple letter below
  - ![k55](./img/k55.png)
  - to an FA
  - ![k56](./img/k56.png)

---

NFAs and Kleene's theorem Part ❸
---
The proofs that FA1+FA2, FA1FA2, and FA1* are all equivalent to other FAs can be done differently by employing NFAs in the process. Once done, convert the result NFAs to FAs.


Step ➀: Build NFAs for the seeds
---
- A NFA accepts only the empty string ϵ 
  - ![k57](./img/k57.png)
- A NFA accepts only the specified letter σ∈Σ 
  - ![k58](./img/k58.png)

Step ➁: Unite NFAs
---
- NFA1 accepts L(r1), NFA2 accepts L(r2), then there is a NFA3 accepts L(r1+r2). Let's denote this as NFA3 = NFA1+NFA2.
  -  Introduce a new and unique start state with two outgoing a-edges and two out­going b-edges but no incoming edges. 
     -  Connect them to the states that the start states of FA1 and FA2 are already connected to. 
     -  Do not eliminate the start states of FA1 and FA2 , but erase their - signs, leaving all their edges intact. 
     -  The new machine is an NFA that clearly accepts exactly language(FA1 ) + lan­guage(FA2)
  - convert the NFA into an FA

💡 Demo
---
Given FA1 and FA2 below,

![k59](./img/k59.png)

Construct a NFA = FA1+FA2,

![k60](./img/k60.png)

---
- Optional
  - For step ➂ ➃, refer to Q7 and Q9.