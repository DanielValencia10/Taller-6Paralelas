# Etapa 1: compila el .jar dentro de Docker (no hace falta Java en el PC)
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /build
COPY pom.xml .
COPY src ./src
RUN mvn -B -q clean package -DskipTests

# Etapa 2: solo el runtime de Java y el .jar, para una imagen mas liviana
FROM amazoncorretto:21
WORKDIR /app
COPY --from=build /build/target/*.jar app.jar
EXPOSE 8085
ENTRYPOINT ["java", "-jar", "/app/app.jar", "--server.address=0.0.0.0"]
