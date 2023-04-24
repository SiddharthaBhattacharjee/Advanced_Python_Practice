from pyDatalog import pyDatalog

pyDatalog.create_terms('X,Y,title,dean')

+title( 'Lucy','professor' )
+title('Danny','professor')
+title('James','lecturer')
print(title(X,Y))
dean(X)<=title(X,'professor')
print(dean(X))
