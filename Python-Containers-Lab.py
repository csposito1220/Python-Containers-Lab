# Exercise 1

students = [
   'Chris', 'Hannah', 'Willow'
]

print(students[1])
print(students[-1])

# Exercise 2

foods = ('pizza', 'chips', 'burgers')

for food in foods:
    print(f"{food} is a good food")

# Exercise 3

for food in foods[-2:]:
    print(food)

# Exercise 4

home_town = {
    'city': 'Atlanta',
    'state': 'GA',
    'population': 55000
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Exercise 5

for key, val in home_town.items():
    print(f"{key} = {val}")

# Exercise 6

cohort = []

for idx, name in enumerate(students):
    cohort.append({
        'student': name,
        'fav-food': foods[idx]
    })

# Exercise 7

awesome_students = [f'{name} is awesome!' for name in students]

# Exercise 8

foods_with_an_a = [food for food in foods if 'a' in food]
print(foods_with_an_a)