#!/usr/bin/python3
import math

def euler_method_with_derivative(dy_dx, y0, x0, x_end, dx):
    x_values = [x0]
    y_values = [y0]
    dy_dx_values = [dy_dx(y0)]

    while x_values[-1] < x_end:
        x_current = x_values[-1]
        y_current = y_values[-1]
        dy_dx_current = dy_dx(y_current)

        y_next = y_current + dy_dx_current * dx
        x_next = x_current + dx
        dy_dx_next = dy_dx(y_next)

        x_values.append(x_next)
        y_values.append(y_next)
        dy_dx_values.append(dy_dx_next)

    # Print the results for each step
    print("x\t\ty\t\tdy/dx")
    for x, y, dydx in zip(x_values, y_values, dy_dx_values):
        print(f"{x:.3f}\t\t{y:.4f}\t\t{dydx:.4f}")
        print(100*(y - math.exp(x))/math.exp(x))

# Define the differential equation dy/dx = y
def dy_dx(y):
    return y

# Parameters
x0 = 0.0       # Initial x value
y0 = 1.0       # Initial y value
x_end = 50.0   # End value of x for the calculation
dx = 0.00001   # Smaller step size

# Run Euler's method with derivative display
euler_method_with_derivative(dy_dx, y0, x0, x_end, dx)
