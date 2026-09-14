Feed = input("Insert a number: ")

if "." in Feed:
    Value = float(Feed)
else:
    Value = int(Feed)

Remainder = Value % 2

print(f"Value is {Value}")
print(f"The remainder is {Remainder} when {Value} is divided by 2.")
print(f"{Value} / 2 = {Value /2} (Remainder: {Remainder})")