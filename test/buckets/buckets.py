from random import permutations


test_one = [i for i in range(0, 1000)]
test_two = [i for i in range(0, 3)]

def maximum_score(scores):
    if len(scores) == 0:
        return 0, ['Done']
    if len(scores) == 1:
        return scores[0]

    left, l_choices = maximum_score(list[1:])
    right, r_choices = maximum_score(list[:-1])

    if left > right:
        return left + scores[0], ['L'] + l_choices
    else:
        return right + scores[-1], ['R'] + r_choices



print(maximum_score(test_two))
