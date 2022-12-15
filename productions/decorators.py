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

            print(str(isomorphisms))

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)

        return inner
    return outer
