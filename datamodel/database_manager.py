from .datamodel import Users, Times


class manager:
    def create_user(session, name):
        new_user = Users(userName=name)
        session.add(new_user)
        session.commit()
        return new_user

    def create_time(session, time_value, user_id):
        new_time = Times(timeValue=time_value, userID=user_id)
        session.add(new_time)
        session.commit()
        return new_time

    def get_user(session, user_id):
        return session.query(Users).filter_by(userID=user_id).first()

    def get_time(session, time_id):
        return session.query(Times).filter_by(timeID=time_id).first()

    def update_user(session, user_id, name):
        user = session.get_user(session, user_id)
        user.userName = name
        session.commit()
        return user

    def update_time(session, time_id, time_value, user_id):
        time = session.get_time(session, time_id)
        time.timeValue = time_value
        time.userID = user_id
        session.commit()
        return time

    def delete_user(session, user_id):
        user = session.get_user(session, user_id)
        session.delete(user)
        session.commit()

    def delete_time(session, time_id):
        time = session.get_time(session, time_id)
        session.delete(time)
        session.commit()
