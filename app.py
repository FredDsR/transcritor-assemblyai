import PySimpleGUI as sg
import assemblyai as aai

transcription_config = aai.TranscriptionConfig(
    language_code='pt',
    punctuate=True,
    format_text=True
)

sg.theme('DarkAmber') 

layout = [  [sg.Text('API Key:', key='teste'), sg.InputText(key='apikey', password_char='*')],
            [sg.Text('Buscar arquivo:'), sg.Input(), sg.FileBrowse(key='filepath')],
            [sg.Button('Ok'), sg.Text('', key='status', justification='center', expand_x=True)],
            [sg.Multiline('Sua transcrição vai aparecer aqui.', key='textbox', expand_x=True, size=(5,10))]]

window = sg.Window('Transcreve pra mim!', layout).Finalize()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Ok':
        try:
            window['status'].update('Trabalhando nisso!')

            aai.settings.api_key = values['apikey']
            transcriber = aai.Transcriber(config=transcription_config)
            transcript = transcriber.transcribe(values['filepath'])
            
            window['status'].update('Tudo pronto!')
            window['textbox'].update(transcript.text)
        except Exception as err:
            sg.Print('Um erro aconteceu :/\nChame seu desenvolvedor!\n\nEssa foi a mensagem do computador:\n\n')
            sg.Print(err)

window.close()
