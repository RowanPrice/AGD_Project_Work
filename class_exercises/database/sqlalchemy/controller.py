import sqlalchemy as sa
import sqlalchemy.orm as so

from models import Person, Activity


class Controller:
    def __init__(self, db_location = 'sqlite:///activities.sqlite'):
        self.engine = sa.create_engine(db_location)

    def get_person_activities(self, first_name, last_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person).where(Person.first_name == first_name and Person.last_name == last_name)
            user = session.scalar(stmt)
            activities = user.activities
            activity_names = [activity.name for activity in activities]
        return activity_names

    def get_all_activities(self):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Activity)
            user = session.scalar(stmt)
            activities = user.name
            activity_names = [activity.name for activity in activities]
        return activity_names

    def get_all_people(self):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person)
            user = session.scalar(stmt)
            people = user.first_name + ' ' + user.last_name
            people_names = [person.name for person in people]
        return people_names



if __name__ == '__main__':
    controller = Controller()