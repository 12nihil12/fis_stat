import numpy as np
from collections import deque


class Network: 
    def __init__(self):
        self.nodes=np.array([0],dtype=int)
        self.edges=np.empty((0,2),dtype=int)
        pass


    def HasNode(self,my_node:int): 
        for node in self.nodes: 
            if my_node==node:
                return True 
            
        return False
    

    def HasEdge(self,mynode1:int,mynode2:int): 
        new_edge=np.array([mynode1,mynode2])
        return np.any(np.all(self.edges == new_edge, axis=1)) or np.any(np.all(self.edges == new_edge[::-1], axis=1))

    
    def AddNode(self,mynode:int): 
        if self.HasNode(mynode): 
            return False
        self.nodes=np.append(self.nodes,mynode)
        return True

    def AddEdge(self,mynode1:int,mynode2:int): 
        assert  self.HasNode(mynode1) and self.HasNode(mynode2) and not mynode1==mynode2
        if self.HasEdge(mynode1,mynode2): 
            return False
        newedge=np.array([mynode1,mynode2])
        self.edges=np.vstack([self.edges,newedge])

        return True


    def ReplaceEdge(self,index:int,replace_node:int,which="second"): 
        assert which== "first" or which=="second"
        assert self.HasNode(replace_node)

        if which=="second": 
            if self.HasEdge(self.edges[index,0],replace_node): 
                return False
            self.edges[index,1]=replace_node
        elif which=="first": 
            if self.HasEdge(self.edges[index,1],replace_node): 
                return False
            self.edges[index,0]=replace_node

        return True


    def GetIndex(self,mynode:int): 
        assert self.HasNode(mynode)
        return np.where(self.nodes==mynode) [0][0]

     
    def GetNeighbors(self, index:int, Z:int=1,circular:bool=False): # get the nodes Z places away from the node marked by index. If circular is set to True, treats the array as spread out in a circle
        assert index >= 0 and index < len(self.nodes)  and Z >= 0 

        Z=Z%len(self.nodes)
    

        if Z==0:
            return None,None
        if circular: 
          
            left_index= (index -Z)%len(self.nodes) 
            right_index= (index +Z)%len(self.nodes) 

            return int(self.nodes[left_index]),int(self.nodes[right_index])

        else: 
            if index - Z  < 0: 
                return None,  int(self.nodes[index+Z])
            elif index + Z > len(self.nodes)-1: 
                return int(self.nodes[index+Z]), None
            else: 
                return int(self.nodes[index-Z]),int(self.nodes[index+Z])
            

    def GetConnectedNodes(self,mynode:int): 
        connected_nodes=set()
        mask = np.any(self.edges == mynode, axis=1)#selects all edges which contain mynode
        for edge in self.edges[mask]:
            connected_node=edge[0] if edge[1]==mynode else edge[1] #finds the node mynode is connected to
            connected_nodes.add(connected_node) #adds it to the set

        return connected_nodes


            

    
    def BFS(self,start_node:int,target_node:int): #implements Breadth-First Search algorithm and returns distance from start node to target node, else it returns -1 if target node is not found
        Q=deque([start_node])
        
        visited=set()

        distance={start_node : 0}

        while Q: 



            node=Q.popleft()

            if node==target_node:
                return distance[node]
            

            for connected_node in self.GetConnectedNodes(node): 
                if connected_node not in visited: 
                    visited.add(node)

                    Q.append(connected_node)
                    distance[connected_node]=distance[node]+1


                
        return -1
 
                
    def FindAveragePathLenght(self): 
        sum=0
        number_of_pairs=len(self.nodes)*(len(self.nodes)-1)/2 # the number of pairs of nodes to connect

        for n in range(0,len(self.nodes)):
            for m in range(n+1,len(self.nodes)): 
                sum=sum+self.BFS(self.nodes[n],self.nodes[m])

        return sum/number_of_pairs




