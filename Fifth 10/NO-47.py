import copy
def copying(List):
    return copy.deepcopy(List)
L = [1,2,3,4,5,[5,7],9,6,[11,23]]
print((copying(L)))