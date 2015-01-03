# -*- coding: utf-8 -*-
# Test file for graph and node class
# Developer
# Ismail AKBUDAK
# ismailakbudak.com
# from graph import *; g=Graph(); g.readFiles()
# from graph_test import * 
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from graph import *

def log(message):
    print("TEST:: %s"%(message))
    pass

def log_neighbours(graph):
    for node in graph.nodes.values():
        log("%s neighbours : %s "%(node, str(node.neighbours)) ) 
    if len(graph.nodes) == 0 :
        log("there are not any node")
            
n1=Node(1,6)
n2=Node(2,6)
n3=Node(3,6)
n4=Node(4,6)
n5=Node(5,6)
n6=Node(6,6)
 
g=Graph()
g.add(n1)
g.add(n2)
g.add(n3)
g.add(n4)
g.add(n5)
g.add(n6)

g.link(n1,n2)
g.link(n1,n6) 
g.link(n2,n3) 
g.link(n2,n4) 
g.link(n2,n5) 
g.link(n2,n6) 
log_neighbours(g)
 
g.remove(n1)
log_neighbours(g)

g.add(n1)
g.link(n1,n3) 
g.link(n1,n4) 
g.link(n1,n5) 
g.link(n1,n6) 

log_neighbours(g)  

log_neighbours(g)

g.readFiles() 

if len(n2.neighbours) == 4 and len(n3.neighbours) == 2 and len(n4.neighbours) == 2 :
    log("completed successfully..")
else:
    log("There is something wrong..")
 
