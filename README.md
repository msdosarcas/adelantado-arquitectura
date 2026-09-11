# Adelantado Arquitectura

Landing page editorial para Adelantado Arquitectura, construida con Python y Streamlit.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Publicar en Render

El proyecto incluye `render.yaml` con la configuración del servicio web.

1. Sube este proyecto a un repositorio de GitHub o GitLab.
2. Entra en [Render](https://render.com) y selecciona **New +** > **Blueprint**.
3. Conecta el repositorio y selecciona la rama que contiene `render.yaml`.
4. Confirma la creación del servicio `adelantado-arquitectura`.

Render instalará las dependencias y ejecutará Streamlit en el puerto asignado automáticamente por la plataforma. No es necesario añadir variables de entorno para esta versión.

También puedes crear un **Web Service** manualmente con estos valores:

```text
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
```
