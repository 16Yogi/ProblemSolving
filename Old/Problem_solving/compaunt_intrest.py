principal = float(input("Principal:"))
rate = float(input("Rate:"))
time = float(input("Time:"))

amount = principal*((pow((1+rate/100),time)))

print("result:",amount)
