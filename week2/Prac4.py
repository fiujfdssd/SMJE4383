#Take the number of points one team is ahead
points_str = input(" Enter the lead in points: ")
points_remaining_int = int(points_str)

#Subtract 3
lead_calculation_float= float(points_remaining_int-3)

#Add half point if the team that is ahead has the ball,
#Remove half point if the other team that is ahead has the ball
has_ball_str = input("Does the lead team have the ball (Yes or No): ")

if has_ball_str == 'Yes':
   lead_calculation_float= lead_calculation_float + 0.5
else:
   lead_calculation_float= lead_calculation_float - 0.5

#Number < 0 = 0
if lead_calculation_float< 0:
   lead_calculation_float= 0

#Square that
lead_calculation_float=lead_calculation_float** 2

#if the result is greater than the number of second left in the game,
#the lead is safe
seconds_remaining_int = int(input("Enter the number of seconds remaining: "))

if lead_calculation_float> seconds_remaining_int:
   print("Lead is safe.")
else:
   print("Lead is not safe")
