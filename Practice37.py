a, b = d[k1], d[k2]  # to simplify the notation
d[k1], d[k2] = a[:-1] + b[-1], b[:-1] + a[-1]
