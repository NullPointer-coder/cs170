# Jingbo Wang
# testing function

def test_1(s):
    print(s) # 'Hey'
    s = "Hello"
    print(s) # 'Hello'
    # you cannot mutate string referred by s
    # str is an immutable type
def test_2(list_str):
    # list, is a mutable type
    # list_str is refering to the object from main_2
    print(list_str)   # 10 20
    list_str = [0, 1] # this step  creates a new list
    print(list_str)   # 0 1

def test_3(list_str):
# list_str is an alias to the object [10, 20]
# from main_3
  list_str.append(30)

def main_1():
    s = 'Hey'
    print(s)
    test_1(s)
    print(s) # 'Hey'

def main_2():
    # list type
    s= [10, 20]
    print(s) # 10 20
    # passing a list object to test_2
    test_2(s)
    print(s) # 10 20

def main_3():
    s = [10, 20] # list is an mutable type
    print(s) # 10 20
    test_3(s)
    print(s) # 10 20 30

main_1()
main_2()
main_3()
