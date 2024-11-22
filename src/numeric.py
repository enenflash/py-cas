import math

superscript = {
    '-': "\u207B",
    '0': "\u2070",
    '1': "\u00B9",
    '2': "\u00B2",
    '3': "\u00B3",
    '4': "\u2074",
    '5': "\u2075",
    '6': "\u2076",
    '7': "\u2077",
    '8': "\u2078",
    '9': "\u2079"
}

subscript = {
    '0': "\u2080",
    '1': "\u2081",
    '2': "\u2082",
    '3': "\u2083",
    '4': "\u2084",
    '5': "\u2085",
    '6': "\u2086",
    '7': "\u2087",
    '8': "\u2088",
    '9': "\u2089"
}

var_alphabet = "abcdefghijklmnopqrstuvwxyz"

# non-recursive constant (fraction)
class Rational:
    pass

# non-recursive constant (power)
class Power:
    pass

# non-recusive constant (multiplication)
class ConstProduct:
    pass

# non-recursive variable (multiplication)
class Term:
    pass

# recursive constant/variable (addition)
class Sum:
    pass

# recursive variable (multiplication)
class Product:
    pass

# recursive constant/variable (power)
class LargePower:
    pass

# recursive variable
class Factorial:
    pass

class Rational:
    def __init__ (self, numerator:int, denominator:int=1) -> None:
        '''
        float values will be floored to int
        '''

        if type(numerator) not in (int, float) or type(denominator) not in (int, float):
            raise TypeError(f"unable to create Rational with type {type(numerator)} and/or {type(denominator)}")
        
        self.numerator = int(numerator)
        self.denominator = int(denominator)

        if denominator == 0:
            raise ZeroDivisionError("cannot create rational with 0 denominator")

        self._simplify_internal()

    def _simplify_internal(self) -> None:
        if type(self.numerator) == float or type(self.denominator) == float:
            self.numerator = self.numerator/self.denominator
            self.denominator = 1
            return
        
        # use this instead of % because mod operator breaks if numbers are too big
        if self.numerator/self.denominator == int(self.numerator/self.denominator):
           self.numerator = int(self.numerator / self.denominator)
           self.denominator = 1
        
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator/gcd)
        self.denominator = int(self.denominator/gcd)
        
        # ensure self.numerator holds the sign and self.denominator is always positive
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def simplify(self) -> int|Rational:
        '''
        collapses rational to int if possible\n
        for example 4/2 = 2
        '''
        # if divisible
        if self.numerator % self.denominator == 0:
            return int(self.numerator / self.denominator)
        
        return self
    
    # Rational ^ -1
    def flip(self) -> int|Rational:
        return Rational(self.denominator, self.numerator).simplify()

    # check if positive (assuming it was simplified)
    @property
    def pos(self) -> bool:
        return self.numerator >= 0
    
    # COMPARISONS

    def __eq__ (self, num2:int|float|Rational) -> bool:     
        # 5/1 = 5.0
        if type(num2) in (int, float):
            return float(self) == num2
        
        # 5/1 = 10/2
        if type(num2) == Rational:
            return float(self) == float(num2)

        # if not int|float|Rational
        return False

    def __ne__ (self, num2:int|float|Rational) -> bool:
        return not self.__eq__(num2)
    
    def __lt__ (self, num2:int|float|Rational) -> bool: # <
        if type(num2) not in (int, float, Rational):
            return NotImplemented
        
        return float(self) < float(num2)

    def __gt__ (self, num2:int|float|Rational) -> bool: # >
        if type(num2) not in (int, float, Rational):
            return NotImplemented
        
        return float(self) > float(num2)

    def __le__ (self, num2:int|float|Rational) -> bool: # <=
        if type(num2) not in (int, float, Rational):
            return NotImplemented
        
        return float(self) <= float(num2)

    def __ge__ (self, num2:int|float|Rational) -> bool: # >=
        if type(num2) not in (int, float, Rational):
            return NotImplemented
        
        return float(self) >= float(num2)
    
    # ABSOLUTE/NEGATION

    def __neg__ (self) -> int|Rational:
        return Rational(-self.numerator, self.denominator).simplify()

    def __pos__ (self) -> int|Rational:
        return self.simplify()

    def __abs__ (self) -> int|Rational:
        return Rational(abs(self.numerator), abs(self.denominator)).simplify()
    
    # MATHEMATICAL OPERATIONS
    
    def __add__ (self, num2:int|float|Rational) -> int|float|Rational:
        if type(num2) not in (int, float, Rational):
            return NotImplemented
        
        if type(num2) == float:
            return self.numerator/self.denominator + num2
        
        if type(num2) == int:
            return Rational(self.numerator+num2*self.denominator, self.denominator).simplify()
        
        # fraction addition
        if self.denominator == num2.denominator:
            return Rational(self.numerator+num2.numerator, self.denominator).simplify()
        
        lcm = math.lcm(self.denominator, num2.denominator)
        numerator = self.numerator*(lcm/self.denominator)+num2.numerator*(lcm/num2.denominator)
        return Rational(numerator, lcm).simplify()
    
    def __radd__ (self, num2:int|float|Rational) -> int|float|Rational:
        if type(num2) not in (int, float, Rational):
            return NotImplemented
        
        return self.__add__(num2)

    def __sub__ (self, num2:int|float|Rational) -> int|float|Rational:
        if type(num2) not in (int, float, Rational):
            return NotImplemented
        
        return self.__add__(-num2)
    
    def __rsub__ (self, num1:int|float|Rational) -> int|float|Rational:
        if type(num1) not in (int, float, Rational):
            return NotImplemented
        
        return (-self).__add__(num1)
    
    def __mul__ (self, num2:int|float|Rational) -> int|float|Rational: 
        if type(num2) not in (int, float, Rational):
            return NotImplemented
        
        if type(num2) == float:
            return self.numerator/self.denominator * num2
        
        if type(num2) == int:
            return Rational(self.numerator*num2, self.denominator).simplify()
        
        # if rational
        return Rational(self.numerator*num2.numerator, self.denominator*num2.denominator).simplify()
    
    def __rmul__ (self, num2:int|float|Rational) -> int|float|Rational:
        if type(num2) not in (int, float, Rational):
            return NotImplemented
        
        return self.__mul__(num2)
    
    def __pow__ (self, power:int|float|Rational) -> int|float|Rational: 
        # check before - no returns allowed until type is confirmed
        if type(power) not in (int, float, Rational):
            return NotImplemented
        
        if power == 0: 
            return 1
        
        if type(power) == float:
            return (self.numerator/self.denominator) ** power
        
        if type(power) == int:
            if power < 0: # flip fraction
                return Rational(self.denominator**abs(power), self.numerator**abs(power)).simplify()
            return Rational(self.numerator**power, self.denominator**power).simplify()
        
        # if rational
        # automatically simplified when Power is declared
        return Power(self, power).simplify()

    def __rpow__ (self, base:int|float|Rational) -> int|float|Rational:
        # check before - no returns allowed until type is confirmed
        if type(base) not in (int, float, Rational):
            return NotImplemented
        
        if self.numerator == 0:
            return 1
        
        if type(base) == float:
            return base**(self.numerator/self.denominator)
        
        # if int or rational
        # Power.simplify() will simplify
        return Power(base, self).simplify()
    
    def __truediv__ (self, num2:int|float|Rational) -> int|float|Rational:        
        if type(num2) == float:
            return self.__mul__(num2**-1)
        
        if type(num2) == int:
            return self.__mul__(Rational(1, num2))
        
        if type(num2) == Rational:
            return self.__mul__(num2.flip())
        
        return NotImplemented
    
    def __rtruediv__ (self, num1:int|float|Rational) -> int|float|Rational:
        if type(num1) not in (int, float, Rational):
            return NotImplemented
           
        return self.flip().__mul__(num1)
    
    # CONVERT TYPE

    def __float__ (self) -> float:
        return self.numerator/self.denominator

    def __repr__ (self) -> str:
        if self.denominator == 1:
            return str(self.numerator)
        
        if type(self.numerator) == int and type(self.denominator) == int and self.numerator in range(-1, 10) and self.denominator in range(1, 10):
            negative = "-" if self.numerator/self.denominator < 0 else ""
            return negative + f"{superscript[str(abs(self.numerator))]}/{subscript[str(abs(self.denominator))]}"
        
        return f"{self.numerator}/{self.denominator}"
    
class Power:
    def __init__ (self, base:int|Rational, power:int|Rational) -> None:
        if type(base) not in (int, float, Rational) or type(power) not in (int, float, Rational):
            raise TypeError(f"unable to create Power with type {type(base)} and/or {type(power)}")
        
        # *1 ensures rational is fully simplified by forcing an operation
        # for example rational (9/1)*1 => 9 int
        self.base = base*1
        self.power = power*1

        self._simplify_internal()

    def _simplify_internal(self) -> None:
        if self.power == 0: self.base = 1; return
        
        # fully simplify for floats
        if type(self.base) == float or type(self.power) == float:
            self.base = float(self.base)**float(self.power)
            self.power = 1
            return

        # 2^5
        if type(self.power) == int:
            self.base = self.base ** self.power
            self.power = 1
            return
        
        # Power can fully simplify: 4^(1/2)=2
        if self.base**float(self.power) == int(self.base**float(self.power)):
            self.base = int(self.base**float(self.power))
            self.power = 1
            return
        
        # 2^(2/3)=4^(1/3)
        if type(self.power) == Rational:
            self.base = self.base ** abs(self.power.numerator)
            self.power = Rational(1, self.power.denominator*(self.power.numerator/abs(self.power.numerator)))
        
        # (1/3)^-1=3, (1/3)^(1/3)=3^-(1/3) (3/2)^-1=(3/2)^1
        if type(self.base) == Rational:
            if self.base.numerator == 1 or (self.base.numerator != 1 and self.power < 0):
                self.base = self.base.flip()
                self.power *= -1

        # ADD HERE include case 4^(1/4)=2^(1/2)

    # assuming _simplify_internal() was called
    def simplify(self) -> int|Rational|Power:
        if self.power == 1:
            return self.base
        
        if self.power == Rational(-1, 2):
            if type(self.base) in (int, float):
                return ConstProduct([Power(self.base, Rational(1, 2)), Rational(1, self.base)])
            return ConstProduct([Power(self.base, Rational(1, 2)), self.base.flip()])
        
        return self
    
    def flip(self) -> Power:
        return Power(self.base, self.power*-1).simplify()
    
    def multipliable(self, num2:int|float|Rational|Power) -> bool:
        if type(num2) == float:
            return True
        
        if type(num2) in (int, Rational):
            return self.base == num2
        
        if type(num2) == Power:
            return self.base == num2.base
        
        return False
    
    def exponentiable(self, num2:int|float|Rational) -> bool:
        pass
    
    # check if positive
    @property
    def pos(self) -> bool:
        return self.base >= 0

    # COMPARISONS
    
    def __eq__ (self, num2:int|float|Rational|Power) -> bool:   
        if type(num2) not in (int, float, Rational, Power):
            return False
        
        return float(self) == float(num2)

    def __ne__ (self, num2:int|float|Rational|Power) -> bool:
        return not self.__eq__(num2)
    
    def __lt__ (self, num2:int|float|Rational|Power) -> bool: # <
        if type(num2) not in (int, float, Rational, Power):
            return NotImplemented
        
        return float(self) < float(num2)

    def __gt__ (self, num2:int|float|Rational|Power) -> bool: # >
        if type(num2) not in (int, float, Rational, Power):
            return NotImplemented
        
        return float(self) > float(num2)

    def __le__ (self, num2:int|float|Rational|Power) -> bool: # <=
        if type(num2) not in (int, float, Rational, Power):
            return NotImplemented
        
        return float(self) <= float(num2)

    def __ge__ (self, num2:int|float|Rational|Power) -> bool: # >=
        if type(num2) not in (int, float, Rational, Power):
            return NotImplemented
        
        return float(self) >= float(num2)

    # ABSOLUTE/NEGATION

    def __neg__ (self) -> Power:
        return Power(self.base * -1, self.power).simplify()

    def __pos__ (self) -> Power:
        return self.simplify()

    def __abs__ (self) -> Power:
        return Power(abs(self.base), self.power).simplify()
    
    # MATHEMATICAL OPERATIONS
    
    def __add__ (self, num2:int|float|Rational|Power):
        if type(num2) not in (int, float, Rational, Power):
            return NotImplemented
        
        return Sum([self, num2]).simplify()

    def __radd__ (self, num1:int|float|Rational|Power):
        if type(num1) not in (int, float, Rational, Power):
            return NotImplemented
        
        return self.__add__(num1)

    def __sub__ (self, num2:int|float|Rational|Power):
        if type(num2) not in (int, float, Rational, Power):
            return NotImplemented
        
        return self.__add__(-num2)

    def __rsub__ (self, num1:int|float|Rational|Power):
        if type(num1) not in (int, float, Rational, Power):
            return NotImplemented
        
        return (-self).__add__(num1)
    
    def __mul__ (self, num2:int|float|Rational|Power) -> int|float|Rational|Power|ConstProduct:
        if type(num2) not in (int, float, Rational, Power):
            return NotImplemented
        
        if type(num2) == float:
            return float(self) * num2
        
        if type(num2) in (int, Rational):
            if self.base == num2:
                return Power(self.base, self.power+1).simplify()

        if type(num2) == Power:
            if self.base == num2.base:
                return Power(self.base, self.power+num2.power).simplify()
            
        # if no shared base
        return ConstProduct([self, num2])
    
    def __rmul__ (self, num2:int|float|Rational|Power) -> int|float|Rational|Power|ConstProduct:
        if type(num2) not in (int, float, Rational, Power):
            return NotImplemented
        
        return self.__mul__(num2)
    
    def __pow__ (self, power:int|float|Rational|Power) -> int|float|Rational|Power:
        if type(power) not in (int, float, Rational, Power):
            return NotImplemented
        
        if power == 0: 
            return 1
        
        if type(power) == float:
            return self.base**float(self.power)**power

        if type(power) != Power:
            return Power(self.base, self.power*power).simplify()
        
        # else if power == base
        return LargePower(self, power).simplify()
    
    def __rpow__ (self, base:int|float|Rational|Power):
        if type(base) not in (int, float, Rational, Power):
            return NotImplemented
        
        return LargePower(base, self).simplify()
    
    def __truediv__ (self, num2:int|float|Rational|Power) -> int|float|Rational|Power|ConstProduct:
        if type(num2) not in (int, float, Rational, Power):
            return NotImplemented
        
        if type(num2) == int:
            return self.__mul__(Rational(1, num2))

        return self.__mul__(num2**-1)
    
    def __rtruediv__ (self, num1:int|float|Rational|Power) -> int|float|Rational|Power|ConstProduct:
        if type(num1) not in (int, float, Rational, Power):
            return NotImplemented
        
        return self.flip().__mul__(num1)

    # CONVERT TYPE

    def __float__ (self) -> float:
        return self.base**float(self.power)

    def __repr__ (self) -> str:
        if type(self.power) != int:
            return f"{self.base}({self.power})"
        
        power_str = ""
        for c in str(self.power):
            power_str += superscript[c]

        return f"{self.base}{power_str}"

class ConstProduct:
    # constants include int, float, rational, base
    def __init__ (self, const_list:list[int|float|Rational|Power]) -> None:
        if type(const_list) != list:
            raise TypeError("const_list provided is not type list")
        
        if len(const_list) == 0:
            raise ValueError("const_list is empty")
        
        if any([type(c) not in (int, float, Rational, Power) for c in const_list]):
            raise TypeError("unable to create ConstProduct with the datatypes provided")

        self._simplify_internal(const_list)

    def _simplify_internal(self, const_list) -> None:
        # simplify all constants first
        for pos, c in enumerate(const_list):
            if type(c) not in (int, float):
                const_list[pos] = c.simplify()

        # simplify everything that is not a base
        self.rational_val = 1
        base_list = []
        for c in const_list:
            if type(c) == Power:
                base_list.append(c)
                continue
            self.rational_val *= c
        
        # if no bases present
        if len(base_list) == 0:
            self.const_list = [self.rational_val]
            return
        
        # sorts through bases
        simplified_base_list = [base_list[0]]
        for new_c in base_list[1:]:
            for pos, current_c in enumerate(simplified_base_list):
                if current_c.multipliable(new_c):
                    simplified_base_list[pos] *= new_c
                    break
            else:
                simplified_base_list.append(new_c)

        # checks if any bases are multipliable to the non_base_val
        base_list = []
        for base in simplified_base_list:
            if base.multipliable(self.rational_val):
                self.rational_val *= base
            else:
                base_list.append(base)

        # if no bases present after simplification
        if len(base_list) == 0:
            self.const_list = [self.rational_val]
            return
        
        self.const_list = [self.rational_val] + base_list

    def simplify(self) -> int|float|Rational|Power|ConstProduct:
        if len(self.const_list) == 1:
            if type(self.const_list[0]) not in (int, float):
                return self.const_list[0].simplify()
            return self.const_list[0]
        
        return self
    
    def flip(self) -> ConstProduct:
        const_list = [c**-1 if type(c) != int else Rational(1, c) for c in self.const_list]
        return ConstProduct(const_list).simplify()

    @property
    def pos(self) -> bool:
        return float(self) >= 0
    
    @property # assuming fully simplified
    def rational(self) -> int|float|Rational:
        return self.rational_val
    
    @property
    def non_rationals(self) -> list:
        return [c for c in self.const_list if type(c) == Power]

    # COMPARISONS
    
    def __eq__ (self, num2:int|float|Rational|Power|ConstProduct) -> bool:
        if type(num2) not in (int, float, Rational, Power, ConstProduct):
            return False
        return float(self) == float(num2)

    def __ne__ (self, num2:int|float|Rational|Power|ConstProduct) -> bool:
        return not self.__eq__(num2)
    
    def __lt__ (self, num2:int|float|Rational|Power|ConstProduct) -> bool: # <
        if type(num2) not in (int, float, Rational, Power, ConstProduct):
            return NotImplemented
        
        return float(self) < float(num2)

    def __gt__ (self, num2:int|float|Rational|Power|ConstProduct) -> bool: # >
        if type(num2) not in (int, float, Rational, Power, ConstProduct):
            return NotImplemented
        
        return float(self) > float(num2)

    def __le__ (self, num2:int|float|Rational|Power|ConstProduct) -> bool: # <=
        if type(num2) not in (int, float, Rational, Power, ConstProduct):
            return NotImplemented
        
        return float(self) <= float(num2)

    def __ge__ (self, num2:int|float|Rational|Power|ConstProduct) -> bool: # >=
        if type(num2) not in (int, float, Rational, Power, ConstProduct):
            return NotImplemented
        
        return float(self) >= float(num2)

    # ABSOLUTE/NEGATION

    def __neg__ (self) -> ConstProduct:
        new_const_list = self.const_list.copy()
        new_const_list[0] *= -1
        return ConstProduct(new_const_list)

    def __pos__ (self) -> ConstProduct:
        return self.simplify()

    def __abs__ (self) -> ConstProduct:
        new_const_list = [abs(c) for c in self.const_list]
        return ConstProduct(new_const_list)

    # MATHEMATICAL OPERATIONS
    
    def __add__ (self, num2:int|float|Rational|Power|ConstProduct) -> int|float|Rational|Power|ConstProduct:
        if num2 not in (int, float, Rational, Power, ConstProduct):
            return NotImplemented
        
        # return Sum
        return Sum([self, num2])

    def __radd__ (self, num1):
        self.__add__(num1)

    def __sub__ (self, num2:int|float|Rational|Power|ConstProduct) -> int|float|Rational|Power|ConstProduct:
        return self.__add__(-num2)

    def __rsub__ (self, num1):
        return (-self).__add__(num1)
    
    def __mul__ (self, num2:int|float|Rational|Power|ConstProduct) -> int|float|Rational|Power|ConstProduct:
        if type(num2) == float:
            return float(self) * num2
        
        if type(num2) in (int, Rational, Power):
            self.const_list.append(num2)
            return ConstProduct(self.const_list).simplify()
        
        if type(num2) == ConstProduct:
            return ConstProduct(self.const_list+num2.const_list).simplify()
        
        return NotImplemented
    
    def __rmul__ (self, num2:int|float|Rational|Power|ConstProduct) -> int|float|Rational|Power|ConstProduct:
        return self.__mul__(num2)
    
    def __pow__ (self, power:int|float|Rational|Power|ConstProduct) -> int|float|Rational|Power|ConstProduct:
        if type(power) == float:
            return float(self) ** power
        
        if type(power) in (int, Rational, Power):
            if power >= 0:
                self.const_list = [c**power for c in self.const_list]
            else:
                self.const_list = [c**power if type(c) != int else Rational(1, c**abs(power)) for c in self.const_list]
            return ConstProduct(self.const_list).simplify()
        
        # INCLUDE ConstProduct**ConstProduct -> large base
        
        return NotImplemented
    
    def __rpow__ (self, base:int|float|Rational|Power|ConstProduct) -> int|float|Rational|Power|ConstProduct:
        if type(base) == float:
            return base**float(self)
        
        # INCLUDE anything**ConstProduct -> large base
        
        return NotImplemented
    
    def __truediv__ (self, num2:int|float|Rational|Power|ConstProduct) -> int|float|Rational|Power|ConstProduct:
        if type(num2) == float:
            return float(self)/num2
        
        if type(num2) in (int, Rational, Power):
            self.const_list.append(num2**-1)
            return ConstProduct(self.const_list).simplify()
        
        if type(num2) == ConstProduct:
            return ConstProduct(self.const_list*num2**-1).simplify()
        
        return NotImplemented
    
    def __rtruediv__ (self, num1:int|float|Rational|Power|ConstProduct) -> int|float|Rational|Power|ConstProduct:
        if type(num1) == float:
            return num1/float(self)
        
        if type (num1) not in (int, Rational, Power, ConstProduct):
            return NotImplemented
        
        return num1*(self**-1)

    # CONVERT TYPE

    def __float__ (self) -> float:
        result = 1
        for c in self.const_list:
            result *= float(c)
        
        return float(result)

    def __repr__ (self) -> str:
        return "".join([str(c)+"*" for c in self.const_list])[:-1]

class Term:
    def __init__ (self, coefficient:int|float|Rational, var_powers:dict={}) -> None:
        if type(coefficient) not in (int, float, Rational, Power, ConstProduct):
            raise TypeError(f"unable to create Term with coefficient of type {type(coefficient)}")
        
        for var in var_powers:
            if var not in var_alphabet:
                raise ValueError(f"{var} of var_powers is not part of the standard alphabet")
        
        self.coefficient = coefficient

        self.var_powers = {}
        for var in var_powers:
            if var_powers[var] != 0:
                self.var_powers[var] = var_powers[var]

        self._simplify_internal()

    def _simplify_internal(self) -> None:
        for var in self.var_powers:
            if self.var_powers[var] == 0:
                self.var_powers.pop(var)

        if type(self.coefficient) not in (int, float):
            self.coefficient.simplify()

    def simplify(self):
        if self.coefficient == 0:
            return 0
        
        if self.var_powers == {}:
            if type(self.coefficient) in (int, float):
                return self.coefficient
            return self.coefficient.simplify()
        
        return self
    
    # Term ^ -1
    def flip(self) -> Term:
        if type(self.coefficient) == int:
            coefficient = Rational(1, self.coefficient)
        else:
            coefficient = self.coefficient**-1
        var_powers = {}
        for var in self.var_powers:
            var_powers[var] = self.var_powers[var]*-1
        return Term(coefficient, var_powers).simplify()
    
    def substitute(self, var_values:dict) -> Term:
        coefficient = self.coefficient
        var_powers = self.var_powers.copy()
        Product = 1
        for var in var_values:
            if var not in self.var_powers:
                continue

            if type(var_values[var]) in (int, float, Rational):
                coefficient *= Power(var_values[var], self.var_powers[var]).simplify()
            else:
                Product *= LargePower(var_values[var], self.var_powers[var]).simplify()
            
            var_powers.pop(var)

        return Product * Term(coefficient, var_powers).simplify()
    
    def differentiate(self, var) -> Term:
        if var not in self.var_powers:
            return 0
    
    def addible(self, term2:Term) -> bool:
        if term2 == 0:
            return True
        return self.var_powers == term2.var_powers
    
    @property # returns positivity of coefficient
    def pos(self) -> bool:
        return self.coefficient >= 0
    
    # COMPARISONS

    # don't use these unless comparing specifically terms
    def __eq__ (self, term2:Term) -> bool:
        if type(term2) != Term:
            return False
        elif self.var_powers == term2.var_powers and self.coefficient == term2.coefficient:
            return True
        
        return False
    
    def __ne__ (self, term2:Term) -> bool:
        return not self.__eq__(term2)
    
    # no lt, gt, le, ge (variable value)

    # ABSOLUTE/NEGATION

    def __neg__ (self) -> Term:
        return Term(self.coefficient*-1, self.var_powers.copy()).simplify()
    
    def __pos__ (self) -> Term:
        return self.simplify()
    
    def __abs__ (self) -> Term:
        return Term(abs(self.coefficient), self.var_powers.copy()).simplify()
        
    # MATHEMATICAL OPERATIONS
    
    def __add__ (self, term2) -> Term|Sum:      
        if type(term2) not in (int, float, Rational, Power, ConstProduct, Term):
            return NotImplemented
        
        if term2 == 0:
            return self
        
        if type(term2) != Term:
            return Sum([self, term2]).simplify()
        
        if term2.var_powers == self.var_powers:
            coefficient = self.coefficient + term2.coefficient
            return Term(coefficient, self.var_powers.copy()).simplify()
        
        return Sum([self, term2]).simplify()
    
    def __radd__ (self, term1) -> Term|Sum:
        if type(term1) not in (int, float, Rational, Power, ConstProduct, Term):
            return NotImplemented
        
        return self.__add__(term1)

    def __sub__ (self, term2:Term) -> Term|Sum:
        if type(term2) not in (int, float, Rational, Power, ConstProduct, Term):
            return NotImplemented
        
        return self.__add__(-term2)
    
    def __rsub__ (self, term1) -> Term|Sum:
        if type(term1) not in (int, float, Rational, Power, ConstProduct, Term):
            return NotImplemented
        
        return (-self).__add__(term1)

    def __mul__ (self, term2) -> Term:
        '''(term2:int|float|Rational|Power|ConstProduct|Term) -> Term
        '''
        if type(term2) in (int, float, Rational, Power, ConstProduct):
            coefficient = self.coefficient * term2
            return Term(coefficient, self.var_powers.copy()).simplify()
        
        if type(term2) != Term:
            return NotImplemented
        
        coefficient = self.coefficient * term2.coefficient
        var_powers = self.var_powers.copy()
        for var in term2.var_powers:
            if var not in var_powers:
                var_powers[var] = term2.var_powers[var]
            else:
                var_powers[var] += term2.var_powers[var]

        return Term(coefficient, var_powers).simplify()
        
    def __rmul__ (self, term1) -> Term:
        '''(term1:int|float|Rational|Power|ConstProduct|Term) -> Term
        '''
        return self.__mul__(term1)
        
    def __pow__ (self, power) -> Term|LargePower:
        if type(power) not in (int, float, Rational, Power, ConstProduct, Term):
            return NotImplemented
        
        if type(power) in (Power, ConstProduct, Term):
            return LargePower(self, power).simplify()
        
        if power == 0:
            return 1

        # flip into to rational if power < 0
        if power < 0 and type(self.coefficient) == int:
            coefficient = Rational(1, self.coefficient**abs(power))
        else:
            coefficient = self.coefficient ** power
        
        var_powers = {}
        for var in self.var_powers:
            var_powers[var] = self.var_powers[var]*power
        return Term(coefficient, var_powers).simplify()
        
    def __rpow__ (self, base) -> Term|LargePower:
        if type(base) not in (int, float, Rational, Power, ConstProduct, Term):
            return NotImplemented
        
        return LargePower(base, self).simplify()

    def __truediv__ (self, term2) -> Term:
        if type(term2) not in (int, float, Rational, Power, ConstProduct, Term):
            return NotImplemented
        
        if type(term2) == int:
            return self.__mul__(Rational(1, term2))
        
        return self.__mul__(term2**-1)
        
    def __rtruediv__ (self, term1) -> Term:
        if type(term1) not in (int, float, Rational, Power, ConstProduct, Term):
            return NotImplemented
        
        return self.flip().__rmul__(term1)
    
    # CONVERTIONS

    def __repr__ (self) -> str:
        repr_str = ""
        
        if self.coefficient == -1:
            repr_str += "-"
        elif self.coefficient != 1:
            repr_str += str(self.coefficient)

        ordered_vars = sorted([var for var in self.var_powers])
        for var in ordered_vars:
            if self.var_powers[var] == 1:
                repr_str += var
                continue
            repr_str += str(var) + "".join([superscript[s] for s in str(self.var_powers[var])])
        return repr_str

class Sum:
    def __init__ (self, term_list:list) -> None:
        if any([type(term) not in numeric for term in term_list]):
            raise TypeError("unable to create Sum with the types provided")
        
        self.term_list = term_list
        self._simplify_internal()

    def _simplify_internal(self) -> None:
        # simplify all terms
        self.term_list = [term.simplify() if type(term) not in (int, float) else term for term in self.term_list]

        # check for embeded Sums -> add together
        term_list = []
        for term in self.term_list:
            if type(term) == Sum:
                term_list += term.term_list
            else:
                term_list.append(term)

        # split terms to constant and var
        rational, bases, var_terms, exp_terms = 0, [], [], []
        for term in term_list:
            if type(term) in (int, float, Rational):
                rational += term
            elif type(term) in (Power, ConstProduct):
                bases.append(term)
            elif type(term) == Term:
                var_terms.append(term)
            else:
                exp_terms.append(term)
        
        # attempt to add vars

        if len(var_terms) != 0:
            new_term_list = [var_terms[0]]
            for old_term in var_terms[1:]:
                for pos, current_term in enumerate(new_term_list):
                    if type(current_term) == int: # -10x + 10x = 0 -> current_term becomes int
                        continue

                    if current_term.addible(old_term):
                        new_term_list[pos] += old_term
                        break
                else:
                    new_term_list.append(old_term)

            for pos, term in enumerate(new_term_list):
                if type(term) in (int, float, Rational):
                    rational += term
                    new_term_list.pop(pos)
        else:
            new_term_list = var_terms

        self.term_list = exp_terms + new_term_list + bases

        if rational != 0 or self.term_list == []:
            self.term_list.append(rational)

    def simplify(self):
        if len(self.term_list) == 1:
            return self.term_list[0]

        return self
        
    def substitute(self, var_values:dict) -> Sum:
        term_list = []
        for term in self.term_list:
            if type(term) in (int, float, Rational, Power, ConstProduct):
                term_list.append(term)
                continue
            term_list.append(term.substitute(var_values))
        return Sum(term_list).simplify()
    
    # a(b+c) = ab + ac
    def distribute(self, term2:int|float|Rational|Power|ConstProduct|Term) -> Sum:
        if term2 == 0: return 0
        
        new_term_list = []
        for term in self.term_list:
            new_term_list.append(term*term2)
        
        return Sum(new_term_list).simplify()
    
    def expand(self) -> Sum:
        new_term_list = []
        for term in self.term_list:
            if type(term) == Product:
                new_term_list.append(term.expand())
            else:
                new_term_list.append(term)

        return Sum(new_term_list).simplify()

    # NO COMPARISONS (all return false)
    def __eq__ (self, exp2) -> bool:
        return False
    
    def __ne__ (self, exp2) -> bool:
        return not self.__eq__ (exp2)

    # SIGNS

    def __neg__ (self) -> Sum:
        term_list = self.term_list.copy()
        term_list[0] *= -1
        return Sum(term_list).simplify()

    def __pos__ (self) -> Sum:
        return self.simplify()
    
    def __abs__ (self) -> Sum:
        term_list = [abs(term) for term in self.term_list]
        return Sum(term_list).simplify()

    # MATHEMATICAL OPERATIONS

    def __add__ (self, exp2) -> Sum:
        if type(exp2) not in numeric:
            return NotImplemented
        
        if type(exp2) != Sum:
            term_list = self.term_list.copy()
            term_list.append(exp2)
            return Sum(term_list).simplify()

        return Sum(self.term_list + exp2.term_list).simplify()

    def __radd__ (self, exp1) -> Sum:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return self.__add__(exp1)

    def __sub__ (self, exp2) -> Sum:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return self.__add__(-exp2)

    def __rsub__ (self, exp1) -> Sum:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return (-self).__add__(exp1)

    def __mul__ (self, exp2) -> Sum:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return Product([self, exp2]).simplify()

    def __rmul__ (self, exp1) -> Sum:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return self.__mul__(exp1)

    def __pow__ (self, exp2) -> LargePower:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return LargePower(self, exp2).simplify()

    def __rpow__ (self, exp1):
        if type(exp1) not in numeric:
            return NotImplemented
        
        return LargePower(exp1, self).simplify()

    def __truediv__ (self, exp2) -> Sum:
        if type(exp2) not in numeric:
            return NotImplemented
        
        if type(exp2) == int:
            return self.__mul__(Rational(1, exp2))

        return self.__mul__(exp2**-1)

    def __rtruediv__ (self, exp1) -> Sum:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return self.flip().__mul__(exp1)

    # CONVERSIONS

    def __repr__ (self) -> str:
        repr_str = str(self.term_list[0])
        for term in self.term_list[1:]:
            if type(term) in (int, float):
                repr_str += ("+" if term >= 0 else "") + str(term)
            elif type(term) in (Sum, Product, LargePower):
                repr_str += "+" + str(term)
            else:
                repr_str += ("+" if term.pos else "") + str(term)
        return repr_str

class Product:
    def __init__ (self, exp_list:list) -> None:
        if any([type(exp) not in numeric for exp in exp_list]):
            raise TypeError("unable to create Product with types provided")
        
        self.exp_list = exp_list

        self._simplify_internal()

    def _simplify_internal(self) -> None:
        # simplify all Sums
        self.exp_list = [exp.simplify() if type(exp) not in (int, float) else exp for exp in self.exp_list]

        # check for embeded Products -> multiply together
        # multiply all small Sums together in first slot
        exp_list = [1]
        for exp in self.exp_list:
            if type(exp) == Product:
                exp_list += exp.term_list
            elif type(exp) in (int, float, Rational, Power, ConstProduct, Term):
                exp_list[0] *= exp
            else:
                exp_list.append(exp)

        # check for large bases

        # remove ones
        self.exp_list = [exp for exp in exp_list if exp != 1]

    def simplify(self):
        if len(self.exp_list) == 1:
            return self.exp_list[0]
        
        return self
    
    def substitute(self, var_values:dict) -> Product:
        exp_list = []
        for exp in self.exp_list:
            if type(exp) in (int, float, Rational, Power, ConstProduct):
                exp_list.append(exp)
                continue
            exp_list.append(exp.substitute(var_values))
        return Product(exp_list).simplify()
    
    def expand(self):
        exp_list = []
        for exp in self.exp_list:
            if type(exp) == Sum:
                exp_list.append(exp)
            elif type(exp) == LargePower:
                exp_list.append(exp.expand())

        if len(exp_list) == 0:
            return self
        
        non_exp_list = [exp for exp in self.exp_list if type(exp) not in (Sum, LargePower)]

        if type(self.exp_list[0]) in (int, float, Rational, Power, ConstProduct, Term):
            exp_list[0] = exp_list[0].distribute(self.exp_list[0])
            non_exp_list.pop(0)

        # (x-3)(2x+2) = 2x(x-3)+2(x-3) = 2x^2-4x-6
        
        while len(exp_list) >= 2:
            exp0 = exp_list[0]
            exp_list[0] = exp0.distribute(exp_list[1].term_list[0])
            for term in exp_list[1].term_list[1:]:
                exp_list[0] += exp0.distribute(term)
            exp_list.pop(1)

        return Product(exp_list+non_exp_list).simplify()
    
    # NO COMPARISONS (all return false)
    def __eq__ (self, exp2) -> bool:
        return False
    
    def __ne__ (self, exp2) -> bool:
        return not self.__eq__ (exp2)

    # ABSOLUTE/NEGATION

    def __neg__ (self) -> Product:
        return self.__mul__ (-1)

    def __pos__ (self) -> Product:
        return self.simplify()

    def __abs__ (self) -> Product:
        return Product([abs(exp) for exp in self.exp_list]).simplify()

    # MATHEMATICAL OPERATIONS

    def __add__ (self, exp2) -> Sum:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return Sum([self, exp2]).simplify()

    def __radd__ (self, exp1) -> Sum:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return self.__add__(exp1)
        
    def __sub__ (self, exp2) -> Sum:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return self.__add__(-exp2)
        
    def __rsub__ (self, exp1) -> Sum:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return (-self).__add__(exp1)

    def __mul__ (self, exp2) -> Product:
        if type(exp2) not in numeric:
            return NotImplemented
        
        exp_list = self.exp_list.copy()
        exp_list.append(exp2)
        return Product(exp_list).simplify()

    def __rmul__ (self, exp1) -> Product:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return self.__mul__(exp1)

    def __pow__ (self, exp2) -> LargePower:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return LargePower(self, exp2).simplify()
    
    def __rpow__ (self, exp1) -> LargePower:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return LargePower(exp1, self).simplify()

    def __truediv__ (self, exp2) -> Product:
        if type(exp2) not in numeric:
            return NotImplemented
        
        if type(exp2) == int:
            return self.__mul__(Rational(1, exp2))
        
        return self.__mul__(exp2**-1)

    def __rtruediv__ (self, exp1) -> Product:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return self.flip().__mul__(exp1)

    # CONVERSIONS

    def __repr__ (self) -> str:
        simple_exp_str = str(self.exp_list[0]) if type(self.exp_list[0]) in (int, float, Rational, Power, ConstProduct, Term, Factorial, LargePower) else f"({self.exp_list[0]})"
        return simple_exp_str + "".join([f"({str(exp)})" if type(exp) not in (LargePower, Factorial) else str(exp) for exp in self.exp_list[1:]])

class LargePower:
    def __init__ (self, base, power) -> None:
        '''(base:numeric, power:numeric)
        includes int, float, Rational, Power, ConstProduct, LargePower, Sum
        '''
        
        if type(base) not in numeric:
            raise TypeError(f"unable to create LargePower with base of type {type(base)}")
        if type(power) not in numeric:
            raise TypeError(f"unable to create LargePower with power of type {type(power)}")

        self.base = base
        self.power = power

        self._simplify_internal()

    def _simplify_internal(self) -> None:
        pass

    def simplify(self):
        if self.base == 0:
            return 0
        if self.power == 0:
            return 1
        if self.power == 1:
            return self.base
        
        if type(self.base) == float or type(self.power) == float:
            return self.base ** self.power
        
        if type(self.base) in (int, float, Rational) and type(self.power) in (int, float):
            if self.power < 0:
                return Rational(1, self.base**abs(self.power))
            return self.base ** self.power

        return self
    
    def substitute(self, var_values:dict) -> LargePower:
        base, power = self.base, self.power
        if type(self.base) not in (int, float, Rational, Power, ConstProduct):
            base = self.base.substitute(var_values)
        if type(self.power) not in (int, float, Rational, Power, ConstProduct):
            power = self.power.substitute(var_values)

        return LargePower(base, power).simplify()
    
    def expand(self) -> LargePower:
        if type(self.power) == int:
            return Product([self.base for i in range(self.power)]).expand()

        return self

    def multipliable(self, num2) -> bool:
        if type(num2) in (Power, LargePower):
            return self.base == num2.base
        
        return self.base == num2

    # NO COMPARISONS (all return false)
    def __eq__ (self, exp2) -> bool:
        return False
    
    def __ne__ (self, exp2) -> bool:
        return not self.__eq__ (exp2)

    # ABSOLUTE/NEGATION

    def __neg__ (self) -> LargePower:
        return LargePower(self.base*-1, self.power).simplify()

    def __pos__ (self) -> LargePower:
        return self.simplify()
    
    def __abs__ (self) -> LargePower:
        return LargePower(abs(self.base), self.power).simplify()

    # MATHEMATICAL OPERATIONS

    def __add__ (self, exp2) -> Sum:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return Sum([self, exp2]).simplify()

    def __radd__ (self, exp1) -> Sum:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return self.__add__(exp1)

    def __sub__ (self, exp2) -> Sum:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return self.__add__(-exp2)

    def __rsub__ (self, exp1) -> Sum:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return (-self).__add__(exp1)

    def __mul__ (self, exp2) -> Product:
        if type(exp2) not in numeric:
            return NotImplemented

    def __rmul__ (self, exp1) -> Product:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return self.__mul__(exp1)

    def __pow__ (self, exp2) -> LargePower:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return LargePower(self, exp2).simplify()

    def __rpow__ (self, exp1) -> LargePower:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return LargePower(exp1, self).simplify()

    def __truediv__ (self, exp2) -> Product:
        if type(exp2) not in numeric:
            return NotImplemented
        
        if type(exp2) == int:
            return Product([self, Rational(1, exp2)]).simplify()
        
        return Product([self, exp2**-1])
    
    def __rtruediv__ (self, exp1) -> Product:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return Product(exp1, self.flip()).simplify()

    # CONVERSIONS

    def __repr__ (self) -> str:
        base_str = f"({self.base})" if type(self.base) in (Rational, ConstProduct, Term, Product, Sum) else str(self.base)
        if type(self.power) == int:
            return base_str + "".join([superscript[i] for i in str(self.power)])
        return f"{base_str}^({self.power})"

class Factorial:
    def __init__ (self, exp:Term|Sum|Product|LargePower|Factorial):
        if type(exp) not in numeric:
            raise TypeError("Sum provided is not numeric")
        
        if type(exp) not in (int, float):
            self.exp = exp.simplify()
        else:
            self.exp = exp

    def simplify(self):
        if type(self.exp) == int:
            total = 1
            for i in range(self.exp):
                total *= i + 1
            return total
        
        return self

    def substitute(self, var_values:dict) -> int|Factorial:
        return Factorial(self.exp.substitute(var_values)).simplify()
    
    def flip(self) -> LargePower:
        return LargePower(self, -1).simplify()
    
    # ABSOLUTE/NEGATION

    def __neg__ (self) -> Product:
        return Product([-1, self]).simplify()
    
    def __pos__ (self) -> Factorial:
        return self
    
    def __abs__ (self) -> Factorial:
        return self
    
    # MATHEMATICAL OPERATIONS

    def __add__ (self, exp2) -> Sum:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return Sum(self, exp2).simplify()
    
    def __radd__ (self, exp1) -> Sum:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return self.__add__(exp1)
    
    def __sub__ (self, exp2) -> Sum:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return self.__add__(-exp2)
    
    def __rsub__ (self, exp1) -> Sum:
        if type(exp1) not in numeric:
            return NotImplemented

        return (-self).__add__(exp1)
    
    def __mul__ (self, exp2) -> Product:
        if type(exp2) not in numeric:
            return NotImplemented

        return Product([self, exp2]).simplify()
    
    def __rmul__ (self, exp1) -> Product:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return self.__mul__(exp1)
    
    def __pow__ (self, exp2) -> LargePower:
        if type(exp2) not in numeric:
            return NotImplemented

        return LargePower(self, exp2).simplify()
    
    def __rpow__ (self, exp1) -> LargePower:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return LargePower(self, exp1).simplify()
    
    def __truediv__ (self, exp2) -> Product:
        if type(exp2) not in numeric:
            return NotImplemented
        
        return self.__mul__(exp2**-1)
    
    def __rtruediv__ (self, exp1) -> Product:
        if type(exp1) not in numeric:
            return NotImplemented
        
        return self.flip().__mul__(exp1)
    
    # CONVERSIONS

    def __repr__ (self) -> str:
        return f"({self.exp})!"

numeric = (int, float, Rational, Power, ConstProduct, Term, Sum, Product, LargePower, Factorial)
