from numeric import *

class Func:
    pass

class Func:
    def __init__ (self, exp:Sum|Product|LargePower, parameters:list[str]) -> None:
        if type(parameters) != list:
            raise TypeError("invalid parameters provided")
        if any([type(p) != str for p in parameters]):
            raise ValueError("invalid parameters provided")
        if type(exp) not in (Term, Sum, Product, LargePower):
            raise TypeError("invalid Sum provided")
        
        self.parameters = parameters

        if type(exp) not in (int, float):
            self.exp = exp.simplify()
        else: self.exp = exp

    def flip(self):
        return self.exp**-1
    
    def evaluate(self, parameters:list) -> Sum|Product|LargePower:
        if type(parameters) != list:
            raise TypeError("incorrect parameter type")
        if any([type(p) not in numeric for p in parameters]):
            raise TypeError("incorrect parameter type")
        
        if len(parameters) < len(self.parameters):
            raise ValueError("insufficient parameters provided")
        if len(parameters) > len(self.parameters):
            raise ValueError("too many parameters provided")
        
        var_values = {}
        for pos, p_name in enumerate(self.parameters):
            if type(parameters[pos]) == Func:
                var_values[p_name] = parameters[pos].exp
                continue
            var_values[p_name] = parameters[pos]

        return self.exp.substitute(var_values)

    # ABSOLUTE/NEGATION

    def __neg__ (self) -> Func:
        return -self.exp
    
    def __pos__ (self) -> Func:
        return self.exp
    
    def __abs__ (self) -> Func:
        return abs(self.exp)
    
    # MATHEMATICAL OPERATIONS

    def __add__ (self, f2) -> Func:
        if type(f2) not in numeric:
            return NotImplemented

        if type(f2) == Func:
            return (self.exp + f2.exp).simplify()
        
        return (self.exp + f2).simplify()
    
    def __radd__ (self, f2) -> Func:
        if type(f2) not in numeric:
            return NotImplemented
        
        return self.__add__(f2)
    
    def __sub__ (self, f2) -> Func:
        if type(f2) not in numeric:
            return NotImplemented

        return self.__add__(-f2)
    
    def __rsub__ (self, f2) -> Func:
        if type(f2) not in numeric:
            return NotImplemented
        
        if type(f2) == Func:
            return (-self).__add__(f2.exp)
        
        return (-self).__add__(f2)
    
    def __mul__ (self, f2) -> Func:
        if type(f2) not in numeric:
            return NotImplemented
        
        if type(f2) == Func:
            return (self.exp * f2.exp).simplify()
        
        return (self.exp * f2).simplify()
    
    def __rmul__ (self, f2) -> Func:
        if type(f2) not in numeric:
            return NotImplemented
        
        return self.__mul__ (f2)
    
    def __pow__ (self, f2) -> Func:
        if type(f2) not in numeric:
            return NotImplemented
        
        if type(f2) == Func:
            return (self.exp ** f2.exp).simplify()
        
        return (self.exp ** f2).simplify()
    
    def __rpow__ (self, f2) -> Func:
        if type(f2) not in numeric:
            return NotImplemented
        
        if type(f2) == Func:
            return (f2.exp ** self.exp).simplify()

        return (f2 ** self.exp).simplify()
    
    def __truediv__ (self, f2) -> Func:
        if type(f2) not in numeric:
            return NotImplemented
        
        return self.__mul__ (f2**-1)
    
    def __rtruediv__ (self, f2) -> Func:
        if type(f2) not in numeric:
            return NotImplemented
        
        return self.flip().__mul__(f2)
    
    # CONVERSIONS
    def __repr__ (self) -> str:
        return str(self.exp)
    
numeric = (int, float, Rational, Power, ConstProduct, Term, Sum, Product, LargePower, Func)
