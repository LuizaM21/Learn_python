from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


current_engine = create_engine('sqlite:///database:', echo=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    index = Column(Integer, primary_key=True)
    student_name = Column(String)
    student_surname = Column(String)
    student_email = Column(String)


class Courses(Base):
    __tablename__ = 'courses'
    index = Column(Integer, primary_key=True)
    course = Column(String)
    hours = Column(Integer)
    price = Column(Float)


class Mentor(Base):
    __tablename__ = 'mentor'
    index = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    social_media = Column(String)


def main():
    Base.metadata.create_all(current_engine)
    session_m = sessionmaker(bind=current_engine)
    session = session_m()
    m = Student(student_name="Marius", student_surname="Matei", student_email="matei.marius@wantsome.com")
    m1 = Student(student_name="Mihaiuc", student_surname="Luiza", student_email="luiza.mihaiuc@domain.com")

    c = Courses(course="physics", hours=5, price=5.6)
    c1 = Courses(course="chemistry", hours=6, price=6.5)

    mentor = Mentor(name="Richard", surname="Feynman", social_media="https://en.wikipedia.org/wiki/Richard_Feynman")
    mentor1 = Mentor(name="Richard", surname="Feynman1", social_media="https://en.wikipedia.org/wiki/Richard_Feynman")

    # make a persistent mark of the data into db
    session.add(m)
    session.add(m1)
    session.add(c)
    session.add(c1)
    session.add(mentor)
    session.add(mentor1)
    session.flush()

    [print(student)for student in session.query(Student)]
    [print(courses) for courses in session.query(Courses)]
    [print(mentor) for mentor in session.query(Mentor)]


if __name__ == '__main__':
    main()
