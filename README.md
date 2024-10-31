# Archivo Validator

Este es un proyecto de Django que permite subir un archivo CSV, validar su estructura y contenido, y mostrar errores de validación. Las reglas de validación son:

1. El archivo debe tener exactamente 5 columnas.
2. Validación por columnas:
   - **Columna 1**: Solo permite números enteros de entre 3 y 10 caracteres.
   - **Columna 2**: Solo permite correos electrónicos válidos.
   - **Columna 3**: Solo permite los valores "CC" o "TI".
   - **Columna 4**: Solo permite valores numéricos entre 500000 y 1500000.
   - **Columna 5**: Permite cualquier valor.

## Requisitos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. **Clonar el repositorio**

   Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/archivo_validator.git
   cd archivo_validator

2. **Instalar dependencias**

    Instala las dependencias listadas en requirements.txt:
        pip install -r requirements.txt

3. **Configuración del proyecto**

    Crea las migraciones iniciales y configura la base de datos de Django:
        python manage.py migrate

4. **Ejecutar el servidor de desarrollo**

     Inicia el servidor de desarrollo de Django:
        python manage.py runserver

5. **Acceder a la aplicación**

    Abre tu navegador y ve a http://127.0.0.1:8000/validator/upload/ para probar la funcionalidad de carga y validación del archivo.

## Uso

    Sube un archivo CSV siguiendo el formato adecuado en la página. Usa los archivos de prueba dispuestos en el repositorio
        -1. Invalido
        -2. ValidoNotAll
        -3. ValidoAll

    Si el archivo es válido, verás un mensaje de éxito. Si hay errores, se mostrarán con la fila y columna donde ocurrieron.

## Licencia

Este proyecto está bajo la Licencia MIT.

