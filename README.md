# RUBI decision tree generator.

### SymPy branch to use

Make sure you have branch of PR https://github.com/sympy/sympy/pull/17614 in
your `PYTHONPATH`
(overriding the default SymPy installation for `import sympy`).

### Generate the decision tree

Run `python decision_tree_rubi_generator.py` and wait for about 30 minutes to 2
hours.

You will then have a new subfolder called `generated_tempdir_<timestamp>`
containing the generated decision tree out of RUBI rules.

### Compute the integrals:

Again, make sure that `PYTHONPATH` points to the correct SymPy branch, as
previously described.

Import the main dispatch:
```python
from generated_tempdir_<timestamp>.generated_part000000 import match_root
```

Run the matcher:
```python
for replacement_func, subst_dict, constraints in match_root(Integral(..., x)):
    result = replacement_func(**subst_dict)
    break
```

WARNING: `result` may be a partial result (i.e. the original expression
transformed into another integration expression). Generally, you need to apply
the matcher recursively a few times in order to get the full result.

The function `check_constraints(subst_dict, constraint_list)` checks whether
all constraints are satisfied by the substitution.

### Example

```python
In [1]: from sympy import *

In [2]: from generated_tempdir_2019_09_15_163300.generated_part000000 import match_root

In [3]: x = symbols("x")

In [4]: expr = Integral(sin(x)*cos(x), x)

In [5]: [i for i in match_root(expr)]
[Int(sin(x), sin(x)),
 -Int(cos(x), cos(x)),
 2*Int(-2*(tan(x/2)**2 - 1)*tan(x/2)/(tan(x/2)**2 + 1)**3, tan(x/2)),
 Int(sin(x)*cos(x), x),
 Int(sin(x)*cos(x), x),
 Int(sin(x), sin(x)),
 sin(x)**2/2,
 -cos(x)**2/2,
 Int(sin(2*x), x)/2,
 Int(sin(2*x)/2, x),
 sin(x)**2/2,
 -cos(x)**2/2]
```

### More examples

```

Expression:
⌠     
⎮ x dx
⌡     

Expected result:
 2
x 
──
2 

RUBI matches:
⎡ 2⎤
⎢x ⎥
⎢──⎥
⎣2 ⎦

==============================

Expression:
⌠      
⎮  2   
⎮ x  dx
⌡      

Expected result:
 3
x 
──
3 

RUBI matches:
⎡ 3   3⎤
⎢x   x ⎥
⎢──, ──⎥
⎣3   3 ⎦

==============================

Expression:
⌠      
⎮  3   
⎮ x  dx
⌡      

Expected result:
 4
x 
──
4 

RUBI matches:
⎡ 4   4⎤
⎢x   x ⎥
⎢──, ──⎥
⎣4   4 ⎦

==============================

Expression:
⌠         
⎮ x + 1   
⎮ ───── dx
⎮ 1 - x   
⌡         

Expected result:
-x - 2⋅log(x - 1)

RUBI matches:
⎡    ⎛x + 1    ⎞   ⎤
⎢-Int⎜─────, -x⎟, x⎥
⎣    ⎝1 - x    ⎠   ⎦

==============================

Expression:
⌠         
⎮   1     
⎮ ───── dx
⎮ x + 1   
⌡         

Expected result:
log(x + 1)

RUBI matches:
[]

==============================

Expression:
⌠          
⎮   x      
⎮ ────── dx
⎮  2       
⎮ x  + 1   
⌡          

Expected result:
   ⎛ 2    ⎞
log⎝x  + 1⎠
───────────
     2     

RUBI matches:
⎡                ⎛  1      2⎞     ⎛  1      2⎞                                        ⎛  1      2⎞⎤
⎢             Int⎜──────, x ⎟  Int⎜──────, x ⎟   2  ┌─  ⎛1, 1 │   2⎞               Int⎜──────, x ⎟⎥
⎢   ⎛ 2    ⎞     ⎜ 2        ⎟     ⎜ 2        ⎟  x ⋅ ├─  ⎜     │ -x ⎟     ⎛ 2    ⎞     ⎜ 2        ⎟⎥
⎢log⎝x  + 1⎠     ⎝x  + 1    ⎠     ⎝x  + 1    ⎠     2╵ 1 ⎝ 2   │    ⎠  log⎝x  + 1⎠     ⎝x  + 1    ⎠⎥
⎢───────────, ───────────────, ───────────────, ────────────────────, ───────────, ───────────────⎥
⎣     2              2                2                  2                 2              2       ⎦

==============================

Expression:
⌠     
⎮ 1   
⎮ ─ dx
⎮ x   
⌡     

Expected result:
log(x)

RUBI matches:
[]

==============================

Expression:
⌠          
⎮ sin(x) dx
⌡          

Expected result:
-cos(x)

RUBI matches:
⎡     ⎛        ⎛x⎞           ⎞         ⎤
⎢     ⎜   2⋅tan⎜─⎟           ⎟         ⎥
⎢     ⎜        ⎝2⎠        ⎛x⎞⎟         ⎥
⎢2⋅Int⎜──────────────, tan⎜─⎟⎟, -cos(x)⎥
⎢     ⎜             2     ⎝2⎠⎟         ⎥
⎢     ⎜⎛   2⎛x⎞    ⎞         ⎟         ⎥
⎢     ⎜⎜tan ⎜─⎟ + 1⎟         ⎟         ⎥
⎣     ⎝⎝    ⎝2⎠    ⎠         ⎠         ⎦

==============================

Expression:
⌠                 
⎮ sin(x)⋅cos(x) dx
⌡                 

Expected result:
   2   
sin (x)
───────
   2   

RUBI matches:
⎡                           ⎛   ⎛   2⎛x⎞    ⎞    ⎛x⎞         ⎞                                                          ⎤
⎢                           ⎜-2⋅⎜tan ⎜─⎟ - 1⎟⋅tan⎜─⎟         ⎟      2         2                           2         2   ⎥
⎢                           ⎜   ⎝    ⎝2⎠    ⎠    ⎝2⎠      ⎛x⎞⎟  -cos (x)   sin (x)  Int(sin(2⋅x), x)  -cos (x)   sin (x)⎥
⎢-Int(cos(x), cos(x)), 2⋅Int⎜────────────────────────, tan⎜─⎟⎟, ─────────, ───────, ────────────────, ─────────, ───────⎥
⎢                           ⎜                  3          ⎝2⎠⎟      2         2            2              2         2   ⎥
⎢                           ⎜     ⎛   2⎛x⎞    ⎞              ⎟                                                          ⎥
⎢                           ⎜     ⎜tan ⎜─⎟ + 1⎟              ⎟                                                          ⎥
⎣                           ⎝     ⎝    ⎝2⎠    ⎠              ⎠                                                          ⎦

==============================

Expression:
⌠         
⎮  ⎛ 2⎞   
⎮  ⎝x ⎠   
⎮ ℯ       
⎮ ───── dx
⎮   2     
⌡         

Expected result:
√π⋅erfi(x)
──────────
    4     

RUBI matches:
⎡   ⎛ ⎛ 2⎞   ⎞⎤
⎢   ⎜ ⎝x ⎠   ⎟⎥
⎢Int⎝ℯ    , x⎠⎥
⎢─────────────⎥
⎣      2      ⎦

==============================

Expression:
⌠          
⎮ log(x) dx
⌡          

Expected result:
x⋅log(x) - x

RUBI matches:
[x⋅log(x) - x, x⋅log(x) - x, x⋅log(x) - x]

==============================

Expression:
⌠      
⎮  a   
⎮ x  dx
⌡      

Expected result:
 a + 1
x     
──────
a + 1 

RUBI matches:
⎡ a + 1   a + 1⎤
⎢x       x     ⎥
⎢──────, ──────⎥
⎣a + 1   a + 1 ⎦

==============================

Expression:
⌠     
⎮ 1   
⎮ ─ dx
⎮ x   
⌡     

Expected result:
log(x)

RUBI matches:
[]

==============================

Expression:
⌠       
⎮ a⋅x dx
⌡       

Expected result:
   2
a⋅x 
────
 2  

RUBI matches:
⎡                2⎤
⎢             a⋅x ⎥
⎢a⋅Int(x, x), ────⎥
⎣              2  ⎦
```
