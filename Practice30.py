n1_n_unique = len(set(str(n1)))
    n2_n_unique = len(set(str(n2)))
    if n1_n_unique> n2_n_unique:
        return n1
    elif n2_n_unique> n1_n_unique:
        return n2
    else:
        return (n1,n2)
