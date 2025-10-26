
import network as nw 
import small_world_network as swn
import numpy as np
import matplotlib.pyplot as plt
import time

#SETTING PARAMETERS

L=10#nodes
Z=2#connections to each side
N=L*2 #total connections



#CREATING THE NETWORK
my_pol_network=swn.SmallWorldNetwork(L,Z)

for n in range(0,my_pol_network.GetL()):
    for z in range(-my_pol_network.GetZ(),+my_pol_network.GetZ()):
        if not z==0:
            assert my_pol_network.network.HasEdge(n,(n+z)%my_pol_network.GetL())


#fig,ax=plt.subplots(1,1,figsize=(10,10))

#COOL DYNAMIC PLOTTING 

""" 
#plt.ion()
for p in np.linspace(0.,1.,p_count): 
        my_pol_network.p=p 
        my_pol_network.ReplaceWShortcuts()
        #my_pol_network.Draw()
        randomness=round(p*100,2)
        #print(i)
        average_path_lenght[t][i]=round(my_pol_network.network.FindAveragePathLenght(),3)
        #print(p," | ",average_path_lenght)
        #ax.set_title(f"Network with {L} nodes, {N} connections and {randomness}% randomness. Average path lenght: {average_path_lenght}")
        #fig.canvas.draw()                   # redraw figure
        #fig.canvas.flush_events()           # flush GUI events
        #time.sleep(1)    
        i=i+1
   



"""









fig2,ax2=plt.subplots(1,1,figsize=(10,10))



trials=10
p_count=10
average_path_lenght=np.empty([trials,p_count])
for t in range(0,trials):
    i=0
    for p in np.linspace(0.,1.,p_count): 
        my_pol_network.p=p 
        my_pol_network.ReplaceWShortcuts()
        #my_pol_network.Draw()
        randomness=round(p*100,2)
        #print(i)
        average_path_lenght[t][i]=round(my_pol_network.network.FindAveragePathLenght(),3)
        #print(p," | ",average_path_lenght)
        #ax.set_title(f"Network with {L} nodes, {N} connections and {randomness}% randomness. Average path lenght: {average_path_lenght}")
        #fig.canvas.draw()                   # redraw figure
        #fig.canvas.flush_events()           # flush GUI events
        #time.sleep(1)    
        i=i+1
   

#time.sleep(1)


#print(average_path_lenght,"\n")

print(average_path_lenght.mean(axis=0))

p=np.linspace(0.,1.,p_count)
mean_path=average_path_lenght.mean(axis=0)
ax2.plot(p,mean_path)

plt.show()