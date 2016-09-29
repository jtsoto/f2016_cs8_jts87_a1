#ask user for preferred measurement system
x = input("USC or Metric?")
if x == "usc":
    uscd = float(input("How many miles driven?"))
    uscg = float(input("How many gallons of gas used?"))
#gas and distance conversions from usc to metric
    metd = uscd*1.60934
    metg = uscg*3.78541
#computing fuel consumption
    mpg = uscd//uscg
    lk = 100*metg//metd
if x == "metric":
    metd = float(input("How many kilometers driven?"))
    metg = float(input("How many liters of gas used?"))
#gas and distance conversions from metric to usc
    uscd = metd*.621371
    uscg = metg*.264172
#computing fuel consumption
    mpg = uscd//uscg
    lk = 100*metg//metd
#putting fuel consumption into categories
if lk > 20:
    cc = "extremely poor"
elif lk > 15 and lk <= 20:
    cc = "poor"
elif lk > 10 and lk <=15:
    cc = "average"
elif lk > 8 and lk <= 10:
    cc = "good"
elif lk <= 8:
    cc = "excellent"
z = " "
print(28*z,('USC'),14*z,('Metric'))
print("Distance",13*z,":",format(uscd,'9.3f'),"miles",z,format(metd,'9.3f'),"km")
print("Gas",18*z,":",format(uscg,'9.3f'),"gallons",z,format(metg,'9.3f'),"liters")
print("Consumption",10*z,":",format(mpg,'9.3f'),"mpg",z,format(lk,'9.3f'),"1/100km")
print("Gas Consumption Rating:",cc)


