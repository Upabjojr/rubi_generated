
def check_constraints(subst, constraints):
    for cons in constraints:
        ret = cons(**{k: v for k, v in subst.items() if k in cons.__code__.co_varnames})
        if not ret:
            return False
    return True
