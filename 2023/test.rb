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

str = "nine9ninesix6xmgbsgfmpgxkzgpzlxqnjsqhr"

for j in 0..str.length
  if str[j,3] == "six"
	puts "in if"
	t=str[j]
    t.sub('six', dict)
  end
end

puts str