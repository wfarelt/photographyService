# photographyService
Proyecto de SW1 de la UAGRM

# curso
https://www.youtube.com/watch?v=OwmbwQJ3Z_Y


## Entorno virtual
python -m venv mvirtual

# Requerimientos
pip install -r requirements.txt

pip install django-ckeditor
pip install Pillow

# Stripe
https://codigofacilito.com/articulos/stripe-django

# Eliminar todos los archivos de migraciones, excepto __init__.py
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

# Generar el 0001_initial.py en cada app con directorio migrations.
./manage.py makemigrations

# migrate fake.
./manage.py migrate --fake