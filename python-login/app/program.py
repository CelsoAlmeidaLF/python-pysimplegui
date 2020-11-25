
import PySimpleGUI as sg
import os
import sys

class Program:

    """class Program"""
    def __init__(self):
        """contruct"""
        self.__init__
        sg.theme('Reddit')   # Add a touch of color
        pass
        
    def Program(self):
        """Method Init Program""" 

        layout = self.Layout()
        title = 'Login'
        gui = self.GUI(title, layout)
        self.Event(gui)
        gui.close()
        pass

    def GUI(self, title, layout):
        """Create the Window"""
        return sg.Window( title , layout)

    def Layout(self):
        # All the stuff inside your window.
        layout = [  
                    #[sg.Text('label')],
                    [sg.Text('Usuario:', size=(7,1)), sg.InputText(key='user',size=(20,1))],
                    [sg.Text('Senha:', size=(7,1)), sg.InputText(key='senha',size=(20,1))],
                    [sg.Checkbox('Salvar o login?')],
                    #[sg.Multiline('', size=(45,5)) ],
                    [sg.Button('Entrar')] 
                 ]
        return layout

    def Event(self, gui):
        """Event Loop to process "events" and get the "values" of the inputs"""
        while True:
            event, values = gui.read()
            if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                break
            if event == 'Entrar':
                if values['user']=='Celso' and values['senha']=='35316':
                   print("Ola, %s" % values['user'] ) 
        pass