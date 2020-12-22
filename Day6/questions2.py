lines = [line.rstrip() for line in open('data.txt')]

answers = []
answer = []
for line in lines:
    if not line:
        answers.append(answer)
        answer = []
        continue
    answer.append(line)
answers.append(answer) # Add last entry

sum2 = 0
for ans in answers:
    sum2 += len(set(ans[0]).intersection(*ans))
print(sum2)