# using dict
dictionary = {}
list1 = []
n = int(input())
if 1 <= n <= 100000:
    for i in range(n):
        name = input()
        temp = name.isalnum()
        if not temp:
            a, b = name.split()
            if len(b) == 8:
                dictionary[a] = b
    # for i in range(n):
    while True:
        try:
            entered = input()
            if len(entered) == 0:
                break
            list1.append(entered)
        except EOFError:
            break
    for i in list1:
        if dictionary.get(i):
            print(f'{i}={dictionary.get(i)}')
        else:
            print("Not found")


# using map
# dictionary = {}
# lis = []
# n = int(input())
# for i in range(n):
#     a, b = map(str, input().split())
#     dictionary[a] = b
#     print(dictionary)
# for i in range(n):
#     names = input()
#     lis += names
# print(lis)
# for i in lis:
#     if dictionary.get(i):
#         print(f'{i}={dictionary.get(i)}')
#     else:
#         print("Not found")
