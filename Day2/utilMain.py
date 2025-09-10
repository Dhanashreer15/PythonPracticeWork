from utilities import string_ops, math_ops, file_ops

# String operations
text = "Hello, World! Welcome to Python."
cleaned = string_ops.remove_punctuation(text)
vowel_count = string_ops.count_vowels(text)
print(f"Cleaned Text: {cleaned}")
print(f"Vowel Count: {vowel_count}")

# Math operations
data = [10, 20, 30, 40, 50]
print(f"Mean: {math_ops.mean(data)}")
print(f"Median: {math_ops.median(data)}")
print(f"Standard Deviation: {math_ops.std_dev(data):.2f}")

# File operations
file_ops.write("sample.txt", "Python is powerful.\nData is everything.")
print("File Content:", file_ops.read("sample.txt"))
print("Keyword 'Data' found?", file_ops.search("sample.txt", "Data"))
