# -*- coding: utf-8 -*-
# Node and graph implementation
# Developer
# Ismail AKBUDAK
# ismailakbudak.com

from matplotlib import pyplot as plt
import networkx as nx
import random
from collections import OrderedDict
import pprint
pp = pprint.PrettyPrinter(indent=4)

# Node objects for graph structure 
class Node(object): 
    
    def __init__(self, ID, CAPACITY):
        self.ID = ID
        self.CAPACITY = CAPACITY
        self.VISITED = False
        self.NAME = 'N:%s-C:%s'%(str(ID),str(CAPACITY))
        self.COORDINATOR = self
        self.neighbours={}
        self.log("node initialized..")
    
    def __repr__(self):
        return self.NAME

    def __str__(self):
        return self.NAME

    """ 
    Add new node to neighbours
    Args:
        Node object
    Return: 
        Boolean result
        If added True otherwise False   
    """    
    def addNeighbour(self,node):
        if not(self.neighbours.has_key(node.ID)):
            self.neighbours[node.ID]=node
            node.neighbours[self.ID]=self
            self.log("neighbour added..")
            return True
        else:
            self.log("neighbour could not added..")
            self.log("ERROR: key '%s' is exist in '%s'"%(node.ID, self) )
            return False

    """ 
    Remove node from neighbours
    Args:
        Node object
    Return: 
        Boolean result
        If removed True otherwise False   
    """
    def removeNeighbour(self,node):
        if self.neighbours.has_key(node.ID):
            self.neighbours.pop(node.ID)
            node.neighbours.pop(self.ID)
            self.log("neighbour removed..")
            return True
        else:
            self.log("neighbour could not removed..")
            self.log("ERROR: key '%s' is not exist in '%s'"%(node.ID, self) )
            return False


    """ 
    Remove all neighbours
    Args:
        None
    Return: 
        Boolean result
        If removed True otherwise False   
    """         
    def remove(self):
        iterator = self.neighbours.copy()
        for node in iterator.values():
            if not(node.removeNeighbour(self)):
                return False
        self.log("removed all neighbours..")
        return True       

    def log(self, message):
        #print("NODE:: %s"%(message) ) 
        pass

# Graph class
class Graph(object):

    def __init__(self):    
        self.nodes={}
        self.lastID=0
        self.traceGrowth=True
        self.traceElection=True
        self.traceLog=True
        self.traceGrowthVisual=False
        self.traceElectionVisual=True
        self.MAX_CAPACITY=400
        self.number = 0
        self.log("Graph initialized..")  
           
    """ 
    Graph grow method
    Args:
        GOWTH_RATE: remove percantage for grow
        GROWTH_LIMIT: max limit for node numbers in graph
        MAX_CAPACITY: Nodes max capacity 
    Return: 
        None 
    """   
    def grow(self, GOWTH_RATE=10, GROWTH_LIMIT=1000, MAX_CAPACITY=400 ):
        self.MAX_CAPACITY = MAX_CAPACITY
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
                    self.log_grow("ERROR: node could not added in grow method")     
            else:
                #remove node
                if len(self.nodes) > 0: 
                    random_node = random.choice(self.nodes.values())
                    self.deleteRandom(random_node)
                    self.remove(random_node)
                    self.log_grow("node has been removed")
                    length -= 1
            if self.traceGrowthVisual and length > 1:
                self.log_grow("figure : %s"%figure)
                figure += 1        
                self.draw()
        self.log_grow("total nodes length : %s"%str(len(self.nodes))  )
    
    """ 
    Delete random node and after the removing check neighbours' neighbours number  
    Args: 
        random_node: node to be removed
    Return: 
        None 
    """   
    def deleteRandom(self,random_node):
        self.log_grow("")
        self.log_grow("DELETE Start +++++++++++++++++++++++++++++++++++++++++++++++++++++")
        self.log_grow("Started Random Node: %s neighbours : %s "%(random_node, str(random_node.neighbours)) )
        if not(random_node):
            self.log_grow("ERROR: random_node is empty in deleteRandom method")
            return
        if len(random_node.neighbours) > 0:
            for item in random_node.neighbours.values():
                #item.neighbours.pop(random_node.ID)
                length = len(item.neighbours) - 1
                self.log_grow("")
                self.log_grow("=============================================================")
                self.log_grow("neighbours length is %s"%( str(length) ))
                self.log_grow("neighbours Node: %s neighbours : %s "%(item, str(item.neighbours)) )
                if length < 3:
                    #node_neighbour = self.getRandomNode2( item )
                    node_neighbour = self.getRandomNode( item )
                    if node_neighbour:
                        if self.link(item,node_neighbour):
                            self.log_grow("nodes connected to node  ")
                        else:
                            self.log_grow("ERROR-1: nodes could not connected to node  ")    
                    else:
                        self.log_grow("ERROR-2: node is None")
                self.log_grow("=============================================================")
        else:
            self.log_grow("ERROR-0: random_node neighbours is empty in deleteRandom method")
        self.log_grow("DELETE END +++++++++++++++++++++++++++++++++++++++++++++++++++++")
        self.log_grow("") 
 
    """ 
    Add new node to random node and connect with its neighbours
    Args: 
        node: new created node
        random_node: random node to be connected
    Return: 
        None 
    """   
    def linkRandom(self, node, random_node):
        self.log_grow("")
        self.log_grow("Start =======================================================")
        self.log_grow("Started Node : %s neighbours : %s "%(node, str(node.neighbours)) ) 
        if not(random_node):
            self.log_grow("ERROR: random_node is empty in linkRandom method")
            return
        self.log_grow("Started Random Node: %s neighbours : %s "%(random_node, str(random_node.neighbours)) )
        if self.link(node,random_node):
            neighbours = self.getAvailableNeighbours(node, random_node)
            length = len(neighbours)
            self.log_grow("AVAILABLE : %s  "%(str(neighbours)) ) 
            self.log_grow("total node length is %s"%( str(len(self.nodes)) ) )    
            self.log_grow("random_node neighbours length is %s"%( str(length) ) )            
            if length >= 2:
                # Get random node neighbours with randomly
                node_neighbour1 = random.choice(neighbours)
                neighbours.remove(node_neighbour1)
                node_neighbour2 = random.choice(neighbours)
            elif length == 1:
                # Choose random node neighbour Get 1 random node not exist in node neighbours and random node
                node_neighbour1 = neighbours[0]
                node_neighbour2 = self.getRandomNode( node, [node_neighbour1] )
            else: 
                # Get 2 random node not exist in node neighbours and random node
                node_neighbour1 = self.getRandomNode( node )
                node_neighbour2 = self.getRandomNode( node, [node_neighbour1] )
            
            if node_neighbour1:
                if self.link(node,node_neighbour1):
                    self.log_grow("nodes connected to random node  ")
                else:
                    self.log_grow("ERROR-1: nodes could not connected to random node  ")    
            else:
                self.log_grow("ERROR-2: node is None")
            if node_neighbour2:
                if self.link(node,node_neighbour2):
                    self.log_grow("nodes connected to random node  ")
                else:
                    self.log_grow("ERROR-3: nodes could not connected to random node  ")    
            else:
                self.log_grow("ERROR-4: node is None")
        else:
            self.log_grow("ERROR: node could not linked to random_node")
            self.remove(node) 
        self.log_grow("END =======================================================")
        self.log_grow("") 

    """ 
    Get availale neighbours and  remove common neighbours created from random neighbours     
    Args: 
        node: new created node
        random_node: random node to be connected
    Return: 
        Node objects array 
    """ 
    def getAvailableNeighbours(self, node, random_node): 
        neighbours = random_node.neighbours.values()    
        forbidden_values = node.neighbours.values() # this code is geting random_node
        forbidden_values.append(node) 
        self.log_grow("AVAILABLE -- forbidden values are %s"%(str(forbidden_values))) 
        for value in forbidden_values:
            if value in neighbours:
                neighbours.remove(value) 
        return neighbours 

    """ 
    Get random node from graph that is not connected before  
    Args: 
        node: new created node
        nodes: forbidden nodes array
    Return: 
        Node object 
    """ 
    def getRandomNode(self, node, nodes=[]): 
        forbidden_values = node.neighbours.values()
        forbidden_values.append(node)
        for item in nodes:
            forbidden_values.append(item) 
        total_values = self.nodes.values()
        self.log_grow("First -- forbidden values are %s"%(str(forbidden_values)))
        self.log_grow("First AVAILABLE -- nodes are %s"%(str(total_values)))
        for value in forbidden_values:
            if value in total_values:
                total_values.remove(value)
        self.log_grow("Second -- forbidden values are %s"%(str(forbidden_values)))
        self.log_grow("Second AVAILABLE -- nodes are %s"%(str(total_values)))
        if len(total_values) > 0:
            new_random_node = random.choice(total_values)
            self.log_grow("LAST AVAILABLE : %s  "%(str(new_random_node)) ) 
            return new_random_node    
        else:
            self.log_grow("ERROR-0: there is no node for neighbour")
            return None     
    """ 
    Add new node to graph 
    Args: 
        node: new node that will add
    Return: 
        Boolean if added True otherwise False
    """ 
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
    
    """ 
    Remove node from graph
    Args: 
        node: new node that will remove
    Return: 
        None
    """ 
    def remove(self, node):
        node.remove()
        self.nodes.pop(node.ID)
        self.log("node removed..")        
    
    """ 
    Remove all graph nodes 
    Args: 
        None
    Return: 
        None
    """ 
    def removeAll(self):
        self.nodes = {}
        self.lastID=0 
        self.log("all nodes removed..")
    
    """ 
    Connect to nodes eachother
    Args: 
        node1: node object
        node2:  nodes object
    Return: 
        None
    """
    def link(self,node1,node2):
        if node1.addNeighbour(node2):
            self.log("nodes linked..")
            return True
        else:
            return False     
    
    """ 
    Start election algorithm on graph
    Args: 
        start: node object that is start point 
    Return: 
        None
    """
    def startElection(self,start):
        self.log_election("BEGIN election =============================")
        self.log_election("start node : "+ str(start))
        self.log_election("END election =============================")
        graph = self.nodes
        visited = {}
        visited_index = {} 
        queue = [start] 
        while queue:
            vertex = queue.pop(0)  
            visited[vertex] = []
            visited_index[vertex.ID] = []
            vertex.VISITED = True 
            for node in  vertex.neighbours.values(): 
                if not(node.VISITED):
                    visited[vertex].append(node)
                    visited_index[vertex.ID].append(node.ID)
                    queue.append( node )  
                    node.VISITED = True

        self.log_pp( "Graph visit path", visited_index,  self.traceElection  ) 

        coordinator_candidates = self.findMaxArray(visited, start, [start])
        
        coordinator = self.findMax(visited, start, start)
        self.log_election("====================================")
        self.log_election("One coordinator result: " + str(coordinator) )
        self.log_election("====================================")
        
        coordinator = random.choice(coordinator_candidates)
        if self.traceElectionVisual:
            self.draw()
            self.draw_node(coordinator, coordinator_candidates)
        self.log_election("====================================")
        self.log_election("Election result : " + str(coordinator_candidates) )
        self.log_election("====================================")
        self.log_election("Coordinator : " + str(coordinator) )
        self.log_election("====================================")
        self.log_election("First status for nodes coordinator")
        self.log_election("====================================")
        self.print_coordinator()
        self.informCoordinator(visited, start, coordinator)
        self.log_election("====================================")
        self.log_election("After inform coordinator to nodes ")
        self.log_election("====================================")
        self.print_coordinator()   
    
    """ 
    Print nodes coordinator
    Args:
        None  
    Return: 
        None
    """      
    def print_coordinator(self):
        for node in self.nodes.values():
            self.log_election(" %s -> %s " % (str(node), str(node.COORDINATOR)) )    
        
    """ 
    Find nodes that has maximum capacity
    Args: 
        visited: graph find path
        start: start point node object 
        max: array of node that has maximum capacity
    Return: 
        Node objects array
    """        
    def findMaxArray(self,visited,start,max=None):   
        if len(visited[start]) == 0:
            if max[0].CAPACITY > start.CAPACITY:
                return max
            elif max[0].CAPACITY == start.CAPACITY:
                if start not in max:
                    max.append(start)
                return max            
            else:    
                return [start]
        if max[0].CAPACITY < start.CAPACITY:
                max = [start]         
        elif max[0].CAPACITY == start.CAPACITY:
            if start not in max:
                max.append(start) 
        for node in visited[start]:
            val = self.findMaxArray(visited,node, max) 
            if max[0].CAPACITY < val[0].CAPACITY:
                max = val         
            elif max[0].CAPACITY == val[0].CAPACITY:
                for node in val:
                    if node not in max:
                        max.append(node)               
        return max   

    """ 
    Find node that has maximum capacity
    Args: 
        visited: graph find path
        start: start point node object 
        max:  node that has maximum capacity
    Return: 
        Node object
    """    
    def findMax(self,visited,start,max=None):  
        if len(visited[start]) == 0:
            if max.CAPACITY > start.CAPACITY:
                return max
            elif max.CAPACITY == start.CAPACITY:
                vals = [max,start]
                return random.choice(vals)        
            else:    
                return start
        if max.CAPACITY < start.CAPACITY:
            max = start         
        elif max.CAPACITY == start.CAPACITY:
            vals = [max,start]
            max = random.choice(vals)  
        for node in visited[start]:
            val = self.findMax(visited,node, max) 
            if max.CAPACITY < val.CAPACITY:
                max = val         
            elif max.CAPACITY == val.CAPACITY:
                vals = [max,val]
                max = random.choice(vals)                 
        return max

    """ 
    Inform  coordinator to all nodes 
    Args: 
        visited: graph find path
        start: start point node object 
        coordinator:  node that is new coordinator
    Return: 
        Node object
    """
    def informCoordinator(self, visited, start, coordinator):
        #self.log_election( str(self.number) + " nodes coordinator")
        #self.number += 1
        #self.print_coordinator()
        if len(visited[start]) == 0:
            start.COORDINATOR = coordinator
            return True
        start.COORDINATOR = coordinator  
        for node in visited[start]:
            self.informCoordinator(visited,node, coordinator) 
        return True

    """ 
    Draw all nodes with CAPACITY property
    Args: 
        MAX_CAPACITY: max capacity for color index
    Return: 
        None
    """
    def draw(self ):
        colors = ["#EFDFBB","orange","lightgreen","lightblue","#FFD300","violet","yellow","#7CB9E8","#E1A95F", "#007FFF","#CCFF00","pink","cyan"]
        length = len(colors) - 1
        # division by zero
        if length >= self.MAX_CAPACITY:
            length = self.MAX_CAPACITY
        amount = self.MAX_CAPACITY / length
        def find_color(node):
            index = node.CAPACITY/amount
            if index > length:
                index = length 
            return colors[index]

        graph = nx.DiGraph()
        for node in self.nodes.values():
            graph.add_node(node)
            for node_neighbour in node.neighbours.values():
                graph.add_edge(node, node_neighbour, color=find_color(node_neighbour) )
        node_colors = map(find_color, graph.nodes())

        if len(self.nodes) > 1:
            edges,edge_colors = zip(*nx.get_edge_attributes(graph,'color').items()) 
        else:
            edges=[]
            edge_colors="yellow"    
        plt.figure(figsize=(10, 10))
        nx.draw(graph,
                with_labels=True,
                font_size=7,
                node_size=1300,
                font_family='ubuntu',
                font_color='red',
                node_color=node_colors, 
                edgelist=edges,
                edge_color=edge_colors, 
                width=0.4)
        
        y=1.13;i=1; flag=False 
        for color in colors:
            if i <= length:
                text =  "%s <= CAPACITY < %s"%(str((i-1) * amount), str(i * amount))
            else: 
                text =  "%s <= CAPACITY  "%(str((i-1) * amount) )
                flag=True
            plt.text(-0.18, y, text, bbox=dict(facecolor=color, alpha=0.5))
            if flag:
                break
            y-=0.033; i+=1
        plt.show(block=False) 


    """ 
    Draw coordinator and coordinator candidates
    Args: 
        coordinator: coordinator node
        coordinator_candidates: node objects array
    Return: 
        None
    """
    def draw_node(self, coordinator, coordinator_candidates):
        coordinator_colors = ["orange", "yellow", "skyblue"]  
        def find_coordinator_color(node):
            if node.ID == coordinator.ID:
                return coordinator_colors[0]
            if node in coordinator_candidates:
                return coordinator_colors[1]
            return coordinator_colors[2] 

        graph = nx.DiGraph()
        for node in self.nodes.values():
            graph.add_node(node)
            for node_neighbour in node.neighbours.values():
                graph.add_edge( node, 
                                node_neighbour,  
                                coordinator_color=find_coordinator_color(node_neighbour) )
        node_coordinator_colors = map(find_coordinator_color, graph.nodes()) 
        coordinator_edges,coordinator_edge_colors = zip(*nx.get_edge_attributes(graph,'coordinator_color').items()) 
        plt.figure(figsize=(10, 10))
        nx.draw(graph,
                with_labels=True,
                font_size=7,
                node_size=1300,
                font_family='ubuntu',
                font_color='red',
                node_color=node_coordinator_colors, 
                edgelist=coordinator_edges,
                edge_color=coordinator_edge_colors, 
                width=0.4)
        
        y=1.13; flag=False 
        for color in coordinator_colors:
            if color == coordinator_colors[0]:
                text = "Coordinator"
            elif color == coordinator_colors[1]: 
                text = "Coordinator candidate"
            else:  
                text = "Normal nodes" 
            plt.text(-0.18, y, text, bbox=dict(facecolor=color, alpha=0.5))
            y-=0.033 
        plt.show(block=False) 

    """ 
    Read nodes and edges from file 
    Args: 
        None
    Return: 
        None
    """
    def readFiles(self):
        #nodes.txt => node_id capacity
        #edges.txt => node_id node_id 
        try:
            f = open('nodes.txt','r')
            lines = f.readlines()
            for line in lines:
                content = line.strip().split()
                if len(content) == 2:
                    ID = int(content[0])
                    CAPACITY = int(content[1])
                    node=Node(ID, CAPACITY)
                    self.add(node)  

            f = open('edges.txt','r')
            lines = f.readlines()
            for line in lines:
                content = line.strip().split()
                if len(content) == 2:
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
        if self.traceLog:  
            print("GRAPH:: %s"%(message) )

    def log_pp(self, message, array, is_write ):
        if is_write:
             print("GRAPH:: %s"%(message) )
             pp.pprint(array) 

    def log_grow(self, message):
        if self.traceGrowth:  
            print("GRAPH GROW:: %s"%(message) )

    def log_election(self, message):
        if self.traceElection:  
            print("GRAPH ELECTION:: %s"%(message) )                