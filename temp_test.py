a=1
do:
    print(str(a), end=" ")
    a+=1
while a<5
else:
    print("程序顺利执行完成")

a=1
do:
    if a==4:
        a+=1
        continue
    print(str(a), end=" ")
    a+=1

    if a==6:
        break
while a<10
else:
    print("break结束不会执行else")
print("程序运行完成")
