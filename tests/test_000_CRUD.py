from ..application import datamodel
from ..application import database_manager
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///C:\\Users\\Simon\\OneDrive\\Dokumente\\4AHIT\\SEW INSY\\WorkTimeTracker\\application\\app_db.sql')
Session = sessionmaker(bind=engine)


@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.close()


def test_create_user(db_session):
    user_name = "Test User"
    new_user = database_manager.Database_Manager.create_user(db_session, user_name)
    assert new_user.userName == user_name
    assert new_user.userID is not None
    db_user = db_session.query(datamodel.Users).filter_by(userID=new_user.userID).first()
    assert db_user is not None
    assert db_user.userName == user_name


def test_create_time(db_session):
    user = datamodel.Users(userName='Test User')
    db_session.add(user)
    db_session.commit()
    start_value = datetime.datetime.now()
    stop_value = start_value + datetime.timedelta(hours=1)
    user_id = user.id
    new_time = database_manager.Database_Manager.create_time(db_session, start_value, stop_value, user_id)
    assert new_time.startValue == start_value
    assert new_time.stopValue == stop_value
    assert new_time.userID == user_id


def test_update_time(db_session):
    user = database_manager.Database_Manager.create_user(db_session, "test_user")
    time = database_manager.Database_Manager.create_time(db_session, "2020-01-01T00:00:00", "2020-01-01T01:00:00", user.id)
    updated_time = database_manager.Database_Manager.update_time(db_session, time.id, "2020-02-01T00:00:00", "2020-02-01T01:00:00")
    assert updated_time.startValue == "2020-02-01T00:00:00"
    assert updated_time.stopValue == "2020-02-01T01:00:00"

def test_read_times(db_session):
    user = database_manager.Database_Manager.create_user(db_session, "test_user")
    time1 = database_manager.Database_Manager.create_time(db_session, datetime(2022, 1, 1), datetime(2022, 1, 2), user.id)
    time2 = database_manager.Database_Manager.create_time(db_session, datetime(2022, 2, 1), datetime(2022, 2, 2), user.id)
    times = database_manager.Database_Manager.read_times(db_session, user.id)
    assert len(times) == 2
    assert time1 in times
    assert time2 in times

