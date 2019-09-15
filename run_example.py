from generated_tempdir_2019_09_15_163300.generated_part000000 import match_root
from sympy import *
from sympy.abc import x, a, b, c, d, m, n

from utils import check_constraints

expr_result = [
    (Integral(x, x), x**2/2),
    (Integral(x**2, x), x**3/3),
    (Integral(x**3, x), x**4/4),
    (Integral((x + 1)/(1 - x), x), -x - 2*log(x - 1)),
    (Integral(1/(x + 1), x), log(x + 1)),
    (Integral(x/(x**2 + 1), x), log(x**2 + 1)/2),
    (Integral(1/x, x), log(x)),
    (Integral(sin(x), x), -cos(x)),
    (Integral(sin(x)*cos(x), x), sin(x)**2/2),
    (Integral(exp(x**2)/2, x), sqrt(pi)*erfi(x)/4),
    (Integral(log(x), x), x*log(x) - x),
    (Integral(x**a, x), x**(a + S(1))/(a + S(1))),
    (Integral(S(1)/x, x), log(x)),
    (Integral(a*x, x), a*(S(1)/S(2))*x**S(2)),
    (Integral(1/(x**2*(a + b*x)**2), x), -b/(a**2*(a + b*x)) - 1/(a**2*x) - 2*b*log(x)/a**3 + 2*b*log(a + b*x)/a**3),
    (Integral(x**6/(a + b*x)**2, x), (-a**6/(b**7*(a + b*x)) - S(6)*a**5*log(a + b*x)/b**7 + 5*a**4*x/b**6 - S(2)*a**3*x**2/b**5 + a**2*x**3/b**4 - a*x**4/(S(2)*b**3) + x**5/(S(5)*b**2))),
    (Integral(1/(x**2*(a + b*x)**2), x), -b/(a**2*(a + b*x)) - 1/(a**2*x) - 2*b*log(x)/a**3 + 2*b*log(a + b*x)/a**3),
    (Integral(a + S(1)/x, x), a*x + log(x)),
    (Integral((a + b*x)**2/x**3, x), -a**2/(2*x**2) - 2*a*b/x + b**2*log(x)),
    (Integral(a**3*x, x), S(1)/S(2)*a**3*x**2),
    (Integral((a + b*x)**3/x**3, x), -a**3/(2*x**2) - 3*a**2*b/x + 3*a*b**2*log(x) + b**3*x),
    (Integral(x**3*(a + b*x), x), a*x**4/4 + b*x**5/5),
    #(Integral((b*x)**m*(d*x + 2)**n, x), 2**n*(b*x)**(m + 1)*hyper((-n, m + 1), (m + 2), -d*x/2)/(b*(m + 1)),),
]

output_file = open("out.run", "wb")

def rubi_first_matcher(expr):
    g = match_root(expr)
    for repl, subst, constraints in g:
        if not check_constraints(subst, constraints):
            continue
        result = repl(**subst)
        return result


def rubi_decision_integrator(expr):
    new_expr = expr.replace(
        lambda x: isinstance(x, Integral),
        lambda x: rubi_first_matcher(x),
    )
    if new_expr is None:
        return None
    if expr == new_expr:
        return expr
    rubi_decision_integrator(expr)


for expr, expected in expr_result:
    g = match_root(expr)

    ret = list(g)
    results = [repl(**subst) for repl, subst, constraints in ret if check_constraints(subst, constraints)]
    #results = [rubi_decision_integrator(expr)]

    clean = [i for i in results if not isinstance(i, Function)]
    pprint(expr)
    pprint(clean)
    print("==============================")
    output_file.write(b"Expression:\n")
    output_file.write(pretty(expr).encode("utf-8"))
    output_file.write(b"\nExpected result:\n")
    output_file.write(pretty(expected).encode("utf-8"))
    output_file.write(b"\nMatched pairs:\n")
    output_file.write(pretty(clean).encode("utf-8"))
    output_file.write(b"\n==============================\n")

output_file.close()
