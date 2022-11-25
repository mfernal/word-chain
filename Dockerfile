# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Base Image
#
FROM python:3.10-slim AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Runtime Image
#
FROM python:3.10-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

# copy the source code
RUN mkdir /code
WORKDIR /code
COPY main.py .
COPY src/ ./src/

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
ENTRYPOINT ["python", "/code/main.py"]
CMD ["--help"]
