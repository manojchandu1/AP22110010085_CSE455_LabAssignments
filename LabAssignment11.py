import sys

def minimax(node, depth, is_maximizing, tree, values, path):
    if depth == 0 or node not in tree:
        return values.get(node, node), [node]

    if is_maximizing:
        best_value = -sys.maxsize
        best_path = []
        for child in tree[node]:
            val, child_path = minimax(child, depth - 1, False, tree, values, path + [child])
            if val > best_value:
                best_value = val
                best_path = [node] + child_path
        return best_value, best_path
    else:
        best_value = sys.maxsize
        best_path = []
        for child in tree[node]:
            val, child_path = minimax(child, depth - 1, True, tree, values, path + [child])
            if val < best_value:
                best_value = val
                best_path = [node] + child_path
        return best_value, best_path

tree_figure1 = {
    'A': ['B1', 'B2', 'B3'],
    'B1': ['C1', 'C2', 'C3'],
    'B2': ['C4', 'C5', 'C6'],
    'B3': ['C7', 'C8', 'C9']
}

values_figure1 = {
    'C1': 12, 'C2': 10, 'C3': 3,
    'C4': 5, 'C5': 8, 'C6': 10,
    'C7': 11, 'C8': 2, 'C9': 12
}

optimal_value_figure1, optimal_path_figure1 = minimax('A', 2, True, tree_figure1, values_figure1, ['A'])
print(f"Optimal Path for Figure 1: {' -> '.join(optimal_path_figure1)}")
print(f"Optimal Value for Figure 1: {optimal_value_figure1}")

tree_figure2 = {
    3: [3, 1],
    3: [3, 8],
    1: [1, 4],
    3: [-1, 3],
    8: [-5, 8],
    1: [1, -4],
    4: [4, -3],
    -1: [5, -1],
    3: [4, 3],
    -5: [-2, -5],
    8: [9, 8],
    1: [6, 1],
    -4: [-4, 2],
    4: [7, 3],
    -3: [3, -3]
}

values_figure2 = {
    5: 5, -1: -1, 4: 4, 3: 3, -2: -2, -5: -5, 9: 9, 8: 8, 6: 6, 1: 1, -4: -4, 2: 2, 7: 7, 3: 3, -3: -3
}

optimal_value_figure2, optimal_path_figure2 = minimax(3, 3, True, tree_figure2, values_figure2, [3])
print(f"Optimal Path for Figure 2: {' -> '.join(map(str, optimal_path_figure2))}")
print(f"Optimal Value for Figure 2: {optimal_value_figure2}")
