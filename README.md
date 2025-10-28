## Plataforma de Gestión de Voluntarios – ONG

Este proyecto corresponde a un desarrollo grupal del Bootcamp de Desarrollo Web con Python y Django, cuyo objetivo fue crear una aplicación web para una organización sin fines de lucro (ONG) que permita gestionar voluntarios y eventos comunitarios de forma eficiente y moderna.

La plataforma está construida con Django, integra un sistema CRUD completo (crear, leer, actualizar y eliminar) y utiliza Bootstrap 5 para una interfaz limpia y responsiva.

## Funcionalidades principales

- Gestión de Voluntarios:
Permite registrar nuevos voluntarios, actualizar sus datos, ver detalles y eliminar registros.

- Gestión de Eventos:
Permite crear, editar, listar y eliminar eventos comunitarios.

- Relación entre Eventos y Voluntarios:
Cada evento puede tener múltiples voluntarios asignados (relación muchos a muchos).

- Protección CSRF:
Todos los formularios incluyen token de seguridad {% csrf_token %}.

- Interfaz intuitiva:
Navegación mediante barra superior y formularios con diseño responsive.

## Tecnologías utilizadas

| Categoría            | Tecnología                 |
| -------------------- | -------------------------- |
| Lenguaje principal   | Python 3.12                |
| Framework backend    | Django 5.2                 |
| Base de datos        | MySQL (MariaDB compatible) |
| Frontend             | HTML5, CSS3, Bootstrap 5   |
| Control de versiones | Git / GitHub               |
| Entorno              | Virtualenv                 |

## Instalación y configuración
1️⃣ Clonar el repositorio
```bash
git clone https://github.com/<usuario>/<nombre_repositorio>.git
cd <nombre_repositorio>
```

2️⃣ Crear y activar entorno virtual
```bash
python -m venv myenv
myenv\Scripts\activate    # (Windows)
```

3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

4️⃣ Configurar base de datos en settings.py
```bash
Ejemplo:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ong_db",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
```

5️⃣ Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

6️⃣ Ejecutar el servidor
```bash
python manage.py runserver
```


Accede desde tu navegador a:
👉 http://127.0.0.1:8000/

## Estructura del proyecto
```bash
M7_AE6_ABPRO-Ejercicio_grupal/
│
├── gestionar_voluntarios/        # App principal
│   ├── migrations/               # Migraciones de base de datos
│   ├── templates/                # HTMLs (voluntarios, eventos, base, index)
│   ├── static/                   # Archivos CSS, JS, imágenes
│   ├── models.py                 # Modelos: Voluntario y Evento
│   ├── views.py                  # Vistas CRUD
│   ├── urls.py                   # Enrutamiento de la app
│   └── forms.py                  # Formularios
│
├── ong/                          # Proyecto principal
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

## Modelos principales
```bash
class Voluntario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    voluntarios = models.ManyToManyField(Voluntario, related_name="eventos", blank=True)
```

## Interfaz de usuario

- Hero de bienvenida en la página principal (index.html).

- Navbar fija con enlaces a Voluntarios y Eventos.

- Formularios claros, protegidos con CSRF.

- Listado de registros en tablas con acciones:

    - Ver detalles

    - Editar

    - Eliminar

## Equipo de desarrollo

Proyecto desarrollado de forma colaborativa en el marco del Módulo 7 del Bootcamp Talento Digital.

Integrantes
- Johana Torres
- Matias Lagos
- Catalina Villegas 	


##  Estado del proyecto

✅ Completado y funcional.
