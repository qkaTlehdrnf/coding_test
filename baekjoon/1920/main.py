import sys
A_num = int(sys.stdin.readline().strip())
A_list = list(map(int, sys.stdin.readline().strip().split()))
B_num = int(sys.stdin.readline().strip())
B_list = list(map(int, sys.stdin.readline().strip().split()))
A_list.sort()
B_list.sort()
answer = ''
for b in B_list:
    while A_list:
        alisttrigger = 0
        if b == A_list[0]:
            answer += '1 '
            break
        elif b < A_list[0]:
            answer += '0 '
            break
        else:
            A_list.pop(0)
    if A_list == [] and alisttrigger == 1:
        answer += '0 '
    if alisttrigger == 0:
        alisttrigger = 1
answer = answer.strip()
print(answer)