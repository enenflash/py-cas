<span style="font-family: Consolas">

# py-cas
algebraic calculator for python

## numeric.py
### Rational
> Rational(numerator, denominator)
* numerator: int, denominator: int
* accepts floats but rounds down
* Rational(5, 3) = 5/3
### Power
> Power(base, power)
* base: int|Rational, power: int|Rational
* Power(5, Rational(1, 2)) = 5^(1/2)
* 5 ** Rational(1, 2) -> returns Power
### ConstProduct
> ConstProduct(const_list)
* const_list: list of int|Rational|Power
* ConstProduct([3, Power(2, Rational(1, 2))]) = 3×2^(1/2)
* 3 * 2 ** Rational(1, 2) -> returns ConstProduct
### Term
> Term(coefficient, var_powers)
* coefficient: int|float|Rational|Power|ConstProduct
* var_powers: dict {var_name, power}
* Term(2, {'x': 2, 'y': 1}) = 2x²y
### Sum
> Sum(term_list)
* term_list: list of any numeric (including itself)
* Term(2, {'x': 2}) + Term(3, {'x': 1}) = 2x²+3x
* 2*(Term(1, {'x': 1})+1) + Term(3, {'x': 1}) -> returns Sum
* Sum([Product([2, Sum([Term(1, {'x': 1})), 1])]), Term(3, {'x': 1})]) = 2(x+1) + 3x
* 2*(Term(1, {'x': 1})+1) + Term(3, {'x': 1}) -> returns Sum
### Product
> Product(exp_list)
* exp_list: list of any numeric (including itself)
* Product([2, Expression([Term(1, {'x': 1}), -1]), LargeBase(Expression([Term(1, {'x': 1}), 2]), 2)]) = 2(x-1)(x+2)²
* 2*(Term(1, {'x': 1})-1)*(Term(1, {'x': 1})+2)**2 -> returns Product
### LargePower
> LargePower(base, power)
* base: any numeric (including itself), power: any numeric (including itself)
* LargeBase(2, Term(1, {'x': 1})) = 2^x
* 2**Term(1, {'x': 1}) -> returns LargeBase
* LargeBase(Expression([Term(1, {'x': 1}), 2]), 3) = (x+2)³
* (Term(1, {'x': 1})+2)**3 -> returns LargeBase
### Factorial
> Factorial(exp)
* exp: any numeric (including itself)
* Factorial(5) = 5!
* Factorial(Term(1, {'x': 1}) + 2) = (x+2)!
<hr>

## functions.py
### Func
> Func(exp, parameters)
* exp: any numeric (not func)
* parameters: list of var_names
* f(x) = 2x^2 -> Func(2*Term(1, {'x': 1})**2, ['x'])
### Evaluating
* f(2) -> func.evaluate(2)
* f(g(x)) -> funcF.evaulate(funcG)

</span>
