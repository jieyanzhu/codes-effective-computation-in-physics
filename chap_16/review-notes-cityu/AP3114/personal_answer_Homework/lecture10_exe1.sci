//lam = poly(0,'lam')
//p = lam^3-4*lam^2-11*lam+30
disp('Excercise 1 (a)')
p1 = poly([5 4 0 1],'x','coeff')
disp('function')
disp(p1)
disp('roots')
disp(lamda1 = roots(p1))

disp('Excercise 1 (b)')
p2 = poly([1 2 2],'x','coeff')
disp('function')
disp(p2)
disp('roots')
disp(lamda2 = roots(p2))

disp('Excercise 1 (c)')
p3 = poly([3 1 1 0 1],'x','coeff')
disp('function')
disp(p3)
disp('roots')
disp(lamda3 = roots(p3))

disp('Excercise 1 (d)')
p4 = poly([-3 0 1],'x','coeff')
disp('function')
disp(p4)
disp('roots')
disp(lamda4 = roots(p4))