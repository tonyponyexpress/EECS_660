# Author: Tony Nguyen
# Class: EECS 660: Algorithms
# Date: 4/5/20
# Brief: Performs Kruskal's Algorithm

import sys

class DisjointSet():
    def __init__( self, totalSets ):
        self.dSet = totalSets

    def Find( self, parent, item ):
        if parent[ item ] == item:
            return item
        else:
            return self.Find( parent, parent[ item ] )

    def Union( self, parent, rank, u, v ):
        u_root = self.Find( parent, u )
        v_root = self.Find( parent, v)
        if rank[ u_root ] < rank[ v_root ]:
            parent[ u_root ] = v_root
        elif rank[ u_root ] > rank [ v_root ]:
            parent[ v_root ] = u_root
        else:
            parent[ v_root ] = u_root
            rank[ u_root ] += 1

class Edge():
    def __init__( self, u, v, w ):
        self.edge = tuple ( ( u, v ) )
        self.v1 = u
        self.v2 = v
        self.weight = w

    def getV1( self ):
        return self.v1

    def getV2( self ):
        return self.v2

    # Operator overloading
    def __str__( self ):
        return f"{ self.edge[ 0 ] } {self.edge[ 1 ] }"

    def __lt__( self, RHS ):
        return self.weight < RHS.weight

    def __gt__( self, RHS ):
        return self.weight > RHS.weight

    def __eq__( self, RHS ):
        return self.weight == RHS.weight

def VerticesList( numOfVertices ):
    vertices = list()
    for num in range( numOfVertices ):
        vertices.append( num )
    return vertices

def EdgesList( grid ):
    edges = []
    for row in range( len( grid ) ):
        for col in range ( len ( grid ) ):
            if grid[ row ][ col ] != 0:
                edge = Edge( row, col, grid[ row ][ col ] )
                edges.append( edge )
            else:
                continue
    edges.sort()
    return edges

def PrintHelper( contents ):
    for item in contents:
        print( item )

def Kruskals( edgesList, verticesList ):
    A = list()
    dSet = DisjointSet( verticesList )
    parent = [ item for item in range( len ( verticesList ) ) ]
    rank = [ 0 for item in range( len ( verticesList ) ) ]
    for edge in edgesList:
        if dSet.Find( parent, edge.getV1() ) == dSet.Find( parent, edge.getV2() ):
            continue
        else:
            dSet.Union( parent, rank, edge.getV1(), edge.getV2() )
            A.append( edge )
    return A

def Main():
    file = open( sys.argv[ 1 ], 'r' )
    grid = []
    for line in file:
        numList = line.split()
        nums = [ int( num ) for num in numList ]
        grid.append( nums )
    output = Kruskals( EdgesList( grid ), VerticesList( len ( grid ) ) )
    PrintHelper( output )

# Call to Main
Main()
