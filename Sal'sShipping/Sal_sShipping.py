
weight = 90

#Ground Shipping 
print("Ground Shipping")
if weight > 10:
  cost_ground = 4.75*weight+20
elif weight > 6:
  cost_ground= 4.00*weight+20
elif weight > 2:
  cost_ground= 3.00*weight+20
else: cost_ground = 1.50*weight+20

print(cost_ground)

#Ground Shipping Premium
print("Ground Shipping Premium")
cost_ground_premium = 125.00
print(cost_ground_premium)

#Drone Shipping

if weight > 10:
  cost_drone = 14.25*weight
elif weight > 6:
  cost_drone= 12.00*weight
elif weight > 2:
  cost_drone= 9.00*weight
else: cost_drone = 4.50*weight
print("Drone Shipping")

print(cost_drone)

#If the cost of Drone Shipping is less than the cost of Ground Shipping and Ground Shipping Premium, then it is the cheapest of the three options.
if cost_drone < cost_ground and cost_drone < cost_ground_premium:
  print("The cheapest method of shipping is Drone Shipping. The price is: " + str(cost_drone))

#If the Drone Shipping isnt the cheapest, we look at the else ifs. If the cost of Ground Shipping is less than the cost of Ground Shipping Premium and Drone Shipping, then it is the cheapest

elif cost_ground < cost_drone and cost_ground < cost_ground_premium:
  print("The cheapest method of shipping is Ground Shipping. The price is: " + str(cost_ground))

#If none of Drone Shipping or Ground Shipping is the cheapest, than the Ground Shipping Premium is the only option left.

else: print("The cheapest method of shipping is Ground Shipping Premium. The price is: " + str(cost_ground_premium))
















