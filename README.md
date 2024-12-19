# Conectar_db
es netamente de proyecto personal, como conectar mi base de datos
# Proyecto de Registro de Personas con Flask y PostgreSQL

Este proyecto es una aplicación web desarrollada en Python utilizando Flask. Permite registrar información de personas a través de un formulario HTML y almacenarla en una base de datos PostgreSQL alojada en [Neon.tech](https://neon.tech/).

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.9 o superior**
- **PostgreSQL**
- **pip** (administrador de paquetes de Python)
- **Debian 12** como sistema operativo

## Configuración inicial

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

```
git clone https://github.com/usuario/proyecto-registro-personas.git
```
```
cd proyecto-registro-personas
```
### 2. crear entorno virtual 
```
python3 -m venv venv
```
```
source venv/bin/activate
```
### 3. instalar dependencias 
```
sudo apt update
sudo apt install -y python3-dev libpq-dev gcc
```
```
pip install flask psycopg2-binary flask-wtf
```

### 4. crear la base de datos 
```

CREATE TYPE estado_civil_tipo AS ENUM ('Soltero', 'Casado', 'Divorciado', 'Viudo', 'Union Libre');
CREATE TYPE nivel_estudio_tipo AS ENUM ('Primaria', 'Secundaria', 'Técnico', 'Tecnólogo', 'Profesional', 'Postgrado');
CREATE TYPE perfil_laboral_tipo AS ENUM ('Empleado', 'Independiente', 'Estudiante', 'Desempleado', 'Otro');
CREATE TYPE si_no_tipo AS ENUM ('Si', 'No');

CREATE TABLE Personas (
    id SERIAL PRIMARY KEY,
    nombre_completo VARCHAR(255) NOT NULL,
    edad SMALLINT NOT NULL CHECK (edad > 0),
    fecha_nacimiento DATE NOT NULL,
    direccion TEXT NOT NULL,
    numero_celular VARCHAR(10) NOT NULL CHECK (numero_celular ~ '^[3][0-9]{9}$'),
    estado_civil estado_civil_tipo NOT NULL,
    nivel_estudio nivel_estudio_tipo NOT NULL,
    perfil_laboral perfil_laboral_tipo NOT NULL,
    convertido si_no_tipo NOT NULL,
    bautizado si_no_tipo NOT NULL
);

```
### 5. Configurar el archivo `app.py `
```
DB_HOST = "tu_host_de_neon.tech"
DB_NAME = "MiBaseDeDatos"
DB_USER = "tu_usuario"
DB_PASSWORD = "tu_contraseña"
```

### 6. ejecutar el archivo `app.py `

_NOTA_:
Abre tu navegador en `http://127.0.0.1:5000` para acceder a la aplicación.
Archivos del proyecto
`app.py`: Código principal de la aplicación Flask.
`templates/form.html`: Plantilla HTML para el formulario.
`requirements.txt`: Lista de dependencias del proyecto.
