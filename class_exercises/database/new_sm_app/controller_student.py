import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.sql.functions import current_user
from sqlalchemy.orm import selectinload

from class_exercises.database.new_sm_app.models import User, Post, Comment


class Controller:
    def __init__(self, db_location = 'sqlite:///social_media.sqlite'):
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

    def get_posts_by_user(self, user_id: int):
        with so.Session(bind=self.engine) as session:
            posts = session.scalars(
                sa.select(Post)
                .where(Post.user_id == user_id)
                .options(selectinload(Post.liked_by_users),
                         selectinload(Post.comments))
            ).all()
        return posts

    def like_post(self, post_id: int) -> None:
        with so.Session(bind=self.engine) as session:
            post = session.get(Post, post_id)
            user = session.get(User, self.current_user_id)

            if post is None or user is None:
                return

            # Prevent duplicate likes
            if post not in user.liked_posts:
                user.liked_posts.append(post)
                session.commit()

    def add_comment(self, post_id: int, text: str) -> None:
        with so.Session(bind=self.engine) as session:
            comment = Comment(
                user_id=self.current_user_id,
                post_id=post_id,
                comment=text
            )
            session.add(comment)
            session.commit()

    def get_comments_for_post(self, post_id: int):
        with so.Session(bind=self.engine) as session:
            post = session.get(Post, post_id)
            if post:
                return post.comments
            return []

    def get_user_info(self):
        with so.Session(bind=self.engine) as session:
            names = session.scalars(sa.select(User.name).order_by(User.name)).all()
            ages = session.scalars(sa.select(User.age).order_by(User.name)).all()
            genders = session.scalars(sa.select(User.gender).order_by(User.name)).all()
            nationalities = session.scalars(sa.select(User.nationality).order_by(User.name)).all()
            users = ''
        return list(names,ages,genders,nationalities)

    def get_posts(self) -> Post:
        with so.Session(bind=self.engine) as session:
            posts = session.scalars(sa.select(Post).order_by(Post.id)).all()
        return posts

    def add_user(self, name: str, age: int, gender: str, nationality: str) -> None:
        with so.Session(bind=self.engine) as session:
            add_user = User(name=name, age=age, gender=gender, nationality=nationality)
            session.add(add_user)
            session.commit()

    def add_post(self, title: str, description: str) -> None:
        with so.Session(bind=self.engine) as session:
            add_post = Post(title=title, description=description, user_id=self.current_user_id)
            session.add(add_post)
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