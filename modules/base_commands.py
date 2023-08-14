import sympy as sp
import re
"""
This module contains the base commands for the calculator.
"""

class BaseCommands:
    def __init__(self,brd) -> None:
        self.brd = brd
        self.current = "$"

    def set(self,var=None,value=None):
        if var is None:
            var = self.current
        if value is None:
            value = self.current
        self.current = var
        return self.brd.set(var,value)
    
    def delete(self,var):
        if var == "$":
            return (None,"Cannot delete $.")
        return self.brd.delete(var),"Ø"
    rem = delete
    
    def deletef(self,var,x="x"):
        return self.brd.deletef(var,x)
    remf = deletef
    
    def get(self,var=None):
        if var is None:
            var = self.current
        return var,self.brd.get(var)
    
    def get_current(self):
        return "_CURRENT_",self.current
    
    def add(self,value,var=None):
        if var is None:
            var = self.current
        return self.brd.add(var,value)
    
    def mul(self,value,var=None):
        if var is None:
            var = self.current
        return self.brd.mul(var,value)
    
    def sub(self,value,var=None):
        if var is None:
            var = self.current
        return self.brd.sub(var,value)
    
    def div(self,value,var=None):
        if var is None:
            var = self.current
        return self.brd.div(var,value)
    
    def expand(self,var=None):
        if var is None:
            var = self.current
        return var,self.brd.expand(var)
    exp = expand
    def simplify(self,var=None):
        if var is None:
            var = self.current
        return var,self.brd.simplify(var)
    
    def factor(self,var=None):
        if var is None:
            var = self.current
        return var,self.brd.factor(var)
    fact = fac = factor

    def solve(self,expr1,expr2,var=None):
        return "_S_",self.brd.solve(expr1,expr2,var)
    simp = simplify

    def func(self,var,value,x=None):
        self.brd.register_function(var,x)
        res = self.brd.exec_func(var,value,x)
        self.current = "$"
        return var+"("+str(res[0])+")", res[1]

    def exit(self):
        return (0,"Exiting console.")