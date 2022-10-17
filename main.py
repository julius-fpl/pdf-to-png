from pdf2image import convert_from_path

poppler_path = r"poppler\Library\bin"
def start():
    pdf = input(r"pdf Pfad angeben:")
    output = input(r"Pfad angeben zum exportieren" + "\n" + r"(z.B. C:\Users\Julius\Downloads\Bild.png Achtung befindet sich ein Bild mit dem selben Namen im Zielordner wird es überschrieben!)" + "\n" + r"oder 1 drücken (dann wird die Datei in den Ordner der .exe gespeichert)")
    if output == "1":
        output = "out.png"
    print("PDF wird zu PNG umgewandelt. Geschätzte Zeit: 5 sec.")
    convert(pdf, output)

def convert(pdf, output):
    try:
        pages = convert_from_path(pdf, 500, poppler_path=poppler_path)
    except:
        print("Datei konnte nicht eingelesen werden!")
    try:
        for page in pages:
            page.save(output, 'PNG')
    except:
        print("Datei konnte nicht umgewandelt / gespeichert werden!")
    i  = input("Gespeichert als " + output + "\n drücken Enter um das Programm zu verlassen oder 1 um es noch einmal zu starten!")
    if i == "1":
        start()

start()