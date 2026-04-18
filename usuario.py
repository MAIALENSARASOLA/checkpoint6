class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

# Creamos un usuario de prueba
maialen = Usuario("Maialen", "P@ssword123")

# Comprobamos que funciona imprimiendo los datos
print("Nombre:", maialen.nombre)
print("Contraseña:", maialen.contraseña)