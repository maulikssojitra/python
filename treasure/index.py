list1 = ["-", "-", "-"]
list2 = ["-", "-", "-"]
list3 = ["-", "-", "-"]
map = [list1, list2, list3]

print("Hiding your treasure! X mark")
position = input()

latter = position[0].lower()
abc = ["a", "b", "c"]
latter_position = abc.index(latter)
number_position = int(position[1]) - 1
map[number_position][latter_position] = "X"

print(f"{list1}\n{list2}\n{list3}")