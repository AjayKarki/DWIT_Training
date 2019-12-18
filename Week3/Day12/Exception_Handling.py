a = 1
b = 1
list1 = []
try:
    print(a / b)
    file = open("abc.txt", 'r')
    file.write("as")
    print(list1[1])
except ZeroDivisionError:
    print("b=0")
except FileNotFoundError as e:
    print("404 File Not Found", e)
except IndexError:
    print("Index Out of bound error")
except IOError as e:
    print("IO Error occured", e)
else:
    print("Executes when there is no error in try block")
finally:
    print("Doesn't care if there are error in try or not this will be executed")
print("test.....")


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b


try:
    print(divide(1, 0))
except:
    print("Division by zero")


def avg(marks):
    """
    This is equivalent of code below
    if len(marks) == 0:
        raise AssertionError
    else:
        return sum(marks) / len(marks)
    """
    assert len(marks) != 0, "List is empty"
    return sum(marks) / len(marks)

try:
    mark2 = [55, 55, 55, 55, 100]
    print("Avg", avg(mark2))

    mark1 = []
    print("Avg", avg(mark1))
    print(avg(mark2))
except AssertionError as e:
    print(e.args)