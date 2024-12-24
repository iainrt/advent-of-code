
def to_int(list: list):
  for i in range(len(list)):
    list[i] = int(list[i])

  return list

def load_data(path: str):
    with open(path) as file:
      data = [
        x.strip()
        for x in file.read().split('\n\n')
      ]
  
    rules = data[0].split('\n')
    instructions = data[1].split('\n')
  
    rules_dict={}
    for i, rule in enumerate(rules):
      rules_dict[i] = rule.split('|')
      to_int(rules_dict[i])
  
    instructions_dict = {}
    for i, instruction in enumerate(instructions):
      instructions_dict[i] = instruction.split(',')
      to_int(instructions_dict[i])
    
    return rules_dict, instructions_dict

# part one

def check_instruction(instruction: list, rule_one: int, rule_two: int):
    """checks whether an instruction meets a rule
    returns True if it does, False if it doesn't"""
  
    if rule_one in instruction and rule_two in instruction:
      rule_one_position = instruction.index(rule_one)
      rule_two_position = instruction.index(rule_two)
      if rule_one_position < rule_two_position:
        return True
      else:
        return False
    else:
      return True

def check_instructions_list(instructions_dict: dict, rules_dict: dict):
    """checks all instructions in a dictionary against a dictionary of rules"""

    rules_count = len(rules_dict)
    output_list = []
    incorrect_output_list = []
    for i in instructions_dict:
      for j in rules_dict:
        if check_instruction(instructions_dict[i], rules_dict[j][0], rules_dict[j][1]):
          if j == (rules_count - 1):
            output_list.append(instructions_dict[i])
          else:
            continue
        else:
          incorrect_output_list.append(instructions_dict[i])
          break

    return output_list, incorrect_output_list

def sum_middle_values(lists: list):

    middle_totals = 0
    for list in lists:
      middle_position = int((len(list)+1)/2)
      middle_value = list[middle_position-1]
      middle_totals = middle_totals + middle_value
    return middle_totals 

# part two

def rearrange_instruction(instruction: list, rule_one: int, rule_two: int):
    """checks if instructions meets a rule and rearranges if not
    returns rearranged instruction and bool True if it was rearranged"""


    if not check_instruction(instruction, rule_one, rule_two):

      position_term_one = instruction.index(rule_one)
      position_term_two = instruction.index(rule_two)
      instruction[position_term_one], instruction[position_term_two] = instruction[position_term_two], instruction[position_term_one]
      rearranged = True

    else:
      rearranged = False

    return instruction, rearranged

def rearrange_instructions_list(incorrect_lists: list, rules_dict: dict):
  """checks all instructions in a list against a dictionary of rules"""

  rearranged_list = []

  for list in incorrect_lists:

    rearranged = True
    while rearranged is True:
    
      for j in rules_dict:
        amended_list, rearranged = rearrange_instruction(list, rules_dict[j][0], rules_dict[j][1])
        if rearranged:
          break
        else:
          continue

  
    rearranged_list.append(amended_list)
      
  return rearranged_list
                   
if __name__ == "__main__":

  test_path = 'input_test.txt'
  main_path = 'input.txt'
  status = 'main'
  
  if status == 'test':
    path = test_path
  else:
    path = main_path
    
  rules, instructions = load_data(path)

  output_list, incorrect_list = check_instructions_list(instructions, rules)
  print('valid lists:', output_list)
  print('incorrect lists:', incorrect_list)
  middle_sum = sum_middle_values(output_list)
  print('Part one solution is:', middle_sum)

  rearranged_list = rearrange_instructions_list(incorrect_list, rules)
  print('rearranged lists:', rearranged_list)
  resorted_middle_sum = sum_middle_values(rearranged_list)
  print('Part two solution is:', resorted_middle_sum)


  # print('rules', rules)
  # print('instructions', instructions)