# -*- coding: utf-8 -*-
# Test file for node class
# Developer
# Ismail AKBUDAK
# ismailakbudak.com

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from graph import Node

def log(message):
    print("TEST:: %s"%(message))

def log_neighbours(node):
    log("%s neighbors : %s "%(node, str(node.neighbors)) ) 

n1=Node(1,1)
n2=Node(2,2)
n3=Node(3,3)
n4=Node(4,4)
n5=Node(5,5)
n6=Node(6,6)

n1.addNeighbor(n2)
n1.addNeighbor(n3)
n1.addNeighbor(n3) 
n1.addNeighbor(n5)
n1.addNeighbor(n6)

n3.addNeighbor(n2)
n4.addNeighbor(n2)

log_neighbours(n1) 
log_neighbours(n2) 
log_neighbours(n3) 
log_neighbours(n4) 
log_neighbours(n5) 
log_neighbours(n6)    
n1.remove()
log_neighbours(n1) 
log_neighbours(n2) 
log_neighbours(n3) 
log_neighbours(n4) 
log_neighbours(n5) 
log_neighbours(n6) 

if len(n1.neighbors) == 0 and len(n3.neighbors) == 1 and len(n4.neighbors) == 1 :
    log("completed successfully..")
else:
    log("There is something wrong..")

