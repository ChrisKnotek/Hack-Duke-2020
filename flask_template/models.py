from sqlalchemy import Column, Integer, String
from database import Base

class Company(Base):
    __tablename__ = 'revs'
    id = Column(Integer, primary_key=True)
    standard = Column(String(20), unique=False)
    points = Column(Integer, unique=False)
    additional_info = Column(String(250), unique=False)

    def __init__(self, standard=None, points=0, additional_info=None):
        self.standard = standard
        self.points = points
        self.additional_info = additional_info

    def __repr__(self):
        return '<Company %r>' % (self.standard)