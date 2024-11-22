# py-cas
algebraic calculator for python

## numeric.py
### Rational
* Rational(numerator, denominator)
* numerator: int, denominator: int
* accepts floats but rounds down
* Rational(5, 3) = 5/3

### Power
* Power(base, power)
* base: int|Rational, power: int|Rational
* Power(5, Rational(1, 2)) = 5^(1/2)
* 5 ** Rational(1, 2) -> returns Power
### ConstProduct
ConstProduct(const_list)
* const_list: list of int|Rational|Power
* ConstProduct([3, Power(2, Rational(1, 2))]) = 3×2^(1/2)
* 3 * 2 ** Rational(1, 2) -> returns ConstProduct
### Term
Term(coefficient, var_powers)
* coefficient: int|float|Rational|Power|ConstProduct
* var_powers: dict {var_name, power}
* Term(2, {'x': 2, 'y': 1}) = 2x²y
### Sum
* Sum(term_list)
* term_list: list of any numeric
* Term(2, {'x': 2}) + Term(3, {'x': 1}) = 2x²+3x
* 2*(Term(1, {'x': 1})+1) + Term(3, {'x': 1}) -> returns Sum
* 2(x+1) + 3x
* Sum([Product([2, Sum([Term(1, {'x': 1})), 1])]), Term(3, {'x': 1})])
* 2*(Term(1, {'x': 1})+1) + Term(3, {'x': 1}) -> returns Sum
### Product
* exp_list: list of any numeric
* 2(x-1)(x+2)²
### LargePower
* base: any numeric
* power: any numeric
* 2^x, (x+2)³
### Factorial
* exp: any numeric
* 5!, (x+2)!
* Factorial(5)
* Factorial(Term(1, {'x': 1}) + 2)

## functions.py
### Func
* exp: any numeric
* parameters: list of var_names
* f(x) = 2x(x-3) -> exp = 2x(x-3), parameters = ['x']
* evaluating: func.evaluate(2)
* f(g(x)): funcF.evaulate(funcG)
