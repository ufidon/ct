__Post machines__

_ict chapter 20_


Post machine (PM)
---
a 5-element tuple (Σ, QUEUE, START, READ, ADD):
- `Σ`: the alphabet of input letters and a `special symbol #`
- `QUEUE or STORE`: 
  - (p1④) a FIFO linear storage, 
    - letters go into it from its `tail` and out from its `head` one letter a time
      - by default, head on the left and tail on the right
    - initially contains the input string
  - the `queue or store` alphabet `Γ` contains all characters can be used in the QUEUE
- (p1①) `READ` states remove the `QUEUE head character` and branch accordingly
  - PMs are deterministic, so no two edges from the READ have the same label
    - nondeterministic PMs (nPMs) can be defined if two or more edges from the READ have the same label
      - it is proved that nPM ≡ PM
  - There may be a branch for every character in Σ or Γ
  - the `ε or Λ` branch means an empty QUEUE was read
- (p1②) `ADD` states concatenate a character to the string in the QUEUE through its tail
  - No branching can take place at an ADD state
  - There may be a branch for every character in Σ or Γ
- (p1③) `An unenterable START` state and `0 or more halt states` called `ACCEPT` and `REJECT`
  - a read character in a READ state without outgoing edges crashes the PM
  - this is equivalent to taking a labeled edge into a REJECT state
  - ∴ PMs can be drawn with or without REJECT states


🍎 Example 1
---
❶ A PM that accepts {aⁿbⁿ | n=0,1,2,3,⋯}
- (p2)
- trace `aaabbb` (p3)
- ---

❷ A PM that accepts {aⁿbⁿaⁿ | n=0,1,2,3,⋯}
- (p2)
- trace `aaabbb` (p4)


☯ Theorem 1
---
Any language that can be accepted by a PM can be accepted by some TM.

Proof by simulating a PM on a TM.
- (p5) keep track of the PM QUEUE by the TM TAPE
- (p6) duplicate PM ADD and READ on the TM TAPE


🍎 Example 2
---
- Simulate PM P (p7) by a TM T (p8)
  - the PM accepts {aⁿbⁿ | n=0,1,2,3,⋯}
- their corresponding states (p9)
- trace `aabb` on T (p10)
- a short notation is applied
  - (a,b,c,d,e;=,D) stands for the instructions
    - (a,a,D)(b,b,D)(c,c,D)(d,d,D)(e,e,D)
    - D is direction L or R


☯ Theorem 2
---
There are subprograms that enable a PM to 
- (p11) add a character to the head of the string in the QUEUE 
- (p12-13) read the character off of the tail of the string


☯ Theorem 3
---
Any language that can be accepted by a TM can be accepted by some PM.

Proof by constructing a PM equivalent to a given TM:
- (p14) track the TM TAPE
  -  a correspondence between `#` and the position of the `TAPE HEAD`
- (p15) the TM converts `cat` into `dog`
- (p16-17) simulate a left move
- (p18) simulate initial state


🍎 Example 3
---
- Given a TM T (p19) that accepts all strings starting with a
  - build a PM (p20) equivalent to T


☯ Theorem 4
---
PM ≡ TM