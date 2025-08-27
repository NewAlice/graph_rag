FROM python:3.12.9-slim

WORKDIR /app/

# Install Poetry
RUN pip install poetry -i https://pypi.tuna.tsinghua.edu.cn/simple && poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install -vv --no-root ; else poetry install --no-root --no-dev -vv ; fi"

COPY ./app /app/app
ENV PYTHONPATH=/app

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 8080

# Run the start script, it will start Gunicorn with Uvicorn
#CMD ["/start.sh"]
CMD ["python", "app/main.py"]