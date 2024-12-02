def main()
	lines = File.read("day1.txt").split
	parser(lines)
	# sum = compute(l)
	# puts sum
end

def parser(lines)
	puts "called parser"
	dict={
		"one" => "1",
		"two" => "2",
		"three" => "3",
		"four" => "4",
		"five" => "5",
		"six" => "6",
		"seven" => "7",
		"eight" => "8",
		"nine" => "9" 
	}
	for i in 0..lines.length-1
	str = lines[i]
	puts "for #{str}"
		for j in 0..str.length-1
			case str[j].downcase

			when "o"
				if str[j][j,3] == "one"
					str[j].sub('one', dict)
				end
			
			when "t"
				if str[j][j,3] == "two"
					str[j].sub('two', dict)
				end
				if str[j][j,4] == "three"
					str[j].sub('three', dict)
				end
			
			when "f"
				puts "in f block for #{str[j,4]}"
				if str[j][j,4] == "four"
					puts "before sub #{str[j]}"
					str[j].sub('four', dict)
					puts "after sub #{str[j]}"
				end
				if str[j][j,4] == "five"
					str[j].sub('five', dict)
				end
			
			when "s"
				puts "in s block for #{str[j,5]}"
				if str[j][j,3] == "six"
					str[j].sub('six', dict)
				end
				if str[j][j,5] == "seven"
					puts "before sub #{str[j]}"
					str[j].sub('seven', dict)
					puts "after sub #{str[j]}"
				end

			when "e"
				if str[j][j,5] == "eight"
					str[j].sub('eight', dict)
				end

			when "n"
				if str[j][j,4] == "nine"
					str[j].sub('nine', dict)
				end

			else
				# continue
			end
		end
	end
	#puts lines
	puts "leaving parser"
	#return lines
end

def compute(lines)
    ary = Array.new
    for i in 0..lines.length-1
        str = lines[i]
        rev_str = str.reverse
        # puts "str is #{str} and rev_str is #{rev_str}"
        number = ''
        for j in 0..str.length-1
            if str[j].match(/[0-9]/)
                number<<str[j]
                # print "Adding #{str[j]}       "
                break
            end
        end
        for j in 0..rev_str.length-1
            if rev_str[j].match(/[0-9]/)
                number<<rev_str[j]
                # puts "Adding #{rev_str[j]}"
                break
            end    
        end
        ary << number.to_i
        # puts "Adding #{number.to_i}"
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
