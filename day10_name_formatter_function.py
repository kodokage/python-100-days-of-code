f_name = input('Enter first name : ')
l_name = input('Enter last name : ')

def name_format(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()

  return (f"{formated_f_name} {formated_l_name}")


formated_string = name_format(f_name, l_name)
print(formated_string)