#Q1.Find sum of n numbers with help of while loop.
def sum():
    num=[1,4,2,3,7]
    i= len(num);
    add=0
    while(i>0):
        add+=num[i-1]
        i=i-1
    print(add)
sum()

#Q2.Take an integer and find whether is prime or not.
def prime():
    num = int(input("Enter the number"))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
prime()