print("          Welcome To Fitness App")
Walking_cal_per_min = 4
Running_cal_per_min = 9
strength_cal_per_min = 6
first_Name = input("Inter your first name: ")
last_name = input("Inter your last name: ")
Weight = float(input("Enter your weight(Kg): "))
Walking_minutes = int(input("Enter minutes of walking: "))
Running_minutes = int(input("Enter minutes of running: "))
strength_minutes = int(input("Enter minutes of strength: "))
Walking_total = Walking_minutes * Walking_cal_per_min
Running_total = Running_minutes * Running_cal_per_min
strength_total = strength_minutes * strength_cal_per_min
total_calories = Walking_total + Running_total + strength_total
total_minutes = Walking_minutes + Running_minutes + strength_minutes
print( "Daily summary" )
print("Name: " , first_Name , last_name )
print("          Hello : " , first_Name , last_name)
print("total minutes: " , total_minutes , "minutes")
print("total calories burned: " , total_calories , "Cal")



