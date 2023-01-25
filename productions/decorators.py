from productions.utils import find_isomorphisms, find_isomorphisms_for_p9, find_isomorphisms_for_p10, find_isomorphisms_for_p13, find_isomorphisms_for_p15

def first_isomorphism(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)

        return inner
    return outer


def all_isomorphisms(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphisms=isomorphisms, **kwargs)

        return inner

    return outer


def first_isomorphism_for_p9(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms_for_p9(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)
            print(isomorphisms)
            return apply_fun(G, *args, isomorphisms=isomorphisms, **kwargs)

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


def first_isomorphism_for_p13(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms_for_p13(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)

        return inner
    return outer


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

def p15_isomorphism(left_side, all_isomorphisms=False):
    return basic_isomorphism(left_side, all_isomorphisms, iso_finder=find_isomorphisms_for_p15)