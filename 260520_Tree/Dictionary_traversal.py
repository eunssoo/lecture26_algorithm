# 딕셔너리를 이용한 이진 트리 구성
# key: 현재 노드
# value: [왼쪽 자식, 오른쪽 자식]

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [None, None],
    'D': [None, None],
    'E': [None, None]
}


# 전위 순회: 현재 노드 → 왼쪽 자식 → 오른쪽 자식
def preorder(tree, node):
    if node is None:
        return

    print(node, end=' ')

    left = tree[node][0]
    right = tree[node][1]

    preorder(tree, left)
    preorder(tree, right)


# 중위 순회: 왼쪽 자식 → 현재 노드 → 오른쪽 자식
def inorder(tree, node):
    if node is None:
        return

    left = tree[node][0]
    right = tree[node][1]

    inorder(tree, left)
    print(node, end=' ')
    inorder(tree, right)


# 후위 순회: 왼쪽 자식 → 오른쪽 자식 → 현재 노드
def postorder(tree, node):
    if node is None:
        return

    left = tree[node][0]
    right = tree[node][1]

    postorder(tree, left)
    postorder(tree, right)
    print(node, end=' ')


# 루트 노드는 A
root = 'A'

print("전위 순회:", end=' ')
preorder(tree, root)
print()

print("중위 순회:", end=' ')
inorder(tree, root)
print()

print("후위 순회:", end=' ')
postorder(tree, root)
print()