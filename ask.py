studentName=input("What is the student name: ")
mathScore=int(input("Enter maths score: "))
scienceScore=int(input("Enter science score: "))
englishScore=int(input("Enter english score: "))
averageScore=(mathScore+scienceScore+englishScore)/3
print("averageScore for " + studentName, averageScore)