flat_tire = "axle"
spare_tire = "trunk"
tools = "trunk"
car = "ground"

print("\n--- Initial State ---")
print("Flat Tire:", flat_tire)
print("Spare Tire:", spare_tire)
print("Tools:", tools)
print("Car:", car)

print("\n--- Planning Execution ---")

print("Step 1: Open trunk")

if spare_tire == "trunk":
    print("Step 2: Take spare tire from trunk")
    spare_tire = "ground"

if tools == "trunk":
    print("Step 3: Take tools (jack & wrench)")
    tools = "ground"

if flat_tire == "axle":
    print("Step 4: Loosen nuts of flat tire")
    print("Step 5: Lift car using jack")
    car = "lifted"

if flat_tire == "axle":
    print("Step 6: Remove flat tire")
    flat_tire = "ground"

if spare_tire == "ground":
    print("Step 7: Mount spare tire on axle")
    spare_tire = "axle"

print("Step 8: Tighten nuts")

print("Step 9: Lower the car")
car = "ground"

print("Step 10: Close trunk")

print("\n--- Goal State ---")
print("Flat Tire:", flat_tire)
print("Spare Tire:", spare_tire)
print("Tools:", tools)
print("Car:", car)

if spare_tire == "axle" and flat_tire == "ground":
    print("\nGoal Achieved: Tire replaced successfully")
else:
    print("\nGoal Not Achieved")
