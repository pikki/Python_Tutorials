def feb_gen(n):
    i = 0
    a = 1
    while i <= n:
        print(i)
        b = i
        i = i + a
        a = b

#ask Kaustubh
# what's the error with n ?
# get some clarity on Memoization

def recur_fib(n):
   if n == 1 or n == 0 :
       return n
   else:
       return(recur_fib(n-2) + recur_fib(n-1))

n = int(input("Enter Fibonacci max limit : "))
feb_gen(n)
#using recurrsion
#for i in range(n):
#    print(recur_fib(i))
