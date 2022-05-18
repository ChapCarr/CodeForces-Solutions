# A. Team
solutions = int(input())
score = 0
total_score = 0
for i in range(solutions):
    a, b, c = input().split()
    score = (int(a) + int(b) + int(c))
    if score >= 2:
        total_score = total_score + 1
print(total_score)



