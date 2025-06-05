FROM python:3.12-slim-bookworm

WORKDIR /eq_cir_management_ui

COPY pyproject.toml poetry.lock /eq_cir_management_ui/

RUN groupadd -r appuser && useradd -r -g appuser -u 999 appuser && chown -R appuser:appuser .

RUN pip install --no-cache-dir poetry==2.1.2 && \
    poetry config virtualenvs.create false && \
    poetry install --without dev

COPY eq_cir_management_ui eq_cir_management_ui

ENV LOG_LEVEL=INFO

USER appuser

EXPOSE 5100

HEALTHCHECK CMD curl --fail http://localhost:5100 || exit 1 

CMD ["python", "app", "--host", "0.0.0.0", "--port", "5100"]
