# Simple Python Program
print("--- 🐍 Python Quick Test ---")

# User Input
name = input("Aapka Naam kya hai? ")
age = int(input("Aapki Umer (Age) kya hai? "))

print(f"\nWelcome {name}!")

# Simple Age Condition
if age >= 18:
    print("✅ Aap Adult hain.")
else:
    print("👶 Aap Abhi Student/Junior hain.")

# Quick Calculation
num1 = float(input("\nPehla Number likhein: "))
num2 = float(input("Doosra Number likhein: "))

print(f"➕ Sum: {num1 + num2}")
print(f"✖️ Multiplication: {num1 * num2}")