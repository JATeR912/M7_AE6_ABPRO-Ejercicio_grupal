En equipos de 3 a 5 personas, desarrollen una aplicación web en Django que implemente un CRUD (Crear, Leer, Actualizar y Eliminar) para gestionar una base de datos específica. Asignen responsabilidades dentro del equipo para optimizar el desarrollo. Cada equipo deberá documentar su proceso y presentar el resultado final.

Contexto del Proyecto

Una organización sin fines de lucro necesita una plataforma para gestionar voluntarios que participan en distintos eventos comunitarios. Su equipo ha sido contratado para desarrollar esta aplicación, que permitirá registrar voluntarios, asignarlos a eventos y actualizar su información.

Los modelos principales serán:

Voluntario: Representa a una persona que se ha registrado para ayudar en eventos.

Evento: Representa actividades organizadas por la ONG.

Ejemplo de estructura de modelo:

from django.db import models

class Voluntario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    voluntarios = models.ManyToManyField(Voluntario, related_name="eventos")

    def __str__(self):
        return self.titulo
Ejercicio 1: Creación de una Aplicación Django para CRUD

Inicien un nuevo proyecto Django y creen una aplicación específica para gestionar los voluntarios y eventos.

Configuren la base de datos y registren los modelos en admin.py para facilitar la administración.

Ejercicio 2: Interacción entre Aplicaciones, Modelos y Vistas

Implementen las vistas necesarias para manejar la lógica de negocio.

Creen plantillas HTML para visualizar la lista de voluntarios, la información de los eventos y los formularios de creación/modificación.

Ejercicio 3: Manejo de Token de Seguridad CSRF

Asegúrense de incluir {% csrf_token %} en los formularios HTML para evitar ataques CSRF.

Ejercicio 4: Enrutamiento

Definan las rutas en urls.py para manejar las diferentes vistas del CRUD.

Utilicen path() para definir las URLs de cada acción.

Ejercicio 5: Paso de Parámetros en el Enrutamiento

Implementen rutas dinámicas que reciban el ID del voluntario o evento para modificar o eliminar registros.

Asegúrense de que las vistas correspondan correctamente a los parámetros de la URL.

Ejercicio 6: Selección de Registros

Implementen una vista que recupere y muestre todos los voluntarios y eventos almacenados en la base de datos.

Utilicen Django ORM con Voluntario.objects.all() y Evento.objects.all().

Ejercicio 7: Creación de Registros

Implementen formularios para agregar nuevos voluntarios y eventos.

Utilicen forms.py para definir la estructura del formulario si es necesario.

Ejercicio 8: Modificación de Registros

Implementen la funcionalidad para editar un voluntario o evento.

Recuperen los datos actuales y prellénenlos en un formulario.

Usen Voluntario.objects.get(id=id) para obtener un registro específico.

Ejercicio 9: Eliminación de Registros

Implementen una vista que permita eliminar voluntarios y eventos.

Creen una plantilla HTML que confirme la eliminación antes de ejecutarla.