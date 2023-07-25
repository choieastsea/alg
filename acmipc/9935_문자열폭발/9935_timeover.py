import sys
input = sys.stdin.readline

if __name__ == "__main__":
    word = input().strip() # ~1000000
    bomb = input().strip() # ~36
    while True:
        new_word = word.replace(bomb,'')
        if word != new_word:
            word = new_word
        else:
            break
    if len(word) > 0:
        print(word)
    else:
        print('FRULA')