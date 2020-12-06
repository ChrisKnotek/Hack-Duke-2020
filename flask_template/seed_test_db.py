from database import init_db
from database import db_session
from models import Company
print("SEEDING TEST DATABASE")
init_db()
rev = Company('Diversity', 4, 'I love it here')
db_session.add(rev)
db_session.commit()
print("DONE!")