#ask user for preferred measurement system
x = input("USC or Metric?")
if x == "usc":
    uscdis = float(input("How many miles driven?"))
    uscgas = float(input("How many gallons of gas used?"))
#gas and distance conversions from usc to metric
    metdis = uscdis*1.60934
    metgas = uscgas*3.78541
if x == "metric":
    metdis = float(input("How many kilometers driven?"))
    metgas = float(input("How many liters of gas used?"))
#gas and distance conversions from metric to usc
    uscdis = metdis*.621371
    uscgas = metgas*.264172
#computing fuel consumption
mpg = uscdis//uscgas
lpk = 100*metgas//metdis
#putting fuel consumption into categories
if lpk > 20:
    cc = "extremely poor"
elif lpk > 15 and lpk <= 20:
    cc = "poor"
elif lpk > 10 and lpk <=15:
    cc = "average"
elif lpk > 8 and lpk <= 10:
    cc = "good"
elif lpk <= 8:
    cc = "excellent"


