

while True:
    commands = []
    num_operand = []
    # 프로그램 명령어 저장
    while True:
        com = input()
        if com == "END":
            break
        if com == "QUIT":
            exit()
        if "NUM" in com:
            commands.append("NUM")
            num_operand.append(int(com[4:]))
        else:
            commands.append(com)

    N = int(input())
    stack = []

    for _ in range(N):
        num = int(input())
        operand = num_operand[:]
        stack.append(num)
        for i in range(len(commands)):
            if commands[i] == "DUP":
                stack.append(stack[-1])
            elif commands[i] == "NUM":
                stack.append(operand[0])
                operand.pop(0)
            elif commands[i] == "POP":
                stack.pop()
            elif commands[i] == "INV":
                stack[-1] = - stack[-1]
            elif commands[i] == "SWP":
                pnum = stack[-1]
                stack[-1] = stack[-2]
                stack[-2] = pnum
            elif commands[i] == "ADD":
                if stack[-1] + stack[-2] > 10**9:
                    print("ERROR")
                    continue
                pnum = stack.pop()
                stack[-1] += pnum
            elif commands[i] == "SUB":
                if stack[-2] - stack[-1] > 10**9:
                    print("ERROR")
                    continue
                pnum = stack.pop()
                stack[-1] -= pnum
            elif commands[i] == "MUL":
                if stack[-1] * stack[-2] > 10**9:
                    print("ERROR")
                    continue
                pnum = stack.pop()
                stack[-1] *= pnum
            elif commands[i] == "DIV":
                if stack[-1] == 0:
                    print("ERROR")
                    continue
                pnum = stack.pop()
                stack[-1] /= pnum
            elif commands[i] == "MOD":
                if stack[-1] == 0:
                    print("ERROR")
                    continue
                pnum = stack.pop()
                stack[-1] %= pnum

        print(stack.pop())





