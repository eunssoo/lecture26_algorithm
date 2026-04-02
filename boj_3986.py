n = int(input())
count = 0

for _ in range(n):
    word = input().strip()
    stack = []

    for ch in word:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if not stack:
        count += 1

print(count)