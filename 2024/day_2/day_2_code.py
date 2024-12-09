import csv

# function to check if a list is safe
def check_if_safe(list):
  previous_difference = None
  for i in range(len(list)-1):

    #print(i, 'out of', len(list)-1)
    difference = list[i+1] - list[i]
    #print(difference)

    if abs(difference) >3:
      #print('difference of ', difference, 'is not safe')
      safe_count = 0
      break
    else:
      if previous_difference == None:
        previous_difference = difference
        #print('First difference')
      elif previous_difference * difference <= 0:
        #print('difference changing sign is not safe')
        safe_count = 0
        break
      else:
        print('next diffence')

    if i == len(list)-2:
      safe_count = 1
      #print('safe')


  return safe_count

with open('input.csv') as csvfile:

  reader = csv.reader(csvfile, delimiter=' ')
  
  list_of_csv = list(reader)

# convert string to integers
for list in list_of_csv:
  for i in range(len(list)):
    list[i] = int(list[i])

# loop through lists to calculate and check differences

safe_counter = 0
for list in list_of_csv:
  #print('Testing list: ', list)
  safe_count = check_if_safe(list)
  safe_counter = safe_counter + safe_count

print("part 1 solution is:", safe_counter)

# part 2
# loop through lists and for any unsafe list remove each list item one by one to check if safe

safe_counter = 0
for list in list_of_csv:
  safe_count = check_if_safe(list)
  if safe_count == 1:
    safe_counter = safe_counter + safe_count
  else:
    for i in range(len(list)):
      new_list = list.copy()
      new_list.pop(i)
      new_safe_count = check_if_safe(new_list)
      if new_safe_count == 1:
        safe_counter = safe_counter + new_safe_count
        break
      else:
        continue

print("part 2 solution is:", safe_counter)
  