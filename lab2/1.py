#mid point
import sympy as sm

x = sm.symbols('x')
f_x = x**3+1
a_limit = -2
b_limit = 2
num = 8
h = (b_limit-a_limit)/num

interval_points = []
for i in range(a_limit*10, b_limit*10+1, 5):
    interval_points.append(i/10)
print("Point in interval with h: ", interval_points)


mid_point_interval = []
for i in range(len(interval_points)-1):
    mid_point_interval.append((interval_points[i]+interval_points[i+1])/2)
print("Mid_points in interval:   ", mid_point_interval)


solution = 0
for i in mid_point_interval:
    solution += h*f_x.subs(x, i)
print("Solution by mid point rule: ", solution)

direct_solution = sm.integrate(eval(str(f_x)), (x, a_limit, b_limit))
print("Direct solution by integration: ", direct_solution)

Error = abs(direct_solution-solution)
print("error:   ", Error)

diff_f = sm.diff(f_x, x)
diff_ff = sm.diff(diff_f, x)
theory_error = (b_limit-a_limit)*diff_ff.subs(x, b_limit)/24*h**2
print("Theory error: ", theory_error)