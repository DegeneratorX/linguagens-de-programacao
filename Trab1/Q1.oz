tree(key:a val:111
    left:tree(key:b val:55
        left:tree(key:x val:100
            left:tree(key:z val:56 left:leaf right:leaf)
            right:tree(key:w val:23 left:leaf right:leaf))
    right:tree(key:y val:105 left:leaf
        right:tree(key:r val:77 left:leaf right:leaf)))
right:tree(key:c val:123
    left:tree(key:d val:119
        left:tree(key:g val:44 left:leaf right:leaf)
        right:tree(key:h val:50
            left:tree(key:i val:5 left:leaf right:leaf)
            right:tree(key:j val:6 left:leaf right:leaf)))
    right:tree(key:e val:133 left:leaf right:leaf)))

proc {DepthFirst Tree}
    case Tree
    of tree(left:L right:R ...) then
        {DepthFirst L}
        {DepthFirst R}
    [] leaf then
        skip
    end
end

The tree-drawing algorithm does a depth-first traversal and calculates the (x,y)
coordinates of each node during the traversal. As a preliminary to running the
algorithm, we extend the tree nodes with the fields x and y at each node:

fun {AddXY Tree}
    case Tree
    of tree(left:L right:R ...) then
        {Adjoin Tree
            tree(x:_ y:_ left:{AddXY L} right:{AddXY R})}
    [] leaf then
        leaf
    end
end