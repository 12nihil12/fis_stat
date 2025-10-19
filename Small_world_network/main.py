
import network as nw 
import small_world_network as swn
import numpy as np
import matplotlib.pyplot as plt
import time

#parameters:

L=50#nodes
Z=2#connections to each side
N=L*2 #total connections

plt.ion()
my_pol_network=swn.SmallWorldNetwork(L,Z)


for n in range(0,my_pol_network.L):
    for z in range(-my_pol_network.Z,+my_pol_network.Z):
        if not z==0:
            assert my_pol_network.network.HasEdge(n,(n+z)%my_pol_network.L)


fig,ax=plt.subplots(1,1,figsize=(10,10))


for p in np.linspace(0.,1.,10): 
    my_pol_network.p=p 
    my_pol_network.ReplaceWShortcuts()
    my_pol_network.Draw(ax)
    randomness=round(p*100,2)
    average_path_lenght=round(my_pol_network.network.FindAveragePathLenght(),3)
    ax.set_title(f"Network with {L} nodes, {N} connections and {randomness}% randomness. Average path lenght: {average_path_lenght}")
    fig.canvas.draw()                   # redraw figure
    fig.canvas.flush_events()           # flush GUI events
    time.sleep(1)    

time.sleep(1)


