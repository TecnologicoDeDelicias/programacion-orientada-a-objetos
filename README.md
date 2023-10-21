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

    def incrementarEdad(self):
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
juan = Persona("Juan", 30);
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

Tema por desarrollar

### 2.4 Métodos: declaración, mensajes, paso de parámetros, retorno de valores

Tema por desarrollar

### 2.5 Constructores y destructores declaración, uso y aplicaciones

Tema por desarrollar

### 2.6 Sobrecarga de métodos

Tema por desarrollar

### 2.7 Sobrecarga de operadores: Concepto y utilidad, operadores unarios y binarios

Tema por desarrollar

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
