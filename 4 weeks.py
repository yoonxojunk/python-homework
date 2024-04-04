def get_fixed_price(discounted_price, discount_rate):
    return discounted_price / (1 - discount_rate / 100)

discount_rate = float(input("할인율은? "))
discounted_price_A = float(input("A 상품의 할인된 가격은? "))
discounted_price_B = float(input("B 상품의 할인된 가격은? "))

original_price_A = get_fixed_price(discounted_price_A, discount_rate)
original_price_B = get_fixed_price(discounted_price_B, discount_rate)

print("A 상품의 정가는", int(original_price_A), "원")
print("B 상품의 정가는", int(original_price_B), "원")
