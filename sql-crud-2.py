from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_WARN_20 = 1
SQLALCHEMY_SILENCE_UBER_WARNING = 1


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Country" table
class Country(base):
    __tablename__ = "Country"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    continent = Column(String)
    language = Column(String)
    currency = Column(String)
    driveson = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records for our Country table
united_kingdom = Country(
    name="United Kingdom",
    continent="Europe",
    language="English",
    currency="GBP",
    driveson="R"
)

united_states = Country(
    name="United States",
    continent="North America",
    language="English",
    currency="USD",
    driveson="L"
)

australia = Country(
    name="Australia",
    continent="Oceana",
    language="English",
    currency="USD",
    driveson="L"
)


# add each instance of our country to our session
# session.add(united_kingdom)
# session.add(united_states)
# session.add(australia)


# commit our session to the database
# session.commit()


# updating a single record
# country = session.query(Country).filter_by(id=1).first()
# country.name = "United Kingdom of Great Britain and Northern Ireland"

# commit our session to the database
session.commit()

# updating multiple records
# driveside = session.query(Country)
# for side in driveside:
#     if side.driveson == "R":
#         side.driveson = "Right"
#     elif side.driveson == "L":
#         side.driveson = "Left"
#     else:
#         print("Side not defined")
#     session.commit()


# deleting a single record
cname = input("Enter a country name: ")
country = (
    session.query(Country).filter_by(name=cname).first()
)

# defensive programming
if country is not None:
    print("Country Found: ", country.name)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(country)
        session.commit()
        print("Country has been deleted")
    else:
        print("Country not deleted")
else:
    print("No records found")


# delete multiple records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()


# query the database to find all Countries
countries = session.query(Country)
for country in countries:
    print(
        country.id,
        country.name,
        country.continent,
        country.language,
        country.currency,
        country.driveson,
        sep=" | ",
    )
