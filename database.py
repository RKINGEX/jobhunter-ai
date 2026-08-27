from sqlmodel import SQLModel, create_engine, Session

# Setting database URL
sqlite_file_name = "jobhunter.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Create engine with sql loggin enabled
engine = create_engine(sqlite_url, echo=True)

# Function to create database and tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

