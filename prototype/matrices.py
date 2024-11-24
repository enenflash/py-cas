from numeric import *

class Matrix:
    pass

class Matrix:
    def __init__ (self, mat:list[list]) -> None:
        for row in mat:
            if any([type(term) not in numeric for term in row]):
                raise TypeError("unable to create Matrix with non-numeric term")
            
        self.mat = mat

    def _simplify_internal(self) -> None:
        for j, row in enumerate(self.mat):
            self.mat[j] = [term.simplify() if type(term) not in (int, float) else term for term in row]

    @property
    def dim(self) -> tuple[int, int]:
        return len(self.mat), len(self.mat[0])
    
    @property
    def columns(self) -> list[list]:
        return [[self.mat[j][i] for j in range(len(self.mat[i]))] for i in range(len(self.mat[0]))]
    
    # find determinant of any size matrix
    @property
    def determinant(self):
        return

    # COMPARISON

    def __eq__ (self) -> bool:
        return False
    
    def __ne__ (self) -> bool:
        return not self.__eq__ (self)
    
    # ABSOLUTE/NEGATION

    def __neg__ (self) -> Matrix:
        return Matrix([[-term for term in row] for row in self.mat])
    
    def __pos__ (self) -> Matrix:
        return self
    
    def __abs__ (self) -> Matrix:
        return Matrix([[abs(term) for term in row] for row in self.mat])
    
    # MATHEMATICAL OPERATIONS

    def __add__ (self, m2:Matrix) -> Matrix:
        if type(m2) != Matrix:
            return NotImplemented
        
        if self.dim != m2.dim:
            raise ValueError("unable to add matrix of unequal dimensions")
        
        return Matrix([[term+m2[j][i] for i, term in enumerate(row)] for j, row in enumerate(self.mat)])
    
    def __radd__ (self, m2:Matrix) -> Matrix:
        if type(m2) != Matrix:
            return NotImplemented
        
        return self.__add__(m2)
    
    def __sub__ (self, m2:Matrix) -> Matrix:
        if type(m2) != Matrix:
            return NotImplemented
        
        return self.__add__(-m2)
    
    def __rsub__ (self, m2:Matrix) -> Matrix:
        if type(m2) != Matrix:
            return NotImplemented
        
        return (-self).__add__(m2)
    
    def __mul__ (self, m2) -> Matrix:
        if type(m2) not in numeric:
            return NotImplemented
        
        if type(m2) != Matrix:
            return Matrix([[term*m2 for term in row] for row in self.mat])
        
        if self.dim[1] != m2.dim[0]:
            raise ValueError("invalid dimensions for matrix multiplication")
        
        # for every row
        #new_mat = []
        #for r in range(len(self.mat)):
        #    new_mat.append([sum([self.mat[r][v]*m2.columns[c][v] for v in range(len(m2.mat))]) for c in range(len(m2.mat[0]))])
        new_mat = [[sum([self.mat[r][v]*m2.columns[c][v] for v in range(len(m2.mat))]) for c in range(len(m2.mat[0]))] for r in range(len(self.mat))]

        return new_mat

    def __rmul__ (self, m2) -> Matrix:
        if type(m2) not in numeric:
            return NotImplemented
        
        if type(m2) != Matrix:
            return self.__mul__(m2)
        
        return m2.__mul__(self)
    
    def __pow__ (self, m2) -> Matrix:

        if len(self.mat) != len(self.mat[0]):
            raise ValueError("invalid dimensions")

    # CONVERSION

    def __repr__ (self) -> str:
        return str(self.mat)

numeric = (int, float, Rational, Power, ConstProduct, Term, Sum, Product, LargePower, Matrix)