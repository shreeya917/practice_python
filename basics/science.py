
print("""
Choose Science operation  you like to perform
    1. Gravity between two object
    2. Force 
    3. Pressure
    4. Density
    5. Velocity
    6. Speed
    7. Acceleration
    8. Liqud pressure
    9. Energy
    10.Power
    11.Work done
    12.Exit
    """)
science_operation = input("Enter Option: ")


if (science_operation == '1'):  # Gravity between two object
    object_1 = float(input("Enter a first mass of an object: "))
    object_2 = float(input("Enter a second  mass of an object: "))
    radius = float(
        input("Enter the distance between the centres of the masses: "))

    G = 6.673*(10**-11)
    gravitional_force = (G*object_1*object_2)/(radius**2)

    print(f"The gravitational force = {gravitional_force:.2f}")


elif (science_operation == '2'):  # Force
    object_3 = float(input("Enter a first mass: "))
    acceleration1 = int(input("Enter acceleration: "))
    force = object_3 * acceleration1

    print(f" Force  = {force:.2f}")

elif (science_operation == '3'):  # Pressure
    force1 = float(input("Enter force: "))
    acc = float(input("Enter acceleration: "))

    pressure = force1 / acc

    print(f"Pressure = {pressure:.2f}")


elif (science_operation == '4'):  # Density
    object_4 = float(input("Enter a first mass: "))
    vol = float(input("Enter  volume : "))

    density = object_4 / vol

    print(f" Density = {density:.2f}")


elif (science_operation == '5'):  # Velocity
    displacement = float(input("Enter Displacement : "))
    time1 = float(input("Enter  tim: "))

    velocity = displacement / time1

    print(f" Velocity = {velocity:.2f}")


elif (science_operation == '6'):  # Speed
    dis = float(input("Enter Distance: "))
    time2 = float(input("Enter Time : "))

    speed = dis / time2

    print(f"Power root of the number = {speed:.2f}")

elif (science_operation == '7'):  # Acceleration
    initial_v = float(input("Enter a Initial velocity : "))
    final_v = float(input("Enter Final velocity : "))
    time3 = float(input("Enter a time: "))

    acceleration = (final_v - initial_v) / time3

    print(f" Accleration = {acceleration:.2f}")


elif (science_operation == '8'):  # Liqud pressure
    liquid_d = float(input("Enter  Liquid Density : "))
    acc_g = float(input("Enter Accleration due to gravity: "))
    liquid_depth = float(input("Enter Liquid Depth: "))

    liquid_pressure = liquid_d * acc_g * liquid_depth

    print(f" Liquid Pressure = { liquid_pressure:.2f}")

elif (science_operation == '9'):  # Energy
    power1 = float(input("Enter  Initial velocity : "))
    time4 = float(input("Enter time: "))

    energy = power1 * time4

    print(f"Energy = {energy:.2f}")

elif (science_operation == '10'):  # Power
    work = float(input("Enter  work : "))
    time5 = float(input("Enter an   Elapsed time: "))

    power = work / time5

    print(f"Power root of the number = {power:.2f}")


elif (science_operation == '11'):  # Work done
    force2 = float(input("Enter  Initial velocity : "))
    distance = float(input("Enter time: "))

    work_done = force2 * distance

    print(f"WorkDone = {work_done:.2f}")


elif (science_operation == '12'):  # exit
    print("Goodbye")

else:  # invalid
    print("Invalid input!!")
