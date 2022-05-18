# Problem A. To many long words
words = int(input())
for i in range(words):
        word = input()
        new_word = word[0] + str(len(word) - 2) + word[-1]
        if len(word) > 10:
            print(new_word)
        else: print(word)
