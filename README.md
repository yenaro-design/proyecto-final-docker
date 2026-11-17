# Proyecto de Monitoreo y Balanceo de Carga con Docker

## 1. Descripción del proyecto

Este proyecto implementa una infraestructura de servicios contenerizados utilizando Docker Compose, con el propósito de demostrar el funcionamiento de un sistema de balanceo de carga, monitoreo y recopilación de métricas.

La arquitectura está compuesta por un servidor Nginx que funciona como proxy inverso y balanceador de carga, tres instancias de una aplicación backend desarrollada en Python con Flask, Prometheus para la recopilación de métricas, Grafana para la visualización de datos, cAdvisor para el monitoreo de contenedores y Nginx Prometheus Exporter para obtener métricas del servidor web.

## 2. Tecnologías utilizadas

- Docker y Docker Compose.
- Python y Flask.
- Nginx.
- Prometheus.
- Grafana.
- Nginx Prometheus Exporter.
- cAdvisor.
- k6 para pruebas de carga.

## 3. Arquitectura del proyecto

La infraestructura utiliza una red personalizada de Docker denominada `red-proyecto`.

El funcionamiento general es el siguiente:

1. Los usuarios envían solicitudes HTTP al servidor Nginx.
2. Nginx distribuye las solicitudes entre tres instancias backend mediante el algoritmo Round Robin.
3. Cada backend procesa las solicitudes y genera métricas de cantidad de peticiones y tiempos de respuesta.
4. Prometheus recopila las métricas de los backends, Nginx Exporter y cAdvisor.
5. Grafana consulta Prometheus y presenta los resultados mediante dashboards.
6. k6 permite realizar pruebas de carga para evaluar el comportamiento de la infraestructura.

## 4. Estructura del proyecto

```text
proyecto-final-docker/
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── evidencias/
├── informe/
├── nginx/
│   └── nginx.conf
├── prometheus/
│   └── prometheus.yml
├── pruebas/
│   └── prueba-carga.js
└── docker-compose.yml
└── README.md
```

## 5. Requisitos para ejecutar el proyecto

- Docker Desktop instalado y funcionando.
- Docker Compose.
- Sistema operativo Windows, Linux o macOS.
- Navegador web.

## 6. Instalación y ejecución

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta:

```bash
cd proyecto-final-docker
```

Construir las imágenes e iniciar los servicios:

```bash
docker compose up -d --build
```

Comprobar el estado de los contenedores:

```bash
docker compose ps
```

Para detener los servicios:

```bash
docker compose down
```

## 7. Acceso a los servicios

| Servicio | Dirección |
|---|---|
| Aplicación mediante Nginx | http://localhost:8080 |
| Estado de Nginx | http://localhost:8080/nginx_status |
| Métricas de Nginx Exporter | http://localhost:9113/metrics |
| Prometheus | http://localhost:9090 |
| Targets de Prometheus | http://localhost:9090/targets |
| cAdvisor | http://localhost:8081 |
| Grafana | http://localhost:3000 |

Credenciales iniciales de Grafana:

- Usuario: `admin`
- Contraseña: `admin123`

## 8. Métricas recopiladas

El proyecto recopila información relacionada con:

- Cantidad total de solicitudes recibidas por cada backend.
- Tiempo de respuesta de las solicitudes.
- Latencia promedio y percentil 95 (P95).
- Conexiones activas de Nginx.
- Uso de CPU de los contenedores.
- Consumo de memoria RAM de los contenedores.

## 9. Pruebas de carga

Se utilizó k6 para evaluar el comportamiento del sistema bajo diferentes niveles de concurrencia.

Resultados de la primera prueba:

| Indicador | Resultado |
|---|---:|
| Solicitudes totales | 3.272 |
| Solicitudes por segundo | 21,79 |
| Usuarios virtuales máximos | 50 |
| Solicitudes fallidas | 0 % |
| Latencia promedio | 6,7 ms |
| Latencia P90 | 9,6 ms |
| Latencia P95 | 10,36 ms |
| Latencia máxima | 34,56 ms |
| Checks exitosos | 100 % |

Los resultados muestran que, durante esta prueba, el sistema procesó las solicitudes sin registrar errores HTTP y mantuvo tiempos de respuesta bajos.

## 10. Persistencia

Docker Compose utiliza volúmenes para conservar los datos de Prometheus y Grafana:

- `prometheus_data`
- `grafana_data`

Esto permite mantener los datos almacenados cuando se reinician los contenedores, siempre que no se eliminen los volúmenes.

## 11. Autores

- Yenaro Samuel Gracia Ruiz
- Alejandro Molina Lara

## 12. Estado del proyecto

Infraestructura desplegada y funcional. Se verificó el balanceo de carga, la recolección de métricas, la visualización en Grafana y la ejecución de pruebas de carga con k6.
