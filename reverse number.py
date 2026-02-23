# a = int(input())
# a = abs(a)
# rev = 0
# while a != 0:
#     digit = a % 10
#     rev = rev * 10 + digit
#     a = a // 10
# print(rev)

def rev_number(a):
    rev = 0
    while a != 0:
        digit = a % 10
        rev = rev * 10 + digit
        a = a // 10
    return rev
a = int(input())
print(rev_number(a))

