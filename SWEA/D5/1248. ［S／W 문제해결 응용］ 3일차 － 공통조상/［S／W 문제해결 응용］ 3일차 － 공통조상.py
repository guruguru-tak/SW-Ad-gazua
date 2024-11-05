# import sys
# sys.stdin = open("input.txt", "r", encoding='utf-8')

t = int(input())

def find_Parent(node, parent):
    # 부모 노드 set 리스트를 만들고 모든 부모를 저장
    ancestor = set()
    # 위 함수에서 들어오는 a가 노드가 되어서 트리구조로 내려온다
    # 들어오는 a(node)가 0이 아니면
    while node != 0:
        # a의 부모 노드를 계속 따라가며 ancestor 집합에 추가해, 루트 노드까지 올라감
        # 조상에 처음 들어오는 8인 node값 부터 set에 입력
        ancestor.add(node)
        # 8번 v의 값인 5가 node에 입력
        # 5 -> 3 -> 3 -> 1 -> 1 -> 0 -> 0
        node = parent[node]

    # node가 반복하다 0인 최고루트로 올라갈때까지 반복
    # ancestor : {8, 1, 3, 5}
    # parent : [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 11]
    # 최고루트로 올라가면 저장된 조상을 반환 -> find_Common_Ancestor 로
    return ancestor


def find_Common_Ancestor(a, b, parent):
    # 처음 비교값 A, B 가 입력됨

    # 두 노드의 조상 리스트를 비교하여 최소 공통 조상 찾기
    # a의 모든 조상을 ancestors_A에 저장
    # 8입력
    ancestors_A = find_Parent(a, parent)

    # 반환된 A 조상을 가지고
    # b도 0이 아니면 반복
    while b != 0:
        # 만약 b가 ancestor : {8, 1, 3, 5} 안에 있다면
        if b in ancestors_A:
            # 해당 b가 공통 조상임
            return b
        # 공통 조상을 아직 못찾았으면 다시 부모 node의 값을 b로 할당
        # b = 13 -> b = 11 -> b = 6
        # print(b)
        # parent[b] : 11 -> 6 -> 3
        b = parent[b]
    # ancestor : {8, 1, 3, 5} 내 에 없으면 공통 조상 없음
    return None

def subtree_Size(node, tree):
    # DFS를 통해 서브 트리의 크기를 계산

    #특정 노드가 "존재하지 않음" 종료 조건
    if node == 0:
        return 0

    # 나 자신을 포함
    size = 1
    # print(tree[node])
    # 이진트리에 양쪽에 두개의 자식노드가 있다
    for child in tree[node]:
        # 왼쪽 제일 아래부터 계속 내려와서 dfs 아래 자식 없으면 그대로
        # size 1 반환하고 , size는 1씩 증가함
        # 노드 9에서 size += subtree_size(8, tree) + subtree_size(6, tree) => size = 3
        # 노드 아래 모든 하위 자식 다 돌아서 1씩 증가하게 해서 갯수 리턴
        size += subtree_Size(child, tree)

    return size


for tc in range(1, t+1):
    V, E, A, B = map(int, input().split())

    tree = [[] for _ in range(V + 1)]
    parent = [0] * (V + 1)


    # 간선 반복
    line = list(map(int, input().split()))
    for i in range(0, len(line), 2):
        v, e = line[i], line[i+1]
        tree[v].append(e)
        # 부모가 몇 번째 v인지 저장
        parent[e] = v

    # print(tree)
    # print(parent)

    # 공통 조상 찾기
    ancestor = find_Common_Ancestor(A, B, parent)
    # 공통 조상의 서브트리 크기 구하기
    size = subtree_Size(ancestor, tree)

    print(f"#{tc} {ancestor} {size}")