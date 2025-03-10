""" Créez un programme qui affiche la position de l’élément le plus en haut à gauche (dans l’ordre) d’une forme au sein d’un plateau. """

import sys
import os.path


def check_argument(args):
    if len(args) != 2:
        print("Usage: python3 feu02.py board.txt to_find.txt")
        return False
    if not os.path.isfile(args[0]):
        print(f"File {args[0]} is not a valid file")
        return False
    if not os.path.isfile(args[1]):
        print(f"File {args[1]} is not a valid file")
        return False
    return True
    
def read_file(filepath):
    matrix = []
    with open(filepath,'r') as f:
        return  f.read()
def files_content(args):
    board = read_file(args[0])
    to_find = read_file(args[1])
    return (board,to_find)

def find_first(board,to_find):
    current_x = 0
    current_y = 0
    first_chars = []
    for c in board:
        
        if c == to_find[0]:
            first_chars.append((current_x,current_y))
         
        current_x+=1
        if c == "\n":
            current_y+=1
            current_x=0
    return first_chars

def to_matrix(content):
    matrix = []
    for line in content.split("\n"):
        if len(line) > 0 :
            matrix.append(list(line))

    return matrix
def check_pattern(board,first,to_find):
    matrix_board = to_matrix(board)
    height = len(matrix_board)
    width = len(matrix_board[0])
    (first_x,first_y) = first
    coords = []
    
    current_x = 0
    current_y = 0
    for c in to_find:
        if c != ' ' and c != '\n':
            if first_y+current_y < height and first_x+current_x < width:
                if c != matrix_board[first_y+current_y][first_x+current_x]:
                   return None
                else:
                    coords.append((current_x+first_x,current_y+first_y,c))
        current_x+=1
        if c == "\n":
            current_y+=1
            current_x=0 
    return coords
    
def print_pattern(board,coords):
    current_x = 0
    current_y = 0
    for c in board:
        found = False
        for (x,y,char) in coords:
            if current_x == x and current_y == y:
                found = True
                print(char,end="")
        current_x+=1
        if c == "\n":
            current_y+=1
            current_x=0 
        if not found:
            if c == "\n":
                print()
            else:
                print("-",end="")
def main():
    args = sys.argv[1:]
    if check_argument(args):
        board,to_find = files_content(args)
        firsts = find_first(board,to_find)
        for first in firsts:
            coords = check_pattern(board,first,to_find)
            if coords:
                print("Trouvé !")
                print(f"Coordonées: {first[0]},{first[1]}")
                print_pattern(board,coords)
                return
        print("Introuvable")
main()