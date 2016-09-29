#ask user for preferred measurement system
x = input("USC or Metric?")
#ask for gallons and miles since usc was inputted
if x == "usc":
    uscd = float(input("How many miles driven?"))
    uscg = float(input("How many gallons of gas used?"))
#gas and distance conversions from usc to metric
    metd = float(uscd*1.60934)
    metg = float(uscg*3.78541)
#computing fuel consumption
    mpg = float(uscd//uscg)
    lk = float(100*metg//metd)
#ask for liters and kms since metrics was inputted
if x == "metric":
    metd = float(input("How many kilometers driven?"))
    metg = float(input("How many liters of gas used?"))
#gas and distance conversions from metric to usc
    uscd = float(metd*.621371)
    uscg = float(metg*.264172)
#computing fuel consumption
    mpg = float(uscd//uscg)
    lk = float(100*metg//metd)
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
#display results
print(28*z,('USC'),14*z,('Metric'))
print("Distance",13*z,":",format(float(uscd),'9.3f'),"miles",z,format(float(metd),'9.3f'),"km")
print("Gas",18*z,":",format(float(uscg),'9.3f'),"gallons",format(float(metg),'9.3f'),"liters")
print("Consumption",10*z,":",format(float(mpg),'9.3f'),"mpg",z,format(float(lk),'11.3f'),"1/100km")
print("Gas Consumption Rating:",cc)


