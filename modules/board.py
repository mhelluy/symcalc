import sympy as sp
from modules.tools import sympify
import re


sp.init_printing()

class Board:
    def __init__(self) -> None:
        self.vars = {"$" : sp.sympify(0),"e":sp.E,"pi":sp.pi,"i":sp.I}
        self.functions = {}

    def delete(self,var):
        del self.vars[var]
        return var
    
    def deletef(self,var,x="x"):
        del self.functions[var,x]
        return var

    def set(self,var,value):
        if type(value) is str:
            self.vars[var] = sympify(value,locals=self.vars)
        else:
            self.vars[var] = value

        for key in self.functions:
            if key[0] == var:
                del self.functions[key]
        return var,self.vars[var]
    
    def add(self,var,value):
        if type(value) is str:
            self.vars[var] += sympify(value,locals=self.vars)
        else:
            self.vars[var] += value
        return var,self.vars[var]
    
    def mul(self,var,value):
        if type(value) is str:
            self.vars[var] *= sympify(value,locals=self.vars)
        else:
            self.vars[var] *= value
        return var,self.vars[var]
    
    def sub(self,var,value):
        if type(value) is str:
            self.vars[var] -= sympify(value,locals=self.vars)
        else:
            self.vars[var] -= value
        return var,self.vars[var]
    
    def div(self,var,value):
        if type(value) is str:
            self.vars[var] /= sympify(value,locals=self.vars)
        else:
            self.vars[var] /= value
        return var,self.vars[var]

    def get(self,var):
        return self.vars[var]
    
    def expand(self,var):
        self.vars[var] = sp.expand(self.vars[var])
        return self.vars[var]

    def factor(self,var):
        self.vars[var] = sp.factor(self.vars[var])
        return self.vars[var]

    def simplify(self,var):
        self.vars[var] = sp.simplify(self.vars[var])
        return self.vars[var]
    
    def register_function(self,var,x=None):
        if x is None:
            chn = re.sub(r"(?:sqrt|cos|sin|tan)\(","",str(self.vars[var]))
            x = chn[re.search(r"[\$a-zA-Z]",chn).start()]
        if (var,x) not in self.functions:
            self.functions[var,x] = sp.lambdify(x,self.vars[var],["sympy"])

    def exec_func(self,var,val,x=None):
        if x is None:
            x = [key for key in self.functions if key[0] == var][0][1]
        ant = sympify(val,locals=self.vars)
        value = self.functions[var,x](ant)
        self.vars["$"] = value
        return ant,value

    def solve(self,expr1,expr2,var=None):
        if type(expr1) is str:
            expr1 = sympify(expr1,locals=self.vars)
        if type(expr2) is str:
            expr2 = sympify(expr2,locals=self.vars)
        if var is None:
            var = str(expr1)[re.search(r"[\$a-zA-Z]",str(expr1)).start()]
        return sp.solve(expr1-expr2,var)
    
    def reduce_ineq(self,expr,var=None):
        if type(expr) is str:
            expr = sympify(expr,locals=self.vars)
        if var is None:
            var = str(expr)[re.search(r"[\$a-zA-Z]",str(expr)).start()]
        return sp.reduce_inequalities(expr,var)
    