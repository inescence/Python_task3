#функция сортировки методом 'пузырек'
def sort_bubble(numbers):
   for i in range(len(numbers)):
       for j in range(len(numbers) - i - 1):
           if numbers[j] > numbers[j + 1]:
               numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
   return numbers


#функция 'бинарного' поиска левого и правого элементов
def binary_search(numbers, numbers_user, left, right):
   if left > right:  # если левая граница превысила правую,
       return False  # значит элемент отсутствует
   middle = (right + left) // 2  # находим середину
   if numbers[middle] == numbers_user:  # если элемент в середине,
       return middle  # возвращаем этот индекс
   elif numbers_user < numbers[middle]:  # если элемент меньше элемента в середине
       # рекурсивно ищем в левой половине
       return binary_search(numbers, numbers_user, left, middle - 1)
   else:  # иначе в правой
       return binary_search(numbers, numbers_user, middle + 1, right)


#тело программы
#вводим числа, проверяем правильность данных, сортируем
what = True
while what:
   try:
       numbers_list = input("Введите последовательность целых чисел через пробел: ").split()


   # разделяем по разделителю (пробел) и записываем строку целых чисел
       numbers = [int(x) for x in numbers_list]
   #    print('числа:', numbers)
   # сортировка
       numbers = sort_bubble(numbers)
       print('Список после сортировки:', numbers)


       numbers_user = input("Введите число из списка для определения индекса: ")
       numbers_user = int(numbers_user)
   #    print("введено число ", numbers_user)
       what = False
   except ValueError:
           print(f'Ошибка {ValueError}')
           print('Введено недопустимое значение.')
           what = input("Повторить ввод чисел? (+ или -): ")
           if what != '+':
               print('До свидания')
               what = False
               exit(1)
           else:
               print('В следующий раз будьте внимательнее!')


#проверяем есть ли искомое число в списке
if numbers_user not in numbers:
    print(f'Нет числа {numbers_user} среди чисел последовательности. {numbers}')
    if numbers_user < min(numbers):
          print(f'число {numbers_user} меньше минимального последовательности. {min(numbers)}')
    if numbers_user > max(numbers):
          print(f'число {numbers_user} больше максимального последовательности {max(numbers)}')
    exit(1)


#вызывается функция бинарного поиска левого и правого элементов
number_index = binary_search(numbers, numbers_user, 0, len(numbers) - 1)


#определяем место искомого числа в списке
print("Индекс введенного числа в списке: ", number_index)
#анализ числа в списке
if number_index == 0:
   print(f'Число {numbers_user} первое значение в списке, следующее {numbers[number_index + 1]}')
elif number_index == int(len(numbers)-1):
   print(f'Число {numbers_user} последнее значение в списке, предыдущее значение {numbers[number_index-1]}')
else:
   print(f'Предыдущее значение {numbers[number_index-1]}, следующее {numbers[number_index + 1]}')