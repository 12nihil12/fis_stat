import numpy as np 
import matplotlib.pyplot as plt
a=0
b=1
N=10
M=1000000
x=np.random.uniform(a,b,size=(M,N))

X=np.amax(x,axis=1)


fig, ax = plt.subplots(1, 1, figsize=(6, 4))
bins = np.linspace(a, b, num=int(M/100))
ax.hist(X,bins=bins,density=True)

x=np.linspace(a,b,1000)

y=(N/((b-a)**N))*(x-a)**(N-1)
plt.plot(x,y,color="red")

print("MEAN: Empirical " , np.mean(X) , " |  expected ",(N*b+a)/(N+1))

print("VARIANCE: Empirical " , np.var(X) , " |  expected ",(N*(b**2-4*a*b-a**2)+2*a**2-2*a*b)/((N+1)**2*(N+2)) )

plt.show()

