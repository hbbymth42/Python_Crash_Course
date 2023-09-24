from pathlib import Path

path = Path('alice.txt')

contents = path.read_text()

common_word_count = 0

for line in contents.splitlines():
    common_word_count += line.lower().count('the ')

print(common_word_count)