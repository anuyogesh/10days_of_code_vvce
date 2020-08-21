# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())

old_stack = list()
new_stack = list()

for i in range(n):
    query = list(map(int,input().split()))
    if query[0] == 1:
        if not new_stack:
            element = query[1]
        new_stack.append(query[1])
    elif query[0] == 2:
        if not old_stack:
            while new_stack:
                old_stack.append(new_stack.pop())
        old_stack.pop()
    else:
        if old_stack:
            print(old_stack[-1])
        else:
            print(element)                        
