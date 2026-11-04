# Taller AWS EC2: API REST CRUD con Spring Boot y Django en Docker

Universidad del Valle – Infraestructuras Paralelas y Distribuidas (750023C)

**Integrantes:** Hector Daniel Carabali Valencia · Sebastián Saldaña Olmos

Dos implementaciones del mismo contrato REST sobre el recurso `productos`
(nombre, descripción, precio, stock), cada una en contenedores con su propia base de datos
y desplegada en su propia instancia EC2.

| Stack | Tecnología | Base de datos | Puerto | Carpeta |
|---|---|---|---|---|
| A | Java 21 + Spring Boot 4 | PostgreSQL 16 | 8085 | [springboot-postgres/](springboot-postgres/) |
| B | Python 3.12 + Django REST Framework | MySQL 8.4 | 8080 | [django-mysql/](django-mysql/) |

## Endpoints (iguales en ambos stacks)

| Método | Ruta | Qué hace | Código si sale bien |
|---|---|---|---|
| POST | `/api/productos` | Crea un producto | 201 |
| GET | `/api/productos` | Lista todos | 200 |
| GET | `/api/productos/{id}` | Trae uno | 200 (404 si no existe) |
| PUT | `/api/productos/{id}` | Reemplaza sus datos | 200 (404 si no existe) |
| DELETE | `/api/productos/{id}` | Lo borra | 204 (404 si no existe) |

Salud: `/actuator/health` (Spring Boot) y `/api/health` (Django).

## Levantar cada stack con Docker Compose

```bash
cd springboot-postgres   # o django-mysql
cp .env.example .env     # en Windows: copy .env.example .env  — y cambia las claves
docker compose up -d --build
docker compose ps
```

## Video

Pendiente: enlace de YouTube.
