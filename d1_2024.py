import re

challenge_input = "d1_2024_challenge_input.txt"
test_input = "d1_2024_test_input.txt"

with open(challenge_input, "r") as input_file:
    raw_location_lists = input_file.readlines() 

def prep_lists(location_lists):
    location_list1 = []
    location_list2 = []

    for line in location_lists:
        nums_only = re.findall(r"\d+", line)
        location_list1.append(int(nums_only[0]))
        location_list2.append(int(nums_only[1]))
    
    location_list1.sort()
    location_list2.sort()

    return location_list1, location_list2

def get_total_distance(list1, list2):
    totals = []
    
    for item in zip(list1, list2):
        totals.append(abs(item[0] - item[1]))
    
    return sum(totals)

def get_similarities(list1, list2):
    similarity_scores = []

    for item1 in list1:
        item1_count = list2.count(item1)
        similarity_scores.append(item1 * item1_count)

    return sum(similarity_scores)

def main():
    location_list1, location_list2 = prep_lists(raw_location_lists)
    total_distance = get_total_distance(location_list1, location_list2)
    print(f"The total distance between lists 1 and 2 is {total_distance}!")

    total_similiarity_score = get_similarities(location_list1, location_list2)
    print(f"The total similarity score is {total_similiarity_score}!")

if __name__ == "__main__":
    main()
