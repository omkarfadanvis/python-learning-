tea_types = ("Black","green","herbal","oolong")
print(tea_types)
print(tea_types[1])

# tea_types[1] = "white" does not support item assignment 
print(len(tea_types))
more_tea = ("herbal","earl grey")
all_tea = tea_types + more_tea
print(all_tea)

if "green" in all_tea:
    print("yes, green tea is present")

more_tea = ("herbal", "earl grey","herbals")
print(more_tea.count("herbal"))
print(more_tea.count("earl grey"))
print(more_tea.count("herbals"))
print(more_tea.count("Herb"))
print(more_tea.index("earl grey"))

tea_types = ("Black", "Green", "Oolong")
(black, green, oolong) = tea_types
print(black)
print(green)
print(oolong)