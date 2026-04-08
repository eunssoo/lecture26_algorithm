n = int(input())

for i in range(1, n + 1):
    words = input().split()
    stack = []

    for word in words:
        stack.append(word)

    result = []
    while stack:
        result.append(stack.pop())

    print(f"Case #{i}: {' '.join(result)}")
