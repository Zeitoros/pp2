score = float(input())

if (score >= 95 and score <= 100):
    print("Grade: A")
elif (score >= 90 and score <= 94):
    print("Grade: A-")
elif (score >= 85 and score <= 89):
    print("Grade: B+")
elif (score >= 80 and score <= 84):
    print("Grade: B")
elif (score >= 75 and score <= 79):
    print("Grade: B-")
elif (score >= 70 and score <= 74):
    print("Grade: C+")
elif (score >= 65 and score <= 69):
    print("Grade: C")
elif (score >= 60 and score <= 64):
    print("Grade: C-")
elif (score >= 55 and score <= 59):
    print("Grade: D+")
elif (score >= 50 and score <= 54):
    print("Grade: D")
else:
    print("Grade: F")