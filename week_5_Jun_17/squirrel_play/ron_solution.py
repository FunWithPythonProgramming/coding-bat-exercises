def squirrel_play(temp, is_summer):
  lower_limit = 60
  upper_limit = 90
  
  if is_summer:
    upper_limit = 100
    
  return lower_limit <= temp <= upper_limit
