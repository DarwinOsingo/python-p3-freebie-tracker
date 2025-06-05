#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Clear old data
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()

# Add companies
c1 = Company(name="ByteCraft", founding_year=2010)
c2 = Company(name="DevHut", founding_year=2015)
c3 = Company(name="AlgoWorks", founding_year=2005)

# Add devs
d1 = Dev(name="Alex M.")
d2 = Dev(name="Jamie T.")
d3 = Dev(name="Sammy G.")
d4 = Dev(name="Riley N.")

# Add freebies
f1 = Freebie(item_name="Bluetooth Headset", value=50, company=c1, dev=d1)
f2 = Freebie(item_name="Tote Bag", value=15, company=c2, dev=d1)
f3 = Freebie(item_name="Coffee Mug", value=10, company=c2, dev=d2)
f4 = Freebie(item_name="Mousepad", value=8, company=c3, dev=d3)
f5 = Freebie(item_name="Dev Notebook", value=20, company=c1, dev=d4)
f6 = Freebie(item_name="Stickers Pack", value=5, company=c3, dev=d2)

# Commit to DB
session.add_all([c1, c2, c3, d1, d2, d3, d4, f1, f2, f3, f4, f5, f6])
session.commit()

print(" Database seeded successfully!")


# Script goes here!
