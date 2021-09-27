"""Task1"""
"""Here is a string (UTF-8 format). We should find the most repeatable symbol"""
"""If we have more than one symbol which has the same number of replays we can return any of them"""

"""Solution 1"""


def solution_1():
    """here we've got O(n*k) complexity"""
    print("input string")
    string = input()
    symbol = "None"
    count = 0

    for top_element in set(string):
        cur_count = 0
        for low_element in string:
            if top_element == low_element:
                cur_count += 1
        if cur_count > count:
            symbol = top_element
            count = cur_count

    print("the result of the first solution:")
    print("the most frequent symbol is", symbol, "\nfrequency is equal to", count)

    return symbol, count


def solution_2():
    """Here we've got O(n) complexity"""
    string = input()
    symbol = "None"
    count = 0
    dictionary = {}

    for element in string:
        if element not in dictionary:
            dictionary[element] = 0
        dictionary[element] += 1

        if dictionary[element] > count:
            symbol = element
            count = dictionary[element]

    print("the result of the second solution:")
    print("the most frequent symbol is", symbol, "\nfrequency is equal to", count)

    return symbol, count


# symbol, count = solution_1()
# symbol, count = solution_2()


"""Task2"""
"""Sum of the sequence"""


def sum_of_elements():
    """here we've got O(n) complexity"""
    sum_ = 0
    list_ = list(map(int, input().split(", ")))
    print(list_)
    for element in list_:
        sum_ += element

    print(f"Sum of the sequence is equal to {sum_}")
    return sum_


sum_ = sum_of_elements()
