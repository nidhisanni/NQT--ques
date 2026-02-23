# a = input()
# rev = ''

# for ch in a:
#     rev = ch + rev 
# print(rev)

def check_plaindrom(a):
    rev = ''
    for ch in a:
        rev = ch + rev
    print(rev)

    if a == rev:
        return 'palindrome'
    else:
        return 'not palindrom'
        
a = input()
print(check_plaindrom(a))