import PySimpleGUI as sg
import zip_creator

label1=sg.Text("Select files to compress")
input1=sg.Input()
choose_button1=sg.FilesBrowse("choose",key="files")

label2=sg.Text("Select destination folder:")
input2=sg.Input()
choose_button2=sg.FolderBrowse("choose",key="folder")

compress_button=sg.Button("Compress")
output_label=sg.Text(key="output")

window=sg.Window("File Compressor",
                 layout=[[label1,input1,choose_button1],
                         [label2,input2,choose_button2],
                         [compress_button,output_label]])
while True:
    event,values=window.read()
    match event:
        case "Compress":
            filepaths=values["files"].split(";")
            folder=values["folder"]
            zip_creator.make_archive(filepaths,folder)
            window["output"].update(value="compression compeleted")
        case sg.WINDOW_CLOSED:
            break

window.close()