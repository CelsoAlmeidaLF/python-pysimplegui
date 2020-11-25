
import PySimpleGUI as sg
import os
import sys

class Program:

    """class Program"""
    def __init__(self):
        """contruct"""
        self.__init__
        sg.theme('Dark Blue')   # Add a touch of color
        pass
        
    def Program(self):
        """Method Init Program""" 

        layout = self.Layout()
        title = 'Titulo do meu projeto'
        gui = self.GUI(title, layout)
        self.Event(gui)
        gui.close()
        pass

    def GUI(self, title, layout):
        """Create the Window"""
        return sg.Window( title , layout)

    def Layout(self):
        # All the stuff inside your window.
        layout = [  [sg.Text('label')],
                    [sg.Text('digite seu texto aqui:'), sg.InputText()],
                    #[sg.Multiline('', size=(45,5)) ],
                    [sg.Button('Ok'), sg.Button('Cancel')] 
                 ]
        return layout

    def Event(self, gui):
        """Event Loop to process "events" and get the "values" of the inputs"""
        while True:
            event, values = gui.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            print('You entered ', values[0])
        pass

#if __name__ == "__main__":
#    import sys
#    prog = Program()
#    prog.Program()