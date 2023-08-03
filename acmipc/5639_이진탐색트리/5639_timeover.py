from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)

"""
    preorder로 BST를 순회한 결과 주어졌을 때,
    해당 트리를 postorder로 순회하기
"""

class Node:
    def __init__(self, num) -> None:
        self.num = num
        self.parent = None # parent, smaller, bigger 모두 int로 표현하고, dict로 접근하자!
        self.smaller = None
        self.bigger = None 
    def __str__(self) -> str:
        return f'{self.num}, parent : {self.parent}, smaller: {self.smaller}, bigger : {self.bigger}'

def postorder(node_num):
    """
    현재 node_num에서부터 [왼 - 오 - 본인] 순으로 탐색
    """
    global nodeDict
    currentNode = nodeDict[node_num]
    if currentNode.smaller is not None:
        postorder(currentNode.smaller)
    if currentNode.bigger is not None:
        postorder(currentNode.bigger)
    print(currentNode.num)

def makeTree(preorder):
    """
    preorder로 주어진 BST를 트리 형식으로 만듦
    """
    global nodeDict
    for i in range(0, len(preorder)-1):
        currentNum = preorder[i]
        nextNum = preorder[i+1]
        currentNode = nodeDict[currentNum]
        nextNode = nodeDict[nextNum]
        # print(f'{i}) current : {currentNum}, next : {nextNum}')
        if currentNum > nextNum:
            # current 가 next보다 크면 next은 current의 왼쪽 자식
            currentNode.smaller = nextNum
            nextNode.parent = currentNum
        else:
            # current가 next보다 작으면 오른쪽으로 가야함 -> 본인의 자식 ~ 조상의 자식 : next가 current의 parent보다 작아지는 시점에서의 오른쪽 자식
            # print(f'{currentNum} 이 {nextNum} 보다 더 작음')
            while currentNode.parent is not None and currentNode.parent < nextNum:
                # print(f'{nextNum}넣는중 ... {currentNum}에서 {currentNode.parent}로 올려~')
                currentNode = nodeDict[currentNode.parent]
                currentNum = currentNode.num
                # print(f'currentNode: {currentNode.num}, currentNum: {currentNum}')
            # print(f'{currentNum}의 bigger로 {nextNum} 설정하려고하는데, 자식 꽉찼나?')
            while currentNode.bigger is not None:
                # 이미 오른쪽 자식이 있다면 내려서 남는 자식 자리에다가 넣어야함
                currentNode = nodeDict[currentNode.bigger]
                currentNum = currentNode.num
            currentNode.bigger = nextNum
            nextNode.parent = currentNum
            
    # for i in range(len(preorder)):
    #     print(f'{i} : {nodeDict[preorder[i]]}')  
    return preorder[0] # root node!      
    
def makeNodes(numList):
    """
    n 개의 노드 만들기
    """
    node_dict = {}
    for i in numList:
        node_dict[i] = Node(i)
    return node_dict

if __name__ == "__main__":
    preorder = []
    while True:
        try:
            preorder.append(int(input()))
        except:
            break
    nodeDict = makeNodes(preorder)
    root_node = makeTree(preorder)
    postorder(root_node)

"""
preorder : root - left - right
        50
    30      98
    24 45  52
5 28     60

50
30
24
5
27
25
26
28
29
45
98
52
60
106
109
108
110

ans

5
26
25
29
28
27
24
45
30
60
52
108
110
109
106
98
50
"""
