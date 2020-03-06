# Author: Tony Nguyen
# KUID: 2878004
# Class: EECS 660 Algorithms
# Brief: SCC Algorithm with BFS.

import sys
import re
from collections import defaultdict

class Graph:
    def __init__( self, dict, t_nodes ):
        # Initializations
        self.graph = dict
        self.totalNodes = t_nodes
        self.vertices = [ totalnodes for totalnodes in range( 1, self.totalNodes + 1 ) ]
        self.graphRev = self.reverseGraph( self.graph )

    # Using BFS to implement SCC
    def BFS( self, s, g ):
        # Initializations
        discovered = [ False for item in range( self.totalNodes + 1 ) ]
        discovered[ 0 ] = True # As soon as search first sees v
        BFSList = list()
        BFSList.append( [ s ] )
        traversed = set()
        traversed.add( s )
        counter = 0
        # Traversals
        while BFSList[ counter ]:
            BFSList.append( [ ] )
            for u in BFSList[ counter ]:
                Edge = g[ u ]
                for v in Edge:
                    if False == discovered[ int( v ) - 1 ]:
                        discovered[ int( v ) - 1 ] = True
                        if not v in traversed:
                            BFSList[ counter + 1 ].append( v )
                            traversed.add( v )
                        else:
                            pass
            counter += 1
        return BFSList

    # Need the reversed graph to check with 2nd BFS traversal on an arbitrary node.
    def reverseGraph( self, g ):
        revGraph = defaultdict( list )
        for u in list( g ):
            for v in g[ u ]:
                revGraph[ v ].append( u )
        return revGraph

    # The SCC Algorithm
    def SCC( self ):
        scc_list = []
        while ( self.vertices ):
            temp = self.vertices[ 0 ]
            BFSGraph = self.BFS( temp, self.graph )
            reduction = [ item for node in BFSGraph for item in node ]
            BFSGraphRev = self.BFS( temp, self.graphRev )
            reduction2 = [ item for node in BFSGraphRev for item in node ]
            strong_component = [ item for item in reduction if item in reduction2 ]
            scc_list.append( strong_component )
            for item in strong_component:
                self.vertices.remove( item )
        return scc_list

def Main():
    File = open( sys.argv[ 1 ], 'r' )
    TotalNodes = int( File.readline() )
    File.readline()
    Edges = defaultdict( list )
    for item in range( TotalNodes ):
        tempVal = File.readline()
        tempVal2 = re.findall( r"[-+]?\d*\.\d+|\d+", tempVal )
        # If it is empty, leave node alone
        if tempVal2 == []:
            pass
        else:
            for content in tempVal2:
                Edges[ item + 1 ].append( int( content ) )
    g = Graph( Edges, TotalNodes )

    # Finally, print the strongly connected components
    for items in g.SCC():
        items.sort()
        for item in items:
            print( str( item ), end = ' ' )
        print()

# Call to main
Main()
