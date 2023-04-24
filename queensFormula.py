from pyDatalog import pyDatalog

pyDatalog.create_terms('N,Q0,Q1,Q2,Q3,Q4,Q5,Q6,Q7')
pyDatalog.creare_terms('ok,queens,next_queen')

#start
queens(Q0) <= (Q0._in(range(8)))

#queens(...) <= queens(..) & next_queen(...)

#next_queen(...) <= next_queen(..) & ok(.n.n)

#end
ok(X1,N,X2) <= (X1 != X2) & (X1 != X2+N) & (X1 != X2-N)
print(queens(X0,X1,X2,X3,X4,X5,X6,X7))
