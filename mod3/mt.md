__Minsky's theorem__

_ict chapter 21_


2PDA
---
- A dPDA with two pushdown stacks
- it is almost the same as a dPDA except
  - its PUSH an POP operations must specify the stack they work on
  - ex. by subscripts: `PUSH₁ x, PUSH₂ y`



🍎 Example 1
---
(p1) A 2PDA that accepts {aⁿbⁿaⁿ | n=1,2,3,⋯}
- (p2) trace `aahhaa`


☯ Theorem 1
---
Minsky 's theorem: 2PDA ≡ TM


☯ Theorem 2
---
2⁺PDA ≡ TM
- 2⁺PDA has 2 and more stacks
- computing power of the models
  - `FA = TG = NFA = 0PDA < dPDA < nPDA = 1nPDA < 2dPDA = 2⁺dPDA = 2⁺nPDA = PM = nPM = TM = nTM`