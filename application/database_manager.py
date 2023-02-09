import datamodel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///C:\\Users\\Simon\\OneDrive\\Dokumente\\4AHIT\\SEW INSY\\WorkTimeTracker\\application\\app_db.sql')
Session = sessionmaker(bind=engine)
session = Session()


class Database_Manager:
    def create_user(self, session, user_name):
        new_user = datamodel.Users(userName=user_name)
        session.add(new_user)
        session.commit()
        return new_user

    def create_time(self, session, start_value, stop_value, user_id):
        new_time = datamodel.Times(startValue=start_value, stopValue=stop_value, userID=user_id)
        session.add(new_time)
        session.commit()
        return new_time

    def read_user(self, session, user_id):
        return session.query(datamodel.Users).filter_by(userID=user_id).first()

    def read_times(self, session, user_id):
        return session.query(datamodel.Times).filter_by(userID=user_id).all()

    def update_user(self, session, user_id, user_name):
        user = session.query(datamodel.Users).filter_by(userID=user_id).first()
        user.userName = user_name
        session.commit()
        return user

    def update_time(self, session, time_id, start_value, stop_value, user_id):
        time = session.query(datamodel.Times).filter_by(timeID=time_id).first()
        time.startValue = start_value
        time.stopValue = stop_value
        time.userID = user_id
        session.commit()
        return time

    def delete_user(self, session, user_id):
        user = session.query(datamodel.Users).filter_by(userID=user_id).first()
        session.delete(user)
        session.commit()

    def delete_time(self, session, time_id):
        time = session.query(datamodel.Times).filter_by(timeID=time_id).first()
        session.delete(time)
        session.commit()

    def get_all_users(session):
        all_users = session.query(datamodel.Users).all()
        return all_users

    def get_last_time_id(self, session):
        last_time = session.query(datamodel.Times).order_by(datamodel.Times.timeID.desc()).first()
        if last_time:
            return last_time.timeID
        else:
            return 1


if __name__ == "__main__":
    dm = Database_Manager
    for i in range(16):
        dm.delete_time(session, time_id=i)
