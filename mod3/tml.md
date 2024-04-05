__Turing languages__

_ict chapter 23_


Recursively enumerable language
---
A language L over the alphabet Σ is called `recursively enumerable` if there is a TM T that 
- accepts every word in L  
  - `ACCEPT(T)=L`
- either rejects (crashes) or loops forever for every word in the complement of L
  - `REJECT(T) + LOOP(T) = L'`


Recursive language
---
A language L over the alphabet Σ is called `recursive` if there is a TM T that 
- accepts every word in L
  - `ACCEPT(T)=L`
- and rejects every word in L'
  - `REJECT(T) = L'` and `LOOP(T)=Φ`


☯ Theorem 1
---
Given a TM T = a PM P = a 2PDA A, then
- `ACCEPT(T)=ACCEPT(P)=ACCEPT(A)`
- `REJECT(T)=REJECT(P)=REJECT(A)`
- `LOOP(T)=LOOP(P)=LOOP(A)`


☯ Theorem 2
---
- ① L is recursive ↔ L' is recursive
- ② If L is r.e. and L' is also r.e., then L is recursive.


☯ Theorem 3
---
The union and intersection of two recursively enumerable languages is recursively enu­merable
- the set of recursively enumerable languages is closed under union and intersection
- Given two TMs T₁ and T₂, then there exist a TM T₃ such that
  - `ACCEPT(T₃)=ACCEPT(T₁)+ACCEPT(T₂)`
