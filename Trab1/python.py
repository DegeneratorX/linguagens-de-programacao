# Definição do nó da árvore
class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.x = 0
        self.y = 0

# Função de auxílio para adicionar coordenadas X, Y a cada nó
def add_xy(tree):
    if tree is None:
        return None
    
    new_tree = TreeNode(tree.key, tree.val, add_xy(tree.left), add_xy(tree.right))
    return new_tree

# Algoritmo de desenho da árvore (percorrendo em profundidade)
def depth_first(tree, level=1, left_lim=0, scale=30):
    if tree is None:
        return left_lim, left_lim

    if tree.left is None and tree.right is None:
        tree.x = left_lim
        tree.y = scale * level
        return left_lim, left_lim

    if tree.left is not None and tree.right is None:
        right_lim = depth_first(tree.left, level + 1, left_lim, scale)[1]
        tree.x = (left_lim + right_lim) // 2
        tree.y = scale * level
        return left_lim, right_lim

    if tree.left is None and tree.right is not None:
        right_lim = depth_first(tree.right, level + 1, left_lim, scale)[1]
        tree.x = (left_lim + right_lim) // 2
        tree.y = scale * level
        return left_lim, right_lim

    l_root_x, l_right_lim = depth_first(tree.left, level + 1, left_lim, scale)
    r_left_lim = l_right_lim + scale
    r_root_x, right_lim = depth_first(tree.right, level + 1, r_left_lim, scale)

    tree.x = (l_root_x + r_root_x) // 2
    tree.y = scale * level
    return l_root_x, right_lim

# Testando com um exemplo de árvore
if __name__ == "__main__":
    # Construindo a árvore exemplo
    tree = TreeNode('a', 111,
                    TreeNode('b', 55, 
                             TreeNode('x', 100, 
                                      TreeNode('z', 56), 
                                      TreeNode('w', 23)),
                             TreeNode('y', 105, None,
                                      TreeNode('r', 77))),
                    TreeNode('c', 123,
                             TreeNode('d', 119,
                                      TreeNode('g', 44),
                                      TreeNode('h', 50,
                                               TreeNode('i', 5),
                                               TreeNode('j', 6))),
                             TreeNode('e', 133)))

    # Adicionando coordenadas X e Y
    tree = add_xy(tree)

    # Aplicando o algoritmo de desenho de árvore
    depth_first(tree)

    # Printando as coordenadas dos nós como um teste
    print(tree.x, tree.y)  # Saída deveria ser as coordenadas x, y do nó raiz