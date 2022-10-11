def hacker():
    data = open('class_register.txt', 'r+', encoding='utf = 8')
    num = data.read().split()
    minimal, maximal = min(num), max(num)
    for i in range(len(num)):
        if num[i] == maximal:
            num[i] = minimal
    data.write('\n' + ' '.join(num))
    data.close()
