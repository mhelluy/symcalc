import sympy as sp
import re

m_functions = ["cos(","sin(","tan(","sqrt(","pi","ln(","log(","sinh(","cosh(","tanh(","arcsin(","arccos(","arctan(","arcsinh(","arccosh(","arctanh(","exp(","factorial(","abs(","sign(","floor(","ceiling(","round(","gamma("]
def sympify(expr,locals=None):
    i = 0
    while i < len(expr) - 1:
        if expr[i:i+2] == ")(":
            expr = expr[:i+1] + "*" + expr[i+1:]
            i += 3
        found = True
        while found:
            for f in m_functions:
                if expr[i:i+len(f)] == f:
                    i += len(f) - 1
                    found = True
                    break
            found = False
        
        if re.match(r"^[a-zA-Z0-9][a-zA-Z\(]$",expr[i:i+2]):
            expr = expr[:i+1] + "*" + expr[i+1:]
        i += 1

    expr = expr.replace("$","SYMCALCDOLLAR")
    locals["SYMCALCDOLLAR"] = locals["$"]
    if type(expr) is str:
        return sp.sympify(expr,locals=locals)
    else:
        return expr
    
def pretty(expr,ante=""):
    if type(expr) is str:
        return ante + expr
    lignes = [len(ante)*" " + l for l in sp.pretty(expr).split("\n")]
    if ante:
        lignes[-1] = ante + lignes[-1][len(ante):]
    return "\n".join(lignes)