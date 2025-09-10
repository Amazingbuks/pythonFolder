studentName=input("What is your name: ")
storylineRating=int(input("Enter rating storyline score: "))
actingRating=int(input("Enter rating acting score: "))
soundtrackRating=int(input("Enter rating soundtrack score"))
averageRating=(storylineRating+actingRating+soundtrackRating)/3
print("averageRating for " + studentName,  averageRating)