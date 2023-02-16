FROM python:3.10.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /api

# In order to leverage caching of Docker, install requirements first
ADD api/requirements.txt .

RUN apt-get update && apt-get -y install gcc && pip install -r requirements.txt

ADD . .

# Expose the default FastAPI port
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
