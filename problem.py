# Problem: Waterwelmon 4A
# Attempt: 6
# Solution: Find if a number is prime or not. If it is not prime
# Divide by 2 and if that is even the answer is YES
# Else NO
num = int(input())

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            if num % 2 != 0:
                flag = False
                break

if flag == True:
    print("YES")
else:
    print("NO")