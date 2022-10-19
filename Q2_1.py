import re
product_count_text = "381 Products found"
number_pattern = r"\d+"
matches_found = re.findall(number_pattern, product_count_text)
product_count_int = int(matches_found[0])
# print(product_count_int)
