import sqlalchemy as sa
import sqlalchemy.orm as so

from class_exercises.database.new_sm_app.models import User, Post, Comment


class Controller:
    def __init__(self, db_location = 'sqlite:///social_media.db'):
        self.current_user_id: int|None = None
        self.viewing_post_user_id: int|None = None
        self.engine = sa.create_engine(db_location)

    def set_current_user_from_name(self, name:str) -> User|None:
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(User).where(User.name == name)).one_or_none()

            if user is None:
                # Fallback behaviour: clear current user and return None
                self.current_user_id = None
                return None

            self.current_user_id = user.id
        return user

    def get_user_name(self, user_id: int|None = None) -> 'str':
        if user_id is None:
            user_id = self.current_user_id
        with so.Session(bind=self.engine) as session:
            name = session.get(User, user_id).name
        return name

    def get_user_names(self) -> list[str]:
        with so.Session(bind=self.engine) as session:
            user_names = session.scalars(sa.select(User.name).order_by(User.name)).all()
        return list(user_names)

    def get_user_info(self):
        with so.Session(bind=self.engine) as session:
            names = session.scalars(sa.select(User.name).order_by(User.name)).all()
            ages = session.scalars(sa.select(User.age).order_by(User.name)).all()
            genders = session.scalars(sa.select(User.gender).order_by(User.name)).all()
            nationalities = session.scalars(sa.select(User.nationality).order_by(User.name)).all()
            users = ''
        return list(names,ages,genders,nationalities)

    def add_user(self, name: str, age: int, gender: str, nationality: str) -> None:
        with so.Session(bind=self.engine) as session:
            add_user = User(name=name, age=age, gender=gender, nationality=nationality)
            session.add(add_user)
            session.commit()

    def get_user_details(self,name):
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(User).where(User.name == name)).one_or_none()
        return user

    def get_user_gender(self,name):
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(User).where(User.name == name)).one_or_none()
        return user.gender

    def get_user_nationality(self,name):
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(User).where(User.name == name)).one_or_none()
        return user.nationality


if __name__ == '__main__':
    controller = Controller()
    print(controller.set_current_user_from_name('Alice'))