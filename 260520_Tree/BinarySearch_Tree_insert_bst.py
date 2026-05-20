# 이진 탐색 트리의 노드 클래스
class STreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key          # 노드에 저장할 값
        self.left = left        # 왼쪽 자식
        self.right = right      # 오른쪽 자식


# 반복문 방식으로 이진 탐색 트리에 값 삽입
def insert_bst(root, key):
    # 트리가 비어 있으면 새 노드를 루트로 만든다.
    if root is None:
        return STreeNode(key)

    # 현재 위치를 root부터 시작
    cur_node = root

    while True:
        # 중복 값은 삽입하지 않음
        if key == cur_node.key:
            return root

        # 삽입할 값이 현재 노드보다 작으면 왼쪽으로 이동
        elif key < cur_node.key:
            # 왼쪽 자식이 비어 있으면 그 자리에 새 노드 삽입
            if cur_node.left is None:
                cur_node.left = STreeNode(key)
                return root

            # 왼쪽 자식이 이미 있으면 왼쪽 자식으로 이동
            else:
                cur_node = cur_node.left

        # 삽입할 값이 현재 노드보다 크면 오른쪽으로 이동
        else:
            # 오른쪽 자식이 비어 있으면 그 자리에 새 노드 삽입
            if cur_node.right is None:
                cur_node.right = STreeNode(key)
                return root

            # 오른쪽 자식이 이미 있으면 오른쪽 자식으로 이동
            else:
                cur_node = cur_node.right


# 중위 순회
# 이진 탐색 트리를 중위 순회하면 오름차순으로 출력된다.
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.key, end=' ')
    inorder(node.right)


# 전위 순회
def preorder(node):
    if node is None:
        return

    print(node.key, end=' ')
    preorder(node.left)
    preorder(node.right)


# 후위 순회
def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.key, end=' ')


# -----------------------------
# 숫자를 입력받아 BST 구성
# -----------------------------

numbers = list(map(int, input("숫자들을 입력하세요: ").split()))

root = None

for num in numbers:
    root = insert_bst(root, num)


# -----------------------------
# 결과 출력
# -----------------------------

print("전위 순회:", end=' ')
preorder(root)
print()

print("중위 순회:", end=' ')
inorder(root)
print()

print("후위 순회:", end=' ')
postorder(root)
print()