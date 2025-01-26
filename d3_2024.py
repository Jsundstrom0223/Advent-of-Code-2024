import re

challenge_input = "d3_2024_challenge_input.txt"
test_input = "d3_2024_test_input.txt"
p2_test_input = "d3_p2_2024_test_input.txt"

with open(challenge_input, "r") as input_file:
    instructions = input_file.read() 

def get_valid_instructions(instructions):

    full_valid_set = re.findall("(mul\(\d{1,3},\d{1,3}\))", instructions)
    nums_only = re.findall("(\d{1,3},\d{1,3})", str(full_valid_set))
    total_valid_instructions(nums_only)

def total_valid_instructions(nums):
    total = 0

    for item in nums:
        split_str = item.split(",")
        to_add = int(split_str[0]) * int(split_str[1])
        total += to_add

    print(total)

get_valid_instructions(instructions)
