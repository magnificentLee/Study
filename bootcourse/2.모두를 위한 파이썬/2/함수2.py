def computepay(hours, rate):
    print("In Computerpay", hours, rate)
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    print("Returning", pay)
    return pay


sh = float(input("Enter Hours: "))
sr = float(input("Enter Rate: "))

xp = computepay(sh, sr)
print("Pay:", xp)