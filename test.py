height=4
for i in range(height//2):
    spaces=height//2-i
    for j in range(height//2-i):
        print(' ',end=' ')
    for j in range(i):
        print('/',end=' ')
    for j in range(i):
        print("\\",end=' ')
    print('\n')
for i in range(height//2):
    for j in range(height//2-i):
        print(' ',end=' ')
    for j in range(i):
        print("\\",end=' ')
    for j in range(i):
        print('/',end=' ')
    print('\n')