from csv_handler import *
from utils import type_effect
from revision import *
from menu import menu

def main():
    type_effect('Hello, Elliott. What are you going to revise today? \n', speed=0.05)
    menu()

main()  # Start the program
