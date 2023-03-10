from datetime import datetime
from time import time;

print()
ts = time()
print("Hoje é:",datetime.utcfromtimestamp(ts).strftime('%d/%m/%Y')) 
print()


import datetime
hora_atual = datetime.datetime.now()
print("A hora atual é:", hora_atual.strftime("%H:%M:%S"))
print()