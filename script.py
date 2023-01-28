# Exercise 1
# Create a list named studentscontaining some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

studentscontaining = ["Jay", "Andy", "Jonathan", "Megan"]
# print(studentscontaining[-1])

# Exercise 2
# Create a tuple named foodscontaining the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".

foodscontaining = ("Pizza", "Burger", "Fries", "Shakes")
# print(type(foodscontaining))
# foodlist=[]
# for f in foodscontaining:
# 	foodlist.append(f"{f} is a good food")
# 	print(f"{f} is a good food" )
# print(foodlist)
	


# Exercise 3
# Using a forloop, print just the last two food strings from foods.
# for f in foodlist:
# 	print(foodlist[:-2])


# Exercise 4
# Create a dictionary named home_towncontaining the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_towncontaining = {
	"city":"Los Angeles",
	"state": "California",
	"population":"3.8 M"
}
print(f'I was born in {home_towncontaining["city"]}, {home_towncontaining["state"]} - {home_towncontaining["population"]} of population')

# Exercise 5
# Iterate over the key: value pairs in home_townand print a string for each item, for example:
# 	"city = Arcadia"
# 	"state = California"
# 	"population = 58000"

# for key,value in home_towncontaining.items():
#   print(f'"{key} = {value}"')



# Exercise 6
# Create an empty list named cohort.
# Using a forloop, add one dictionary to the cohortlist for each student name. Each dictionary should have this shape:
# {
# 	'student': 'Tina',
# 	'fav_food': 'Cheeseburger'
# }
# Iterate over cohort printing out each element.

cohort =[]
cohortlist={}
for i in studentscontaining:
	for f in foodscontaining:
		cohortlist["student"] = i
		cohortlist["fav-food"]= f
	print(cohortlist)


# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.

awesome_students = []
for i in studentscontaining:
	awesome_students.append(f'{i} is awesome')
print(awesome_students)

# Exercise 8
# Using the tuple foods and list comprehension within a forloop, 
# print each food string that contains the letter a.

for i in foodscontaining:
	if 'a' in i:
		print(f"food containing a: {i} ")

