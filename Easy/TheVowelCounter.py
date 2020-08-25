string = input()
print(sum([1 for i in string if i in [
      'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']]))
