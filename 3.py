file = open("input.txt")
final = []
for line in file:
    for idx, char in enumerate(line):
        try:
            check = [char, line[idx + 1], line[idx + 2],
                     line[idx + 3], line[idx + 4], line[idx + 5],
                     line[idx + 5]]
        except IndexError:
            break
        if (check[0].isupper() is True and check[1].isupper() is True
                and check[2].isupper() and check[3].islower() is True
                and check[4].isupper() is True and check[5].isupper() is True
                and check[6].isupper()):
            final.append(check)
print(final)
