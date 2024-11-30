def main()
    lines = File.read("day1.txt").split
    sum = compute(lines)
    puts sum
end

def compute(lines)
    ary = Array.new
    for i in 0..lines.length-1
        str = lines[i]
        rev_str = str.reverse
        puts "str is #{str} and rev_str is #{rev_str}"
        number = ''
        for j in 0..str.length-1
            if str[j].match(/[0-9]/)
                number<<str[j]
                print "Adding #{str[j]}       "
                break
            end
        end
        for j in 0..rev_str.length-1
            if rev_str[j].match(/[0-9]/)
                number<<rev_str[j]
                puts "Adding #{rev_str[j]}"
                break
            end    
        end
        ary << number.to_i
        puts "Adding #{number.to_i}"
    end
    sum=0
    #puts ary
    for i in 0..ary.length-1
        sum=sum+ary[i]
    end
    return sum
    #return 0
end

main