N=int(input())

def divisors(n):
    i=1
    divisor_list=[]
    while i*i<=n:
        if n%i==0:
            divisor_list.append(i)
            if n//i!=i:
                divisor_list.append(n//i)
        i+=1
    divisor_list.sort()
    return divisor_list

print(divisors(N))