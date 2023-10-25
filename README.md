# Programación Orientada a Objetos

Esta asignatura aporta al perfil del Ingeniero la capacidad de analizar, desarrollar, implementar y administrar software de aplicación orientado a objetos, cumpliendo con estándares de calidad, con el fin de apoyar la productividad y competitividad de las organizaciones.

## Plan de trabajo

Los detalles de la materia así como el plan de trabajo pueden ser consultados en el siguiente [documento](https://www.delicias.tecnm.mx/doc/Oferta_Educativa/Sistemas/2Semestre/ProgramacionOrientadaaObjetos.pdf).

### Requisitos para tomar la materia

- Equipo de cómputo
- Conexión a Internet
- Cuenta de Github
- Instalar editor de código (VSCode recomendable)

### Criterios de Evaluación

- Examen 50%
- Prácticas y tareas 40% (Cada práctica/tarea tendrá criterios específicos)
- Asistencia y puntualidad 10%

> :eyes: Nota: Para tener derecho al examen deberá contar con todas las prácticas/tareas realizadas y entregadas en tiempo y forma

## Unidad 1: Introducción al paradigma de la programación orientada a objetos

En esta unidad se presentan los conceptos de la programación orientada a objetos, teniendo la intención de introducir al estudiante en los elementos del modelo de objetos, así como el uso básico del lenguaje de modelado unificado.

### 1.1 Elementos del modelo de objetos: clases, objetos, abstracción, modularidad, encapsulamiento, herencia y polimorfismo.

La Programación Orientada a Objetos (POO) es un paradigma de programación enfocado en representar los objetos del mundo real y de este modo simular de una manera más precisa las diferentes necesidades de un sistema o aplicación.

Un **objeto** puede representar tanto elementos físicos (carro, producto, etc..), personas (usuario, estudiante, etc..) o incluso conceptos abstractos resultantes de la interacción de los usuarios con el sistema (venta, compra, pedido, etc..).

Una **clase** sirve como una plantilla de la cual se definen las características (atributos) y operaciones (métodos) que los objetos que pertenecen a dicha clase pueden contener.

![Clase y Objeto](./docs/images/clase-objeto.png)

Por ejemplo, la clase `Automovil` puede contener los atributos `marca`, `modelo`, `tipoDeTransmision`, etc.., y los métodos `arrancar`, `acelerar`, `frenar`, etc...

![Objeto carro con atributos y métodos](./docs/images/objeto-carro-atributos-metodos.png)

Dependiendo del contexto del sistema a desarrollar, los atributos y métodos pueden variar en número y complejidad, ya que es posible que una clase defina atributos de otras clases. Por ejemplo, en algunos sistemas, bastará con que el atributo motor sea una simple cadena de texto, pero en otros un objeto de la clase `Motor` con sus propios atributos y métodos.

Se le conoce como **instancia** a un objeto creado a partir de una clase concreta que contiene un estado inicial, el cual puede ser modificado durante la ejecución del programa.

![Ejemplo de instancia](./docs/images/ejemplo_instancia.png)

La **abstracción** es el proceso de definir el grado de detalle que una clase debe contener. A mayor detalle, menor abstracción y viceversa.

![Ejemplo de Abstracción](./docs/images/abstraccion-concepto.jpeg)

La **modularidad** se refiere al proceso de dividir un sistema complejo en diferentes subelementos (módulos) que contemplan funciones o características afines.

![Ejemplo de Modularidad](./docs/images/modularidad-concepto.jpeg)

El **encapsulamiento** es el proceso por el cual ciertos detalles de implementación son ocultados al usuario final y solamente se muestra lo necesario para poder interctuar con los objetos y/o clases.

![Ejemplo de Encapsulamiento](./docs/images/encapsulamiento-concepto.jpeg)

La **herencia** es el mecanismo por el cual las clases pueden compartir sus atributos y métodos, permitiendo así poder crear una jerarquía de objetos con rasgos comunes, y agregar nuevos comportamientos y atributos, así como de redefinir los heredados por las clases base.

![Ejemplo de Herencia](./docs/images/herencia-ejemplo-basico.png)

El **polimorfismo** es una propiedad que permite a los objetos interactuar de diferentes formas según sea el contexto de la ejecución. Las formas más comunes de polimorfismo se presentan en la Sobrecarga de métodos y la Sobre-escritura.

![Ejemplo de Polimorfismo](./docs/images/polimorfismo-ejemplo-basico.png)

### 1.2 Lenguaje de modelado unificado: diagrama de clases

UML es un lenguaje de modelado estándar que nos permite representar visualmente los diferentes elementos que componen un sistema.

Para representar una clase, se puede utilizar la notación UML que se muestra a continuación:

![Clase Persona en UML](./docs/images/diagrama-clase-persona.jpeg)

Un diagrama de clases muestra un conjunto de clases, interfaces y colaboraciones, así como sus relaciones. Gráficamente, un diagrama de clases es una colección de nodos y arcos.

![Diagrama de clases](./docs/images/diagrama-clases-ejemplo.png)

Los diagramas de clases se utilizan para modelar la vista de diseño estática de un sistema. Esto incluye, principalmente, modelar el vocabulario del sistema, modelar las colaboraciones o modelar los esquemas.

## Unidad 2: Clases y objetos

Esta unidad se centra en la definición e implementación de clases y objetos permitiendo al estudiante adquirir las competencias fundamentales de la programación orientada a objetos.

### 2.1 Declaración de clases: atributos, métodos, encapsulamiento

La declaración de una clase consiste en definir la estructura de la misma.

Veamos unos ejemplos simples en diferentes lenguajes.

Java:

```java
class Persona {}
```

Python:

```python
class Persona:
  pass
```

Ruby:

```ruby
class Persona
end
```

Javascript:

```js
class Persona {}
```

C++:

```cpp
class Persona {};
```

Con lo anterior, solamente hemos definido el nombre de la clase. Vamos a agregar los atributos `nombre`, `edad` y `vive` con sus tipos de datos correspondientes.

Java:

```java
class Persona {
  String nombre;
  int edad;
  boolean vive;
}
```

Python:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.vive = True
```

Ruby:

```ruby
class Persona
  attr_accessor :nombre, :edad, :vive
end
```

Javascript:

```js
class Persona {
  nombre;
  edad;
  vive;
}
```

C++:

```cpp
#include <string>

class Persona {
public:
    std::string nombre;
    int edad;
    bool vive;
};
```

> :eyes: Observe que en algunos lenguajes no es necesario indicar explícitamente el tipo de dato, ya que el lenguaje resuelve de manera dinámica el tipo necesario

Los atributos nos permiten almacenar información pertinente sobre cada objeto que se cree a partir de la clase, las cuales pueden (o no) ser modificadas durante la ejecución del programa.

Por último vamos a definir algunos métodos básicos, como por ejemplo `saludar`, `incrementarEdad` y `morir`.

Java:

```java
class Persona {
  String nombre;
  int edad;
  boolean vive;

  void saludar() {
    System.out.println("Hola, mi nombre es " + nombre);
  }

  void incrementarEdad() {
    edad = edad + 1;
  }

  void morir() {
    vive = false;
  }
}
```

Python:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.vive = True

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def incrementar_edad(self):
        self.edad = self.edad + 1

    def morir(self):
        self.vive = False
```

Ruby:

```ruby
class Persona
  attr_accessor :nombre, :edad, :vive

  def saludar
    puts "Hola, mi nombre es #{@nombre}"
  end

  def incrementar_edad
    @edad = @edad + 1
  end

  def morir
    @vive = false
  end
end
```

Javascript:

```js
class Persona {
  nombre;
  edad;
  vive;

  saludar() {
    console.log(`Hola, mi nombre es ${this.nombre}`);
  }

  incrementarEdad() {
    this.edad = this.edad + 1;
  }
}
```

C++:

```cpp
#include <iostream>
#include <string>

class Persona {
public:
    std::string nombre;
    int edad;
    bool vive;

    void saludar() {
      std::cout << "Hola, mi nombre es " << nombre << std::endl;
    }

    void incrementarEdad() {
      edad++;
    }

    void morir() {
      vive = false;
    }
};
```

Cada lenguaje define la manera en que los métodos son declarados, así como si es necesario especificar un valor de retorno, tal es el caso de Java y C++, los cuales para el caso de no retornar un valor se debe emplear la palabra reservada `void` (vacío).

Uno de los problemas con las declaraciones anteriores es que los atributos y métodos son accesibles por otras clases, pudiendo modificar y leer sus valores directamente, lo cual puede romper el encapsulamiento de la clase.

Por ejemplo:

Java:

```java
class Persona {
  // Atributos y métodos
}

// Otra clase
public class Programa {
  public static void main(String[] args) {
    Persona juan = new Persona();
    juan.saludar();
    juan.nombre = "Pedro";
    juan.edad = -10;
    juan.vive = true;
    juan.saludar();

    juan.morir();
    juan.saludar();
    juan.vive = true;
  }
}
```

En este ejemplo, es posible escribir directamente los valores de los atributos por cualquier valor sin que existan restricciones, como es el caso del atributo vive, que puede ser modificado una vez que el método morir ha sido ejecutado.

Una mejor manera de escribir las clases es mantener los atributos privados y sólo tener métodos para acceder a ellos para agregar las validaciones correspondientes.

Java:

```java
class Persona {
  private String nombre;
  private int edad;
  private boolean vive = true;

  // otros métodos

  void morir() {
    if (vive) {
      vive = false;
    }
  }

  void saludar() {
    if (vive) {
      System.out.println("Hola, mi nombre es " + nombre);
    } else {
      System.out.println("DEP: " + nombre);
    }
  }
}

// Otra clase
public class Programa {
  public static void main(String[] args) {
    Persona juan = new Persona("Juan", 30);
    juan.saludar();
    juan.morir();
    juan.saludar();
  }
}
```

En esta nueva versión de la clase Persona, los atributos son acompañados de la palabra clave private, la cual nos indica que solamente pueden ser accedidos dentro de la misma clase, pero no fuera de ella, y solo es posible interactuar a traves de los métodos de la misma.

#### Práctica: Crear la clase Persona en diferentes lenguajes

Instrucciones

1. Crear una carpeta llamada practicas/unidad2 en el repositorio personal
2. Dentro de la carpeta crear las siguientes carpetas y archivos correspondientes:

   - :file_folder: java
     - Persona.java
   - :file_folder: ruby
     - Persona.rb
   - :file_folder: python
     - Persona.py
   - :file_folder: js
     - Persona.js
   - :file_folder: cpp
     - Persona.cpp

3. Escribir el código correspondiente en cada archivo y ejecutarlo.

### 2.2 Instanciación de una clase

Instanciar se refiere al proceso de creación de un objeto a partir de una clase. Esto se logra a traves del uso del (los) constructor(es) de la clase. Ejemplos:

Java:

```java
Persona juan = new Persona("Juan", 30);
// o alternativamente
var juan = new Persona("Juan", 30);
```

Python:

```python
juan = Persona("Juan", 30)
```

Ruby:

```ruby
juan = Persona.new("Juan", 30);
```

Javascript:

```js
const juan = new Persona("Juan", 30);
```

C++:

```cpp
Persona juan("Juan", 30);
```

### 2.3 Referencia al objeto actual

Al momento de crear y manipular un objeto o instancia de una clase, es necesario en algunos casos hacer referencia asimismo dentro de la clase.

Para ello se utiliza una palabra reservada definida por el lenguaje. Aquí algunos ejemplos:

Java:

```java
class Persona {
  String nombre;

  // otro código ...

  boolean esMayorQue(Persona otraPersona) {
    // Utilizamos la palabra this para hacer referencia al objeto actual
    // No es requerida a menos que el nombre de la variable o parámetro tenga conflicto con el atributo
    return this.edad > otraPersona.edad;
  }
}

// Ejemplo en uso

Persona juan = new Persona("Juan", 20);
Persona pedro = new Persona("Pedro", 15);

if (pedro.esMayorQue(juan)) {
  System.out.println("Pedro es mayor que Juan");
} else if (juan.esMayorQue(pedro)) {
  System.out.println("Juan es mayor que Pedro");
} else {
  System.out.println("Ambos tienen la misma edad");
}

```

Python:

```python
class Persona:
  # otro código...

  # Se usa la palabra self para hacer referencia al objeto actual
  def es_mayor_que(self, otra_persona):
    return self.edad > otra_persona.edad

# Ejemplo de uso
juan = Persona("Juan", 20)
pedro = Persona("Pedro", 15)

if juan.es_mayor_que(pedro):
  print("Juan es mayor que Pedro")
elif pedro.es_mayor_que(juan):
  print("Pedro es mayor que Juan")
else:
  print("Ambos tienen la misma edad")

```

Ruby:

```ruby
class Persona
  # otro código

  # se usa la palabra self para hacer referencia al objeto actual
  def es_mayor_que(otra_persona)
    return self.edad > otra_persona.edad
  end

  # es posible acceder a los atributos utilizando un @ antes del nombre del atributo
  def es_mayor_de_edad
    @edad > 18 # la palabra return es opcional
  end

end

# Ejemplo de uso
juan = Persona.new("Juan", 20)
pedro = Persona.new("Pedro", 15)

if juan.es_mayor_que(pedro)
  puts "Juan es mayor que Pedro"
elsif pedro.es_mayor_que juan # No es necesario poner el paréntesis para llamar la función
  puts "Pedro es mayor que Juan"
else
  puts "Ambos tienen la misma edad"
end

```

#### Práctica: Agregar métodos con referencia al objeto actual

Instrucciones:

1. En su repositorio de ejemplos cree un nuevo branch llamado `practica-referencia-objeto-actual`

```
git branch practica-referencia-objeto-actual
```

2. Hacer checkout al nuevo branch

```
git checkout practica-referencia-objeto-actual
```

3. Agregue el método `esMayorQue` en los diferentes lenguajes
4. Una vez terminados los cambios haga commit

```
git commit -m "Se agregan ejemplos de referencia al objeto actual"
```

5. Haga push con la siguiente instrucción

```
git push -u origin practica-referencia-objeto-actual
```

6. Cree un Pull Request y añada al profesor como revisor y a algún compañero de clase

7. Una vez revisado el código haga merge a `main`

### 2.4 Métodos: declaración, mensajes, paso de parámetros, retorno de valores

En la programación orientada a objetos (POO), un método es una función o procedimiento asociado a un objeto particular o a una clase. Los métodos son una de las características clave de la POO y se utilizan para representar el comportamiento de los objetos y las operaciones que pueden realizar.

Los métodos son una parte fundamental de la POO y se utilizan para modelar el comportamiento de objetos en un programa. Permiten la modularidad, la reutilización de código y la representación de comportamiento específico de objetos, lo que hace que la programación orientada a objetos sea una metodología poderosa y flexible para el desarrollo de software.

### Declaración de métodos

Cada lenguaje define su sintaxis para declarar métodos, pero de manera general estos son los elementos principales:

- **Nombre del método**: por lo general se utilizan verbos en infinitivo que indican una acción tales como: `imprimir`, `mostrar`, `dibujar`, etc... Normalmente son escritos en minúsculas, pero en caso de contener 2 o más palabras se puede usar la notación camel case (ejemplo: `imprimirReporte`) o la notación snake case (ejemplo: `imprimir_reporte`).

- **Visibilidad**: Algunos lenguajes permiten definir la visibilidad de los métodos a traves de palabras reservadas como `private`, `package`, `public`, o a traves de otros mecanismos.

- **Tipo de método**: Algunos lenguajes permiten definir métodos de instancia o métodos de clase, siendo estos últimos definidos por la palabra clave `static`.

- **Parámetros**: Un método puede contener 0 o multiples parámetros siendo el límite definido por el lenguaje. Normalmente se busca que la cantidad de parámetros no exceda de 4 para su facilidad de uso.

- **Tipo de retorno**: En algunos lenguajes es requerido definir el tipo de retorno explícitamente, como es el caso de Java y C++. En el caso de que no exista un valor de retorno algunos lenguajes utilizan el tipo `void`.

- **Cuerpo del método**: Aquí es donde se definen las operaciones o algoritmos propios del método. Normalmente un método debe ser concreto y cumplir solamente una única responsabilidad.

A continuación se muestran algunos ejemplos en diferentes lenguajes

Java:

```java
public class Persona {

  public void saludar() {
    // aquí va el cuerpo del método
  }

  public static void metodoEstatico() {
    System.out.println("Este método se puede invocar sin necesidad de un objeto")
  }

  // También es posible pasar objetos de clases que hemos creado nosotros
  public boolean meGusta(Comida comida) {
    return this.comidasFavoritas.contains(comida);
  }

  private String contarSecreto() {
    return "Solo yo puedo invocar este método";
  }
}

// Uso

Persona juan = new Persona("Juan", 20);

juan.addComidaFavorita(chocolate);
juan.addComidaFavorita(pizza);

// Este método puede ser invocado desde cualquier lugar ya que es público
juan.saludar();

// No es necesario tener una instancia de clase para usar este método
Persona.metodoEstatico()

// Aunque es valido usar:

juan.metodoEstatico()

// Esto nos daria un error de compilación, ya que el método es privado
String secreto = juan.contarSecreto();

// Aquí vemos el uso de parámetros
boolean gustaBrocoli = juan.meGusta(brocoli);

```

Python:

En Python, no existen clases públicas o privadas de la misma manera que en algunos otros lenguajes de programación, como Java o C++. Python sigue el principio de "consentimiento del adulto" en lugar de "imposición", lo que significa que no restringe el acceso a los miembros de una clase. En su lugar, confía en convenciones y buenas prácticas para lograr la encapsulación y proteger la privacidad de los miembros de la clase.

Sin embargo, Python utiliza una convención para indicar que ciertos miembros de una clase no deben ser accedidos desde fuera de la clase. Esta convención es la siguiente:

Los miembros (atributos o métodos) cuyos nombres comienzan con un guion bajo (`_`) se consideran "privados" y no deberían ser accedidos directamente desde fuera de la clase. Por ejemplo, `_mi_atributo` o `_mi_metodo()`.

Los miembros cuyos nombres comienzan y terminan con dos guiones bajos (`__`) tienen un comportamiento de "name mangling" y son más difíciles de acceder desde fuera de la clase. Por ejemplo, `__mi_atributo` se convierte en `_nombre_de_clase__mi_atributo`.
Es importante destacar que estas convenciones son solo un acuerdo entre los desarrolladores y el lenguaje en sí no impide el acceso a estos miembros de ninguna manera. Si bien puedes acceder a los miembros "privados" de una clase en Python, es una práctica recomendada no hacerlo directamente y respetar la privacidad de los atributos y métodos.

En resumen, Python no implementa explícitamente el concepto de clases públicas o privadas, pero fomenta la encapsulación y la protección de miembros de clase a través de convenciones y buenas prácticas de programación.

```python
class Persona:
  atributo_de_clase = 42

  def saludar():
    # aquí va el cuerpo del método

  def metodo_estatico():
    print("Este es un método estático")

  def me_gusta(self, comida):
    return comida in self.comidas_favoritas

  def __contar_secreto():
    return "Solo yo puedo invocar este método"

  @classmethod
  def metodo_de_clase(cls):
    print(f"Este es un método de clase. El valor del atributo de clase es {cls.atributo_clase}")


# Uso

juan = Persona("Juan", 20)
juan.add_comida_favorita(chocolate)
juan.add_comida_favorita(pizza)

# Saludar puede ser invocado desde cualquier lugar
juan.saludar();

# Llamada al método estático desde la clase
Persona.metodo_estatico()
# Llamada desde el objeto

juan.metodo_estatico()

# Intentar acceder al método privado generará un error:
secreto = juan.__contar_secreto();

# Método que recibe un parámetro
gusta_brocoli = juan.me_gusta(brocoli);

# Llamando a método de clase
Persona.metodo_de_clase()
juan.metodo_de_clase

```

### 2.5 Constructores y destructores declaración, uso y aplicaciones

En programación orientada a objetos (POO), un constructor y un destructor son métodos especiales que se utilizan para inicializar y liberar recursos de un objeto, respectivamente. Estos conceptos son especialmente relevantes en lenguajes de programación que gestionan la asignación y liberación de memoria de manera explícita, como C++.

#### Constructor

Un constructor es un método especial que se llama automáticamente cuando se crea una instancia (objeto) de una clase.
Su función principal es inicializar los atributos del objeto y realizar cualquier tarea de inicialización necesaria.
Los constructores suelen recibir argumentos que se utilizan para configurar el objeto durante la creación.
Los constructores tienen el mismo nombre que la clase y no tienen un tipo de retorno explícito.
En muchos lenguajes, una clase puede tener varios constructores con diferentes parámetros, lo que se conoce como sobrecarga de constructores.

Veamos algunos ejemplos:

Java:

```java

public class Boton {
  // otras propiedades y atributos ...

  // Constructor sin argumentos
  public Boton() {
    this("Boton", 100, 300);
  }
  // Constructor con un argumento
  public Boton(String texto) {
    this(texto, 100, 300);
  }

  private Boton(String texto, int alto, int ancho) {
    this.texto = texto;
    this.alto = alto;
    this.ancho = ancho;
  }
}

// Uso

Boton boton1 = new Boton();
Boton boton2 = new Boton("Boton 2");

// Esto produce un error ya que no se puede acceder al constructor privado
Boton boton3 = new Boton("Boton 3", 50, 400);
```

Python:

```python
class Boton:
  def __init__(self, texto = "Boton", alto = 100, ancho = 300)
    self.texto = texto
    self.alto = alto
    self.ancho = ancho

# Uso

if __name__ == "__main__":
  boton1 = Boton()
  boton2 = Boton("Boton 2")
  boton3 = Boton("Boton 3", 50, 400)
```

#### Destructor

Un destructor es un método especial que se llama automáticamente cuando un objeto se destruye o sale de ámbito.
Su función principal es liberar los recursos utilizados por el objeto, como memoria dinámica u otros recursos adquiridos durante la vida del objeto.

En algunos lenguajes, como C++, los destructores se utilizan para garantizar una limpieza adecuada y prevenir pérdidas de memoria y fugas de recursos.

En lenguajes de programación gestionados por recolección de basura, como Java o Python, la gestión de la memoria se realiza automáticamente, y los programadores no necesitan preocuparse por los destructores. En su lugar, se utilizan métodos de finalización o recolección de basura para liberar recursos.

```cpp
class MiClase {
public:
    MiClase() {
        // Constructor
    }

    ~MiClase() {
        // Destructor
        // Realizar tareas de limpieza aquí
    }
};
```

### 2.6 Sobrecarga de métodos

La sobrecarga de métodos en programación orientada a objetos (POO) es un concepto que permite definir múltiples métodos con el mismo nombre en una clase, pero con diferentes listas de argumentos (parámetros). En otras palabras, es la capacidad de una clase de tener varios métodos con el mismo nombre, pero cada uno de ellos acepta un conjunto distinto de parámetros.

La sobrecarga de métodos permite que una clase ofrezca diferentes funcionalidades o comportamientos basados en la cantidad o el tipo de argumentos que recibe. Esto hace que el código sea más flexible y fácil de usar, ya que los programadores pueden llamar al método con diferentes argumentos según sus necesidades.

En lenguajes de programación como Java o C++, la sobrecarga de métodos se basa en la firma del método, que incluye el nombre del método y la lista de tipos de parámetros. Los métodos sobrecargados deben tener el mismo nombre pero una firma de parámetros diferente.

Java:

```java
class Reservacion {

  void reservar(Date fechaInicio, Date fechaFin) {
    // lógica para reservar dentro de esas fechas
  }

  void reservar(Date fechaInicio, int numeroDeDias) {
    // lógica para reservar desde una fecha dada y calcular la fecha fin en base al # de días
  }
}

```

En Python, Ruby o Javascript no existe el concepto como tal, si no que se tendría que determinar el tipo de dato dentro del método

Javascript:

```js
class Reservacion {
  reservar(fechaInicio, parametro) {
    if (typeof parametro === "number") {
      // lógica para cuando se pasa un número
    } else {
      // lógica para cuando se pasa otro dato
    }
  }
}
```

### 2.7 Sobrecarga de operadores: Concepto y utilidad, operadores unarios y binarios

La sobrecarga de operadores o también llamada "Operator Overloading" es una funcionalidad que algunos lenguajes utilizan para definir más de una operación para un operador dado.

El ejemplo más común es el operador +, que dependiendo de los operandos, realiza una funcionalidad distinta.

Veamos un ejemplo en Java:

Java:

```java
var resultado1 = 145 + 25;
System.out.println(resultado1);


var resultado2 = 145 + "25";
System.out.println(resultado2);
```

En algunos lenguajes como C++, C# o Python, es posible redefinir las operaciones aritméticas de clases personalizadas.

C++

```cpp
#include <iostream>

class NumeroComplejo {
public:
    NumeroComplejo(double real, double imaginario) : real(real), imaginario(imaginario) {}

    NumeroComplejo operator+(const NumeroComplejo& otro) {
        return NumeroComplejo(real + otro.real, imaginario + otro.imaginario);
    }

    void mostrar() {
        std::cout << real;
        if (imaginario >= 0) {
            std::cout << " + " << imaginario << "i";
        } else {
            std::cout << " - " << -imaginario << "i";
        }
        std::cout << std::endl;
    }

private:
    double real;
    double imaginario;
};

int main() {
    NumeroComplejo numero1(3.0, 4.0);  // Crea un número complejo (3 + 4i)
    NumeroComplejo numero2(1.5, -2.5); // Crea otro número complejo (1.5 - 2.5i)

    NumeroComplejo suma = numero1 + numero2; // Suma los números complejos

    std::cout << "Número 1: ";
    numero1.mostrar(); // Muestra el primer número complejo
    std::cout << "Número 2: ";
    numero2.mostrar(); // Muestra el segundo número complejo
    std::cout << "Suma: ";
    suma.mostrar(); // Muestra el resultado de la suma

    return 0;
}

```

Python:

```cpp
class NumeroComplejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __add__(self, otro):
        suma_real = self.real + otro.real
        suma_imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(suma_real, suma_imaginario)

    def mostrar(self):
        if self.imaginario >= 0:
            print(f"{self.real} + {self.imaginario}i")
        else:
            print(f"{self.real} - {abs(self.imaginario)}i")

# Crear dos números complejos
numero1 = NumeroComplejo(3.0, 4.0)   # Número complejo (3 + 4i)
numero2 = NumeroComplejo(1.5, -2.5)  # Número complejo (1.5 - 2.5i)

# Sumar los números complejos
suma = numero1 + numero2

# Mostrar los números complejos y su suma
print("Número 1:")
numero1.mostrar()
print("Número 2:")
numero2.mostrar()
print("Suma:")
suma.mostrar()
```

## Unidad 3: Herencia

Esta unidad tiene como propósito la creación de objetos que incorporen propiedades y métodos de otros objetos, construyéndolos a partir de éstos sin necesidad de reescribirlo todo.

### 3.1 Definición: clase base, clase derivada

Tema por desarrollar

### 3.2 Clasificación: herencia simple, herencia múltiple

Tema por desarrollar

### 3.3 Reutilización de miembros heredados

Tema por desarrollar

### 3.4 Referencia al objeto de la clase base

Tema por desarrollar

### 3.5 Constructores y destructores en clases derivadas

Tema por desarrollar

### 3.6 Redefinición de métodos en clases derivadas

## Unidad 4: Polimorfismo

Esta unidad trata una de las características fundamentales de la programación orientada a objetos: el polimorfismo, que permite reutilizar métodos con el mismo nombre, pero con relación a la clase a la que pertenece cada uno, con comportamientos diferentes.

### 4.1 Definición

Tema por desarrollar

### 4.2 Clases abstractas: definición, métodos abstractos, implementación de clases abstractas, modelado de clases abstractas

Tema por desarrollar

### 4.3 Interfaces: definición, implementación de interfaces, herencia de interfaces

Tema por desarrollar

### 4.4 Variables polimórficas (plantillas): definición, uso y aplicaciones

Tema por desarrollar

### 4.5 Reutilización de código

Tema por desarrollar

## Unidad 5: Excepciones

En esta unidad se tratan situaciones excepcionales que se presentan en tiempo de ejecución.

### 5.1 Definición

Tema por desarrollar

### 5.2 Tipos de excepciones

Tema por desarrollar

### 5.3 Propagación de excepciones

Tema por desarrollar

### 5.4 Gestión de excepciones: manejo de excepciones, lanzamiento de excepciones

Tema por desarrollar

### 5.5 Creación y manejo de excepciones definidas por el usuario

Tema por desarrollar

## Unidad 6: Flujos y archivos

En esta unidad se aplican las operaciones necesarias para el manejo de archivos de texto y binarios, temas que se utilizarán en materias posteriores.

### 6.1 Definición

Tema por desarrollar

### 6.2 Clasificación: Archivos de texto y binarios

Tema por desarrollar

### 6.3 Operaciones básicas y tipos de acceso

Tema por desarrollar

### 6.4 Manejo de objetos persistentes

Tema por desarrollar
