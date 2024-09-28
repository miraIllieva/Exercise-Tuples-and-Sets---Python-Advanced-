text = input()

# Create empty dictionary

char_count = {}

# Loop each charahter in the text

for char in text:
    if char not in char_count:
        char_count[char] = 0
    char_count[char] += 1

for char in sorted(char_count):
    print(f"{char}: {char_count[char]} time/s")