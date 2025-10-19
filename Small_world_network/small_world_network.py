import numpy as np
import matplotlib.pyplot as plt 
import random
import network

class SmallWorldNetwork: #it's L nodes, labeled 0,..., L-1 are placed like the vertices of a L-sided regular poligon
    def __init__(self,my_L:int=10,my_Z:int=1,my_p:float=0.1):
        assert my_L >0 and my_Z >= 0 and my_p >=0 and my_p <=1
        self.L=my_L #number of nodes
        self.Z=my_Z%my_L#number of short edges connections each node has to each side
        self.p=my_p # p*L*Z is the number of shortcuts: p=0 for a completely clustered network, p=1 for a completely random one
        self.network=network.Network()

        self.network.nodes=np.linspace(0,self.L-1,self.L,dtype=int)
        if self.Z == 0: return
        for n in range(0,self.L): 
            for z in range(1,self.Z+1): 
                #left_node,right_node= self.network.GetNeighbors(n,z)
                self.network.AddEdge((n-z)%self.L,n)
                self.network.AddEdge(n,(n+z)%self.L)

    def AddShortcuts(self):

        i=0
        while i < int(self.L*2*self.Z*self.p): 

            shortcut1,shortcut2=np.random.choice(self.network.nodes,2,replace=False) 
            if self.network.AddEdge(shortcut1,shortcut2):
                i=i+1


    def ReplaceWShortcuts(self):

        if self.p==1: 
            for index in range(0,len(self.network.edges)):
                while not self.network.ReplaceEdge(index,random.choice(self.network.nodes)):
                    pass


        indeces=np.random.choice(range(0,len(self.network.edges)),size=int(self.L*self.Z*self.p),replace=False)
        for index in indeces:
            while not self.network.ReplaceEdge(index,random.choice(self.network.nodes)):
                pass


    def Draw(self,ax): 

        angles = np.linspace(0, 2 * np.pi,self.L, endpoint=False)

        # Convert polar coordinates to Cartesian coordinates
        x = np.cos(angles)
        y = np.sin(angles)

        # Create a closed loop by adding the first point at the end
        x = np.append(x, x[0])
        y = np.append(y, y[0])

        
        ax.plot(x, y,"*",markersize=30,color="purple")
        for (n,m) in self.network.edges: 
            
            if (abs(n-m))%(self.L-2) > self.Z: 
                ax.plot([x[n],x[m]],[y[n],y[m]],color="red")
            
                
            else:    
                ax.plot([x[n],x[m]],[y[n],y[m]],color="black")
            

        
    

    


    