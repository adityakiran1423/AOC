import re

def main():
    lines=[]
    sum_one=[]
    # sum_two=[]
    with open("D1P1.txt", "r") as file:
        for i in file:
            line=i.rstrip()
            lines.append(line)
    p_1(lines)
    p_2(lines)

def p_1(lines):
    fs = 0
    sum = []
    numbers = []  # list to contain inly the numbers part of each word
    temp = ""  # string to store the numbers
    for i in range(len(lines)):
        temp = ""
        for char in lines[i]:
            if char.isdigit():
                temp += char
        numbers.append(temp)

    for i in range(len(numbers)):
        temp1 = numbers[i]
        if len(temp1) == 1:
            temp = temp1[0] + temp1[0]
        else:
            temp = temp1[0] + temp1[-1]
        sum.append(temp)
    for i in range(len(sum)):
        fs += int(sum[i])
    print(fs)
    #return sum

def p_2(lines):

    pass

main()

'''
    for i in num_list:
    try:
        i=int(i)
        print(f"Converted {i}")
    except ValueError:
        pass
'''

'''
def parser1(str_val)->str:
    num_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    sorted_keys = sorted(num_dict.keys(), key=len, reverse=True)
    for key in sorted_keys:
        str_val = re.sub(key, num_dict[key], str_val)
    return str_val

def parser2(str_val)->str:
    num_dict = {"eno": "1", "owt": "2", "eerht": "3", "ruof": "4", "evif": "5", "xis": "6", "neves": "7", "thgie": "8", "enin": "9"}
    for key in num_dict:
        str_val = re.sub(key, num_dict[key], str_val)
    return str_val[::-1]

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

def part_two(lines)->None:
    lines1=[]
    lines2=[]
    num_list=[]
    ans=0
    num=''
    for i in range(len(lines)):
        lines1.append(parser1(lines[i]))
        lines2.append(parser2(lines[i][::-1]))
    sum=part_one(lines2)
    
    for i in range(len(lines)):
        line1, line2=reverse(lines1[i]), lines2[i]

    for i in range(len(lines1)):
        if lines1[i]==lines2[i]:
            num_list.append(sum[i])
            print(f"{i+1} Appending {sum[i]}")
        else:
            for j in line2:
                if j.isdigit:
                    num=j
                    for k in line1:
                        if k.isdigit:
                            num+=k
                            num_list.append(num)
                            num=''
                            break
            print(f"{i+1} in else appending {num_list[i]}")
            num=''
    # num_list = [int(i) if i.isdigit() else i for i in num_list]
    # for i in num_list:
    #     if isinstance(i, int):    
    #         ans+=int(i)
    #         print(f"added {i}")
    #     else:
    #         pass
    # print(ans)

    print(f"Length of num list is : {len(num_list)}")
    for i in range(len(lines)):
        print(i+1, lines1[i], lines2[i], num_list[i])
'''


'''
54968
54094
answers from sub
'''
