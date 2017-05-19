#! python 3
#! CH4_comma_code.py
def convert_list_to_string(words):
    print ('{}, and {}'.format(', '.join(words[:-1]), words[-1]))

list1 = []

for items in range(0,5):
    items = input()
    list1.append(items)
print (list1)

convert_list_to_string(list1)
