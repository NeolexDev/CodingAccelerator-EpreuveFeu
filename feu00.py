""" Créez un programme qui affiche un rectangle dans le terminal. """
import sys

def check_args():
   if len(sys.argv) != 3:
      print("Usage: python feu00.py <width> <height>")
      sys.exit(1)
   width = int(sys.argv[1])
   height = int(sys.argv[2])
   return width, height

def print_rectable(width, height):
   print("o" + "-" * (width - 2) + "o")
   for i in range(height-2):
      print("|" + " " * (width - 2) + "|")
   if height > 1:
        print("o" + "-" * (width - 2) + "o")

def main():
   width, height = check_args()
   print_rectable(width, height)
main()