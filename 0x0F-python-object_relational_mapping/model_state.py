from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+mysql:// {}:{}localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_pinge=[True])
    
Base = declarative_base()

class State(Base):
    __table__= 'states'

    id = Column(Interger, primary_key=True, autoincrement=True, nullable=False)
    name = Column(string(128))