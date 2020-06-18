def caught_speeding(speed, is_birthday):
  lowest_speed = 60
  small_ticket_low = 61
  small_ticket_high = 80
  highest_speed = 81
  
  if is_birthday:
    lowest_speed += 5
    small_ticket_low += 5
    small_ticket_high += 5 
    highest_speed += 5
  
  if speed <= lowest_speed:
    return 0
  elif small_ticket_low <= speed <= small_ticket_high:
    return 1
  else:
    return 2


if __name__ == "__main__":
  #assert(caught_speeding(60, False)) == 0
  #assert(caught_speeding(65, False)) ==  1
  assert(caught_speeding(65, True)) == 0
  assert(caught_speeding(80, False)) == 1
  assert(caught_speeding(85, False)) == 2
  assert(caught_speeding(85, True)) == 1
  assert(caught_speeding(70, False)) == 1
  assert(caught_speeding(75, False)) == 1
  assert(caught_speeding(75, True)) == 1
  assert(caught_speeding(40, False)) == 0
  assert(caught_speeding(40, True)) == 0
  assert(caught_speeding(90, False)) == 2
