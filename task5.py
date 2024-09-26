import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, node_colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node_colors.get(node[0], "#FFFFFF") for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Генерація кольорів від темного до світлого
def generate_colors(num_colors):
    return ["#%02x%02x%02x" % (int(255 * i / num_colors), 100, 240) for i in range(num_colors)]

# Алгоритм обходу в глибину (DFS) за допомогою стека
def dfs(tree_root):
    stack = [tree_root]
    visited = set()
    order = []
    
    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            order.append(node)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    return order

# Алгоритм обходу в ширину (BFS) за допомогою черги
def bfs(tree_root):
    queue = [tree_root]
    visited = set()
    order = []
    
    while queue:
        node = queue.pop(0)
        if node.id not in visited:
            visited.add(node.id)
            order.append(node)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return order

# Відображення обходу
def visualize_traversal(tree_root, traversal_order):
    num_nodes = len(traversal_order)
    colors = generate_colors(num_nodes)
    
    node_colors = {}
    for i, node in enumerate(traversal_order):
        node_colors[node.id] = colors[i]
    
    draw_tree(tree_root, node_colors)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід у глибину (DFS)
dfs_order = dfs(root)
print("Обхід у глибину (DFS):", [node.val for node in dfs_order])
visualize_traversal(root, dfs_order)

# Обхід у ширину (BFS)
bfs_order = bfs(root)
print("Обхід у ширину (BFS):", [node.val for node in bfs_order])
visualize_traversal(root, bfs_order)