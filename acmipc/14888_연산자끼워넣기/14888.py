import sys
input = sys.stdin.readline

def BT(ops_count, ops_sequence):
    global n
    global sequence_list
    """
    ops_count의 조합으로 (n-1)만큼 갔을 때의 search space 만들어주는 함수
    """
    # print(f"BT called with ops_count : {ops_count}, ops_sequencd : {ops_sequence}")
    if len(ops_sequence) == n - 1:
        # 종료 조건 -> ops_sequence로 계산 수행
        sequence_list.append(ops_sequence)
    else:
        # search space 확장
        for i,ops in enumerate(ops_count):
            if ops >= 1:
                ops_count[i] -= 1
                BT(ops_count, ops_sequence+[i])
                ops_count[i] += 1

def calculate_with_ops(num_list, sequence):
    # + - * / 계산
    # print(f'calculator with num_list : {num_list}, sequence : {sequence}')
    result = num_list[0]
    for i, op in enumerate(sequence):
        if op == 0:
            result += num_list[i + 1]
        elif op == 1:
            result -= num_list[i + 1]
        elif op == 2:
            result *= num_list[i + 1]
        else:
            # 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다
            if result < 0:
                # print(result, num_list[i+1])
                result = -((-result) // num_list[i+1])
            else:
                result //= num_list[i + 1]
    # print('calc result',result)
    return result

def solve(num_list, ops_count, n):
    BT(ops_count,[]) 
    # sequence_list로 숫자 계산
    result_max = -10**9
    result_min = 10**9
    for sequence in sequence_list:
        result = calculate_with_ops(num_list, sequence)
        if result > result_max:
            result_max = result
        if result < result_min:
            result_min = result
    return result_max, result_min

if __name__=='__main__':
    n = int(input())
    num_list = list(map(int, input().split())) 
    ops_count = list(map(int,input().split())) # + - * / 순서대로
    sequence_list = []
    mx, mn = solve(num_list, ops_count, n)
    print(mx)
    print(mn)