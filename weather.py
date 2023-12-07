import random
import json


def generate_data_object():
    data = {
        "location": generate_random_string(8),
        "temperature": random.randint(-30, 40),
        "humidity": random.randint(0, 100),
        "wind_speed": random.randint(0, 50),
        "description": generate_random_string(12),
        "sunrise": generate_random_time(),
        "sunset": generate_random_time(),
        "pressure": random.randint(900, 1100),
        "visibility": random.randint(1, 20),
        "rainfall": random.randint(0, 50)
    }
    return data

def generate_random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_time():
    hour = str(random.randint(0, 23)).zfill(2)
    minute = str(random.randint(0, 59)).zfill(2)
    return f"{hour}:{minute}"

num_objects = int(input("Enter the number of objects: "))

data_list = []
for _ in range(num_objects):
    data_list.append(generate_data_object())

# to file
with open("json_test.json", "w") as file:
    json.dump(data_list, file, indent=4)

# to console
print(json.dumps(data_list, indent=4))

print("done for", num_objects, "objects")