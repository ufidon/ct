# Exercise solutions

__Transition Graphs__.Challenges with TG
---
- `(a)(bb)(b₊)`(ab)(bb)(a)(bb)(a)
- `(a)(b)(b)(b₊)`(ab)(bb)(a)(bb)(a)
- `(a)(b)(bb₊)`(ab)(bb)(a)(bb)(a)


Absorbing rules
---
- $`\mathbf{(a+b)^*=b^*(a+b)^*=a^*(a+b)^*=(a+b)^*a^*=(a+b)^*b^*}`$
  - prove by $`\mathbf{(a+b)^* = (a^*b)^*a^*=(b^*a)^*b^*=a^*(ba^*)^*=b^*(ab^*)^*}`$
- $`\mathbf{(a+b)^*b(a+b)^* = a^*b(a+b)^*=(a+b)^*ba^*}`$
  - ⇒ $`\mathbf{(a+b)^*b(a+b)^*=(a^*b)^*a^*b(a^*b)^*a^*=r^*rr^*a^*}`$
  - ⇒ $`\mathbf{(a+b)^*a(a+b)^*b(a+b)^* = (a+b)^*ab(a+b)^*}`$