# 이진 트리의 노드 클래스
class TreeNode:
    def __init__(self, data, left=None, right=None):
        # 노드에 저장할 데이터
        self.data = data

        # 왼쪽 자식 노드
        self.left = left

        # 오른쪽 자식 노드
        self.right = right

    # 왼쪽 자식 설정
    def set_left(self, left):
        self.left = left

    # 오른쪽 자식 설정
    def set_right(self, right):
        self.right = right


# 전위 순회: 현재 노드 → 왼쪽 자식 → 오른쪽 자식
def preorder(node):
    if node is None:
        return

    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


# 중위 순회: 왼쪽 자식 → 현재 노드 → 오른쪽 자식
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)


# 후위 순회: 왼쪽 자식 → 오른쪽 자식 → 현재 노드
def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data, end=' ')


# -----------------------------
# 이진 트리 구성
# -----------------------------

# 루트 노드 A 생성
my_tree = TreeNode('A')

# B 노드를 만들고 A의 왼쪽 자식으로 연결
new_node = TreeNode('B')
my_tree.set_left(new_node)

# C 노드를 만들고 A의 오른쪽 자식으로 연결
new_node = TreeNode('C')
my_tree.set_right(new_node)

# A의 왼쪽 자식인 B 노드를 cur_node가 가리키게 함
cur_node = my_tree.left

# D 노드를 만들고 B의 왼쪽 자식으로 연결
new_node = TreeNode('D')
cur_node.set_left(new_node)

# E 노드를 만들고 B의 오른쪽 자식으로 연결
new_node = TreeNode('E')
cur_node.set_right(new_node)


# -----------------------------
# 순회 결과 출력
# -----------------------------

print("전위 순회:", end=' ')
preorder(my_tree)
print()

print("중위 순회:", end=' ')
inorder(my_tree)
print()

print("후위 순회:", end=' ')
postorder(my_tree)
print()