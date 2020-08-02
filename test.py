import json

nums = [3, 5, 56, 4, 68, 3, 9, 91, 59]

filename = 'nums.json'
with open(filename, 'w') as f:
    json.dump(nums, f)

filename = 'nums.json'
with open(filename) as fl:
    nums_new = json.load(fl)

print(nums_new)