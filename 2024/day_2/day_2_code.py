import csv

with open('input_test.csv') as csvfile:

  reader = csv.reader(csvfile, delimiter=' ')
  
  list_of_csv = list(reader)

# convert string to integers
for list in list_of_csv:
  for i in range(len(list)):
    list[i] = int(list[i])

# loop through lists to calculate and check differences
safe_count = 0
for list in list_of_csv:
  print('Testing list: ', list)

  previous_difference = None
  for i in range(len(list)-1):

    print(i, 'out of', len(list)-1)
    difference = list[i+1] - list[i]
    print(difference)
    
    if abs(difference) >3:
      print('difference of ', difference, 'is not safe')
      break
    else:
      if previous_difference == None:
        previous_difference = difference
        print('First difference')
      elif previous_difference * difference <= 0:
        print('difference changing sign is not safe')
        break
      else:
        print('next diffence')

    if i == len(list)-2:
      safe_count += 1
      print('safe')

  print('safe count is', safe_count)


print("part 1 solution is:", safe_count)