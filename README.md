# Checkpoint 6

**Estudiante:** Maialen  
**Curso:** Full Stack Development Program  

---

## Introducción

En este checkpoint voy a explicar algunos conceptos básicos de Programación Orientada a Objetos en Python y también algunos conceptos relacionados con APIs.

La idea es entender qué son, para qué sirven y ver ejemplos sencillos.

---

## 1. ¿Para qué usamos clases en Python?

Las clases se usan para organizar mejor el código y para crear objetos.

Una clase funciona como una plantilla. Después, a partir de esa plantilla, podemos crear objetos con sus propios datos.

Por ejemplo, si quiero trabajar con usuarios, puedo crear una clase `Usuario` y luego hacer varios usuarios sin tener que escribir lo mismo todo el rato.

Sirven para:

- organizar el código
- reutilizar código
- representar cosas del mundo real dentro del programa

### Ejemplo

```python
class Perro:
    pass
### Explicación del ejemplo

En este ejemplo, Perro es una clase vacía.

Todavía no hace mucho, pero ya sirve como base para crear objetos más adelante.

## 2. ¿Qué método se ejecuta automáticamente al crear una instancia?

El método que se ejecuta automáticamente es __init__.

Este método sirve para darle valores iniciales al objeto cuando lo creamos.

Por ejemplo, si creamos una persona, ahí podemos guardar su nombre o su edad.

### Ejemplo
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

p1 = Persona("Maialen")
print(p1.nombre)
Explicación del ejemplo

Aquí, __init__ se ejecuta cuando creamos p1.

El valor "Maialen" se guarda en self.nombre.

Después, al imprimirlo, sale el nombre guardado.

## 3. ¿Cuáles son los tres verbos de API más comunes?

Tres verbos muy comunes en APIs son:

GET → sirve para obtener datos
POST → sirve para enviar o crear datos
DELETE → sirve para borrar datos

Se usan para que una aplicación pueda comunicarse con un servidor.

### Ejemplo sencillo

Si una tienda online quiere mostrar productos, normalmente usa GET.

Si un usuario se registra, se suele usar POST.

Si quiere borrar su cuenta, se puede usar DELETE.

## 4. ¿MongoDB es SQL o NoSQL?

MongoDB es una base de datos NoSQL.

No funciona con tablas como las bases de datos SQL.

En lugar de eso, guarda la información en documentos parecidos a JSON.

Esto hace que sea más flexible cuando los datos no son siempre iguales.

Ejemplo sencillo

En una base de datos SQL, normalmente todos los registros tienen columnas fijas.

En MongoDB, un documento puede tener unos campos y otro documento puede tener otros diferentes.

Eso da más libertad en algunos proyectos.

5. ¿Qué es una API?

Una API es una forma de comunicación entre programas.

Sirve para que una aplicación pueda pedir información o enviar datos a otra.

Por ejemplo, una página web puede pedir datos a un servidor usando una API.

Ejemplo sencillo

Cuando una app del tiempo te enseña la temperatura de tu ciudad, normalmente está usando una API para pedir esos datos a otro servicio.

6. ¿Qué es Postman?

Postman es una herramienta que sirve para probar APIs.

Con Postman podemos mandar peticiones como GET o POST y ver qué responde el servidor.

Es útil porque nos permite comprobar si una API funciona sin tener que hacer primero una página web completa.

Ejemplo de uso

Con Postman puedo:

poner una URL
elegir el tipo de petición
enviar la petición
ver la respuesta

Por ejemplo, si hago una petición GET, puedo ver si me devuelve una lista de usuarios.

7. ¿Qué es el polimorfismo?

El polimorfismo significa que una misma acción puede funcionar de manera distinta según el objeto.

En palabras más simples, es cuando algo tiene el mismo nombre o la misma idea, pero no hace exactamente lo mismo en todos los casos.

### Ejemplo
print(len("hola"))
print(len([1, 2, 3]))
Explicación del ejemplo

Aquí usamos len() en un texto y también en una lista.

La función es la misma, pero funciona con tipos de datos distintos.

En los dos casos devuelve la longitud.

8. ¿Qué es un método dunder?

Los métodos dunder son métodos especiales de Python.

Se escriben con doble guion bajo al principio y al final, por ejemplo: __init__.

Python los usa para hacer acciones especiales dentro de las clases y objetos.

Algunos ejemplos
__init__ → para iniciar datos del objeto
__str__ → para mostrar el objeto como texto
__len__ → para definir la longitud
Ejemplo
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
Explicación del ejemplo

En este caso, __init__ es un método dunder que se usa para guardar el título del libro cuando creamos el objeto.

9. ¿Qué es un decorador de Python?

Un decorador es una función que modifica o añade algo a otra función sin cambiar su código por dentro.

Sirve para agregar comportamiento extra.

Ejemplo
def mi_decorador(func):
    def wrapper():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return wrapper

@mi_decorador
def saludar():
    print("Hola")

saludar()
Explicación del ejemplo

Primero se ejecuta el mensaje de antes.

Luego se ejecuta la función saludar().

Y al final se imprime el mensaje de después.

Así, el decorador añade algo sin cambiar la función original.

Ejercicio práctico: clase Usuario
class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

usuario1 = Usuario("Maialen", "1234")

print("Nombre:", usuario1.nombre)
print("Contraseña:", usuario1.contraseña)
Explicación del ejercicio

En este ejercicio he creado una clase llamada Usuario.

Cuando creo un objeto, guardo dos datos: el nombre y la contraseña.

Después los imprimo para comprobar que se han guardado bien.

Conclusión

En este checkpoint he trabajado conceptos básicos de clases, objetos, APIs y herramientas como Postman.

También he repasado ideas importantes de Python como __init__, los métodos dunder, el polimorfismo y los decoradores.

Todo esto me sirve para entender mejor cómo se organiza el código y cómo se comunican las aplicaciones.


Y este sería tu archivo **`usuario.py`**:

```python
class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

usuario1 = Usuario("Maialen", "1234")

print("Nombre:", usuario1.nombre)
print("Contraseña:", usuario1.contraseña)

