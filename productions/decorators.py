from productions.utils import find_isomorphisms, find_isomorphisms_for_p9, find_isomorphisms_for_p10


def first_isomorphism(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)

        return inner
    return outer


def first_isomorphism_for_p9(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms_for_p9(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)

        return inner
    return outer


def first_isomorphism_for_p10(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms_for_p10(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)

        return inner
    return outer
