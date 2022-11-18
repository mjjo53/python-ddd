import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config.api_config import ApiConfig
from seedwork.infrastructure.database import Base


@pytest.fixture
def engine():
    config = ApiConfig()
    engine = create_engine(config.DATABASE_URL, echo=config.DEBUG)

    with engine.begin() as connection:
        Base.metadata.drop_all(connection)
        Base.metadata.create_all(connection)

        return engine


@pytest.fixture
def db_session(engine):

    with Session(engine) as session:
        yield session
