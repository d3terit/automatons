from afd import AFD
from afnd import AFND
from graphviz import *

class Conversion(AFND):
    def __init__(self):
        super().__init__()
        self.alphabet = ["a", "b"]
        self.states = ["q0", "q1", "q2", "q3"]
        self.initial_states = ["q0","q2"]
        self.final_states = ["q3"]
        self.transitions = [
            {"current_state": "q0", "letter": "a", "next_state": "q1"},
            {"current_state": "q0", "letter": "b", "next_state": "q2"},
            {"current_state": "q1", "letter": "a", "next_state": "q3"},
            {"current_state": "q1", "letter": "b", "next_state": "q2"},
            {"current_state": "q2", "letter": "a", "next_state": "q1"},
            {"current_state": "q2", "letter": "b", "next_state": "q3"},
            {"current_state": "q3", "letter": "a", "next_state": "q3"},
            {"current_state": "q3", "letter": "b", "next_state": "q3"}
        ]
        self.epsilon_transitions = [
            {"current_state": "q0", "letter": "b", "next_state": "q1"},
            {"current_state": "q0", "letter": "a", "next_state": "q2"},
            {"current_state": "q1", "letter": "b", "next_state": "q3"},
            {"current_state": "q2", "letter": "a", "next_state": "q3"}
        ]
        self.afd = self.createBlankAFD()
    
    def showMenu(self):
        self.clearConsole()
        print("1. Ingresar alfabeto")
        print("2. Ingresar estados")
        print("3. Ingresar estados iniciales")
        print("4. Ingresar estados finales")
        print("5. Ingresar transiciones")
        print("6. Ingresar transiciones epsilon")
        print("7. Ver AFND")
        print("8. Ejecutar AFND")
        print("9. Ver diagrama de estados")
        print("10. Convertir AFND a AFD")
        print("11. Ver AFD")
        print("12. Ejecutar AFD")
        print("13. Ver diagrama de estados AFD")
        print("0. Salir")
        option = input("Ingrese una opción: ")
        if option == "1":
            self.setAlphabet()
        elif option == "2":
            self.setStates()
        elif option == "3":
            self.setInitialStates()
        elif option == "4":
            self.setFinalStates()
        elif option == "5":
            self.setTransitions()
        elif option == "6":
            self.addEpsilonTransition()
        elif option == "7":
            self.showAFND()
        elif option == "8":
            self.executeAFND()
        elif option == "9":
            self.showAFNDDiagram()
        elif option == "10":
            self.convertAFNDtoAFD()
        elif option == "11":
            self.afd.showAFD(self.showMenu)
        elif option == "12":
            self.afd.executeAFD(self.showMenu)
        elif option == "13":
            self.afd.showAFDDiagram(self.showMenu)
        elif option == "0":
            exit()

    def createBlankAFD(self):
        afd = AFD()
        afd.states = []
        afd.initial_states = []
        afd.final_states = []
        afd.transitions = []
        return afd
    
    def getAFNDStates(self):
        states = []
        for state in self.initial_states:
            states.append(self.getAFNDState(state))
        return states

    def convertAFNDtoAFD(self):
        self.clearConsole()
        self.afd = self.createBlankAFD()
        self.afd.alphabet = self.alphabet
        self.afd.final_states = self.final_states
        newStates = [self.initial_states]
        
        self.afd.states = self.getAFNDStates()
        input("AFD generado")
        self.showMenu()


if __name__ == "__main__":
    conversion = Conversion()
    conversion.showMenu()