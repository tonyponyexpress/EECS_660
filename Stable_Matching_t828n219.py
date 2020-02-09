# Author: Tony Nguyen
# KUID: 2878004
# Class: EECS 660 Algorithms
# Brief: Performs the stable matching algorithm.

import sys

class Man:
    def __init__( self, aList ):
        self.isFree = True # All men start forever alone
        self.preference = aList
        self.partner = -1

class Woman:
    def __init__( self, aList ):
        self.isFree = True # All women start forever alone
        self.preference = aList
        self.partner = -1

# Parses input text file, then calls the stable matching function and prints the results.
def Main():
    file = open( sys.argv[ 1 ], 'r' )
    values = file.readline()
    totalMenAndWomen = int( values )
    menPreferences = [ None ] * totalMenAndWomen
    womenPreferences = [ None ] * totalMenAndWomen

    file.readline() # Skip empty line.

    for man in range( totalMenAndWomen ):
        menPreferences[ man ] = []
        women = file.readline()
        menPreferences[ man ] = women.split( "," )
        preferences = []
        for i in menPreferences[ man ]:
            preferences.append( int( i ) )
        menPreferences[ man ] = preferences

    file.readline() # Skip empty line.

    for woman in range( totalMenAndWomen ):
        womenPreferences[ woman ] = []
        men = file.readline()
        womenPreferences[ woman ] = men.split( "," )
        preferences = []
        for i in womenPreferences[ woman ]:
            preferences.append( int( i ) )
        womenPreferences[ woman ] = preferences

    Stable_Matching( totalMenAndWomen, menPreferences, womenPreferences )

def Stable_Matching( totalMenAndWomen, menPreferences, womenPreferences ):
    men = []
    women = []
    for person in range( totalMenAndWomen ):
        men.append( Man( menPreferences[ person ] ) )
        women.append( Woman( womenPreferences [ person ] ) )
    marriedMen = 0

    while marriedMen < totalMenAndWomen:
        for man in range( totalMenAndWomen ):
            if men[ man ].isFree:
                highestWoman = men[ man ].preference[ 0 ] - 1 # Highest ranked woman
                men[ man ].preference.pop( 0 )
                if women[ highestWoman ].isFree:
                    men[ man ].partner = highestWoman
                    men[ man ].isFree = False
                    women[ highestWoman ].partner = man
                    women[ highestWoman ].isFree = False
                    marriedMen += 1
                else:
                    manPrime = women[ highestWoman ].partner
                    if women[ highestWoman ].preference.index( man + 1 ) > women[ highestWoman ].preference.index( manPrime + 1 ):
                        pass
                    else:
                        men[ man ].partner = highestWoman
                        men[ man ].isFree = False
                        women[ highestWoman ].partner = man
                        women[ highestWoman ].isFree = False
                        men[ manPrime ].isFree = True
                        men[ manPrime ].partner = -1

    for man in range( totalMenAndWomen ):
        print( str( man + 1 ) + ", " + str( men[ man ].partner + 1 ) )

Main()
