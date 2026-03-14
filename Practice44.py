def count_unique_even_odd(l: list)-> dict:
  counts = {'even':0,"odd":0}
    for num in set(l):
      if(num % 2 == 0):
        counts['even'] += 1
      else:
        counts['odd'] += 1
  return (counts)
