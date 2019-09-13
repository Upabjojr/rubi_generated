from generated_tempdir_2019_09_13_233901.generated_part000000 import match_root
from sympy import *

x = symbols("x")

def check_constraints(subst, constraints):
    for cons in constraints:
        ret = cons(**{k: v for k, v in subst.items() if k in cons.__code__.co_varnames})
        if not ret:
            return False
    return True


expr_list = [
    Integral(x, x),
    Integral(x**2, x),
    Integral(1/(1+x), x),
    Integral(1/x, x),
    Integral(sin(x), x),
    Integral(sin(x)*cos(x), x),
]

for expr in expr_list:
    g = match_root(expr)

    ret = list(g)
    results = [repl(**subst) for repl, subst, constraints in ret if check_constraints(subst, constraints)]

    clean = [i for i in results if not isinstance(i, Function)]
    pprint(expr)
    pprint(clean)
    print("===========================")
