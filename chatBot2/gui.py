import PySimpleGUI as sg
from bot import chatbot

sg.theme("DarkTeal")

layout = [
    [sg.Text("You: "), sg.InputText(key="-INPUT-")],
    [sg.Button("Send", bind_return_key=True), sg.Button("Clear")],
    [sg.Text("Bot: "), sg.Text(size=(40, 1), key="-OUTPUT-")],
]

window = sg.Window("Python Basic", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Send":
        user_input = values["-INPUT-"]
        bot_response = chatbot.get_response(user_input)  # Use a instância de ChatBot importada
        window["-OUTPUT-"].update(bot_response)
    elif event == "Clear":
        window["-INPUT-"].update("")

window.close()