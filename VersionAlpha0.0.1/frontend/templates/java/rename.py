# f = open("Edge1.txt", "r")

with open('Survey.txt', 'r') as f:
    for line in f:
        print("\"",line,"\",")