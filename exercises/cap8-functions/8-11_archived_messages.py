def show_messages(sent_messages):
    for sent_message in sent_messages:
        print(sent_message)


def send_messages(texts, sent_messages):
    while texts:
        current_text = texts.pop()
        print(f"moving the text:{current_text}")
        sent_messages.append(current_text)
        print(f"the text:{current_text}is moved")

texts = ['saca','los','pedos','tiezos','de','la','olla','cuadrada','de','satanas','el','chile','peludo']
sent_messages = []
#verificar el orde de llamado de funciones
#enviar primero los mensajes
send_messages(texts, sent_messages)
#despues mostras los enviados
show_messages(sent_messages)
#pasando una copia de lista
send_messages(texts[:],sent_messages)