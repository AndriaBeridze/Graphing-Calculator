import turtle
import math
from tkinter import * 
from tkinter import messagebox

wn = turtle.Screen()
equaton = ""
power, coefficient = [], []
seperate_expressions = []
current_index, current_string = 0, ""
do_you_want_to_continue = "Yes"
current_point = 0
x, y = [], []
tr = turtle.Turtle()
turtle.title("Graphing Calculator")
height, width = 200, 350
ty = 0

scr = turtle.Screen()

scr.setup(width=0.5, height=0.5)

tr.color("Red")
tr.hideturtle()
tr.speed("fastest")
tr.penup()
tr.goto(width, height)
tr.pendown()
tr.goto(width, -height)
tr.goto(-width, -height)
tr.goto(-width, height)
tr.goto(width, height)

tr.color("black")
tr.penup()
tr.goto(-width, 0)
tr.pendown()
tr.goto(width, 0)
tr.penup()
tr.goto(0, -height)
tr.pendown()
tr.goto(0, height)

for i in range(1, 20):
      point = i - 10
      tr.penup()
      tr.goto(point * width / 10, 5)
      tr.pendown()
      tr.goto(point * width / 10, -5)

for i in range(1, 20):
      point = i - 10
      tr.penup()
      tr.goto(5, point * height / 10)
      tr.pendown()
      tr.goto(-5, point * height / 10)


def calculate_equation(value):
      answer = 0
      if equation[0] == 's':
            answer = math.sin(value)
      elif equation[0] == 'c':
            answer = math.cos(value)
      else:
            for i in range(len(power)):
                  answer += coefficient[i] * value ** power[i]
      return answer

def DrawTrapeziod(a, b):
      tr.color("Blue")
      for i in range(4):
            if a[i] > 0:
                  a[i] = min(a[i], 10)
            else:
                  a[i] = max(a[i], -10)
            if b[i] > 0:
                  b[i] = min(b[i], 10)
            else:
                  b[i] = max(b[i], -10)
      tr.penup()
      tr.goto(a[3] * width / 10, b[3] * height / 10)
      tr.pendown()
      tr.begin_fill()
      for i in range(4):
            tr.goto(a[i] * width / 10, b[i] * height / 10)
      tr.end_fill()


def integral(x):
      global equation
      if equation == "sin(x)":
            return -math.cos(x)
      if equation == "cos(x)":
            return math.sin(x)
      answer = 0
      for i in range(len(coefficient)):
            if power[i] == -1:
                  answer += math.log(abs(x)) * coefficient[i]
            else:
                  answer += coefficient[i] / (power[i] + 1) * x ** (power[i] + 1)
      return answer

def derivative(x):
      global equation
      if equation == "sin(x)":
            return math.cos(x)
      if equation == "cos(x)":
            return -math.sin(x)
      answer = 0
      for i in range(len(coefficient)):
            answer += coefficient[i] * (power[i]) * x ** (power[i] - 1)
      return answer

equation = turtle.textinput("Function", "Enter Function")

if equation[0] != 's' and equation[0] != 'c':
      if equation[0] != '-':
            equation = "+" + equation

      for i in range(len(equation)):
            if equation[i] >= '0' and equation[i] <= '9':
                  if equation[i - 1] == '^':
                        current_string += '+'
            current_string += equation[i]

      equation = current_string

      for i in range(len(equation)):
            #Seperating Expressions
            current_string = ""
            if current_index > i:
                  continue
            while True:
                  if i == len(equation):
                        break
                  if equation[i] == '+' or equation[i] == '-':
                        if equation[i - 1] != '^' and i != current_index:
                              break

                  current_string += equation[i]
                  i += 1
            current_index = i
            seperate_expressions.append(current_string)

      for i in range(len(seperate_expressions)):
            expression = seperate_expressions[i]
            c, p = 0, 0
            is_c_positive, is_p_positive = True, True
            current_index = 0
            #Finding Coefficient of Exspression
            if expression[0] == '-':
                  is_c_positive = False
            current_index += 1
            while True:
                  if current_index != len(expression) and expression[current_index] >= '0' and expression[current_index] <= '9':
                        c = c * 10 + int(expression[current_index])
                  else:
                        break
                  current_index += 1
            if c == 0:
                  c = 1
            if is_c_positive == False:
                  c *= -1
            coefficient.append(c)
            #Finding Power of Expression
            while current_index != len(expression) and expression[current_index] != "x":
                  current_index += 1
            if current_index == len(expression):
                  power.append(0)
                  continue
            else:
                  if current_index == len(expression) - 1:
                        power.append(1)
                        continue
            current_index += 2
            if expression[current_index] == '-':
                  is_p_positive = False
            current_index += 1
            while True:
                  if current_index != len(expression) and expression[current_index] >= '0' and expression[current_index] <= '9':
                       p = p * 10 + int(expression[current_index])
                  else:
                        break
                  current_index += 1
            if is_p_positive == False:
                  p *= -1
            power.append(p)

current_point = -10
while current_point <= 10:
      y1 = calculate_equation(current_point)
      if y1 > 0:
            y.append(min(y1, 10))
      else:
            y.append(max(y1, -10))
      x.append(current_point)
      current_point += 0.1

for i in range(len(x)):
      if i == 0:
            tr.penup()
      if i != 0 and abs(y[i] - y[i - 1]) > 10:
            tr.penup()
      if y[i] == 10 or y[i] == -10:
            if i != 0 and y[i - 1] != y[i]:
                  tr.color("Blue")
            else:
                  tr.color("Red")
      else:
            tr.color("Blue")
      tr.goto(x[i] * width / 10, y[i] * height / 10)
      tr.pendown()

while do_you_want_to_continue == "Yes":
      operation = turtle.textinput("Function", "Integration - I / Differentiation - D")
      if operation == "I":
            a = float(turtle.textinput("Lower Bound", "Enter Lower Bound"))
            b = float(turtle.textinput("Upper Bound", "Enter Upper Bound"))
            current_point = a
            while current_point != b:
                  next_point = min(current_point + 0.1, b)
                  current_x = [current_point, next_point, next_point, current_point]
                  current_y = [0, 0, calculate_equation(next_point), calculate_equation(current_point)]
                  DrawTrapeziod(current_x, current_y)
                  current_point = min(current_point + 0.1, b)
            messagebox.showinfo("Answer", "Integral From " + str(a) + " To " + str(b) + " Equals To " + str(round(integral(b) - integral(a), 3)))
            
      elif operation == "D":
            tr.penup()
            x = float(turtle.textinput("Value", "Enter Value"))
            d = derivative(x)
            y = calculate_equation(x)
            current_point = -10
            while current_point < 10:
                  current_value = y + d * (current_point - x)
                  if current_value > 10:
                        current_value = 10
                  if current_value < -10:
                        current_value = -10
                  if current_value != 10 and current_value != -10:
                        tr.color("Blue")
                  tr.goto(current_point * width / 10, current_value * height / 10)
                  tr.pendown()
                  current_point += 0.1
                  if current_value == 10 or current_value == -10:
                        tr.color("Red")
            messagebox.showinfo("Answer", "Derivative At " + str(x) + " Equals To " + str(round(d, 3)))

      else:
            messagebox.showwarning("Alert", "Invalid Operation")
      do_you_want_to_continue = turtle.textinput("Continue", "Do You Want To Continue")

messagebox.showinfo("End", "End of Program")

wn.mainloop()
