import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val

    def __le__(self, other):
        return self.val <= other.val

    def __ge__(self, other):
        return self.val >= other.val


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors, ax):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors[node[0]] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=node_colors,
        with_labels=True,
        ax=ax,
    )


def build_heap(heap):
    if not heap:
        return None
    root = heap[0]
    for i in range(len(heap)):
        if 2 * i + 1 < len(heap):
            heap[i].left = heap[2 * i + 1]
        if 2 * i + 2 < len(heap):
            heap[i].right = heap[2 * i + 2]
    return root


def bfs_traversal(root):
    visited = set()
    queue = [root]
    colors = {}
    while queue:
        node = queue.pop(0)
        if node.id not in visited:
            visited.add(node.id)
            colors[node.id] = generate_color(len(visited))
            queue.extend([child for child in [node.left, node.right] if child])
    return colors


def dfs_traversal(root):
    visited = set()
    stack = [root]
    colors = {}
    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            colors[node.id] = generate_color(len(visited))
            stack.extend([child for child in [node.right, node.left] if child])
    return colors


def generate_color(index):
    hex_color = format(index * 0xFFF000 % 0x80FF00, "06x")
    return f"#{hex_color}"


heap = [Node(6), Node(3), Node(10), Node(1), Node(5), Node(2), Node(4)]
heapq.heapify(heap)
heap_root = build_heap(heap)

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

bfs_colors = bfs_traversal(heap_root)
draw_tree(heap_root, bfs_colors, axs[0])
axs[0].set_title("BFS Traversal")

dfs_colors = dfs_traversal(heap_root)
draw_tree(heap_root, dfs_colors, axs[1])
axs[1].set_title("DFS Traversal")

plt.show()
