def lone_sum(a, b, c):
  ab = a == b
  ac = a == c
  bc = b == c
  
  if ab and ac:
    return 0
  elif ab:
    return c
  elif ac:
    return b
  elif bc:
    return a
  else:
    return a + b + c
