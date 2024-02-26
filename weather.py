import random
import json


def generate_data_object():
    weather_data = {
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
    return weather_data


def generate_random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_time():
    hour = str(random.randint(0, 23)).zfill(2)
    minute = str(random.randint(0, 59)).zfill(2)
    return f"{hour}:{minute}"


def main():
    num_objects = int(input("Enter the number of objects: "))

    data_list = [generate_data_object() for _ in range(num_objects)]

    with open("weather.json", "w") as file:
        json.dump(data_list, file, indent=4)

    print(json.dumps(data_list, indent=4))

    print(f"Completed for {num_objects} objects.")


if __name__ == '__main__':
    main()
