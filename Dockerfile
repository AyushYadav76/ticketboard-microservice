# Use Eclipse Temurin JDK 17 (Ubuntu 22.04 base - lightweight and official)
FROM eclipse-temurin:17-jdk-jammy

WORKDIR /app

COPY target/ticketboard-0.0.1-SNAPSHOT.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]