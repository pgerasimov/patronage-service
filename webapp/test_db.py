# application starts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from webapp import Worker

Session = sessionmaker()

# ... later
engine = create_engine('sqlite:///webapp.db')
Session.configure(bind=engine)

sess = Session()


q = sess.query(Worker).filter(Worker.id == '1').all()

print(q)