alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
letter_to_num = {letter: i + 1 for i, letter in enumerate(alphabet)}
num_to_letter = {i + 1: letter for i, letter in enumerate(alphabet)}
to_change = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
to_change = "map"
output = ""
for i in to_change:
    try:
        shift = letter_to_num[i] + 2
    except: 
        output += i
        continue
    if shift < 1:
        shift += 26
    elif shift > 26:
        shift -= 26
    output += f"{num_to_letter[shift]}"
print(output)
