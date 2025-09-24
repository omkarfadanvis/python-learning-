dict= {"masala":"spicy","ginger":"zesty","green":"Mild"}
# dict["masala"]
# print(dict.get("ginger"))

# dict["green"]="fresh"
# print(dict)

# for x in dict:
#     print(x,dict[x])

for key,value in dict.items():
    print(key,value)    

if "masala" in dict:
    print("yes, 'masala' is a key in the dict")

print(len(dict))

dict["earl grey"] = "Citrus"
print(dict)

dict.pop("ginger")
print(dict)

dict.popitem()
print(dict)

dict_copy =dict.copy()
print(dict_copy)

tea_shop = {
    "chai":{"masala":"spicy","ginger":"zesty","green":"Mild"},
    "coffee":{"espresso":"strong","latte":"milky","cappuccino":"foamy"}
}

print(tea_shop["chai"]["masala"])
print(tea_shop["coffee"]["latte"])

squared_num = {x:x**2 for x in range(10)}
print(squared_num)

squared_num.clear()
print(squared_num)

keys = ['a', 'b', 'c']
values = [1, 2, 3]
new_dict = dict.fromkeys(keys , values)
print(new_dict)

new_dict = dict.fromkeys(keys)
print(new_dict)

default_value="omkar"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)