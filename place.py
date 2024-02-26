import random
import json


def generate_place_data_object():
    place_data = {
        "name": generate_random_string(8),
        "latitude": random.uniform(-90, 90),
        "longitude": random.uniform(-180, 180),
        "country_code": generate_random_string(2),
        "continent": generate_random_string(6),
        "elevation": random.randint(0, 5000),
        "timezone": generate_random_string(5),
        "nearest_city": generate_random_string(10),
        "tourism": random.randint(0, 5000),
        "local_language": generate_random_string(6),
        "currency": generate_random_string(3),
        "air_quality_index": random.randint(0, 500),
        "average_temperature": random.randint(-10, 40)
    }
    return place_data


def generate_random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_time():
    hour = str(random.randint(0, 23)).zfill(2)
    minute = str(random.randint(0, 59)).zfill(2)
    return f"{hour}:{minute}"


def main():
    num_objects = int(input("Enter the number of objects: "))

    place_data_list = [generate_place_data_object() for _ in range(num_objects)]

    with open("place.json", "w") as file:
        json.dump(place_data_list, file, indent=4)

    print(json.dumps(place_data_list, indent=4))

    print(f"Completed for {num_objects} objects.")


if __name__ == '__main__':
    main()
