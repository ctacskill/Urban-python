from fake_math import divide as fake_div
from true_math import divide as true_div

result_1 = fake_div(24, 6)
result_2 = fake_div(1, 0)
result_3 = true_div(15, 3)
result_4 = true_div(3, 0)
print(result_1)
print(result_2)
print(result_3)
print(result_4)
