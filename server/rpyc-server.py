import rpyc


class CalculadoraService(rpyc.Service):
    def exposed_resolve(self, expression):
        if isinstance(expression, str):
            result = eval(expression)
        else:
            result = "Expression not found"
        return result


if __name__ == "__main__":
    server = rpyc.ThreadedServer(CalculadoraService, port = 18811)
    server.start()