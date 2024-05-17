class IdCliente:
    def __init__(self, fecha_de_registro, vip):
        self._fecha_de_registro = fecha_de_registro
        self._vip = vip

    @property
    def fecha_de_registro(self):
        return self._fecha_de_registro

    @fecha_de_registro.setter
    def fecha_de_registro(self, nueva_fecha):
        self._fecha_de_registro = nueva_fecha

    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, nuevo_estado):
        self._vip = nuevo_estado

    def mostrar_cliente(self):
        return f'fecha_de_registro:{self._fecha_de_registro},vip:{self._vip}'

if __name__=='__main__':
    cliente1 = IdCliente(fecha_de_registro="2023-03-11", vip=True)
    print(cliente1.mostrar_cliente())
    print(cliente1.fecha_de_registro)
    cliente1.fecha_de_registro = '2024-03-11'
    print(cliente1.vip)
    cliente1.vip = True
