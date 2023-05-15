from pyDatalog import pyDatalog
pyDatalog.create_atoms('parent,male,female,son,daughter,X,Y,Z')
+male('adam')
+female('anne')
+female('barney')
+male('james')
+parent('barney','adam')
+parent('james','anne')

#The first rule is read as follows: for all X and Y, X is the son of Y if there exists X and Y such that
#Y is the parent of X and X is male.
#The second rule is read as follows: for all X and Y, X is the daughter of Y if there exists X and Y such that Y is the parent of X and X is female.
son(X,Y)<= male(X) & parent(Y,X)
daughter(X,Y)<= female(X) & parent(Y,X)
print(pyDatalog.ask('son(adam,Y)'))
print(pyDatalog.ask('daughter(anne,Y)'))
print(son('adam',Y))
