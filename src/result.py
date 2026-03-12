
from add import add


def addition(a, b):
    c = add(a, b)
    return "The sum of {} and {} is {}".format(a, b, c)

if __name__ == "__main__":
    a = 70
    b = 80
    result = addition(a, b)
    print("Calculating the sum of {} and {}...".format(a, b))
    print(result)
    print("Done!")