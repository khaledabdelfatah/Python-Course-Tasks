#Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.



sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

new_dict = {}
for key in keys:
    if key in sample_dict:
        new_dict[key] = sample_dict[key]

print(new_dict)
