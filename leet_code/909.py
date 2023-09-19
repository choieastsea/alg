from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        q = deque()
        q.append([1,0]) # [blockNum,time]
        visited =[False for _ in range(n*n+1)]
        while q:
            # print(q)
            blockNum, time = q.popleft()
            # 목적지 도달한 경우
            if blockNum == n*n:
                return time
            # 1~6칸 이동
            for i in range(1,7):
                nextBlockNum = blockNum + i
                nextRow = n-1 - (nextBlockNum-1)//n
                nextCol = (nextBlockNum-1)%n if (n-1-nextRow)%2 == 0 else n-1-(nextBlockNum-1)%n
                # print(nextBlockNum, nextRow,nextCol)
                if nextBlockNum <= n*n and not visited[nextBlockNum]:
                    visited[nextBlockNum] = True
                    if board[nextRow][nextCol] != -1:
                        q.append([board[nextRow][nextCol], time+1])
                    else:
                        q.append([nextBlockNum, time + 1])
        return -1