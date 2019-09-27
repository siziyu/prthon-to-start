def fblq(n):
    if n <= 2:
        return 1
    else:
        return fblq(n-2) + fblq(n-1)
i = int(input("您需要几位斐波拉契数:"))
if i <= 0:
    print("请输出正数")
else:
    print("斐波拉契数列：")
    for t in range (1, i+1):
        print(fblq(t))
