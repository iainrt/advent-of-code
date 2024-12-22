from typing import List, Tuple

Coordinate = Tuple[int,int]
Letter = str
Wordsearch = dict[Coordinate, Letter]

path = 'input.txt'

def load_wordsearch(path: str):
    
    with open(path) as file:
      grid = [
          line.strip()
          #for x in file.read().split("\n")
          for line in file.readlines()
      ]
    
    wordsearch = {}
    for i, line in enumerate(grid):
        y_max = len(grid)
    
        for j, char in enumerate(line):
            x_max = len(line)
            coordinate = (j,i)
            letter = char
            wordsearch[coordinate] = letter
    
    #print(wordsearch)

    return wordsearch, x_max, y_max

# puzzle part 1

def search_word_E(wordsearch: Wordsearch, x_max: int, y_max: int):
    
    word_count = 0
    for y in range(y_max):    
        for x in range(x_max-3):
            if wordsearch[(x,y)] == 'X' and wordsearch[(x+1,y)] == 'M' and wordsearch[(x+2,y)] == 'A' and wordsearch[(x+3,y)] == 'S':
                word_count += 1
    print(word_count)
    return word_count

def search_word_W(wordsearch: Wordsearch, x_max: int, y_max: int):

    word_count = 0
    for y in range(y_max):    
        for x in range(3,x_max):
            if wordsearch[(x,y)] == 'X' and wordsearch[(x-1,y)] == 'M' and wordsearch[(x-2,y)] == 'A' and wordsearch[(x-3,y)] == 'S':
                word_count += 1
    print(word_count)
    return word_count

def search_word_S(wordsearch: Wordsearch, x_max: int, y_max: int):

    word_count = 0
    for x in range(x_max):    
        for y in range(y_max-3):
            if wordsearch[(x,y)] == 'X' and wordsearch[(x,y+1)] == 'M' and wordsearch[(x,y+2)] == 'A' and wordsearch[(x,y+3)] == 'S':
                word_count += 1
    print(word_count)
    return word_count

def search_word_N(wordsearch: Wordsearch, x_max: int, y_max: int):

    word_count = 0
    for x in range(x_max):    
        for y in range(3,y_max):
            if wordsearch[(x,y)] == 'X' and wordsearch[(x,y-1)] == 'M' and wordsearch[(x,y-2)] == 'A' and wordsearch[(x,y-3)] == 'S':
                word_count += 1
    print(word_count)
    return word_count

def search_word_NE(wordsearch: Wordsearch, x_max: int, y_max: int):

    word_count = 0
    for x in range(x_max-3):    
        for y in range(3,y_max):
            if wordsearch[(x,y)] == 'X' and wordsearch[(x+1,y-1)] == 'M' and wordsearch[(x+2,y-2)] == 'A' and wordsearch[(x+3,y-3)] == 'S':
                word_count += 1
    print(word_count)
    return word_count

def search_word_SE(wordsearch: Wordsearch, x_max: int, y_max: int):

    word_count = 0
    for x in range(x_max-3):    
        for y in range(y_max-3):
            if wordsearch[(x,y)] == 'X' and wordsearch[(x+1,y+1)] == 'M' and wordsearch[(x+2,y+2)] == 'A' and wordsearch[(x+3,y+3)] == 'S':
                word_count += 1
    print(word_count)
    return word_count

def search_word_SW(wordsearch: Wordsearch, x_max: int, y_max: int):

    word_count = 0
    for x in range(3, x_max):    
        for y in range(y_max-3):
            if wordsearch[(x,y)] == 'X' and wordsearch[(x-1,y+1)] == 'M' and wordsearch[(x-2,y+2)] == 'A' and wordsearch[(x-3,y+3)] == 'S':
                word_count += 1
    print(word_count)
    return word_count

def search_word_NW(wordsearch: Wordsearch, x_max: int, y_max: int):

    word_count = 0
    for x in range(3, x_max):    
        for y in range(3, y_max):
            if wordsearch[(x,y)] == 'X' and wordsearch[(x-1,y-1)] == 'M' and wordsearch[(x-2,y-2)] == 'A' and wordsearch[(x-3,y-3)] == 'S':
                word_count += 1
    print(word_count)
    return word_count

wordsearch, x_max, y_max = load_wordsearch(path)
total_count = (search_word_E(wordsearch, x_max, y_max) 
            + search_word_W(wordsearch, x_max, y_max)
            + search_word_N(wordsearch, x_max, y_max)
            + search_word_S(wordsearch, x_max, y_max)
            + search_word_NE(wordsearch, x_max, y_max) 
            + search_word_NW(wordsearch, x_max, y_max)
            + search_word_SE(wordsearch, x_max, y_max)
            + search_word_SW(wordsearch, x_max, y_max)
              )

print('Answer to part 1:', total_count)

# puzzle part 

def search_word_MAS(wordsearch: Wordsearch, x_max: int, y_max: int):

    word_count = 0
    for x in range(1, x_max-1):    
        for y in range(1, y_max-1):
            if wordsearch[(x,y)] == 'A':
                if wordsearch[(x-1,y-1)] == 'M' and wordsearch[(x+1,y+1)] == 'S' and wordsearch[(x+1,y-1)] == 'M' and wordsearch[(x-1,y+1)] =='S':
                    word_count += 1
                elif wordsearch[(x-1,y-1)] == 'M' and wordsearch[(x+1,y+1)] == 'S' and wordsearch[(x+1,y-1)] == 'S' and wordsearch[(x-1,y+1)] =='M':
                    word_count += 1
                elif wordsearch[(x-1,y-1)] == 'S' and wordsearch[(x+1,y+1)] == 'M' and wordsearch[(x+1,y-1)] == 'M' and wordsearch[(x-1,y+1)] =='S':
                    word_count += 1
                elif wordsearch[(x-1,y-1)] == 'S' and wordsearch[(x+1,y+1)] == 'M' and wordsearch[(x+1,y-1)] == 'S' and wordsearch[(x-1,y+1)] =='M':
                    word_count += 1
                else:
                    pass
            else:
                pass

    print(word_count)
    return word_count

part_two = search_word_MAS(wordsearch, x_max, y_max)
print('Answer to part 2:', part_two)
