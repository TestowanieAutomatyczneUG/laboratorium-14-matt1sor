
def ISBNumber(num):
    num = list(num.replace('-', ''))
    sum = 0
    for i in range(len(num)):
        if (i+1)%2 == 0:
            sum += (int(num[i]) * 3)
        else:
            sum += (int(num[i]))
    if sum%10 == 0:
        return str(0)
    return str(10-((sum//10)%10))