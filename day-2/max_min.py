"""
	first sort the list
	then get the first element and the last element.

"""


def find_max_min(param):
    param.sort()
    result = []  # result will be stored in a list

    first = param[0]
    last = param[len(param) - 1]

    if first == last:
        result.append(first)
        return result
    else:
        result.append(first)  # append means to permanently join
        result.append(last)
        return result


find_max_min([80, 8, 6, 12, 99, 78, 8, 965, 28])
