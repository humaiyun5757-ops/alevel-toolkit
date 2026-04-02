from physics import kinetic_energy, suvat_v
from maths import quadratic

print("A-Level Toolkit")

choice = input("Choose: (1) KE (2) SUVAT (3) Quadratic: ")

if choice == "1":
    m = float(input("Mass (kg): "))
    v = float(input("Velocity (m/s): "))
    print("KE =", kinetic_energy(m, v))

elif choice == "2":
    u = float(input("Initial velocity: "))
    a = float(input("Acceleration: "))
    t = float(input("Time: "))
    print("Final velocity =", suvat_v(u, a, t))

elif choice == "3":
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    print("Solutions =", quadratic(a, b, c))
