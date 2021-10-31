def gravity_between_two_object(object_1, object_2, radius):
    G = 6.673*(10**-11)
    g_force = (G*object_1*object_2)/(radius**2)
    return g_force


def force(object_3, acceleration1):
    force = object_3 * acceleration1
    return force


def pressure(force1, acc):
    pressure = force1 / acc
    return pressure


def density(object_4, vol):
    density = object_4 / vol
    return density


def velocity(displacement, time1):
    velocity = displacement / time1
    return velocity


def speed(dis, time2):
    speed = dis / time2
    return speed


def acceleration(final_v, initial_v, time3):
    acceleration = (final_v - initial_v) / time3
    return acceleration


def liquid_pressure(liquid_d, acc_g, liquid_depth):
    liquid_pressure = liquid_d * acc_g * liquid_depth
    return liquid_pressure


def energy(power1, time4):
    energy = power1 * time4
    return energy


def power(work, time5):
    power = work / time5
    return power


def work_done(force2, distance):
    work_done = force2 * distance
    return work_done


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

    gravitional_force = gravity_between_two_object(object_1, object_2, radius)

    print(f"The gravitational force = {gravitional_force:.2f}")


elif (science_operation == '2'):  # Force
    object_3 = float(input("Enter a first mass: "))
    acceleration1 = int(input("Enter acceleration: "))
    f = force(object_3, acceleration1)
    print(f" Force  = {f:.2f}")

elif (science_operation == '3'):  # Pressure
    force1 = float(input("Enter force: "))
    acc = float(input("Enter acceleration: "))

    press = pressure(force1, acc)

    print(f"Pressure = {press:.2f}")


elif (science_operation == '4'):  # Density
    object_4 = float(input("Enter a first mass: "))
    vol = float(input("Enter  volume : "))

    densityy = density(object_4, vol)

    print(f" Density = {densityy:.2f}")


elif (science_operation == '5'):  # Velocity
    displacement = float(input("Enter Displacement : "))
    time1 = float(input("Enter  tim: "))

    velocityy = velocity(displacement, time1)

    print(f" Velocity = {velocityy:.2f}")


elif (science_operation == '6'):  # Speed
    dis = float(input("Enter Distance: "))
    time2 = float(input("Enter Time : "))

    speedd = speed(dis, time2)

    print(f"Power root of the number = {speedd:.2f}")

elif (science_operation == '7'):  # Acceleration
    initial_v = float(input("Enter a Initial velocity : "))
    final_v = float(input("Enter Final velocity : "))
    time3 = float(input("Enter a time: "))

    accelerationn = acceleration(final_v, initial_v, time3)

    print(f" Accleration = {accelerationn:.2f}")


elif (science_operation == '8'):  # Liqud pressure
    liquid_d = float(input("Enter  Liquid Density : "))
    acc_g = float(input("Enter Accleration due to gravity: "))
    liquid_depth = float(input("Enter Liquid Depth: "))

    liquid_pressuree = liquid_pressure(liquid_d, acc_g, liquid_depth)

    print(f" Liquid Pressure = { liquid_pressuree:.2f}")

elif (science_operation == '9'):  # Energy
    power1 = float(input("Enter  Initial velocity : "))
    time4 = float(input("Enter time: "))

    energyy = energy(power1, time4)

    print(f"Energy = {energyy:.2f}")

elif (science_operation == '10'):  # Power
    work = float(input("Enter  work : "))
    time5 = float(input("Enter an   Elapsed time: "))

    powerr = power(work, time5)

    print(f"Power root of the number = {powerr:.2f}")


elif (science_operation == '11'):  # Work done
    force2 = float(input("Enter  Initial velocity : "))
    distance = float(input("Enter time: "))

    work_donee = work_done(force2, distance)

    print(f"WorkDone = {work_donee:.2f}")


elif (science_operation == '12'):  # exit
    print("Goodbye")

else:  # invalid
    print("Invalid input!!")
