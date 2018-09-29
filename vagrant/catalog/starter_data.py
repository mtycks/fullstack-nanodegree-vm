from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Category, Wall, WallPhoto

from datetime import datetime

engine = create_engine('sqlite:///waldir.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



# user1 = User(username = "mtycks", profile_photo = "https://pbs.twimg.com/profile_images/921075673967427584/N-XXBDyo_400x400.jpg", cover_photo = "https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/40654903_2007751745950119_928326691057565696_n.jpg?_nc_cat=105&oh=13857b58ce506f504e56b6512aec9c1c&oe=5C163763", full_name = "Matthew Mesa", email = "matthewmesa@gmail.com", created = datetime.now(), password_hash = "1234")
# session.add(user1)
# session.commit()

# category1 = Category(title = "Los Angeles", description = "Los Angeles, CA", user_id = 1, created = datetime.now(), parent = 0)
# session.add(category1)
# session.commit()


print "Starter data has been added"
