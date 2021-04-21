import pyupbit

access_key = "75zwEj4KcEiPLZ0G1yDOFUy8rba1CxIgK6xXxwQ9"
secret_key = "xzqEMO7exrlxNMvmBe1f7on592mEyRD1IdfuR8uI"

upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())