s = []
def evenandodd(para):
    odd = even = ''
    s = len(para)
    for i in range(s):
        if i % 2 == 0:
            even += para[i]
        else:
            odd += para[i]
    return f"{even} {odd}"


for j in range(int(input())):
    s.append(input())
for k in s:
    output = evenandodd(k)
    print(output)

