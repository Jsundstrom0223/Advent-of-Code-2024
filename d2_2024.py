challenge_input = "d2_2024_challenge_input.txt"
test_input = "d2_2024_test_input.txt"

with open(challenge_input, "r") as input_file:
    raw_data = input_file.readlines() 

stripped_data = [r.rstrip().split(" ") for r in raw_data]
clean_data = [[int(x) for x in l] for l in stripped_data]

 
def check_safety(data):
    counter = 0

    for report in data:
        ascending = sorted(report)
        descending = sorted(report, reverse=True)
        safe = True

        if ascending == report or descending == report:
            for i, level in enumerate(report):
                if i != len(report) - 1:
                    if abs(level - report[i + 1]) < 1 or abs(level - report[i + 1]) > 3:
                        safe = False
                        break
            if safe:
                counter +=1
    return counter
                
safe_reports = check_safety(clean_data)
print(f"There are {safe_reports} safe reports.")