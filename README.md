# Proyecto Django con UV

Proyecto Django configurado con UV como gestor de paquetes.

## Requisitos

- Python 3.12+
- UV instalado globalmente

## Instalación de UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Estructura del proyecto

```
project/
├── app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
├── project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env
├── database.db
├── manage.py
```

## Entorno virtual

Crea un entorno virtual con uv:

```bash
uv venv --python 3.12.0
source .venv/bin/activate
```

## Variables de entorno

Crea un archivo `.env` en la carpeta project:

```
DEBUG=True
SECRET_KEY=tu-secret-key-aqui
DATABASE_URL=database.db
```

## Migraciones

Genera las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

Crea un superusuario para el panel de administración:

```bash
python manage.py createsuperuser
```

## Despliegue

```bash
uv run gunicorn --bind 127.0.0.1:8000 project.wsgi
```