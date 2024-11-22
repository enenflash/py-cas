from numeric import *

class Vector:
    pass

class Vector:
    def __init__ (self, i, j) -> None:
        if type(i) not in numeric or type(j) not in numeric:
            raise TypeError(f"unable to create vector with type {type(i)} and type {type(j)}")
        
        self.i = i
        self.j = j

        self._simplify_internal()

    def _simplify_internal(self) -> None:
        pass

    @property
    def magnitude(self):
        return (self.i**2 + self.j**2)**Rational(1, 2)
    
    @property # implement cosine and sine
    def angle(self):
        return 0
    
    @property
    def unitV(self):
        i_val = Rational(self.i, self.magnitude) if type(self.i) == int and type(self.magnitude) == int else self.i/self.magnitude
        j_val = Rational(self.j, self.magnitude) if type(self.j) == int and type(self.magnitude) == int else self.j/self.magnitude
        return Vector(i_val, j_val)
    
    # a.b/|b|
    def SProj_on(self, v2:Vector):
        if type(v2) != Vector:
            raise TypeError("must be vector")
        
        dotP = self.__mul__(v2)

        if type(dotP) == int and v2.magnitude == int:
            return Rational(dotP, v2.magnitude).simplify()
        
        return dotP/v2.magnitude
        
    # a.b/|b| * b.unitV
    def VProj_on(self, v2:Vector) -> Vector:
        if type(v2) != Vector:
            raise TypeError("must be vector")
        
        return self.SProj_on(v2) * v2.unitV

    def resolute(self, v2:Vector) -> Vector:
        if type(v2) != Vector:
            raise TypeError("must be vector")
        
        return self - self.VProj_on(v2)

    # COMPARISONS

    def __eq__ (self, v2) -> bool:
        return False

    def __ne__ (self, v2) -> bool:
        return not self.__eq__ (v2)
    
    # ABSOLUTE/NEGATION
    
    def __neg__ (self) -> Vector:
        return Vector(-self.i, -self.j)
    
    def __pos__ (self) -> Vector:
        return self
    
    def __abs__ (self) -> Vector:
        return Vector(abs(self.i), abs(self.j))
    
    # MATHEMATICAL OPERATIONS

    def __add__ (self, v2:Vector) -> Vector:
        if type(v2) != Vector:
            return NotImplemented
        
        return Vector(self.i + v2.i, self.j + v2.j)
    
    def __radd__ (self, v2:Vector) -> Vector:
        if type(v2) != Vector:
            return NotImplemented
        
        return self.__add__(v2)
    
    def __sub__ (self, v2:Vector) -> Vector:
        if type(v2) != Vector:
            return NotImplemented
        
        return self.__add__(-v2)
    
    def __rsub__ (self, v2:Vector) -> Vector:
        if type(v2) != Vector:
            return NotImplemented
        
        return (-self).__add__(v2)
    
    def __mul__ (self, v2):
        if type(v2) not in numeric:
            return NotImplemented
        
        # dot product
        if type(v2) == Vector:
            return self.i * v2.i + self.j * v2.j
        
        return Vector(self.i*v2, self.j*v2)
    
    def __rmul__ (self, v2):
        if type(v2) not in numeric:
            return NotImplemented
        
        return self.__mul__(v2)
    
    # no pow, rpow, rtruediv

    def __truediv__ (self, v2) -> Vector:
        if type(v2) not in numeric:
            return NotImplemented
        
        if type(v2) == int:
            return Vector(self.i * Rational(1, v2), self.j * Rational(1, v2))
        
        return Vector(self.i * v2**-1, self.j * v2**-1)
    
    # CONVERSIONS

    def __repr__ (self) -> str:
        return f"<{self.i}, {self.j}>"
    
numeric = (int, float, Rational, Power, ConstProduct, Term, Sum, Product, LargePower, Vector)
