return sum(
  1
  for num in nums
  if num is not None  and num%2 and len(str(abs(num)))==3
)
