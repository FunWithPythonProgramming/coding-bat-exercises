from ron_solution import caught_speeding

def test_caught_speed_60_false():
  assert(caught_speeding(60, False)) == 0

def test_caught_speed_65_false():
  assert(caught_speeding(65, False)) ==  1

def test_caught_speed_65_true():
  assert(caught_speeding(65, True)) == 0

def test_caught_speed_80_false():
  assert(caught_speeding(80, False)) == 1

def test_caught_speed_85_false():
  assert(caught_speeding(85, False)) == 2
  
def test_caught_speed_85_true():
  assert(caught_speeding(85, True)) == 1

def test_caught_speed_70_false():
  assert(caught_speeding(70, False)) == 1

def test_caught_speed_75_false():
  assert(caught_speeding(75, False)) == 1

def test_caught_speed_75_true():
  assert(caught_speeding(75, True)) == 1

def test_caught_speed_40_false():
  assert(caught_speeding(40, False)) == 0

def test_caught_speed_40_true():
  assert(caught_speeding(40, True)) == 0

def test_caught_speed_90_false():
  assert(caught_speeding(90, False)) == 2
