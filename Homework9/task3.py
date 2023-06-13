# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

sum_purchase = 0
list_sum_purchase = []
with open('test_file/task_3.txt', mode='r', encoding='utf-8') as f:
    for i in f:
        i = i[:-1]
        if i == '':
            list_sum_purchase.append(sum_purchase)
            sum_purchase = 0
        else:
            sum_purchase += int(i)
max_sum = []

# for i in list_sum_purchase:
while len(max_sum) < 3:
    max_sum.append(max(list_sum_purchase))
    list_sum_purchase.remove(max(list_sum_purchase))
three_most_expensive_purchases = sum(max_sum)

sum2 = 0
for u in range(3):
    # sum2 += list_sum_purchase.pop(list_sum_purchase.index(max(list_sum_purchase)))
    max_el = max(list_sum_purchase)
    list_sum_purchase.remove(max_el)
    sum2 += max_el
print(sum2)
assert three_most_expensive_purchases == 202346