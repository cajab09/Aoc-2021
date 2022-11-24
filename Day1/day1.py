# naming the file I want to read / providing the path
filename = "/Users/anamanya/GITHUB/Aoc-2021/Day1/input.txt"

#Opening the file
with open(filename) as file:
    # reading lines into a list
    lines = [int(line.rstrip()) for line in file]

#print the list of what I have read.
#print(lines)
increase_count=0
decrease_count=0
for index, value in enumerate(lines):
    #print(f"{index}: {value}")
    if index > 0:
        if value > lines[index-1]:
            #print(f"{value} - (increasing)")
            increase_count=increase_count+1
        else:
            decrease_count=decrease_count+1
            #print(f"{value} - (decreasing)")

print(increase_count)