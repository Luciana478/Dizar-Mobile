import PySimpleGUI

font = ("Century Gothic", 36)
otherFont = ("Consolas",18)
otherFontChild = ("Segoe UI",18)
PySimpleGUI.theme("Reddit")
layout = [
    [PySimpleGUI.Image(r"C:\Users\Usuário\OneDrive\-fire_86891.png"),PySimpleGUI.Text("FIRE ",font=font),PySimpleGUI.Button("Execute",font=otherFontChild,border_width=0),PySimpleGUI.Button("Stop",font=otherFontChild,border_width=0)],
    [PySimpleGUI.Text("1.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont,default_text="print('hello, world'),")],
    [PySimpleGUI.Text("2.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont)],
    [PySimpleGUI.Text("3.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont)],
    [PySimpleGUI.Text("4.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont)],
    [PySimpleGUI.Text("5.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont)],
    [PySimpleGUI.Text("6.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont)],
    [PySimpleGUI.Text("7.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont)],
    [PySimpleGUI.Text("8.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont)],
    [PySimpleGUI.Text("9.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont)],
    [PySimpleGUI.Text("10.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont)],
    [PySimpleGUI.Text("11.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont)],
    [PySimpleGUI.Text("12.",font=otherFont),PySimpleGUI.Input(size=80,border_width=0,font=otherFont)],
]

PyWindow = PySimpleGUI.Window("Fire 2021", layout)

while True:
    eventos, valores = PyWindow.Read()
    if eventos == PySimpleGUI.WIN_CLOSED:
        break
