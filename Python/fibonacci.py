def fibonacci(num):
    if (num <= 1):
        return num
    else:
        return (fibonacci(num-1)+fibonacci(num-2))

fine=int(input())
k=0
while True:
    if(fibonacci(k)>fine):
        break
    else:
        print(fibonacci(k))
        k+=1