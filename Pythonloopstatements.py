#THE RANGE
#Task1 
#Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.
#Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."

import random
moods = ["happy", "sad", "cranky", "excited", "calm", "angry","hangry"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday","Sunday"]
day=  range(7)
mood=random.shuffle(moods)
for day in days:
    for mood in moods:
        print(f"On {day} were you feeling {mood}?")





#======================================2. Double Scoop with Nested Loops==================================================================
#Task 1
#Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.
#Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"


time= ["morning", "afternoon", "night"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday","Sunday"]
moods = ["happy", "sad", "cranky", "excited", "calm", "angry","hangry"]
mood= random.shuffle(moods)
time_of_day= range(3)


for days in day:
     for mood in moods:
        for time_of_day in time:

          print(f"On {day} {time_of_day} were you feeling {mood}?")






 


