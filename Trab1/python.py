# Global variable for scale
SCALE = 30

def depth_first(tree, level, left_lim, root_x=None, right_lim=None):
    if isinstance(tree, dict):
        x = tree.get('x')
        y = tree.get('y')
        left = tree.get('left')
        right = tree.get('right')

        if left == 'leaf' and right == 'leaf':
            return (root_x, SCALE * level)
        elif left != 'leaf' and right == 'leaf':
            return depth_first(left, level+1, left_lim, root_x, right_lim)
        elif left == 'leaf' and right != 'leaf':
            return depth_first(right, level+1, left_lim, root_x, right_lim)
        else:
            l_root_x, l_right_lim = depth_first(left, level+1, left_lim, root_x, right_lim)
            r_left_lim = l_right_lim + SCALE
            r_root_x, r_right_lim = depth_first(right, level+1, r_left_lim, root_x, right_lim)
            root_x = (l_root_x + r_root_x) // 2
            return (root_x, SCALE * level)
    return None

def prog(s):
    s1, s2 = s.split(' ', 1)
    y = id_fn(s2)
    s3 = s2.split(';', 1)[1]
    z = stat(s3)
    sn = s3.split('end', 1)[1]
    return ('prog', y, z)

def stat(s):
    t, s2 = s.split(' ', 1)
    if t == 'begin':
        return sequence(stat, lambda x: x == ';', s2, 'end')
    elif t == 'if':
        c, s3 = comp(s2)
        x1 = stat(s3.split('then', 1)[1])
        x2 = stat(s3.split('else', 1)[1])
        return ('if', c, x1, x2)
    elif t == 'while':
        c, s3 = comp(s2)
        x = stat(s3.split('do', 1)[1])
        return ('while', c, x)
    elif t == 'read':
        return ('read', id_fn(s2))
    elif t == 'write':
        return ('write', expr(s2))
    elif is_ident(t):
        e = expr(s2.split(':=', 1)[1])
        return ('assign', t, e)
    else:
        raise Exception("Error")

def sequence(non_term, sep, s1, end_token):
    x1, rest = non_term(s1)
    if sep(rest.split(' ')[0]):
        x2 = sequence(non_term, sep, rest.split(' ', 1)[1], end_token)
        return (x1, x2)
    else:
        return x1

def comp(s):
    return sequence(expr, cop, s, None)

def expr(s):
    return sequence(term, eop, s, None)

def term(s):
    return sequence(fact, top, s, None)

def cop(y):
    return y in ['<', '>', '<=', '>=', '==', '!=']

def eop(y):
    return y in ['+', '-']

def top(y):
    return y in ['*', '/']

def fact(s):
    if is_int(s.split(' ')[0]) or is_ident(s.split(' ')[0]):
        return s.split(' ')[0], s.split(' ', 1)[1]
    else:
        e = expr(s.split('(', 1)[1].split(')', 1)[0])
        return e

def id_fn(s):
    x = s.split(' ')[0]
    if is_ident(x):
        return x, s.split(' ', 1)[1]
    return None

def is_ident(x):
    return isinstance(x, str) and x.isalpha()

def is_int(t):
    try:
        int(t)
        return True
    except ValueError:
        return False

# Main execution
a = prog("program foo ; while a + 3 < b do b := b + 1 end")
print(a)