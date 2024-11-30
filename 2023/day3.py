def main():
    symbols=[]
    lines=[]
    with open("D3data.txt", "r") as file:
        for line in file:
            temp=line.rstrip()
            lines.append(temp)
    # for i in lines:
    #     line=i
    #     for j in line:
    #         print(j, end='')
    #     print()
    for i in lines:
        line=i
        for j in line:
            if j.isdigit():
                pass
            elif j=='.':
                pass
            elif j=='\n':
                pass
            else:
                if j in symbols:
                    pass
                else:
                    symbols.append(j)
    all_numbers=store_all_numbers(lines)
    check_invalid_numbers(all_numbers, lines, symbols)
    for i in all_numbers:
        print(i)
    '''    
    lines -> test input
    all_part_numbers -> list which stores all the numbers of the test input
    symbols -> list which contains all the symbols
    '''


def store_all_numbers(engine_schematic):
    temp='' #stores the each number and then appends to a list it is a valid number
    all_part_numbers=[]
    for r in range(140):
        temp=''
        for c in range(140):
            if engine_schematic[r][c].isdigit():
                temp+=engine_schematic[r][c]
            else:
                if temp=='':
                    pass
                else:
                    all_part_numbers.append(temp)
                    #print(temp, end='    ')
                temp=''
        #print('\n')
    return all_part_numbers

def check_invalid_numbers(all_numbers, engine_schematic, symbols):
    for r in range(140):
        line=engine_schematic[r]
        for c in range(140):
            ...
            
main()

'''
def calculate_adjacent_elements(number,column_index, row_index, engine_schematic): #function return a list of the adjacent characters
    adjacent_elements=[]
    # appending adjacent left and right elements
    if column_index-1!=0:
        adjacent_elements.append(engine_schematic[row_index][column_index-1])
    adjacent_elements.append(engine_schematic[row_index][column_index+len(number)])
    # appending left and right side corner elements
    if (column_index-1 and row_index-1)!=0:
        adjacent_elements.append(engine_schematic[row_index-1][column_index-1])
    if column_index-1!=0 and row_index+1<140:
        adjacent_elements.append(engine_schematic[row_index+1][column_index-1])
    if row_index-1!=0 and column_index+len(number)<140:
        adjacent_elements.append(engine_schematic[row_index-1][column_index+len(number)])
    if row_index+1 and column_index+len(number)<140:
        adjacent_elements.append(engine_schematic[row_index+1][column_index+len(number)])

    # appending upper and below edge elements
    for i in range(len(number)):
        if row_index-1!=0:
            adjacent_elements.append(engine_schematic[row_index-1][column_index+i])
    for i in range(len(number)):
        if (row_index+1 and column_index+i)<140:
            adjacent_elements.append(engine_schematic[row_index+1][column_index+i])
    return adjacent_elements
'''