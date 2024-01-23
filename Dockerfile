FROM ubuntu:latest

ENV USER=user \
    WORKDIR=/app

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y \
    sudo \
    python3 \
    python3-pip

RUN mkdir /app && \
    adduser -u 1000 --disabled-password --gecos "" $USER && chown -R $USER /app && \
    adduser $USER sudo && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER $USER
WORKDIR $WORKDIR

ENV PATH="$PATH:/home/$USER/.local/bin/:"

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN pip install poetry
COPY poetry.lock pyproject.toml $WORKDIR
RUN poetry install --no-root
