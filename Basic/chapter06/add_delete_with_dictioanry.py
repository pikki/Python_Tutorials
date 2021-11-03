user3 = dict(
    name = "Alan",
    email = "a@lan.com",
    age = 56
)

# Add data to dict
user3["favourite_bowler"] = "Ravichandran Ashwin"

del user3['age']
print(user3)

user3.pop("email")
print(user3)

user3.popitem()  # get rid off the last key value pair
print(user3)
