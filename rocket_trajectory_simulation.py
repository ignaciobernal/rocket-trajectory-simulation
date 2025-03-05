# Importing packages
import sympy as sym
import numpy as np
t = sym.Symbol("t")

# Constants declaration
tc = float(input("Moment of end of combustion (s): ")) # RECOMMENDED VALUE tc = 11
theta = float(input("Optimal angle (rad): ")) # RECOMMENDED VALUE theta = 0.75
g = 9.81
ve = float(input("Gas exit velocity: ")) # RECOMMENDED VALUE ve = 1200
b = float(input("Constant b: ")) # RECOMMENDED VALUE b = 0.055
sen = np.sin(theta)
ln = sym.log(1 - b*t)
fact1 = 1
fact2 = 2
fact3 = 6
f_t = t + (1 - b*t)*ln/b

# {Function vy} and symbolic derivatives
vy = -ve*sen*ln - g*t

#derivada primera
der1_vy = sym.diff(vy, t)

#derivada segunda
der2_vy = sym.diff(der1_vy, t)

#derivada tercera
der3_vy = sym.diff(der2_vy, t)


# Function and numeric derivativs
vy_tc = sym.sympify(vy).subs(t,tc)
der1_vy_tc = sym.sympify(der1_vy).subs(t,tc)
der2_vy_tc = sym.sympify(der2_vy).subs(t,tc)
der3_vy_tc = sym.sympify(der3_vy).subs(t,tc)

# Taylor polynomial of degree 3 of vy at tc
pvy_t = vy_tc + der1_vy_tc*(t - tc) + (der2_vy_tc/fact2)*(t - tc)**2 + (der3_vy_tc/fact3)*(t - tc)**3
    
# Numeric polynomial
pvy_tc = sym.sympify(pvy_t).subs(t,tc)
print('Vertical speed vy = ',pvy_tc,' m/s')

# {Function y_t} and symbolic derivatives
y = ve*sen*f_t - (g/2)*t**2

#derivada primera
der1_y = sym.diff(y, t)

#derivada segunda
der2_y = sym.diff(der1_y, t)

#derivada tercera
der3_y = sym.diff(der2_y, t)


# Function and numeric derivatives
f_tc = sym.sympify(f_t).subs(t,tc)
y_tc = sym.sympify(y).subs(t,tc)
der1_y_tc = sym.sympify(der1_y).subs(t,tc)
der2_y_tc = sym.sympify(der2_y).subs(t,tc)
der3_y_tc = sym.sympify(der3_y).subs(t,tc)

# Taylor polynomial of degree 3 of y(t) at tc
py_t = y_tc + der1_y_tc*(t - tc) + (der2_y_tc/fact2)*(t - tc)**2 + (der3_y_tc/fact3)*(t - tc)**3
    
# Numerical polynomial
py_tc = sym.sympify(py_t).subs(t,tc)
print('Vertical position y = ',py_tc,' m')
