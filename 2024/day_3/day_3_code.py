import re

with open('input.txt', 'r') as file:
  data = file.read()


# function for part 1
def product_sum_calc(input):
  
  regex = r"mul\(\d{1,3},\d{1,3}\)"
  match_list = re.findall(regex, input)
  product_sum = 0
  
  for calc in match_list:
      
    integers = re.findall(r"\d{1,3}", calc)
    product = int(integers[0]) * int(integers[1])
    product_sum = product_sum + product

  return product_sum
  
  #print("The answer to part 1 is", product_sum)

# part 2

regex_do = r"do\(\)"
do_split = re.split(regex_do, data)
#print(do_split)

do_list = []

for item in do_split:
  regex_dont = r"don't\(\)"
  dont_split = re.split(regex_dont, item)
  do_list.append(dont_split[0])
  #print(dont_split)

#print(do_list)

product_sum = 0

for item in do_list:

  new_product_sum = product_sum_calc(item)
  product_sum = product_sum + new_product_sum

print(product_sum)
  



