# 이진 탐색 트리의 노드 클래스
class STreeNode:
    def __init__(self, key, left=None, right=None):
        # 노드가 저장하는 값
        self.key = key

        # 왼쪽 자식 노드
        # 현재 노드보다 작은 값이 들어간다.
        self.left = left

        # 오른쪽 자식 노드
        # 현재 노드보다 큰 값이 들어간다.
        self.right = right


# 재귀 방식 이진 탐색 트리 검색 함수
def search_bst(node, key):
    # 현재 노드가 None이면 찾는 값이 없는 것
    if node is None:
        return None

    # 찾는 값이 현재 노드의 값과 같으면 현재 노드 반환
    if key == node.key:
        return node

    # 찾는 값이 현재 노드보다 작으면 왼쪽 서브트리에서 검색
    elif key < node.key:
        return search_bst(node.left, key)

    # 찾는 값이 현재 노드보다 크면 오른쪽 서브트리에서 검색
    else:
        return search_bst(node.right, key)


# 반복문 방식 이진 탐색 트리 검색 함수
def search_bst_iter(node, key):
    # node가 None이 될 때까지 반복
    while node is not None:

        # 찾는 값이 현재 노드의 값과 같으면 현재 노드 반환
        if key == node.key:
            return node

        # 찾는 값이 현재 노드보다 작으면 왼쪽으로 이동
        elif key < node.key:
            node = node.left

        # 찾는 값이 현재 노드보다 크면 오른쪽으로 이동
        else:
            node = node.right

    # 반복이 끝났다는 것은 찾는 값이 없다는 뜻
    return None


# -----------------------------
# 이진 탐색 트리 직접 구성
# -----------------------------

# 각 노드 생성
node10 = STreeNode(10)
node25 = STreeNode(25)
node35 = STreeNode(35)

node20 = STreeNode(20, node10, node25)
node40 = STreeNode(40, node35, None)

root = STreeNode(30, node20, node40)


# -----------------------------
# 검색 테스트
# -----------------------------

target = 25

result = search_bst(root, target)

if result is not None:
    print("재귀 검색 결과:", result.key)
else:
    print("재귀 검색 결과: 찾는 값이 없습니다.")


result = search_bst_iter(root, target)

if result is not None:
    print("반복 검색 결과:", result.key)
else:
    print("반복 검색 결과: 찾는 값이 없습니다.")