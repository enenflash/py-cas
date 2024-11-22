from numeric import *
from functions import *
from vectors import *

# SIMPLIFYING EXACT VALUES
print(f"(1/3)*4^(1/3)*5/(1/6) = {Rational(1, 3)*Power(4, Rational(1, 3))*5/Rational(1, 6)}")
print(((Power(2, Rational(1, 2))-Rational(1, 2))*2)**Rational(1, 2)+Power(3, Rational(1, 2)))

# STORING EXPRESSIONS
print((Term(-3, {'x': 1})+Term(5, {'x': 2}))*Rational(1, 2))
print((Term(2, {'x': 2})+Rational(1, 5))/Term(1, {'x': 1}))

# EXPANDING EXPRESSIONS
exp = (Term(1, {'x': 1})-1)*(Term(1, {'x': 1})-3)*(Term(2, {'x': 1})+2)**2
print(f"{exp} = {exp.expand()}")
exp = 2**Term(1, {'x': 1})

# SUBSTITUTING RATIONALS
print("2x^2*y | x = 3 =>", Term(2, {'x': 2, 'y': 1}).substitute({'x': 3, 'y': 4}))
exp = Term(1, {'a': 1})*(Term(1, {'x': 1})-Term(1, {'m': 1}))*(Term(1, {'x': 1})-Term(1, {'p': 1}))*(Term(1, {'x': 1})-Term(1, {'q': 1}))
print(f"{exp} | a=1, m=-2, p=3, q=1, x=0 -> {exp.substitute({'x': 0, 'a': 1, 'm':-2, 'p': 3, 'q': 1})}")

# FUNCTIONS
funcF = Func((Term(1, {'x': 1})-1)*(Term(1, {'x': 1})-3)*(Term(2, {'x': 1})+2), ['x'])
funcG = Func(Term(1, {'x': 2})+Term(2, {'x': 1})+4, ['x'])
print(f"Define f(x) = {funcF.exp}")
print(f"f(2) = {funcF.evaluate([2])}")
print(f"Define g(x) = {funcG.exp}")
print(f"f(x^2 - 1) = {funcF.evaluate([Term(1, {'x': 2}) - 1])}")
print(f"f(g(x)) = {funcF.evaluate([funcG])}")
print(f"f(g(2)) = {funcF.evaluate([funcG.evaluate([2])])}")
print(f"expand(f(x)) = {funcF.exp.expand()}")   
print(f"expand(f(x)) + g(x) = {Func(funcF.exp.expand(), ['x']) + funcG}")

# FACTORIAL
fac = Factorial(5)
print("5! =", fac.simplify())

# PERMUTATIONS AND COMBINATIONS
nPr = Func(Factorial(Term(1, {'n': 1}))/Factorial(Term(1, {'n': 1})-Term(1, {'r': 1})), ['n', 'r'])
nCr = Func(Factorial(Term(1, {'n': 1}))/(Factorial(Term(1, {'n': 1})-Term(1, {'r': 1}))*Factorial(Term(1, {'r': 1}))), ['n', 'r'])
print(f"nPr(10, 3) = {nPr.evaluate([10, 3])}")
print(f"nCr(5, 2) = {nCr.evaluate([5, 2])}")
print(f"nCr(2x, x) = {nCr.evaluate([Term(2, {'x': 1}), Term(1, {'x': 1})])}")

# VECTORS
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(f"v1 = {v1}, v2 = {v2}")
print(f"v1*5 = {v1*5}")
print(f"v1·v2 = {v1*v2}")
print(f"|v2| = {v2.magnitude}")
v3 = Vector(Term(2, {'x': 1}), Term(1, {'x': 1}))
v4 = Vector(1, Term(3, {'x': 1}))
print(f"v3 = {v3}, v4 = {v4}")
print(f"4*v3·(1/2)*v4 = {4*v3*Rational(1, 2)*v4}")
print(f"|v3| = {v3.magnitude}")
