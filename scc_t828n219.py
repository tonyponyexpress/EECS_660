# Author: Tony Nguyen
# KUID: 2878004
# Class: EECS 660 Algorithms
# Brief: SCC Algorithm with BFS.
import sys
from collections import defaultdict

class Graph:
    def __init__( self, dict, t_nodes ):
        self.Graph = dict
        self.totalNodes = t_nodes
        self.BFSResults = list()

    def BFS( self, source ):
        # Initializations
        discovered = [ False for i in range( self.totalNodes ) ]
        discovered[ 0 ] = True # As soon as search first sees v
        for item in self.Graph[ source ]:
            discovered.append( False )
        L = list()
        BFS = list()
        L.append( [ source ] )
        i = 0

        # Traversals
        for index in range( len( L[ i ] ) ):
            for item in L[ i ]:
                edge = self.Graph[ item ]
                u = int( item )
                v = int( edge[ 0 ] )
                if False == discovered[ v ]:
                    discovered[ v ] = True
                    BFS.append( edge ) # Add the edge to the tree
                    L.append( [ v ] ) # Add v to the list
            i+=1
        self.BFSResults = BFS

def Main():
    File = open( sys.argv[ 1 ], 'r' )
    TotalNodes = int( File.readline() )
    File.readline()
    Edges = defaultdict( list )
    for index in range( TotalNodes ):
        temp = File.readline().split()
        for item in temp:
            Edges[ index + 1 ].append( item )
    G = Graph( Edges, TotalNodes )
    G.BFS( 1 )
    print( G.BFSResults )

# Call to main
Main()
