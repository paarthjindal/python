string = "this is a test string"
char_frequency = {}

for char in string:
  if char not in char_frequency:
    char_frequency[char] = 0
  char_frequency[char] += 1

for char, count in char_frequency.items():
  print(f"{char}: {count}")
for char, count in frequency.items():
    print(char, ":", count)  