import sys
input = sys.stdin.readline

if __name__ == "__main__":
    word = input().strip() 
    bomb = input().strip() 
    bomb_length = len(bomb)
    output = []
    for i in range(len(word)):
        # print(f"before : {output}, i : {i}, word[{i}] : {word[i]}")
        output.append(word[i])
        if word[i] == bomb[-1]:
            # need to check whether output be popped
            if output[-bomb_length:] == list(bomb):
                for _ in range(bomb_length): output.pop()
                # output = output[:-bomb_length] 로 했더니 시간초과가 난다...
        # print(f"after : {output}")
    if len(output) == 0:
        print('FRULA')
    else:
        print("".join(output))
       
                
    