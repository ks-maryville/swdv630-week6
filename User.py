from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///:memory", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"

    user_id = Column("user_id", Integer, primary_key=True)
    email = Column("email", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    role = Column("role", String, nullable=False)

    def __init__(self, user_id, email, password, role):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return f"({self.user_id}; {self.email}; {self.role})"


def main():
    try:
        #  Add Users to Database

        user = User(None, "emailone", "newpassword", "role")
        user2 = User(None, "emailtwo", "newpassword", "role")
        user3 = User(None, "emailthree", "newpassword", "role")
        session.add(user)
        session.add(user2)
        session.add(user3)
        session.commit()
    except IntegrityError:
        print("user email already exists")
        session.rollback()

    # Retrieve Users From Database
    result = session.query(User).all()
    print(result)


if __name__ == "__main__":
    main()
