lst1=['car','model','year']
lst2=[{'name':'ankush','class':10},'mahindra',2013]
my_dict=dict()
for key in lst1:
    for value in lst2:
       
        my_dict[key]=value
        lst2.remove(value)
        break
keys ="mouse"
values = "2 bytes"
if keys in my_dict:
    print(my_dict)
else:
    my_dict[keys] = values

print(my_dict)