import bluetooth

socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

ADDRESS = "DC:A6:32:49:22:59"
PORT = 1
try:
        socket.connect((ADDRESS, PORT))
except:
        print("AVVIA PRIMA IL SERVER! ;D")
        exit(0)
try:
    while True:
            socket.send(input("Inserisci un carattere da inviare: "))

            print(socket.recv(1024).decode())
except:
    print("Connessione chiusa.")
    socket.close()