import sys
from collections import deque

input = sys.stdin.readline

BLANK = 0
APPLE = 1 
SNAKE = 2

# orientation 바꾸기
RIGHT = 'D'
LEFT = 'L'

# orientation (4종류)
ORIENTATION = [(0,1), (1,0), (0,-1), (-1,0)]


class Map:
    def __init__(self, size:int) -> None:
        self.size = n
        self.blocks = [[BLANK for _ in range(size)]for _ in range(size)]
        self.blocks[0][0] = SNAKE
        self.snake = deque()
        self.snake.append((0,0))
        self.snake_orientation = 0 # ORIENTATION[snake_orientation] 만큼 움직일 것
        self.time = 0
        self.gaming = True

    def __str__(self) -> str:
        matrix = ''
        for row in range(self.size):
            for col in range(self.size):
                matrix += f'{self.blocks[row][col]}'
            matrix += '\n'
        return matrix+'\n'

    def changeOrientation(self, direction:str):
        """
        뱀 머리 방향을 바꿔줌 (-1,0) : 왼쪽으로 이동할 것
        """
        if direction == RIGHT:
            self.snake_orientation = (self.snake_orientation + 1) %4
        else:
            self.snake_orientation = (self.snake_orientation-1) %4
    
    def checkIsAvailable(self, row, col)->bool:
        """
        row, col로 이동할 때, 가능한지 여부를 판단하여 return
        """
        # 1. 벽
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        # 2. 자기 자신
        if self.blocks[row][col] == SNAKE:
            return False
        return True
    
    def moveHead(self)->bool:
        """
        orientation 방향으로 뱀의 머리를 이동. 안끝나면 true 리턴
        """
        self.time += 1
        orientation = ORIENTATION[self.snake_orientation]
        moved_head_row = self.snake[0][0] + orientation[0]
        moved_head_col = self.snake[0][1] + orientation[1]
        # 1. check if finish
        if not self.checkIsAvailable(moved_head_row, moved_head_col):
            return False
        # 2. move 
        if self.blocks[moved_head_row][moved_head_col] == APPLE:
            # 사과 먹었으니 그대로 확장
            self.blocks[moved_head_row][moved_head_col] = SNAKE
            self.snake.appendleft((moved_head_row, moved_head_col))
        else:
            # 확장
            self.blocks[moved_head_row][moved_head_col] = SNAKE
            self.snake.appendleft((moved_head_row, moved_head_col))
            # 꼬리 자르기
            tail_row, tail_col = self.snake.pop() 
            self.blocks[tail_row][tail_col] = BLANK
        return True

if __name__ == "__main__":
    n = int(input()) # board's size
    snake_game = Map(n)
    k = int(input()) # apple num
    apple_locations = []
    for _ in range(k):
        row, col  = map(lambda x: int(x)-1, input().split())
        snake_game.blocks[row][col] = APPLE
    # print(snake_game)
    rotation = int(input())
    time_logs = []
    for _ in range(rotation):
        timestamp, direction = input().split()
        while snake_game.time < int(timestamp):
            if not snake_game.moveHead():
                print(snake_game.time)
                exit(0)
            # print(snake_game)
        snake_game.changeOrientation(direction)
        # print('orientation:',snake_game.snake_orientation)

    while True:
        if not snake_game.moveHead():
            print(snake_game.time)
            exit(0)
        # print(snake_game)