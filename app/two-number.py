from excel_data import get_new_student_number, get_student_number

student_number = get_student_number(1000)
new_number = get_new_student_number()

dict_number = dict(zip(student_number, new_number))

print(dict_number)

# for old_number,new_number in dict_number.items():
#     print(old_number)
#     print(new_number)