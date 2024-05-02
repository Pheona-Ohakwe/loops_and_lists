#1. PYTHON LIST TRANSFORMATION

#Task1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print("grades after .sort", grades)

#Task2
total=(sum(grades))
print(total)
average=(total / len(grades))
print(average)


#================================2. Advanced List Methods and Identity Operators==============================================

#Task1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and  "Alice" in attended:
   print("Alice")
if "Bob" in submitted and "Bob" in attended:
   print("Bob")
if "Charlie" in submitted and "Charlie" in attended:
   print("Charlie")
if "David" in submitted and "David" in attended:
   print("David")
if "Eve" in submitted and "Eve" in attended:
   print("Eve")
if "Frank" in submitted and "Frank" in attended:
   print ("Frank")





#==================================3. Advanced Slicing Techniques==============================================================

#Task1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

week_two_temperatures = temperatures[7:14]
print(week_two_temperatures)

#Task2

over_100_temperatures = temperatures [23:29:1]
print(over_100_temperatures)

