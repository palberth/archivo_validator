# validator/views.py
from django.shortcuts import render
from .forms import UploadFileForm
import csv
import re

def validate_file_data(rows):
    errors = []
    for i, row in enumerate(rows):
        if len(row) != 5:
            errors.append((i+1, "Número de columnas incorrecto"))
            continue
        
        # Validar Columna 1
        if not (row[0].isdigit() and 3 <= len(row[0]) <= 10):
            errors.append((i+1, 1, "Columna 1 debe ser un número entero entre 3 y 10 caracteres"))

        # Validar Columna 2
        if not re.match(r"[^@]+@[^@]+\.[^@]+", row[1]):
            errors.append((i+1, 2, "Columna 2 debe ser un correo electrónico válido"))

        # Validar Columna 3
        if row[2] not in ["CC", "TI"]:
            errors.append((i+1, 3, "Columna 3 solo permite 'CC' o 'TI'"))

        # Validar Columna 4
        try:
            value = int(row[3])
            if not (499999 <= value <= 1500000):
                errors.append((i+1, 4, "Columna 4 debe estar entre 500000 y 1500000"))
        except ValueError:
            errors.append((i+1, 4, "Columna 4 debe ser un número entero"))

    return errors

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            decoded_file = file.read().decode("utf-8").splitlines()
            reader = csv.reader(decoded_file)
            rows = list(reader)
            errors = validate_file_data(rows)

            if errors:
                return render(request, "validator/upload.html", {"form": form, "errors": errors})
            else:
                return render(request, "validator/upload.html", {"form": form, "success": "Archivo validado correctamente"})
    else:
        form = UploadFileForm()
    return render(request, "validator/upload.html", {"form": form})
