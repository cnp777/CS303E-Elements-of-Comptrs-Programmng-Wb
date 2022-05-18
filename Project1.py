# File: Project1.py
# Student: Clara Torslov
# UT EID: ct 32699
# Course Name: CS303E
#
# Date: March 7th, 2022
# Description of Program: Converts from English length units to metric length units and vice versa dependent on user inputs.

ErrorMessage = "\nERROR: Answer must be 1, 2 or 3. Try again."

print("")
print("Welcome to the English/Metric conversion utility.")
print("")

print("This utility allows you to convert between English units", "(miles, feet, inches) and metric units (kilometers, meters,",
"centimeters).", sep = "\n")

print("")
print("------------------------------------------------------------")
print("")
print("Which direction would you like to convert:")
print("   For English to Metric type: 1")
print("   For Metric to English type: 2")
print("   To Quit type:               3")
print("")

direction = input("Input your answer (1, 2 or 3): ")

if(direction == "1"):
    print("")
    print("Select English units to convert to metric equivalent:")
    print("   For miles type:  1")
    print("   For feet type:   2")
    print("   For inches type: 3")
    print("")
    EnglishUnits = input("Choose English units to convert (1, 2 or 3): ")

    while (not EnglishUnits == "1" and not EnglishUnits == "2" and not EnglishUnits == "3"):
        print(ErrorMessage)
        print("")
        print("Select English units to convert to metric equivalent:")
        print("   For miles type:  1")
        print("   For feet type:   2")
        print("   For inches type: 3")
        print("")
        EnglishUnits = input("Choose English units to convert (1, 2 or 3): ")

    E_unit = "miles" if (EnglishUnits == "1") else "feet" if (EnglishUnits == "2") else "inches"

    print("")
    print("Convert to which metric units:")
    print("   For kilometers type:  1")
    print("   For meters type:      2")
    print("   For centimeters type: 3")
    print("")
    MetricUnits = input("Choose target metric units (1, 2 or 3): ")

    while (not MetricUnits == "1" and not MetricUnits == "2" and not MetricUnits == "3"):
        print(ErrorMessage)
        print("")
        print("Convert to which metric units:")
        print("   For kilometers type:  1")
        print("   For meters type:      2")
        print("   For centimeters type: 3")
        print("")
        MetricUnits = input("Choose target metric units (1, 2 or 3): ")

    M_unit = "kilometers" if (MetricUnits == "1") else "meter" if (MetricUnits == "2") else "centimeter"

    print("")
    numConvert = float(input("Enter the number of {} to convert to {}: ".format(
        "miles" if (EnglishUnits == "1") else "feet" if (EnglishUnits == "2") else "inches",
        "kilometers" if (MetricUnits == "1") else "meter" if (MetricUnits == "2") else "centimeters")))

    if(EnglishUnits == "1" and MetricUnits == "1"):
        result = ((numConvert * 5280.0) * 0.3048) / 1000.0
        print("")
        print("RESULT:", numConvert, E_unit, "=", format(result, ".3f"), M_unit)

    elif (EnglishUnits == "1" and MetricUnits == "2"):
        result = ((numConvert * 5280.0) * 0.3048)
        print("")
        print("RESULT:", numConvert, E_unit, "=", format(result, ".3f"), M_unit)

    elif (EnglishUnits == "1" and MetricUnits == "3"):
        result = ((numConvert * 5280.0) * 0.3048) * 100.0
        print("")
        print("RESULT:", numConvert, E_unit, "=", format(result, ".3f"), M_unit)

    elif (EnglishUnits == "2" and MetricUnits == "1"):
        result = (numConvert*0.3048)/1000.0
        print("")
        print("RESULT:", numConvert, E_unit, "=", format(result, ".3f"), M_unit)

    elif (EnglishUnits == "2" and MetricUnits == "2"):
        result = numConvert * 0.3048
        print("")
        print("RESULT:", numConvert, E_unit, "=", format(result, ".3f"), M_unit)

    elif (EnglishUnits == "2" and MetricUnits == "3"):
        result = (numConvert * 0.3048) * 100.0
        print("")
        print("RESULT:", numConvert, E_unit, "=", format(result, ".3f"), M_unit)

    elif (EnglishUnits == "3" and MetricUnits == "1"):
        result = ((numConvert/12.0)*0.3048)/1000.0
        print("")
        print("RESULT:", numConvert, E_unit, "=", format(result, ".3f"), M_unit)

    elif (EnglishUnits == "3" and MetricUnits == "2"):
        result = (numConvert/12.0) * 0.3048
        print("")
        print("RESULT:", numConvert, E_unit, "=", format(result, ".3f"), M_unit)

    elif (EnglishUnits == "3" and MetricUnits == "3"):
        result = ((numConvert/12.0) * 0.3048) * 100.0
        print("")
        print("RESULT:", numConvert, E_unit, "=", format(result, ".3f"), M_unit)

elif(direction == "2"):
    print("")
    print("Select metric units to convert to English equivalent:")
    print("   For kilometers type:  1")
    print("   For meters type:      2")
    print("   For centimeters type: 3")
    print("")

    MetricUnits = input("Choose metric units to convert (1, 2 or 3): ")

    while (not MetricUnits == "1" and not MetricUnits == "2" and not MetricUnits == "3"):
        print(ErrorMessage)
        print("")
        print("Select metric units to convert to English equivalent:")
        print("   For kilometers type:  1")
        print("   For meters type:      2")
        print("   For centimeters type: 3")
        print("")

        MetricUnits = input("Choose metric units to convert (1, 2 or 3): ")

    M_unit = "kilometers" if (MetricUnits == "1") else "meter" if (MetricUnits == "2") else "centimeters"

    print("")
    print("Convert to which English units:")
    print("   For miles type:  1")
    print("   For feet type:   2")
    print("   For inches type: 3")
    print("")

    EnglishUnits = input("Choose target English units (1, 2 or 3): ")

    while (not EnglishUnits == "1" and not EnglishUnits == "2" and not EnglishUnits == "3"):
        print(ErrorMessage)
        print("")
        print("Convert to which English units:")
        print("   For miles type:  1")
        print("   For feet type:   2")
        print("   For inches type: 3")
        print("")

        EnglishUnits = input("Choose target English units (1, 2 or 3): ")

    E_unit = "miles" if (EnglishUnits == "1") else "feet" if (EnglishUnits == "2") else "inches"

    print("")
    numConvert = float(input("Enter the number of {} to convert to {}: ".format(
        "kilometers" if (MetricUnits == "1") else "meter" if (MetricUnits == "2") else "centimeter",
        "miles" if (EnglishUnits == "1") else "feet" if (EnglishUnits == "2") else "inches")))

    if(MetricUnits == "1" and EnglishUnits == "1"):
        result = ((numConvert * 1000.0) * 3.28084) / 5280.0
        print("")
        print("RESULT:", numConvert, M_unit, "=", format(result, ".3f"), E_unit)

    elif(MetricUnits == "1" and EnglishUnits == "2"):
        result = (numConvert*1000.0)*3.28084
        print("")
        print("RESULT:", numConvert, M_unit, "=", format(result, ".3f"), E_unit)

    elif(MetricUnits == "1" and EnglishUnits == "3"):
        result = ((numConvert*1000.0)*3.28084)*12.0
        print("")
        print("RESULT:", numConvert, M_unit, "=", format(result, ".3f"), E_unit)

    elif(MetricUnits == "2" and EnglishUnits == "1"):
        result = (numConvert * 3.28084) / 5280.0
        print("")
        print("RESULT:", numConvert, M_unit, "=", format(result, ".3f"), E_unit)

    elif(MetricUnits == "2" and EnglishUnits == "2"):
        result = (numConvert * 3.28084)
        print("")
        print("RESULT:", numConvert, M_unit, "=", format(result, ".3f"), E_unit)

    elif (MetricUnits == "2" and EnglishUnits == "3"):
        result = (numConvert * 3.28084) * 12.0
        print("")
        print("RESULT:", numConvert, M_unit, "=", format(result, ".3f"), E_unit)

    elif (MetricUnits == "3" and EnglishUnits == "1"):
        result = ((numConvert/100.0) * 3.28084) / 5280.0
        print("")
        print("RESULT:", numConvert, M_unit, "=", format(result, ".3f"), E_unit)

    elif (MetricUnits == "3" and EnglishUnits == "2"):
        result = ((numConvert/100.0) * 3.28084)
        print("")
        print("RESULT:", numConvert, M_unit, "=", format(result, ".3f"), E_unit)

    elif (MetricUnits == "3" and EnglishUnits == "3"):
        result = ((numConvert/100.0) * 3.28084)*12.0
        print("")
        print("RESULT:", numConvert, M_unit, "=", format(result, ".3f"), E_unit)

elif(direction == "3"): print("\nThanks for using our converter. Goodbye!")

else: print(ErrorMessage)