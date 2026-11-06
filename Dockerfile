FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TF_CPP_MIN_LOG_LEVEL=2
WORKDIR /src
COPY requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY src /src
RUN chmod a+x docker-entrypoint.sh
