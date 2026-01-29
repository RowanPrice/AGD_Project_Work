import sqlalchemy as sa
import sqlalchemy.orm as so
from models import Person, Activity


class Controller:
    def __init__(self, db_location='sqlite:///activities.sqlite'):
        self.engine = sa.create_engine(db_location, echo=False)

    def add_person(self, first_name, last_name):
        with so.Session(self.engine) as session:
            person = Person(first_name=first_name, last_name=last_name)
            session.add(person)
            session.commit()

    def add_activity(self, activity_name):
        with so.Session(self.engine) as session:
            stmt = sa.select(Activity).where(Activity.name == activity_name)
            if session.scalar(stmt):
                return False

            activity = Activity(name=activity_name)
            session.add(activity)
            session.commit()
            return True

    def delete_person(self, first_name, last_name):
        with so.Session(self.engine) as session:
            stmt = sa.select(Person).where(
                Person.first_name == first_name,
                Person.last_name == last_name
            )
            person = session.scalar(stmt)

            if not person:
                return False

            session.delete(person)
            session.commit()
            return True

    def add_person_to_activity(self, first_name, last_name, activity_name):
        with so.Session(self.engine) as session:
            person_stmt = sa.select(Person).where(
                Person.first_name == first_name,
                Person.last_name == last_name
            )
            activity_stmt = sa.select(Activity).where(Activity.name == activity_name)

            person = session.scalar(person_stmt)
            activity = session.scalar(activity_stmt)

            if not person or not activity:
                return False

            if activity in person.activities:
                return False

            person.activities.append(activity)
            session.commit()
            return True

    def get_person_activities(self, first_name, last_name):
        with so.Session(self.engine) as session:
            stmt = sa.select(Person).where(
                Person.first_name == first_name,
                Person.last_name == last_name
            )
            person = session.scalar(stmt)

            if not person:
                return []

            return [activity.name for activity in person.activities]

    def get_all_activities(self):
        with so.Session(self.engine) as session:
            stmt = sa.select(Activity)
            activities = session.scalars(stmt).all()
            return [activity.name for activity in activities]

    def get_all_people(self):
        with so.Session(self.engine) as session:
            stmt = sa.select(Person)
            people = session.scalars(stmt).all()
            return [f"{p.first_name} {p.last_name}" for p in people]

    def get_activity_people(self, activity_name):
        with so.Session(self.engine) as session:
            stmt = sa.select(Activity).where(Activity.name == activity_name)
            activity = session.scalar(stmt)

            if not activity:
                return []

            return [f"{p.first_name} {p.last_name}" for p in activity.attendees]

if __name__ == '__main__':
    controller = Controller()
