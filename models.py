from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column("title", String(55))
    body = Column("body", String(255))
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column("name", String(55))
    email = Column("email", String(255))
    password = Column("password", String(55))

    blogs = relationship("Blog", back_populates="owner")