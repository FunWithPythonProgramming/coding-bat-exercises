def string_match(a, b):
  match_count = 0
  
  for index in range(len(a)-1):
    if a[index:index+2] == b[index:index+2]:
      match_count += 1
  
  return match_count
