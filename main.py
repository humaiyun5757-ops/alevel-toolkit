from physics import kinetic_energy, suvat_v
from maths import quadratic
import math

print("Welcome to the A-Level Toolkit")

while True:
    print("\nChoose an option:")
    print("(1) Kinetic Energy")
    print("(2) SUVAT (final velocity)")
    print("(3) Quadratic solver")
    print("(4) Projectile range")
    print("(5) Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        m = float(input("Mass (kg): "))
        v = float(input("Velocity (m/s): "))
        print("Kinetic Energy =", kinetic_energy(m, v))

    elif choice == "2":
        u = float(input("Initial velocity (m/s): "))
        a = float(input("Acceleration (m/s^2): "))
        t = float(input("Time (s): "))
        print("Final velocity =", suvat_v(u, a, t))

    elif choice == "3":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        print("Solutions =", quadratic(a, b, c))

    elif choice == "4":
        print("Projectile motion (range)")
        u = float(input("Initial velocity (m/s): "))
        theta = float(input("Angle (degrees): "))
        g = 9.81

        R = (u**2 * math.sin(math.radians(2 * theta))) / g
        print("Range =", R)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")
