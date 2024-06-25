''' 
Completes the following steps of small task:
. Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
. Mention Variable of Total Marks and assign 300 to it
. Calculate Percentage

'''

englishMarks = 98
islamiatMarks = 96
mathsMarks = 99
marksObtained = englishMarks + islamiatMarks + mathsMarks
totalMarks = 300
percentage = round(marksObtained / totalMarks * 100,2)

print(f"English Marks : {englishMarks}")
print(f"Islamiat Marks : {islamiatMarks}")
print(f"Maths Marks : {mathsMarks}")
print(f"Marks Obtained : {marksObtained} Out of : {totalMarks}")
print(f"Percentage : {percentage}") 