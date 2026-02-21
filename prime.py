a = int(input(''))

if a <= 1:
    print('NOT PRIME')
    
else:
    is_prime = True
    
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            is_prime = False
            break
    if is_prime:
        print('prime')
    else:
        print('Not prime')