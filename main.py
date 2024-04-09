# Remove the first N elements from a List in Python

my_list = ['a', 'b', 'c', 'd', 'e', 'f']

# ✅ remove first N elements from list (using list slicing)
n = 2

new_list = my_list[n:]
print(new_list)  # 👉️ ['c', 'd', 'e', 'f']