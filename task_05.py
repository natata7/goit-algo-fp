from collections import deque
import uuid
import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary Tree"):
    if tree_root is None:
        return

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(9, 6))
    plt.title(title, fontsize=14, fontweight="bold")
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
        font_color="white",
        font_weight="bold",
    )
    plt.show()


def generate_color_gradient(step: int, total_steps: int) -> str:
    if total_steps <= 1:
        factor = 0.0
    else:
        factor = step / (total_steps - 1)

    r = int(0 + (175 - 15) * factor)
    g = int(0 + (200 - 30) * factor)
    b = int(225)

    return f"#{r:02X}{g:02X}{b:02X}"


def count_nodes(root: Node) -> int:
    if root is None:
        return 0
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        count += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count


def visualize_dfs(root: Node):
    if root is None:
        return

    total_nodes = count_nodes(root)
    stack = [root]
    visited_order = []

    while stack:
        node = stack.pop()
        visited_order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    for step, node in enumerate(visited_order):
        node.color = generate_color_gradient(step, total_nodes)

    draw_tree(root, title="Обхід у глибину (DFS) — Стек")


def visualize_bfs(root: Node):
    if root is None:
        return

    total_nodes = count_nodes(root)
    queue = deque([root])
    visited_order = []

    while queue:
        node = queue.popleft()
        visited_order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    for step, node in enumerate(visited_order):
        node.color = generate_color_gradient(step, total_nodes)

    draw_tree(root, title="Обхід у ширину (BFS) — Черга")


def create_sample_tree() -> Node:
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(8)
    return root


if __name__ == "__main__":
    tree_dfs = create_sample_tree()
    visualize_dfs(tree_dfs)

    tree_bfs = create_sample_tree()
    visualize_bfs(tree_bfs)