import json
with open('input.json', 'r') as file:
    data = json.load(file)

# TODO решите задачу
def task(data) -> float:
    x = 0
    x = sum([item['score'] * item ['weight'] for item in data])
    return round(x, 3)


print(task(data))
