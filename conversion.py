# Elaborado por Daniel Hernando Mantilla 
# Código: 1005040227
from afd import AFD
from afnd import AFND
from graphviz import *
class Conversion(AFND):
    #clase conversion que hereda de la clase AFND
    def __init__(self):
        #constructor de la clase conversion
        #se inicializan los atributos de la clase
        #se llama al constructor de la clase padre
        #se inicializa el atributo afd de tipo AFD en blanco
        super().__init__()
        self.afd = self.createBlankAFD()
    
    def showMenu(self):
        #metodo que muestra el menu de opciones
        #1. ingresar el alfabeto
        #2. ingresar los estados
        #3. ingresar los estados iniciales
        #4. ingresar los estados finales
        #5. ingresar las transiciones
        #6. ingresar las transiciones epsilon
        #7. ver el automata
        #8. ejecutar el automata
        #9. ver el diagrama del automata
        #10. convertir el automata a AFD
        #11. ver el AFD
        #12. ejecutar el AFD
        #13. ver el diagrama del AFD
        #0. salir
        # si la opción ingresada no es válida
        # se muestra un mensaje de error
        # y se vuelve a solicitar la opción
        # hasta que se ingrese una opción válida
        # si la opción ingresada es válida
        # se retorna la opción
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
        #metodo que crea un AFD en blanco
        #se crea un objeto de tipo AFD y se retorna
        afd = AFD()
        afd.states = []
        afd.initial_states = []
        afd.final_states = []
        afd.transitions = []
        return afd
    
    def addStates(self, states, state):
        #metodo que añade los estados a la lista de estados
        #se recorrer las letras del alfabeto
        #se obtienen los estados siguientes llamando al metodo getNextStates
        #se recorre la lista de estados siguientes
        #si el estado siguiente no está en la lista de estados
        #se añade el estado siguiente a la lista de estados
        #se llama recursivamente al metodo addStates
        for letter in self.alphabet:
            nextStates = self.getNextStates(state, letter)
            for nextState in nextStates:
                if nextState not in states and nextState != "Ø": #Ø es el estado muerto
                    states.append(nextState)
                    self.addStates(states, nextState)
        return states
    
    def getAFNDStates(self):
        #metodo que obtiene los estados del AFD
        #se inicializa con los estados iniciales
        #se llama al metodo addStates para añadir los estados siguientes
        #se retorna la lista de estados
        states = self.initial_states[:]
        self.addStates(states, self.initial_states[0])
        return states
    
    def getNextStates(self, state, letter):
        #metodo que obtiene los estados siguientes
        #se inicializa la lista de estados siguientes en blanco
        #se recorre la lista de transiciones
        #si el estado actual es igual al estado actual de la transición
        #y la letra es igual a la letra de la transición
        #se añade el estado siguiente a la lista de estados siguientes
        #si no se encuentra ninguna transición
        #se añade el estado Ø a la lista de estados siguientes
        #se retorna la lista de estados siguientes
        nextStates = []
        add = False
        for transition in self.transitions:
            if transition["current_state"] == state and transition["letter"] == letter:
                nextStates.append(transition["next_state"])
                add = True
        if not add:
            nextStates.append("Ø")
        return nextStates

    def getAFNDTransitions(self):
        #metodo que obtiene las transiciones del AFD
        #se inicializa la lista de transiciones en blanco
        #se recorre la lista de estados
        #se recorre la lista de letras del alfabeto
        #se obtienen los estados siguientes llamando al metodo getNextStates
        #se recorre la lista de estados siguientes
        #se añade la transición a la lista de transiciones
        #se retorna la lista de transiciones
        transitions = []
        for state in self.afd.states:
            for letter in self.alphabet:
                nextStates = self.getNextStates(state, letter)
                if len(nextStates) > 0:
                    transitions.append({"current_state": state, "letter": letter, "next_state": nextStates})
                else: # añade transicion al conjunto vacio
                    transitions.append({"current_state": state, "letter": letter, "next_state": "Ø"})
        return transitions

    def convertAFNDtoAFD(self):
        #metodo que convierte el AFND a AFD
        #se crea un AFD en blanco llamando al metodo createBlankAFD
        #llama al metodo getAFNDStates para obtener los estados del AFD
        #llama al metodo getAFNDTransitions para obtener las transiciones del AFD
        #muestra un mensaje de que el AFD se ha creado correctamente
        self.clearConsole()
        self.afd = self.createBlankAFD()
        self.afd.alphabet = self.alphabet
        self.afd.final_states = self.final_states
        self.afd.states = self.getAFNDStates()
        self.afd.initial_states = self.initial_states[0]
        self.afd.transitions = self.getAFNDTransitions()
        input("AFD generado")
        self.showMenu()


if __name__ == "__main__":
    #se crea un objeto de tipo conversion
    #se llama al metodo showMenu
    conversion = Conversion()
    conversion.showMenu()