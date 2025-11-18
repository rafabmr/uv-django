# Proyecto Django con UV

Proyecto Django configurado con UV como gestor de paquetes y entornos virtuales.

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
├── db.sqlite3
├── manage.py
```

## Variables de entorno

Crea un archivo `.env` en la raíz:

```
DEBUG=True
SECRET_KEY=tu-secret-key-aqui
DATABASE_URL=sqlite:///db.sqlite3
```

## Despliegue

```bash
uv pip install gunicorn
uv run gunicorn config.wsgi:application
```