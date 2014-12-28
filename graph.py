# -*- coding: utf-8 -*-
# Node and graph implementation
# Developer
# Ismail AKBUDAK
# ismailakbudak.com

from matplotlib import pyplot as plt
import networkx as nx
import random
from collections import OrderedDict

# Node class 
class Node(object): 
    
    def __init__(self, ID, CAPACITY):
        self.ID = ID
        self.CAPACITY = CAPACITY
        self.NAME = 'N:%s-C:%s'%(str(ID),str(CAPACITY))
        self.log("node initialized..")
        self.neighbors={}
    
    def __repr__(self):
        return self.NAME

    def __str__(self):
        return self.NAME

    def addNeighbor(self,node):
        if not(self.neighbors.has_key(node.ID)):
            self.neighbors[node.ID]=node
            node.neighbors[self.ID]=self
            self.log("neighbor added..")
            return True
        else:
            self.log("neighbor could not added..")
            self.log("ERROR: key '%s' is exist in '%s'"%(node.ID, self) )
            return False
    
    def removeNeighbor(self,node):
        if self.neighbors.has_key(node.ID):
            self.neighbors.pop(node.ID)
            node.neighbors.pop(self.ID)
            self.log("neighbor removed..")
            return True
        else:
            self.log("neighbor could not removed..")
            self.log("ERROR: key '%s' is not exist in '%s'"%(node.ID, self) )
            return False

    def remove(self):
        iterator = self.neighbors.copy()
        for node in iterator.values():
            node.removeNeighbor(self)
        self.log("removed all neighbors..")       

    def log(self, message):
        #print("NODE:: %s"%(message) ) 
        pass
# Graph class
class Graph(object):

    def __init__(self):    
        self.nodes={}
        self.lastID=0  
           
    #TODO
    def grow(self, GOWTH_RATE=10, GROWTH_LIMIT=1000, MAX_CAPACITY=400 ):
        length = len(self.nodes)
        figure = 1
        while length < GROWTH_LIMIT:
            number = random.randint(1,100)
            if number > GOWTH_RATE:
                #add new node
                while self.nodes.has_key(self.lastID):
                    self.lastID += 1
                
                if len(self.nodes) > 0:
                    random_node = random.choice(self.nodes.values())    
                else:
                    random_node = None
                CAPACITY = random.randint(1, MAX_CAPACITY)     
                node = Node(self.lastID, CAPACITY)
                if self.add(node):
                    self.linkRandom(node, random_node)
                    length += 1
                else:
                    self.log_method("ERROR: node could not added in grow method")     
            else:
                #remove node
                if len(self.nodes) > 0: 
                    random_node = random.choice(self.nodes.values())
                    self.deleteRandom(random_node)
                    self.remove(random_node)
                    self.log_method("remove node")
                    length -= 1
            self.log_method("figure : %s"%figure)
            figure += 1        
            self.draw()
        self.log_method("total nodes length : %s"%str(len(self.nodes))  )
    
    #TODO
    def deleteRandom(self,random_node):
        self.log_method("")
        self.log_method("DELETE Start +++++++++++++++++++++++++++++++++++++++++++++++++++++")
        self.log_method("Started Random Node: %s neighbors : %s "%(random_node, str(random_node.neighbors)) )
        if not(random_node):
            self.log_method("ERROR: random_node is empty in deleteRandom method")
            return
        if len(random_node.neighbors) > 0:
            for item in random_node.neighbors.values():
                #item.neighbours.pop(random_node.ID)
                length = len(item.neighbors) - 1
                self.log_method("")
                self.log_method("=============================================================")
                self.log_method("neighbours length is %s"%( str(length) ))
                self.log_method("neighbours Node: %s neighbors : %s "%(item, str(item.neighbors)) )
                if length < 3:
                    node_neighbor = self.getRandomNode2( item )
                    if node_neighbor:
                        if self.link(item,node_neighbor):
                            self.log_method("nodes connected to node  ")
                        else:
                            self.log_method("ERROR-1: nodes could not connected to node  ")    
                    else:
                        self.log_method("ERROR-2: node is None")
                self.log_method("=============================================================")
        else:
            self.log_method("ERROR-0: random_node neighbours is empty in deleteRandom method")
        self.log_method("DELETE END +++++++++++++++++++++++++++++++++++++++++++++++++++++")
        self.log_method("") 

    # Get random node for delete process    
    def getRandomNode2(self, node, nodes=[]): 
        forbidden_values = node.neighbors.values()
        forbidden_values.append(node)
        for item in nodes:
            forbidden_values.append(item) 
        total_values = self.nodes.values()
        self.log_method("First -- forbidden values are %s"%(str(forbidden_values)))
        self.log_method("First AVAILABLE -- nodes are %s"%(str(total_values)))
        for value in forbidden_values:
            if value in total_values:
                total_values.remove(value)
        self.log_method("Second -- forbidden values are %s"%(str(forbidden_values)))
        self.log_method("Second AVAILABLE -- nodes are %s"%(str(total_values)))
        if len(total_values) > 0:
            new_random_node = random.choice(total_values)
            self.log_method("LAST AVAILABLE : %s  "%(str(new_random_node)) ) 
            return new_random_node    
        else:
            self.log_method("ERROR-0: there is no node for neighbour")
            return None 

    # Add neighbours to new random node 
    def linkRandom(self, node, random_node):
        self.log_method("")
        self.log_method("Start =======================================================")
        self.log_method("Started Node : %s neighbors : %s "%(node, str(node.neighbors)) ) 
        self.log_method("Started Random Node: %s neighbors : %s "%(random_node, str(random_node.neighbors)) )
        if not(random_node):
            self.log_method("ERROR: random_node is empty in linkRandom method")
            return
        if self.link(node,random_node):
            neighbors = self.getAvailableNeighbours(node, random_node)
            length = len(neighbors)
            self.log_method("AVAILABLE : %s  "%(str(neighbors)) ) 
            self.log_method("total node length is %s"%( str(len(self.nodes)) ) )    
            self.log_method("random_node neighbours length is %s"%( str(length) ) )            
            if length >= 2:
                # Get random node neighbours with randomly
                node_neighbor1 = random.choice(neighbors)
                neighbors.remove(node_neighbor1)
                node_neighbor2 = random.choice(neighbors)
            elif length == 1:
                # Choose random node neighbour Get 1 random node not exist in node neighbours and random node
                node_neighbor1 = neighbors[0]
                node_neighbor2 = self.getRandomNode( node, [node_neighbor1] )
            else: 
                # Get 2 random node not exist in node neighbours and random node
                node_neighbor1 = self.getRandomNode( node )
                node_neighbor2 = self.getRandomNode( node, [node_neighbor1] )
            
            if node_neighbor1:
                if self.link(node,node_neighbor1):
                    self.log_method("nodes connected to random node  ")
                else:
                    self.log_method("ERROR-1: nodes could not connected to random node  ")    
            else:
                self.log_method("ERROR-2: node is None")
            if node_neighbor2:
                if self.link(node,node_neighbor2):
                    self.log_method("nodes connected to random node  ")
                else:
                    self.log_method("ERROR-3: nodes could not connected to random node  ")    
            else:
                self.log_method("ERROR-4: node is None")
        else:
            self.log_method("ERROR: node could not linked to random_node")
            self.remove(node) 
        self.log_method("END =======================================================")
        self.log_method("") 

    # remove common neighbours from random neighbours    
    def getAvailableNeighbours(self, node, random_node): 
        neighbors = random_node.neighbors.values()    
        forbidden_values = node.neighbors.values() # this code is geting random_node
        forbidden_values.append(node) 
        self.log_method("AVAILABLE -- forbidden values are %s"%(str(forbidden_values))) 
        for value in forbidden_values:
            if value in neighbors:
                neighbors.remove(value) 
        return neighbors 

    def getRandomNode(self, node, nodes=[]): 
        forbidden_values = node.neighbors.values()
        forbidden_values.append(node)
        for item in nodes:
            forbidden_values.append(item) 
        total_values = self.nodes.values()
        self.log_method("First -- forbidden values are %s"%(str(forbidden_values)))
        self.log_method("First AVAILABLE -- nodes are %s"%(str(total_values)))
        for value in forbidden_values:
            if value in total_values:
                total_values.remove(value)
        self.log_method("Second -- forbidden values are %s"%(str(forbidden_values)))
        self.log_method("Second AVAILABLE -- nodes are %s"%(str(total_values)))
        if len(total_values) > 0:
            new_random_node = random.choice(total_values)
            self.log_method("LAST AVAILABLE : %s  "%(str(new_random_node)) ) 
            return new_random_node    
        else:
            self.log_method("ERROR-0: there is no node for neighbour")
            return None     

    def add(self, node):
        if not(self.nodes.has_key(node.ID)):
            self.nodes[node.ID]=node
            self.lastID += 1
            self.log("node added..")
            return True
        else:
            self.log("node could not added..")
            self.log("ERROR: key '%s' is exist"%(node.ID) )
            return False

    def remove(self, node):
        node.remove()
        self.nodes.pop(node.ID)
        self.log("node removed..")        

    def removeAll(self):
        self.nodes = {}
        self.lastID=0 
        self.log("all nodes removed..")

    def link(self,node1,node2):
        if node1.addNeighbor(node2):
            self.log("nodes linked..")
            return True
        else:
            return False     
    
    def draw(self):
        graph = nx.DiGraph()
        for node in self.nodes.values():
            graph.add_node(node)
            for node_neighbor in node.neighbors.values():
                graph.add_edge(node, node_neighbor)
        subgraphs = list(nx.strongly_connected_components(graph))
        colors = ["skyblue","lightyellow",  "skyblue", "orange", "aliceblue"]
        def find_color(node): 
            for subgraph in subgraphs:
                if node in subgraph: 
                    if  node.CAPACITY > 300:
                        return colors[3]
                    elif  node.CAPACITY > 200:
                        return colors[2]
                    elif  node.CAPACITY > 100:
                        return colors[1]
                    else:    
                        return colors[subgraphs.index(subgraph)]
            return "lightyellow"
        node_colors = map(find_color, graph.nodes())
        plt.figure(figsize=(10, 10))
        nx.draw(graph,
                with_labels=True,
                font_size=7,
                node_size=1300,
                font_family='ubuntu',
                font_color='red',
                node_color=node_colors,
                edge_color='orange',
                width=0.3)
        plt.show(block=False)

    def readFiles(self):
        #nodes.txt => node_id capacity
        #edges.txt => node_id node_id 
        try:
            f = open('nodes.txt','r')
            lines = f.readlines()
            for line in lines:
                content = line.strip().split()
                ID = int(content[0])
                CAPACITY = int(content[1])
                node=Node(ID, CAPACITY)
                self.add(node)  

            f = open('edges.txt','r')
            lines = f.readlines()
            for line in lines:
                content = line.strip().split()
                id1 = int(content[0])
                id2 = int(content[1])
                if self.nodes.has_key(id1) and self.nodes.has_key(id2):
                    node1 = self.nodes[ id1 ]
                    node2 = self.nodes[ id2 ]
                    self.link( node1, node2 )
                else:
                    if not(self.nodes.has_key(id1)):
                        self.log("ERROR: key '%s' is not exist"%(id1) )
                    if not(self.nodes.has_key(id2)):
                        self.log("ERROR: key '%s' is not exist"%(id2) )
            self.log('Files readed successfully..')
        except Exception, error:
            self.log('Files could not read..')
            self.log('ERROR: %s' % error)   
    
    def log(self, message):
        #print("GRAPH:: %s"%(message) )   
        pass
        
    def log_method(self, message):
        print("GRAPH:: %s"%(message) )         