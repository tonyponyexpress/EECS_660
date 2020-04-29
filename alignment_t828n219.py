# Author: Tony Nguyen
# KUID: 2878004
# Class: EECS_660
# Assignment: Homework 4

import sys
sys.setrecursionlimit(10**6)

def mis_match_operation(result_1, result_2, j):
    result_2 += y[j-1]
    result_1 += '-'
    j -= 1
    return result_2, result_1, j


def align_operation(result_1, result_2, i, j):
    result_2 += y[j-1]
    result_1 += x[i-1]
    i -= 1
    j -= 1
    return result_2, result_1, i, j


def ignore_operation(result_1, result_2, i, j):
    while(i != 0):
        result_2 += '-'
        result_1 += x[i-1]
        i -= 1
    while(j != 0):
        result_2 += y[j-1]
        result_1 += '-'
        j -= 1
    return result_2, result_1, i, j


def retrieve_sequence(x, y):
    result_1 = ""
    result_2 = ""
    i = len(x)
    j = len(y)
    for perm in range(sys.maxsize):
        try:
            direction = dictionary[(i, j)]
        except:
            direction = "ignore"
        if(direction == "mismatch"):
            result_2, result_1, j = mis_match_operation(result_1, result_2, j)
        elif(direction == "align"):
            result_2, result_1, i, j = align_operation(
                result_1, result_2, i, j)
        elif(direction == "ignore"):
            result_2, result_1, i, j = ignore_operation(
                result_1, result_2, i, j)
            break
        else:
            result_1 += x[i-1]
            result_2 += '-'
            i -= 1
    result_1 = result_1[::-1]
    result_2 = result_2[::-1]
    return result_1, result_2


def deltaFormula(x, y, j, i):
    if x[j] != y[i]:
        return 1
    else:
        return 0


def alignment(x, y):
    array_sequence = [
        [0 for i in range(len(y)+1)] for j in range(len(x)+1)]
    # Initialize A[i,0] = i& for each i
    for i in range(1, len(x)+1):
        array_sequence[i][0] = i
        dictionary[(0, i)] = "ignore"
    # Initialize A[0,j] = j& for each j
    for j in range(1, len(y)+1):
        array_sequence[0][j] = j
        dictionary[(j, 0)] = "ignore"
    # recurrence algorithm
    for j in range(1, len(x)+1):
        for i in range(1, len(y)+1):
            diag = array_sequence[j-1][i-1] + deltaFormula(x, y, j-1, i-1)
            top = array_sequence[j-1][i] + 1
            left = array_sequence[j][i-1]+1
            min_value = min(top, left, diag)
            if(min_value == diag):
                dictionary[(j, i)] = "align"
            # prioritize mismatch over insertion!
            elif(min_value == top and top == left):
                dictionary[(j, i)] = "mismatch"
            elif(min_value == top):
                dictionary[(j, i)] = "insertion"
            else:
                dictionary[(j, i)] = "mismatch"
            array_sequence[j][i] = min_value
    # return A[m,n]
    n = len(y)
    m = len(x)
    solution = array_sequence[m][n]
    return solution

def main():
    fileName = sys.argv[1]
    dictionary = dict()
    f = open(fileName, 'r')
    x = f.readline().rstrip()
    y = f.readline().rstrip()
    score = alignment(x, y)
    result_1, result_2 = retrieve_sequence(x, y)
    print(score)
    print(result_1)
    print(result_2)

# Call to Main
main()
