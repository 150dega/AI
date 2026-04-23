print("Laptop Troubleshooting Expert System")

power = input("Is laptop turning ON? (yes/no): ")
charging = input("Is charger connected? (yes/no): ")
slow = input("Is laptop very slow? (yes/no): ")
overheat = input("Is laptop overheating? (yes/no): ")
wifi = input("Is WiFi working? (yes/no): ")

print("\n--- Diagnosis ---")

if power == "no" and charging == "no":
    print("Solution: Connect the charger")

elif power == "no" and charging == "yes":
    print("Solution: Check battery or power button")

elif slow == "yes":
    print("Solution: Close background apps / Upgrade RAM")

elif overheat == "yes":
    print("Solution: Clean fan / Use cooling pad")

elif wifi == "no":
    print("Solution: Restart router / Check network settings")

else:
    print("Laptop is working fine")
