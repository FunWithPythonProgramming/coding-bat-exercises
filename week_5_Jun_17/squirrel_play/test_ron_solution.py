from ron_solution import squirrel_play

def test_squirrel_play_70_false():
  assert squirrel_play(70, False)

def test_squirrel_play_95_false():
  assert not squirrel_play(95, False)

def test_squirrel_play_95_true():
  assert squirrel_play(95, True)

def test_squirrel_play_90_false():
  assert squirrel_play(90, False)

def test_squirrel_play_90_true():
  assert squirrel_play(90, True)

def test_squirrel_play_50_false():
  assert not squirrel_play(50, False)

def test_squirrel_play_50_true():
  assert not squirrel_play(50, True)

def test_squirrel_play_100_false():
  assert not squirrel_play(100, False)

def test_squirrel_play_100_true():
  assert squirrel_play(100, True)

def test_squirrel_play_105_true():
  assert not squirrel_play(105, True)

def test_squirrel_play_59_false():
  assert not squirrel_play(59, False)

def test_squirrel_play_59_true():
  assert not squirrel_play(59, True)

def test_squirrel_play_60_false():
  assert squirrel_play(60, False)