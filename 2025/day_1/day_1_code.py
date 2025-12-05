# Title and Purpose

# Import any modules

# Class, Function and Prodecure definitions

# Main Program
if __name__ == "__main__":
    # All code is idented from here
    # Initialize global 

    with open("input.txt", "r") as file:
        data = file.readlines()
    
    instructions = []
    for item in data:
        adjustment = item.rstrip()
        instructions.append(adjustment)

    dial_position = 50
    zero_counter = 0
    
    # part a
    for item in instructions:
        if item[0] =="R":
            dial_position += int(item[1:])
        else:
            dial_position -= int(item[1:])
        
        dial_position %= 100
        #print(f"Dial position is now {dial_position}")
        if dial_position ==0:
            zero_counter += 1
    print(f"The part A password is {zero_counter}")
    
    # part b
    dial_position = 50
    zero_counter = 0

    for item in instructions:
        direction = item[0]
        amount = int(item[1:])
        for step in range(amount):
            if direction == "R":
                dial_position += 1
            else:
                dial_position -= 1
            
            dial_position %= 100

            if dial_position ==0:
                zero_counter += 1
    
    print(f"The part B password is {zero_counter}")


