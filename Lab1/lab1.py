import json

data=json.load(
    open("simple_data.json")
)

print(f'Data from Simple JSON:\n{data}')