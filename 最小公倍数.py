def gbs(x, y):
    if x > y:
        num = x
    else:
        num = y
#注意取左不取右原则
    for i in range (num,x*y+1):
        if ((i % x == 0) and (i % y == 0)):
            com = i
            break
#注意局部变量
    return com
num1 = int(input ("请输入第一位数:"))
num2 = int(input ("请输入第二位数:"))
print(num1,"和",num2,"最小公倍数为", gbs(num1 ,num2))
