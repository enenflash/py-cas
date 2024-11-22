# py-cas
algebraic calculator for python

## numeric.py
### Rational
* numerator: int, denominator: int
* excepts floats but rounds down
### Power
* base: int|Rational, power: int|Rational
### ConstProduct
* const_list: list of int|Rational|Power
### Term
* coefficient: int|float|Rational|Power|ConstProduct
* var_powers: dict {var_name, power}
### Sum
* term_list: list of any numeric
### Product
* exp_list: list of any numeric
### LargePower
* base: any numeric
* power: any numeric
### Factorial
* exp: any numeric

## functions.py
### Func
* exp: any numeric
* parameters: list of var_names
