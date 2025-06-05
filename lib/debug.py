#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

# Setup engine and session
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Sample queries to poke around with
print("\n--- Devs ---")
for dev in session.query(Dev).all():
    print(dev)

print("\n--- Companies ---")
for company in session.query(Company).all():
    print(company)

print("\n--- Freebies ---")
for freebie in session.query(Freebie).all():
    print(f"{freebie.dev.name} got a {freebie.item_name} from {freebie.company.name}")

# Start interactive debugger
import ipdb; ipdb.set_trace()
