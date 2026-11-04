# Stack A: Spring Boot + PostgreSQL

API CRUD de `productos` con Java 21, Spring Boot 4.1 (Spring Web, Spring Data JPA, Validation,
Actuator, SpringDoc) y PostgreSQL 16. Puerto **8085**.

## Estructura

```
src/main/java/com/univalle/productos/
├── ProductosApplication.java
├── model/Producto.java                  # entidad JPA (tabla productos)
├── repository/ProductoRepository.java   # JpaRepository: save, findAll, deleteById...
└── controller/ProductoController.java   # los cinco endpoints REST
```

## Ejecutar con Docker Compose (local)

```bash
cp .env.example .env          # Windows: copy .env.example .env
docker compose up -d --build
docker compose logs -f app    # esperar "Started ProductosApplication"
```

## Probar

```bash
curl -X POST http://localhost:8085/api/productos -H "Content-Type: application/json" -d @producto.json
curl http://localhost:8085/api/productos
curl http://localhost:8085/api/productos/1
curl -X PUT http://localhost:8085/api/productos/1 -H "Content-Type: application/json" -d @producto.json
curl -X DELETE http://localhost:8085/api/productos/1
curl http://localhost:8085/actuator/health
```

En PowerShell usar `curl.exe`. Swagger UI: http://localhost:8085/swagger-ui/index.html

## Publicar en Docker Hub

```bash
docker login
docker compose build app
docker compose push app
```

## Desplegar en EC2 (Ubuntu 22.04)

En la EC2 solo van `docker-compose.yml` y un `.env` con claves de producción:

```bash
sed -i '/build: \./d' docker-compose.yml
docker compose pull
docker compose up -d
```

Security Group: 22 (My IP) y 8085 (0.0.0.0/0). El 5432 no se abre.
