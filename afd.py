# Elaborado por Daniel Hernando Mantilla
# Código: 1005040227
import os
from graphviz import *


class AFD:
    # clase para representar un automata finito determinista

    def __init__(self):
        # constructor
        # inicializa los atributos de la clase
        # alphabet: lista de caracteres que representan el alfabeto
        # states: lista de estados del automata
        # initial_states: lista de estados iniciales del automata
        # final_states: lista de estados finales del automata
        # transitions: lista de transiciones del automata
        #   cada transicion es un diccionario con las llaves
        #   current_state: estado actual
        #   letter: letra de la transicion
        #   next_state: estado siguiente
        #   ej: {"current_state": "q0", "letter": "a", "next_state": "q1"}
        self.alphabet = ["0", "1"]
        self.states = ["s0", "s1", "s2", "s3", "s4", "s5", "s6",
                       "s7", "s8", "s9", "s10", "s11", "s12", "s13", "s14", "s15"]
        self.initial_state = "s0"
        self.final_states = ["s7", "s15"]
        self.transitions = [
            {"current_state": "s0", "letter": "0", "next_state": "s1"},
            {"current_state": "s0", "letter": "1", "next_state": "s1"},
            {"current_state": "s1", "letter": "0", "next_state": "s2"},
            {"current_state": "s1", "letter": "1", "next_state": "s2"},
            {"current_state": "s2", "letter": "0", "next_state": "s3"},
            {"current_state": "s2", "letter": "1", "next_state": "s3"},
            {"current_state": "s3", "letter": "0", "next_state": "s4"},
            {"current_state": "s3", "letter": "1", "next_state": "s4"},
            {"current_state": "s4", "letter": "0", "next_state": "s5"},
            {"current_state": "s4", "letter": "1", "next_state": "s5"},
            {"current_state": "s5", "letter": "0", "next_state": "s6"},
            {"current_state": "s5", "letter": "1", "next_state": "s6"},
            {"current_state": "s6", "letter": "0", "next_state": "s7"},
            {"current_state": "s6", "letter": "1", "next_state": "s7"},
            {"current_state": "s7", "letter": "0", "next_state": "s8"},
            {"current_state": "s7", "letter": "1", "next_state": "s8"},
            {"current_state": "s8", "letter": "0", "next_state": "s9"},
            {"current_state": "s8", "letter": "1", "next_state": "s9"},
            {"current_state": "s9", "letter": "0", "next_state": "s10"},
            {"current_state": "s9", "letter": "1", "next_state": "s10"},
            {"current_state": "s10", "letter": "0", "next_state": "s11"},
            {"current_state": "s10", "letter": "1", "next_state": "s11"},
            {"current_state": "s11", "letter": "0", "next_state": "s12"},
            {"current_state": "s11", "letter": "1", "next_state": "s12"},
            {"current_state": "s12", "letter": "0", "next_state": "s13"},
            {"current_state": "s12", "letter": "1", "next_state": "s13"},
            {"current_state": "s13", "letter": "0", "next_state": "s14"},
            {"current_state": "s13", "letter": "1", "next_state": "s14"},
            {"current_state": "s14", "letter": "0", "next_state": "s15"},
            {"current_state": "s14", "letter": "1", "next_state": "s15"},
            {"current_state": "s15", "letter": "0", "next_state": "s8"},
            {"current_state": "s15", "letter": "1", "next_state": "s8"},
        ]

    def clearConsole(self):

        # función para limpiar la consola
        # dependiendo del sistema operativo
        # en el que se ejecute el programa
        # se usa el comando adecuado
        # para limpiar la consola
        # en windows: cls
        # en linux: clear
        # en mac: clear
        os.system('cls' if os.name == 'nt' else 'clear')

    def showMenu(self):
        # función para mostrar el menú de opciones
        # y solicitar la opción a ejecutar
        # 1: ingresar alfabeto
        # 2: ingresar estados
        # 3: ingresar estado inicial
        # 4: ingresar estados finales
        # 5: ingresar transiciones
        # 6: mostrar automata
        # 7: validar cadena
        # 8: ver diagrama de estados
        # 0: salir
        # si la opción ingresada no es válida
        # se muestra un mensaje de error
        # y se vuelve a solicitar la opción
        # hasta que se ingrese una opción válida
        # si la opción ingresada es válida
        # se retorna la opción
        self.clearConsole()
        print("Menú principal")
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
        # función para ingresar el alfabeto
        # se solicita al usuario que ingrese
        # el alfabeto separado por comas
        self.clearConsole()
        self.alphabet = input(
            "Ingrese el alfabeto separado por comas: ").split(",")
        self.showMenu()

    def setStates(self):
        # función para ingresar los estados
        # se solicita al usuario que ingrese
        # los estados separados por comas
        self.clearConsole()
        self.states = input(
            "Ingrese los estados separados por comas: ").split(",")
        self.showMenu()

    def setInitialState(self):
        # función para ingresar el estado inicial
        # se solicita al usuario que ingrese
        # el estado inicial
        self.clearConsole()
        self.initial_state = input("Ingrese el estado inicial: ")
        self.showMenu()

    def setFinalStates(self):
        # función para ingresar los estados finales
        # se solicita al usuario que ingrese
        # los estados finales separados por comas
        self.clearConsole()
        self.final_states = input(
            "Ingrese los estados finales separados por comas: ").split(",")
        self.showMenu()

    def setTransitions(self):
        # función para ingresar las transiciones
        # se solicita al usuario que ingrese
        # las transiciones por cada estado y letra
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
        # función para mostrar la tabla de transiciones
        # en forma de tabla
        # se recorre el alfabeto
        # y se muestra el estado siguiente
        # para cada estado y letra
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
        # función para mostrar el AFD
        # se muestra el alfabeto
        # los estados
        # el estado inicial
        # los estados finales
        # y la tabla de transiciones
        # si se pasa una función como parámetro
        # se ejecuta la función al finalizar
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
        # función para ejecutar el AFD
        # se solicita al usuario que ingrese una cadena a validar
        # se valida la cadena ingresada con el AFD
        # si la cadena es válida se muestra un mensaje de aceptación
        # si la cadena no es válida se muestra un mensaje de rechazo
        # si se pasa una función como parámetro se ejecuta la función al finalizar
        self.clearConsole()
        word = input("Ingrese la palabra a evaluar: ")
        current_state = self.initial_state
        for letter in word:
            if letter in self.alphabet:
                for transition in self.transitions:
                    if type(transition["next_state"]) is list:
                        if transition["current_state"] == current_state and transition["letter"] == letter:
                            current_state = transition["next_state"][0]
                            break
                    elif transition["current_state"] == current_state and transition["letter"] == letter:
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

    def getTransition(self, state):
        # función para obtener las transiciones de un estado
        # se recorren las transiciones y se obtienen las transiciones del estado ingresado
        # se retorna  una lista con las transiciones
        # si no hay transiciones se retorna una lista vacía
        transitions = []
        for transition in self.transitions:
            if transition["current_state"] == state:
                bol = False
                for transition2 in transitions:
                    if transition2["next_state"] == transition["next_state"]:
                        transition2["letter"] = f"{transition2['letter']}, {transition['letter']}"
                        bol = True
                if not bol:
                    transitions.append(transition)
        return transitions

    def calcTransitions(self):
        # función para calcular las transiciones
        # se recorren los estados y se obtienen las transiciones de cada estado
        # se recorren las transiciones y se obtienen las transiciones de cada estado siguiente
        transitions = []
        for state in self.states:
            for transition in self.getTransition(state):
                transitions.append(transition)
        return transitions

    def showAFDDiagram(self, callback=None):
        # función para mostrar el diagrama del AFD
        # crea un grafico con la librería graphviz
        # se recorren los estados y se agregan al grafico
        # se recorren las transiciones y se agregan al grafico
        # se muestra el grafico y se guarda en un archivo dentro de la carpeta diagrams
        # si se pasa una función como parámetro se ejecuta la función al finalizar
        self.clearConsole()
        diagram = Digraph(comment="Diagrama de estados")
        diagram.attr(rankdir="LR", size='100,50')
        for i in range(len(self.states)):
            if self.states[i] == self.initial_state:
                diagram.node(self.states[i], fillcolor="green", style="filled")
            if self.states[i] in self.final_states:
                diagram.node(self.states[i], shape='doublecircle')
            else:
                diagram.node(self.states[i])
        transitions = self.calcTransitions()
        for transition in transitions:
            if type(transition["next_state"]) == list:
                for next_state in transition["next_state"]:
                    if next_state in self.final_states:
                        diagram.edge(
                            transition["current_state"], next_state, label=transition["letter"], color="red")
                    else:
                        diagram.edge(transition["current_state"],
                                     next_state, label=transition["letter"])
            else:
                if transition["next_state"] in self.final_states:
                    diagram.edge(
                        transition["current_state"], transition["next_state"], label=transition["letter"], color="red")
                else:
                    diagram.edge(transition["current_state"],
                                 transition["next_state"], label=transition["letter"])
        diagram.node("init", shape='point')
        diagram.edge("init", self.initial_state)
        diagram.render(filename='diagram.gv', directory='diagrams',
                       view=True, format="jpg", cleanup=True)
        if callback is not None:
            callback()
        else:
            self.showMenu()


if __name__ == "__main__":
    # función para mostrar el menú
    # se crea una instancia de la clase AFD
    afd = AFD()
    afd.showMenu()
