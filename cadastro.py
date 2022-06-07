from PySimpleGUI import PySimpleGUI as sg
#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(20,2))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,2))],
    [sg.Checkbox('lembrar')],
    [sg.Button('Entrar')]
]
#janela
janela=sg.Window('Tela de login', layout)
#leitura
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'alezy' and valores['senha'] == '1234':
            print('Bem vindo Alezy')