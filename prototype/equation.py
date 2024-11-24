from numeric import *
from functions import *
from utility import *

class Equation:
    pass

class Equation:
    def __init__ (self, lhs, rhs) -> None:
        if type(lhs) not in numeric or type(rhs) not in numeric:
            raise TypeError("unable to create Equation with types provided")
        
        self.lhs = lhs
        self.rhs = rhs

        test_rhs = rhs - lhs

        if type(test_rhs) in (int, float):
            raise ArithmeticError("equation is not equal")

        if test_rhs.variables == []:
            raise ArithmeticError("equation is not equal")

    def solve(self, var) -> list:
        rhs = (self.rhs - self.lhs).expand().simplify()

        if type(rhs) == LargePower:
            return []
        
        if any([type(term) == LargePower for term in rhs]):
            return []
        
        if type(rhs.term_list[-1]) not in (int, float, Rational, Power, ConstProduct):
            return [0] + Equation(0, rhs.__mul__(Term(1, {'x': -1}))).solve(var)
        
        # ACCOUNT FOR OTHER VARS
        
        multiple = 1
        for pos, term in enumerate(rhs.term_list):
            if type(term) == Rational:
                multiple *= rhs.term_list[pos].denominator
                continue
            if type(term) != Term:
                continue
            if type(term.coefficient) == Rational:
                multiple *= rhs.term_list[pos].coefficient.denominator

        rhs = (rhs*multiple).expand()

        funcF = Func(rhs, ['x'])

        p = factors(funcF.exp.term_list[-1])
        q = factors(funcF.exp.term_list[0].coefficient)

        solutions = []
        for b in q:
            for a in p:
                if funcF.evaluate([Rational(a, b)]) == 0 and Rational(a, b).simplify() not in solutions:
                    solutions.append(Rational(a, b).simplify())
                if funcF.evaluate([-Rational(a, b)]) == 0 and -Rational(a, b).simplify() not in solutions:
                    solutions.append(-Rational(a, b).simplify())

        return solutions
    
    def __repr__ (self) -> str:
        return f"{self.lhs}={self.rhs}"