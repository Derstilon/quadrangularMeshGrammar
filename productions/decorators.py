from productions.utils import find_isomorphisms

def first_isomorphism(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)

        return inner
    return outer

def isomorphism_P5(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms(G, left_side)
            
            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            keys = isomorphisms[0]
            counter = 0
            for p_1 in keys:
                for p_3 in keys:
                    if p_1 < p_3 and G.nodes[p_1]['label'] == 'E' and G.nodes[p_3]['label'] == 'E':
                        x1 = G.nodes[p_1]['pos'][0]
                        x3 = G.nodes[p_3]['pos'][0]
                        y1 = G.nodes[p_1]['pos'][1]
                        y3 = G.nodes[p_3]['pos'][1]
                        mid_x = (x1+x3)/2
                        mid_y = (y1+y3)/2
                        for p_2 in keys:
                            x2 = G.nodes[p_2]['pos'][0]
                            y2 = G.nodes[p_2]['pos'][1]
                            if(G.nodes[p_2]['label'] == 'E' and x2 == mid_x and y2 == mid_y):
                                if (p_1, p_2) in set(G.edges) and (p_3, p_2) in set(G.edges):
                                    counter += 1

            print('counter', counter)
            if counter != 1: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)

        return inner
    return outer

def isomorphism_P6(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms(G, left_side)
            
            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            keys = isomorphisms[0]
            counter = 0
            for p_1 in keys:
                for p_3 in keys:
                    if p_1 < p_3 and G.nodes[p_1]['label'] == 'E' and G.nodes[p_3]['label'] == 'E':
                        x1 = G.nodes[p_1]['pos'][0]
                        x3 = G.nodes[p_3]['pos'][0]
                        y1 = G.nodes[p_1]['pos'][1]
                        y3 = G.nodes[p_3]['pos'][1]
                        mid_x = (x1+x3)/2
                        mid_y = (y1+y3)/2
                        for p_2 in keys:
                            x2 = G.nodes[p_2]['pos'][0]
                            y2 = G.nodes[p_2]['pos'][1]
                            if(G.nodes[p_2]['label'] == 'E' and x2 == mid_x and y2 == mid_y):
                                if (p_1, p_2) in set(G.edges) and (p_3, p_2) in set(G.edges):
                                    counter += 1

            print('counter', counter)
            if counter != 2: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)

        return inner
    return outer