import random

names = ['Meet', 'Yash', 'jay', 'John', 'Jane', 'mark']
listSize = len(names)
randomPerson = random.randint(0, listSize - 1)
person_who_pay = names[randomPerson]
print(f"{person_who_pay}  will pay the bill.")


print("--------------------------------------------------------------")


# nested List
list1 = ["hello", "bello", "chello"]
list2 = ["nikal", "chall"]
margeList = [list1, list2]
print(margeList[0][1])