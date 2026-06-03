'''n = int(input())
org=n
class check(palindrome):
    def __init__(self,n):
        self.n=n
    def is_palindrome(self):
        rev=0
        while self.n>0:
            dig=self.n%10
            rev=rev*10+dig
            self.n=self.n//10
    print(rev)
    if rev==org:
        print("Palindrome")
    else:
        print("Not Palindrome")
'''
'''def palindrome(n):
    mul=1
    for i in range(2,n+1):
        mul=mul*i
    return mul
n=int(input())
print(palindrome(n))'''
'''
def fibonacci(n):
    a=0
    b=1
    print(a,end=" ")
    for i in range(n):
        print(b,end=" ")
        a,b=b,a+b

n=int(input())
fibonacci(n)
'''
'''
m=int(input())
n=m
count=0
while n>0:
    count=count+1
    n//=10
ad=0
while m>0:
    dig=m%10
    ad+=dig**count
    m//=10
print(ad)'''