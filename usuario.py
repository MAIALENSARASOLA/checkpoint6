class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

usuario1 = Usuario("maialen", "1234")

print(usuario1.nombre_usuario)
print(usuario1.contrasena)
