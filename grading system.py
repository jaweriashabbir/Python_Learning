"""
1) and (if both conditions are true it executes the statements)
2)or (if any conditions among  the two are true it executes the statements)
"""
score = int(input('Enter your score:'))
if (score >= 90) and (score <= 100):
    print('grade:A')
elif (score >= 80) and (score <= 89):
    print("grade:B")
elif (score >= 70) and (score <= 79):
    print("grade:C")
elif (score >= 60) and (score <= 69):
    print("grade:D")
elif (score < 60) and (score >= 0):
    print("Fail")
elif (score > 100) or (score < 0):
    print("Invalid range")
