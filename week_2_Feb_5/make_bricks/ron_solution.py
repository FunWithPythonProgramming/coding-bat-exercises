def make_bricks(small, big, goal):
  needed_fives = goal // 5
  needed_ones = goal % 5
  
  if small == goal:
    return True
  elif (goal % 5 == 0) and (big >= goal // 5):
    return True
  
  if big*5 > goal:
    return small >= (goal % 5)
  else:
    return small >= (goal - big*5)
