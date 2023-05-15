from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y,Z, works_in, department_size, manager, indirect_manager, count_of_indirect_reports')
# Mary works in Production
+works_in('Mary', 'Production')
+works_in('Sam',  'Marketing')
+works_in('John', 'Production')
+works_in('John', 'Marketing')
+(manager['Mary'] == 'John')
+(manager['Sam']  == 'Mary')
+(manager['Tom']  == 'Mary')

indirect_manager(X,Y) <= (manager[X] == Y)
print(works_in(X,  'Marketing'))
#indirect_manager(X,Y) <= (manager[X] == Z) & indirect_manager(Z,Y)
print(indirect_manager('Sam',X))
print(indirect_manager(X,Y))

