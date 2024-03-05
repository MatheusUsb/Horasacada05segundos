# Horasacada05segundos
# Script em Python que mostra a hora atual a cada 5 segundos

import time

def show_current_time():
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print("Hora atual:", current_time)
        time.sleep(5)  # Aguarda 5 segundos

show_current_time()
