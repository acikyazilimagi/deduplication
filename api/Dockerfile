FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /api

# In order to leverage caching of Docker, install requirements first
ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

# Expose the default FastAPI port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
