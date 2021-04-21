import pyupbit

access_key = "75zwEj4KcEiPLZ0G1yDOFUy8rba1CxIgK6xXxwQ9"
secret_key = "xzqEMO7exrlxNMvmBe1f7on592mEyRD1IdfuR8uI"

upbit = pyupbit.Upbit(access_key, secret_key)
ret = upbit.buy_limit_order("KRW-XRP", 100, 20)
print(ret)