number = list(map(int, input().split()))

fix_value, product_value, price = number

if price <= product_value:
	print(-1)
else:
	print(int(fix_value / (price - product_value) + 1))
