import rpyc


server_host = "localhost"
server_port = 18811
conn = rpyc.connect(server_host, port=server_port)

calc_services = conn.root

print("Somando (8**2) + 51**3")
resultado = calc_services.resolve('(8**2) + 51**3')
print(resultado)