inventario= [
	{"hostname": "Core-SW01", "ip": "10.0.0.1", "status": "up"},
	{"hostname": "Dist-SW02", "ip": "10.0.0.2", "status": "down"},
	{"hostname": "Access-SW03", "ip": "10.0.0.3", "status": "up"},
	{"hostname": "Edge-R01", "ip": "172.16.1.1", "status": "down"}
]

#Imprimir todos los hostnames
print("Hostnames")
print("______________________")
for h in inventario:
	print(h["hostname"])
print("______________________")
#Imprimir todas las IPS
print("IPS")
print("______________________")
for a in inventario:
    print(a["ip"])
print("______________________")
print("Downs")
#Imprimir todos los que esten en down
print("______________________")
for p in inventario:
    if p["status"] == "down":
        print(p["hostname"])
print("______________________")