# Author: Tony Nguyen
# KUID: 2878004
# Class: EECS_660
# Assignment: Homework 4

import sys
sys.setrecursionlimit( 10 ** 6 )

def MismatchHelper( res1, res2, j ):

    res2 += y[ j - 1 ]
    res1 += '-'
    j -= 1

    return res2, res1, j


def AlignHelper( res1, res2, i, j ):

    res2 += y[ j - 1]
    res1 += x[ i - 1 ]
    i -= 1
    j -= 1

    return res2, res1, i, j


def SkipHelper( res1, res2, i, j ):

    while( i != 0 ):
        res2 += '-'
        res1 += x[ i - 1 ]
        i -= 1

    while( j != 0 ):
        res2 += y[ j - 1 ]
        res1 += '-'
        j -= 1

    return res2, res1, i, j

def DeltaHelper( x, y, j, i ):
    return 1 if x[ j ] != y[ i ] else 0

def getSequence( x, y ):

    res1 = ""
    res2 = ""
    i = len( x )
    j = len( y )
    for iter in range( sys.maxsize ):
        try:
            operation = Dict[ ( i, j ) ]
        except:
            operation = "skip"
        if( operation == "mismatch" ):
            res2, res1, j = MismatchHelper( res1, res2, j )
        elif( operation == "align" ):
            res2, res1, i, j = AlignHelper( res1, res2, i, j )
        elif( operation == "skip" ):
            res2, res1, i, j = SkipHelper( res1, res2, i, j )
            break
        else:
            res1 += x[ i - 1 ]
            res2 += '-'
            i -= 1
    res1 = res1[ :: - 1 ]
    res2 = res2[ :: - 1 ]
    return res1, res2

def Alignment( x, y ):

    arr = [ [ 0 for i in range( len( y ) + 1 ) ] for j in range( len( x ) + 1 ) ]

    for i in range( 1, len( x ) + 1 ):
        arr[ i ][ 0 ] = i
        Dict[ ( 0, i ) ] = "skip"

    for j in range( 1, len( y ) + 1 ):
        arr[ 0 ][ j ] = j
        Dict[ ( j, 0 ) ] = "skip"

    for j in range( 1, len( x ) + 1 ):
        for i in range( 1, len( y ) + 1 ):
            diagonal = arr[ j - 1 ][ i - 1 ] + DeltaHelper( x, y, j - 1, i - 1 )
            top = arr[ j - 1 ][ i ] + 1
            left = arr[ j ][ i - 1 ] + 1
            minVal = min( top, left, diagonal )
            if( minVal == diagonal ):
                Dict[ ( j, i ) ] = "align"
            elif( minVal == top and top == left ):
                Dict[ ( j, i ) ] = "mismatch"
            elif( minVal == top ):
                Dict[ ( j, i ) ] = "insertion"
            else:
                Dict[ ( j, i ) ] = "mismatch"
            arr[ j ][ i ] = minVal

    a = len( x )
    b = len( y )
    result = arr[ a ][ b ]
    return result

if __name__ == "__main__":
    Dict = dict()
    File = open( sys.argv[ 1 ], 'r' )
    x = File.readline().rstrip()
    y = File.readline().rstrip()
    score = Alignment( x, y )
    res1, res2 = getSequence( x, y )
    print( score )
    print( res1 )
    print( res2 )
