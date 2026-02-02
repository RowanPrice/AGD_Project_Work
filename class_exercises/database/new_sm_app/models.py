import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

class Base(so.DeclarativeBase):
    pass

# Define the likes table as a secondary table
# The primary key for the table is set to be the composite key from the two FKs
likes_table = sa.Table(
    'likes',
    Base.metadata,
    sa.Column('user_id', sa.Integer,
              sa.ForeignKey(column='users.id',ondelete='CASCADE'),
              primary_key=True),
    sa.column('post_id', sa.Integer,
              sa.ForeignKey(column='posts.id', ondelete='CASCADE'),
              primary_key=True),
)

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    age: Mapped[Optional[int]]
    gender: Mapped[Optional[str]]
    nationality: Mapped[Optional[str]]

# Many-to-many: posts that are liked by the user - defined by the likes table
    liked_posts: Mapped[list['Post']] = relationship(
        secondary=likes_table,
        back_populates='liked_by_users',
    )

    comments_made: Mapped[list['Comment']] = relationship(
        back_populates= 'user',
        cascade = 'all, delete-orphan',
    )

    def __repr__(self):
        return f"User(name='{self.name}', age={self.age}, gender='{self.gender}', nationality='{self.nationality}')"

class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True, index=True)
    description: Mapped[Optional[str]]
    user_id: Mapped[int] = mapped_column(index=True)

    liked_by_users: Mapped[list['User']] = relationship(
        secondary=likes_table,
        back_populates='liked_posts',
    )

    comments_made: Mapped[list['Comment']] = relationship(
        back_populates='post',
        cascade = 'all, delete-orphan',
    )

    def __repr__(self):
        return f"Post(title='{self.title}', description={self.description}, user_id='{self.user_id}')"

class Comment(Base):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        sa.ForeignKey('users.id',ondelete='CASCADE'), nullable=False
    )
    post_id: Mapped[int] = mapped_column(
        sa.ForeignKey('post.id',ondelete='CASCADE'), nullable=False
    )
    comment: Mapped[str]
    user: Mapped[User] = so.relationship(back_populates='comments_made')
    post: Mapped[Post] = so.relationship(back_populates='comments_made')

    def __repr__(self):
        return f"Comment(post_id='{self.post_id}', comment={self.comment}, user_id='{self.user_id}')"