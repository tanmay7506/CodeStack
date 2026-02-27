 m1 = len(l1) // 2
    m2 = len(l2) // 2
    return (
        (elem in l1[:m1] and elem in l2[m2:])
        or (elem in l1[m1:] and elem in l2[:m2])
    )    
