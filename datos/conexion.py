from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost:3306/biblioteca_digital"
motor_db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=motor_db)
sesion = Session()