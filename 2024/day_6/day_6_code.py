from typing import List, Tuple

Coordinate = Tuple[int,int]
Symbol = str
Maze = dict[Coordinate, Symbol]
Direction = str
Guard = Tuple[Coordinate, Direction]

def load_maze(path: str):

  with open(path) as file:
    grid = [
        line.strip()
        for line in file.readlines()
    ]

  maze = {}
  for i, line in enumerate(grid):
      y_max = len(grid)-1

      for j, char in enumerate(line):
          x_max = len(line)-1
          coordinate = (j,i)
          letter = char
          maze[coordinate] = letter

  #print(maze)
  #print(x_max)
  #print(y_max)

  return maze, x_max, y_max

def locate_start(maze: Maze) -> Coordinate:
    """finds starting point of the guard"""
    for coordinate, symbol in maze.items():
        if symbol == '^':
            return coordinate

def add_location(location_list: List, coordinate: Coordinate) -> List:
    """adds a coordinate to a list"""

    if coordinate not in location_list:
      location_list.append(coordinate)
    
    return location_list

def check_coordinate(maze: Maze, coordinate: Coordinate):
    """checks what is in a coordinate"""

    symbol = maze.get(coordinate)
    return symbol

def check_inbounds(coordinate: Coordinate, x_max: int, y_max: int) -> bool:
    """checks for guard leaving maze, returns false when out of bounds"""
    x, y = coordinate

    if x < 0 or x > x_max or y < 0 or y > y_max:
      inbounds = False
    else:
      inbounds = True

    return inbounds
    
def guard_move(maze: Maze, guard: Guard) -> Guard:
    """moves the guard to next location"""

    x, y = guard[0]
    direction = guard[1]

    if direction == 'U':
      y -= 1
      if check_coordinate(maze, (x,y)) == '#':
        direction = 'R'
        y +=1
      else:
        direction = 'U'
      coordinate = (x,y)
      guard = (coordinate, direction)

    elif direction == 'R':
      x += 1
      if check_coordinate(maze, (x,y)) == '#':
        direction = 'D'
        x -=1
      else:
        direction = 'R'
      coordinate = (x,y)
      guard = (coordinate, direction)

    elif direction == 'D':
      y += 1
      if check_coordinate(maze, (x,y)) == '#':
        direction = 'L'
        y -=1
      else:
        direction = 'D'
      coordinate = (x,y)
      guard = (coordinate, direction)

    elif direction == 'L':
      x -= 1
      if check_coordinate(maze, (x,y)) == '#':
        direction = 'U'
        x +=1
      else:
        direction = 'L'
      coordinate = (x,y)
      guard = (coordinate, direction)

    return guard

def part_one(maze: Maze, x_max: int, y_max: int) -> List:
    """finds the number of locations visited by the guard"""
    
    guard = (locate_start(maze),'U')
    location_list = []
    inbounds = check_inbounds(guard[0], x_max, y_max)

    while inbounds:
    
      if guard[0] not in location_list:
        location_list.append(guard[0])

      guard = guard_move(maze, guard)
      inbounds = check_inbounds(guard[0], x_max, y_max)

    print('Part one solution:', len(location_list))
    return location_list

def part_two(maze: Maze, x_max: int, y_max: int, coordinate_list: List):
    """returns the number of locations that can be blocked to make the guard loop"""

    obstacle_list = []
    guard_start = (locate_start(maze),'U')
    i = 0
    
    for coordinate in coordinate_list:
      i +=1
      print('Location:', i,'/', len(coordinate_list))
      test_maze = maze.copy()
      guard = guard_start

      if coordinate == guard[0]:
        continue
      else:
        test_maze[coordinate] = '#'
        inbounds = check_inbounds(guard[0], x_max, y_max)
        visited_list = set()

        while inbounds:
          if guard not in visited_list:
            visited_list.add(guard)
          else:
            obstacle_list.append(coordinate)
            break

          guard = guard_move(test_maze, guard)
          inbounds = check_inbounds(guard[0], x_max, y_max)



    print('Part two solution:', len(obstacle_list))

        


if __name__ == "__main__":

  test_path = 'input_test.txt'
  main_path = 'input.txt'
  status = 'main'
  
  if status == 'test':
    path = test_path
  else:
    path = main_path

  maze, x_max, y_max = load_maze(path)
  location_list = part_one(maze, x_max, y_max)
  part_two(maze, x_max, y_max, location_list)
  