"""CRUD Module aka Database Manager."""


from .datamodel import Times, Users


class manager:
    """CRUD Module."""

    def create_user(session, name):
        """Create User in Database."""
        new_user = Users(userName=name)
        session.add(new_user)
        session.commit()
        return new_user

    def create_time(session, time_value, user_id):
        """Create new timevalue in Database."""
        new_time = Times(timeValue=time_value, userID=user_id)
        session.add(new_time)
        session.commit()
        return new_time

    def get_user(session, user_id):
        """Get User from Database."""
        return session.query(Users).filter_by(userID=user_id).first()

    def get_time(session, time_id):
        """Get time from Database."""
        return session.query(Times).filter_by(timeID=time_id).first()

    def update_user(session, user_id, name):
        """Update User in Database."""
        user = session.get_user(session, user_id)
        user.userName = name
        session.commit()
        return user

    def update_time(session, time_id, time_value, user_id):
        """Update Time in Database."""
        time = session.get_time(session, time_id)
        time.timeValue = time_value
        time.userID = user_id
        session.commit()
        return time

    def delete_user(session, user_id):
        """Delete User from Database."""
        user = session.get_user(session, user_id)
        session.delete(user)
        session.commit()

    def delete_time(session, time_id):
        """Delete Time From Database."""
        time = session.get_time(session, time_id)
        session.delete(time)
        session.commit()
