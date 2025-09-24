word="test"
l=len(word)
if l%2==1:
    print(f"word = {word} Результат: {word[l//2]}")
else:
    print(f"word = {word} Результат: {word[l//2-1:l//2+1]}")
