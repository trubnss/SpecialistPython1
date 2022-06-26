# Напишите функцию принимающую общее количество объектов(например, товаров)
# которые нужно отобразить и количество объектов, которые нужно отобразить на каждой странице.
# Функция должна вычислять количество страниц для отображения всех объектов.

# Под пагинацией понимают показ ограниченной части информации на одной
# веб-странице и вывода списка остальных страниц.

def pagination(num_items, items_on_page):
    if num_items % items_on_page == 0:
        return num_items // items_on_page
    else:
        return (num_items // items_on_page) + 1


num_items = int(input("num_items: "))
items_on_page = int(input("items_on_page: "))

print(pagination(num_items, items_on_page))

