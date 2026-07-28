def eratosthenes(n):
    for i in range(2,int(n**0.5)+1):
	    if prime[i]:
		    for j in range(2*i,n+1,i):
			    prime[j]=False

n=int(input())
prime=[True]*(n+1)
eratosthenes(n)
list_prime=[]
for i in range(2,n+1):
	if prime[i]:
	    list_prime.append(i)

print(list_prime)