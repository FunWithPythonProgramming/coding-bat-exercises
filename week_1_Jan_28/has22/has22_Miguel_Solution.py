def has22(numbers):
  int_array_count = len(numbers)

  for index in range(int_array_count -1):
    if numbers[index] == 2 and numbers[index + 1] == 2:
      return True
  return False

