import sys

V, E = map(int, sys.stdin.readline().split())
edgelist = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]

def find_root(node, rootlist):
    while rootlist[node] != node:
        node = rootlist[node]
    return node

def kruskal_algorithm(V, E, edgelist):
    def get_weight(edge):
        return edge[2]

    edgelist.sort(key=get_weight)

    rootlist = [i for i in range(V + 1)]
    weight_sum = 0
    edge_cnt = 0

    for edge in edgelist:
        node1, node2, weight = edge
        root1 = find_root(node1, rootlist)
        root2 = find_root(node2, rootlist)

        if root1 != root2:
            rootlist[root2] = root1
            weight_sum += weight
            edge_cnt += 1

        if edge_cnt == V - 1:
            break

    return weight_sum

result = kruskal_algorithm(V, E, edgelist)

print(result)


