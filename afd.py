import os
from graphviz import *


class AFD:
    def __init__(self):
        self.alphabet = ["a", "b"]
        self.states = ["s1", "s2", "s3"]
        self.initial_state = "s1"
        self.final_states = ["s3"]
        self.transitions = [
            {"current_state": "s1", "letter": "a", "next_state": "s2"},
            {"current_state": "s1", "letter": "b", "next_state": "s1"},
            {"current_state": "s2", "letter": "a", "next_state": "s3"},
            {"current_state": "s2", "letter": "b", "next_state": "s1"},
            {"current_state": "s3", "letter": "a", "next_state": "s2"},
            {"current_state": "s3", "letter": "b", "next_state": "s3"}
        ]

    def clearConsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def showMenu(self):
        self.clearConsole()
        print("1. Ingresar alfabeto")
        print("2. Ingresar estados")
        print("3. Ingresar estado inicial")
        print("4. Ingresar estados finales")
        print("5. Ingresar transiciones")
        print("6. Ver AFD")
        print("7. Ejecutar AFD")
        print("8. Ver diagrama de estados")
        print("0. Salir")
        option = input("Ingrese una opción: ")
        if option == "1":
            self.setAlphabet()
        elif option == "2":
            self.setStates()
        elif option == "3":
            self.setInitialState()
        elif option == "4":
            self.setFinalStates()
        elif option == "5":
            self.setTransitions()
        elif option == "6":
            self.showAFD()
        elif option == "7":
            self.executeAFD()
        elif option == "8":
            self.showAFDDiagram()
        elif option == "0":
            exit()
        else:
            print("Opción inválida")
            input("")
            self.showMenu()

    def setAlphabet(self):
        self.clearConsole()
        self.alphabet = input(
            "Ingrese el alfabeto separado por comas: ").split(",")
        self.showMenu()

    def setStates(self):
        self.clearConsole()
        self.states = input(
            "Ingrese los estados separados por comas: ").split(",")
        self.showMenu()

    def setInitialState(self):
        self.clearConsole()
        self.initial_state = input("Ingrese el estado inicial: ")
        self.showMenu()

    def setFinalStates(self):
        self.clearConsole()
        self.final_states = input(
            "Ingrese los estados finales separados por comas: ").split(",")
        self.showMenu()

    def setTransitions(self):
        self.clearConsole()
        self.transitions = []
        for state in self.states:
            for letter in self.alphabet:
                next_state = input(
                    "Ingrese el estado siguiente para la transición " + state + " - " + letter + ": ")
                self.transitions.append(
                    {"current_state": state, "letter": letter, "next_state": next_state})
        self.showMenu()

    def showTransitionTable(self):
        print("Tabla de transiciones:")
        print("\t", end="")
        for letter in self.alphabet:
            print(letter, end="\t")
        print()
        for state in self.states:
            print(state, end="\t")
            for letter in self.alphabet:
                for transition in self.transitions:
                    if transition["current_state"] == state and transition["letter"] == letter:
                        print(transition["next_state"], end="\t")
            print()

    def showAFD(self, callback=None):
        self.clearConsole()
        print("Alfabeto: ", self.alphabet)
        print("Estados: ", self.states)
        print("Estado inicial: ", self.initial_state)
        print("Estados finales: ", self.final_states)
        self.showTransitionTable()
        input("\nRegresar...")
        if callback is not None:
            callback()
        else:
            self.showMenu()

    def executeAFD(self, callback=None):
        self.clearConsole()
        word = input("Ingrese la palabra a evaluar: ")
        current_state = self.initial_state
        for letter in word:
            if letter in self.alphabet:
                for transition in self.transitions:
                    if transition["current_state"] == current_state and transition["letter"] == letter:
                        current_state = transition["next_state"]
                        break
            else:
                print("La palabra no pertenece al lenguaje")
                input("\nRegresar...")
                self.showMenu()
        if current_state in self.final_states:
            print("La palabra pertenece al lenguaje")
        else:
            print("La palabra no pertenece al lenguaje")
        input("\nRegresar...")
        if callback is not None:
            callback()
        else:
            self.showMenu()

    def showAFDDiagram(self, callback=None):
        self.clearConsole()
        diagram = Digraph(comment="Diagrama de estados")
        diagram.attr(rankdir='LR', size='8,5')
        diagram.node('ini', shape='Mdiamond')
        for state in self.states:
            if state in self.final_states:
                diagram.node(state, shape='doublecircle')
            else:
                diagram.node(state)
        diagram.edge('ini', self.initial_state)
        for transition in self.transitions:
            diagram.edge(transition["current_state"],
                         transition["next_state"], label=transition["letter"])
        diagram.render(filename='diagram.gv', directory='diagrams',
                       view=True, cleanup=True, format='svg')
        if callback is not None:
            callback()
        else:
            self.showMenu()


if __name__ == "__main__":
    afd = AFD()
    afd.showMenu()