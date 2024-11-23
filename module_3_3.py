#print_params создаём фуекцию
def print_params(a=1, b ='строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
#распаковываем параметры
values_list = ["Сергей", 777, [1,2,3]]
values_dict = {'a':777, 'b' : 'Сергей', 'c' : [1,2,3]}
print_params(*values_list)
print_params(**values_dict)
#Распаковка + отдельные параметры
values_list_2 = [77.77, 'Строка']
print_params(*values_list_2, 42)
