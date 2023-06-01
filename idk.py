x = "0010"

duplicate_counter = 0
zero_counter = 0
one_counter = 0

start = None

result = ""

seen_opposite = False

seen = []
for digit in range(len(x)):
    seen = []
    result = ""
    for inc in range(digit, len(x)):
        start = x[digit]
        start = x[digit]
        seen.append(x[inc])

        if x[inc]!=start:
            seen_opposite=True
        if x[inc]==start and seen_opposite==True:
            if zero_counter==one_counter:
                duplicate_counter+=1
            continue
        if x[inc] == '0':
            zero_counter+=1
        elif x[inc] =='1':
            one_counter+=1
        result+=x[inc]
print(duplicate_counter)