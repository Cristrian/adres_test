# 
FROM python:3.10-alpine

# ENV DATABASE = adres.db
# ENV ACQUIS_TABLE = acquisitions
# ENV RECORDS_TABLE = records
# ENV HOST = localhost
# ENV PORT=80

# 
WORKDIR /src

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY ./src ./

# 
CMD ["fastapi", "run", "main.py", "--port", "80"]
# CMD ["fastapi", "run", "app/app/api.py", "--port", "80"]