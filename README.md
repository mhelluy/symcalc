# symcalc
A calculator which can manipulate expressions with symbols

## Getting started

Symcalc needs `sympy` to be installed :
```bash
pip install sympy
```

Then you can launch it:
```bash
python3 symcalc.py
```

## Use as a calculator
```
SYMCALC v1.0
>>> 2/3 * 89
178/3
>>> sqrt(100)/17
10
──
17
>>> cos(1.5pi)/sqrt(3)
0
>>> sin(1.5pi)/sqrt(3)
-√3 
────
 3
>>> 67^2/9
4489/9
>>> i^2
-1
>>> ln(e^2)
2
```

## Use symbols and make operation with them
```
>>> (x-3)(x+2)
(x - 3)⋅(x + 2)
>>> !expand
 2
x  - x - 6
>>> !factor
(x - 3)⋅(x + 2)
>>> + 2
(x - 3)⋅(x + 2) + 2
>>> !expand
 2
x  - x - 4
>>> (a-b)(a+b)
(a - b)⋅(a + b)
>>> !expand
 2    2
a  - b
```

## Use expressions
```
>>> A = (x-1)(x+3)
A = (x - 1)⋅(x + 3)
>>> !expand
     2
A = x  + 2⋅x - 3
>>> *2
       2
A = 2⋅x  + 4⋅x - 6
>>> 9x+10
9⋅x + 10
>>> !set B
B = 9⋅x + 10
>>> A + B
   2
2⋅x  + 13⋅x + 4
>>> !set C
       2
C = 2⋅x  + 13⋅x + 4
```

## Use expressions as math functions

```
>>> C = 2x**2 + 13x + 4
       2
C = 2⋅x  + 13⋅x + 4
>>> C:9
C(9) = 283
>>> C:y
          2
C(y) = 2⋅y  + 13⋅y + 4
>>> C:2x
            2
C(2*x) = 8⋅x  + 26⋅x + 4
>>> C:x^2
             4       2
C(x**2) = 2⋅x  + 13⋅x  + 4
>>> + 1
   4       2
2⋅x  + 13⋅x  + 5
```

## Solve equations and reduce inequalities
Use `==` between two expressions to solve equations :
```
   4       2
2⋅x  + 13⋅x  + 5
>>> !set D
       4       2
D = 2⋅x  + 13⋅x  + 5
>>> D == 9
      ⎡       ___________        ___________       _____________      _____________⎤
      ⎢      ╱ 13   √201        ╱ 13   √201       ╱   13   √201      ╱   13   √201 ⎥
      ⎢-ⅈ⋅  ╱  ── + ──── , ⅈ⋅  ╱  ── + ──── , -  ╱  - ── + ──── ,   ╱  - ── + ──── ⎥
_S_ = ⎣   ╲╱   4     4       ╲╱   4     4      ╲╱     4     4     ╲╱     4     4   ⎦
```
Use `>`, `<`, `>=`, or `<=`, between two expressions to reduce inequalities :
```
>>> sqrt(x+1) > sqrt(2x^2+x)

⎛            √2⎞   ⎛           -√2     ⎞
⎜0 ≤ x ∧ x < ──⎟ ∨ ⎜x ≤ -1/2 ∧ ──── < x
⎝            2 ⎠   ⎝            2      ⎠
```
