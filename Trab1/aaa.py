# Definindo a estrutura da árvore usando tuplas. 
# Uma folha é representada por None. 
# Um nó é representado por (chave, valor, esquerda, direita).

# Exemplo de árvore conforme fornecido
example_tree = ("a", 111, 
    ("b", 55, 
        ("x", 100, 
            ("z", 56, None, None), 
            ("w", 23, None, None)), 
        ("y", 105, None, 
            ("r", 77, None, None))), 
    ("c", 123, 
        ("d", 119, 
            ("g", 44, None, None), 
            ("h", 50, 
                ("i", 5, None, None), 
                ("j", 6, None, None))), 
        ("e", 133, None, None)))

SCALE = 30  # Definindo a escala conforme o exemplo

# Função para calcular as coordenadas dos nós
def depth_first(tree, level, left_lim):
    if tree is None:  # Caso base: se a árvore for uma folha
        return left_lim, left_lim, None
    
    key, val, left, right = tree  # Desempacotando o nó
    
    if left is None and right is None:  # Se o nó for uma folha
        x = y = left_lim
        return x, left_lim, (key, val, level * SCALE, left_lim, None, None)
    
    if left is not None and right is None:  # Se o nó tiver apenas filho à esquerda
        x, right_lim, new_left = depth_first(left, level + 1, left_lim)
        y = left_lim
        return x, right_lim, (key, val, level * SCALE, x, new_left, None)
    
    if left is None and right is not None:  # Se o nó tiver apenas filho à direita
        x, right_lim, new_right = depth_first(right, level + 1, left_lim)
        y = left_lim
        return x, right_lim, (key, val, level * SCALE, x, None, new_right)
    
    # Se o nó tiver dois filhos
    l_root_x, l_right_lim, new_left = depth_first(left, level + 1, left_lim)
    r_root_x, r_right_lim, new_right = depth_first(right, level + 1, l_right_lim + SCALE)
    x = (l_root_x + r_root_x) // 2
    return x, r_right_lim, (key, val, level * SCALE, x, new_left, new_right)

# Testando a função com a árvore exemplo
_, _, new_tree = depth_first(example_tree, 1, SCALE)

# Função para imprimir a árvore com as coordenadas
def print_tree_with_coordinates(tree):
    if tree is not None:
        key, val, y, x, left, right = tree
        print(f"Key: {key}, Value: {val}, X: {x}, Y: {y}")
        print_tree_with_coordinates(left)
        print_tree_with_coordinates(right)

# Imprimindo a árvore com as coordenadas
print_tree_with_coordinates(new_tree)