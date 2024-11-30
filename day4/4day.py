def main():
    all_numbers = []
    numbers = []
    winning_numbers = []
    with open("D4data.txt", "r") as file:
        for line in file:
            _, cards = line.rstrip().split(": ")
            all_numbers.append(cards)
    for i in range(len(all_numbers)):
        number, winning_number = all_numbers[i].split(" | ")
        numbers.append(number)
        winning_numbers.append(winning_number)
    for i in range(len(numbers)):
        numbers[i].strip()
    for i in range(len(winning_numbers)):
        winning_numbers[i].strip()
    for i in range(len(numbers)):
        numbers[i] = numbers[i].split()

    for i in range(len(winning_numbers)):
        winning_numbers[i] = winning_numbers[i].split()
    compare(numbers, winning_numbers)
    #count_cards(numbers, winning_numbers)


def compare(numbers, winning_numbers):
    append_value, sum1,sum2, count = 1, 0,0, 0
    count_list, numbers_temp, match_list = [], [], []
    for i in range(206):
        count, append_value = 0, 1
        numbers_temp, win_numbers_temp = numbers[i], winning_numbers[i]
        for j in range(len(numbers_temp)):
            if numbers_temp[j] in win_numbers_temp:
                count += 1
        match_list.append(count)
        if count > 1:
            for i in range(count - 1):
                append_value = append_value * 2
            count_list.append(append_value)
        else:
            if count == 1:
                count_list.append(1)
            else:
                count_list.append(0)
    
    for i in range(len(count_list)):
        sum1 += int(count_list[i])
    calc_part_two(match_list) # match_list includes the number of matches in each card 

def calc_part_two(match_list):
    count=[0]*206
    sum, counter=0,1
    for i in range(len(match_list)):
        counter=1
        while counter<=match_list[i]:
            try:
                count[i+counter]+=1
            except IndexError:
                pass
            counter+=1
    print("This was count list")
    for i in count:
        sum+=i
    print(sum)

main()
