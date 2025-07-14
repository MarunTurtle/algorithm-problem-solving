# 앞에서 2번째 원소
# 뒤에서 2번째 원소
# a로 대체

word = input()
new_word = word[0] + 'a' + word[2:-2] + 'a' + word[-1:]

print(new_word)