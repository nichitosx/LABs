
with open('input.txt', 'r') as file:
    content = file.read()

num_letters = sum(1 for char in content if char.isalpha())
num_words = len(content.split())
num_lines = content.count('\n') + 1

print("Input file contains:")
print(num_letters, "letters")
print(num_words, "words")
print(num_lines, "lines")