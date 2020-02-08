from typing import List
def divid_by_n(num: int, n: int) -> str:
    """Return base <n> representation of <num>.
    """
    q, r = divmod(num, n)
    stack = []
    stack.append(r)
    while (q > 0):
        q, r = divmod(q, n)
        stack.append(r)

    converted = ""
    while stack != []:
        converted += str(stack.pop())

    return converted

if __name__ == "__main__":
    actual = divid_by_n(11311110000, 10)
    print("actual for 11311110000: " + str(actual))

    actual = divid_by_n(5, 2)
    print("\n\nactual for 5 base 2: " + str(actual))

    actual = divid_by_n(10, 2)
    print("\n\nactual for 10 base 2: " + str(actual))




