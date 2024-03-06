# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./steps/fastapi/step-01-fastapi/requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./steps/fastapi/step-01-fastapi /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
