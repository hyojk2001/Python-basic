import pybithumb

con_key = "224a47977687bb70eca884f164c3f79a"
sec_key = "b845dc01063e3038e277008af88b4f78"

bithumb = pybithumb.Bithumb(con_key, sec_key)

balance = bithumb.get_balance("BTC")
print(balance)