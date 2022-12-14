# Instrucciones para ejecutar este proyecto

### 1. Abrir Git Bash para `Windows` o una terminal para `Linux/Unix`.

- Clonar el proyecto
```bash
git clone https://github.com/johannacc/Entrega_Intermedia_Cornejo_Carrera.git

### 3. Crear y activar entorno virtual
(Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

(Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

### 5. Navegamos hacia la carpeta del proyecto `my_blog`
```bash
cd Entrega_Intermedia_Cornejo_Carrera
```

### 6. Se crean las migraciones que son una "plantilla" para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py makemigrations
```

### 7. Se ejecuta la migración para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py migrate
```

### 8. Se levanta el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto `http://127.0.0.1:8000/`
```bash
python manage.py runserver
```

- Es hora de ir al navegador y en una pestaña nueva navegar hacia para visualizar el proyecto que hicimos.
En la barra superior encontrará los botones para dirigirse a las apps (Viajes, Hospedajes, Foro)

Ir al botón home en la parte superior izquierda de la web para desplazarte desde cualquier app hacia la página principal.

En el home encontrará información acerca de nosotros y allí tambien nuestro LinkedIn para ponerse en contacto.

En la ventana Viajes encontrará un breve resumen de nuestros destinos y un botón "Viajes 2022-2023" para completar el formulario, que luego podrá visualizarse en la misma sección.

En la ventana Hospedaje s tambien contará con información de las opciones de alojamiento y podrá completar un formulario para ayudar a otros viajeros. Dicho formulario lo podrá visualizar, editar y eliminar en caso de ser necesario.

En la ventana Foro podrá llenar un formulario para dejarnos una reseña.
Por último, en el home cuenta con un buscador para poder encontrar los alojamientos de manera más sencilla.
