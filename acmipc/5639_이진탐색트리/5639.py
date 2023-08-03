from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

def postorder(strt, end):
    """
        postorder 함수는 preorder 배열과 범위가 주어졌을 때, 해당 범위를 tree로 하는 postorder를 수행
        preorder의 순서는 root - left subtree - right subtree 인데, 
        BST에서 left < root < right 임을 이용하여 재귀적으로 left- right - root 순으로 postorder 탐색
    """
    global preorder
    # print(f'postorder({strt},{end})')

    if strt == end:
        print(preorder[strt])
        return
    currentRoot = preorder[strt]
    leftStart = 0
    rightStart = 0
    for i in range(strt, end+1): # strt에서부터 end까지 탐색
        if leftStart == 0 and preorder[i] < currentRoot:
            leftStart = i
        if rightStart == 0 and preorder[i] > currentRoot:
            rightStart = i
    # print(f'leftStrt : {leftStart} ({preorder[leftStart]}), right : {rightStart} ({preorder[rightStart]})')
    if leftStart != 0:
        if rightStart-1 >= leftStart:
            postorder(leftStart, rightStart-1)
        else:
            postorder(leftStart, end)
    if rightStart != 0:
        postorder(rightStart, end)
    print(currentRoot)
        
    

if __name__ == "__main__":
    preorder = []
    while True:
        try:
            preorder.append(int(input()))
        except:
            break
    postorder(0, len(preorder)-1)
