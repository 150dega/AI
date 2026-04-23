P_Rain = float(input("Enter P(Rain): "))
P_Traffic_given_Rain = float(input("Enter P(Traffic | Rain): "))
P_Traffic = float(input("Enter P(Traffic): "))

print("\n--- Step 1: Given Values ---")
print("P(Rain) =", P_Rain)
print("P(Traffic | Rain) =", P_Traffic_given_Rain)

numerator = P_Traffic_given_Rain * P_Rain

print("\n--- Step 2: Numerator ---")
print("P(Traffic | Rain) * P(Rain) =", numerator)

P_Rain_given_Traffic = numerator / P_Traffic

print("\n--- Step 3: Bayes Formula ---")
print("P(Rain | Traffic) = (P(Traffic | Rain) * P(Rain)) / P(Traffic)")

print("\n--- Final Result ---")

:contentReference[oaicite:0]{index=0}

print("P(Rain | Traffic) =", P_Rain_given_Traffic)
