Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_dic = {"name" : "aqsa", "age":20, "gender":"female", "university":"COMSATS", "degree":"BBA", "subject":"Programing", "topic":"dictionary", "miss":"sameet"}
>>> #display inforamtion
>>> print(my_dic["age"])
20
>>> #accessing value
>>> new_dic=my_dic["degree"]
>>> print(new_dic)
BBA
>>> #modifying values
>>> my_dic["age"]=19
>>> print(my_dic)
{'name': 'aqsa', 'age': 19, 'gender': 'female', 'university': 'COMSATS', 'degree': 'BBA', 'subject': 'Programing', 'topic': 'dictionary', 'miss': 'sameet'}
>>> #keys
>>> print(my_dic.keys())
dict_keys(['name', 'age', 'gender', 'university', 'degree', 'subject', 'topic', 'miss'])
>>> #values
>>> print(my_dic.values())
dict_values(['aqsa', 19, 'female', 'COMSATS', 'BBA', 'Programing', 'dictionary', 'sameet'])
>>> #items
>>> print(my_dic.items())
dict_items([('name', 'aqsa'), ('age', 19), ('gender', 'female'), ('university', 'COMSATS'), ('degree', 'BBA'), ('subject', 'Programing'), ('topic', 'dictionary'), ('miss', 'sameet')])
>>> #clear
>>> my_dic.clear()
>>> print(my_dic)
{}
>>> # adding new key pair
>>> my_dic["CGPA"]=3.15
>>> print(my_dic)
{'CGPA': 3.15}
>>> #remove
>>> del my_dic["topic"]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    del my_dic["topic"]
KeyError: 'topic'
>>> #get
>>> x= my_dic.get("gender")
>>> print(x)
None
