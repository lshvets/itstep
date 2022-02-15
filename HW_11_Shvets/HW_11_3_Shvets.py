s = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you.'
spe = '!?.'
count_spe = 0
for i in range(len(s)):
    a = s[i]
    for q in range(len(spe)):
        if a == spe[q]:
            count_spe = count_spe + 1
print(count_spe)

