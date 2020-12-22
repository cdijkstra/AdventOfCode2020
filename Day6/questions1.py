lines = [line.rstrip() for line in open('data.txt')]

answers = []
answer = ""
for line in lines:
    answer += line
    if not line:
        answers.append(answer)
        answer = ""
answers.append(answer) # Add last entry

sum = 0
for ans in answers:
    sum += len(''.join(set(ans)))
print(sum)