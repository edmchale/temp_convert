from conversions import f2c, c2f
print("Temperature converter")
print("Choose 1 to convert F to C")
print("Choose 2 to convert C to F")
choice = input("Choice: ")
if choice == "1":
    tf = float(input("Enter deg F: "))
    tc = f2c(tf)
    print(tf, " deg F = ", tc," deg C")
elif choice == "2":
    tc = float(input("Enter deg C: "))
    tf = c2f(tc)
    print(tc, "deg C = ", tf, " deg F")
else:
    print("You did not pick 1 or 2")

