""" Créez un programme qui reçoit une expression arithmétique dans une chaîne de caractères et en retourne le résultat après l’avoir calculé. """
import sys

operators =  "+*-/%()"

# get the next element in the string
def next_element(string):
   if string[0] in operators:
         return string[0]
   element = ""
   for c in string:
      if c in operators:
         if element.strip() == "":
            element+=c
            return element
         else:
            return element
      element+=c
   return element

# Translate the INFIX expression to Postfix RPN expression 
def to_rpn(string):
   string = string.strip()
   rpn = ""
   operator_stack = []
   stack = []
   last_operator = ''
   element = next_element(string)
   while element:
      string = string[len(element):]
      stripped_element = element.strip()
      if stripped_element in operators:
         if stripped_element == ")":
            while True:
               popped = operator_stack.pop()
               if popped == '(':
                  break
               stack.append(popped)
         elif stripped_element == "(":
            operator_stack.append(stripped_element)
         else:
            if len(operator_stack):
               last_operator = operator_stack[len(operator_stack)-1]
               if len(last_operator) and last_operator in "/*%":
                  stack.append(operator_stack.pop())
            operator_stack.append(stripped_element)
      else:
         stack.append(stripped_element)
      if len(string)  == 0:
         while len(operator_stack) > 0:
            popped = operator_stack.pop()
            stack.append(popped)
         return stack
      
      element = next_element(string)
   return rpn

# Evaluate a RPN expression
def eval_rpn(rpn):
   stack = []
   for c in rpn:
      if c.isdigit():
         stack.append(int(c))
      else:
         right = stack.pop()
         left = stack.pop()
         res = 0
         if c == '+':
            res = left+right
         elif c == '-':
            res = left-right
         elif c == '*':
            res = left*right
         elif c == '/':
            res = left/right
         elif c == '%':
            res = left%right
         stack.append(res)
   return stack[0]

def main():
   rpn = to_rpn(sys.argv[1])
   print(eval_rpn(rpn))

main()