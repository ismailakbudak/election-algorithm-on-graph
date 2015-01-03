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

def log_neighbours(graph):
    for node in graph.nodes.values():
        log("%s neighbours : %s "%(node, str(node.neighbours)) ) 
    if len(graph.nodes) == 0 :
        log("there are not any node")

g=Graph()  
g.traceGrowth = False
g.traceLog = True
g.traceElection = True
g.traceElectionVisual = True

g.readFiles()

#log_neighbours(g) 

g.grow( 10, 20, 9 )

node = random.choice(g.nodes.values())
g.startElection(node)
 

input("TEST:: sonlandırmak için enter a basınız..") 
