registered = input()
fee_paid = input()
identity_verified = input()
system_check = input()

# Check whether the student can access the online exam
if registered ==  "No":
    print("Access Denied: Registration Incomplete")
elif registered == "Yes" and (fee_paid == "No" or identity_verified == "No"):
    print("Access Denied: Verification Pending")
elif registered == "Yes" and fee_paid == "Yes" and identity_verified == "Yes" and system_check == "Fail":
    print("Access Denied: System Check Failed")
else:
    print("Access Granted")