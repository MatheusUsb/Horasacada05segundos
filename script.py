import time

def show_current_time():
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print("Hora atual:", current_time)
        time.sleep(5) 

show_current_time()