# Dictionary items are key value pairs enclosed in curly brackets 
# Dictionary is ordered of python 3.7 
# Dictionary is mutuable 
# Dictionary keys are unique, cannot be duplicated
# Dictionary accepts different data types

''' Dict Attributes '''

# print(dir(dict))
# print(help(dict.pop))

''' Creating Python Dictionary '''

# dict_example = {}
# dict_example = {'name': 'Adriana', 'age': 40}

# dict_example = ([(1, 'car'), (2, 'bicycle')]) # list of tuples
# dict_example = dict([(1, 'car'), (2, 'bicycle')]) # convert list of tuples into key value pair dictionary 

# print(dict_example)

''' Access Dictionary Values '''

# student = {'name': 'Adriana', 'age': 40}
# print(student['name'])
# print(student.get('age'))
# print(student.keys())
# print(student.values())

# students = [{'name': 'Adriana', 'age': 40}, {'name': 'Jonh', 'age': 45}]
# print(students[1]['name'])
# print(students[0])

# for i in range(len(students)):
#     print(students[i]['name'])

''' Changing Dictionary Elements '''

# student = {'name': 'Adriana', 'age': 40}
# student['age'] = 37
# student.update({'name': 'Laura', 'age': 34})

# print(student)

# ====================================================

# student = {'name': 'Adriana', 'age': 40}
# student.setdefault('name', 'Laura') # Check if the key exists and if does do nothing
# student.setdefault('subject', 'python') # If deosn't, it creates 
# student.setdefault('subject', 'math') # do nothing as 'subject' has already populated

# print(student)

''' Remove Elements from Dictionary '''

# student = {'name': 'Adriana', 'age': 40}
# student.pop('age') 

# print(student)

# ====================================================

# student = {'name': 'Adriana', 'age': 40}
# student.popitem()  

# print(student)

# print(help(dict.popitem))

# ====================================================

# student = {'name': 'Adriana', 'age': 40}
# student.clear()
# print(student)

# ====================================================

# student = {'name': 'Adriana', 'age': 40}
# del student
# print(student)

''' Dictionary Membership Test '''

# student = {'name': 'Adriana', 'age': 40}
# print('name' in student) # return a boolean 
# print('age' not in student)