# CRUD de Hoteles con Flask y PostgreSQL usando Docker Compose

## 🧾 Descripción
Este proyecto es una API sencilla para la gestión de hoteles. Permite realizar operaciones CRUD conectándose a una base de datos PostgreSQL.

## ▶️ Instrucciones

1. Clona este repositorio o descomprime este archivo zip.
2. Abre una terminal y ubícate en la carpeta raíz del proyecto.
3. Ejecuta el siguiente comando:

```bash
docker-compose up --build
```

4. Accede a [http://localhost:5000/hoteles](http://localhost:5000/hoteles) para interactuar con la API.

## 🛠 Servicios
- Flask backend: puerto `5000`
- PostgreSQL: puerto interno `5432`, con persistencia en volumen `db-data`
