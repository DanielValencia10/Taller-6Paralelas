# Stack B: Django REST Framework + MySQL

API REST CRUD de **productos** (nombre, descripción, precio, stock) con Python 3.12,
Django 6.1, Django REST Framework y MySQL 8.4, desplegada con Docker Compose en local y en AWS EC2.

Responsable: Sebastián Saldaña Olmos

## Endpoints (puerto 8080)

| Método | Ruta | Qué hace | Código |
|---|---|---|---|
| POST | `/api/productos` | Crea un producto | 201 |
| GET | `/api/productos` | Lista todos | 200 |
| GET | `/api/productos/{id}` | Trae uno | 200 / 404 |
| PUT | `/api/productos/{id}` | Reemplaza sus datos | 200 / 404 |
| DELETE | `/api/productos/{id}` | Lo borra | 204 / 404 |
| GET | `/api/health` | Estado de la API | 200 |

Datos inválidos (nombre vacío, precio negativo, campos faltantes) responden 400.

## Levantar con Docker Compose

```bash
cp .env.example .env        # en Windows: copy .env.example .env
docker compose up -d --build
docker compose ps
docker compose logs -f app
```

Prueba rápida:

```bash
curl -X POST http://localhost:8080/api/productos -H "Content-Type: application/json" -d @producto.json
curl http://localhost:8080/api/productos
```

## Despliegue en AWS EC2

1. En el PC: `docker login`, `docker compose build app`, `docker compose push app`.
2. En la EC2 (Ubuntu 22.04 con Docker): copiar `docker-compose.yml`, crear `.env`,
   borrar la línea `build: .`, y ejecutar `docker compose pull` y `docker compose up -d`.
3. Security Group: puerto 22 solo desde My IP y puerto 8080 abierto. El 3306 no se abre.

## Archivos

- `config/`: proyecto Django (settings con variables de entorno y rutas).
- `productos/`: modelo, serializer, ViewSet y migraciones.
- `Dockerfile`, `docker-compose.yml`, `.env.example`: contenedores.
