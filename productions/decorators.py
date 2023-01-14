from productions.utils import find_isomorphisms, find_isomorphisms_for_p13


def basic_isomorphism(left_side, all_isomorphisms=False, iso_finder=find_isomorphisms):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = iso_finder(G, left_side)
            if not isomorphisms: 
                return apply_fun(G, *args, **kwargs)
            if not all_isomorphisms:
                return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)
            return apply_fun(G, *args, isomorphisms=isomorphisms, **kwargs)
        return inner
    return outer

def p13_isomorphism(left_side, all_isomorphisms=False):
    return basic_isomorphism(left_side, all_isomorphisms, iso_finder=find_isomorphisms_for_p13)


