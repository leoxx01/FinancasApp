from datetime import datetime

data = datetime.now()

data = str(data)

ano = data[0:4]
mes = data.split('-')

print(f"{ano}-{mes[1]}-01")

print(data)