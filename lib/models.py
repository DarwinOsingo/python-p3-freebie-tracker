from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    def __repr__(self):
        return f'<Company {self.name}>'

    def give_freebie(self, dev, item_name, value):
        """Create and give a new freebie to a dev, then commit to DB."""
        from models import Freebie  # import here to avoid circular import

        # You need access to the session object here. 
        # Adjust the import path as needed based on your project structure
        from lib import session

        new_freebie = Freebie(
            item_name=item_name,
            value=value,
            company=self,
            dev=dev
        )
        session.add(new_freebie)
        session.commit()
        return new_freebie

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'<Dev {self.name}>'

    def received_one(self, item_name, value, company):
        """Check if this dev already received a freebie matching these details."""
        return any(
            freebie.item_name == item_name and freebie.value == value and freebie.company == company
            for freebie in self.freebies
        )

    def freebie_items(self):
        """List all item names this dev has received."""
        return [freebie.item_name for freebie in self.freebies]

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())

    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    company = relationship("Company", backref=backref("freebies", cascade="all, delete-orphan"))
    dev = relationship("Dev", backref=backref("freebies", cascade="all, delete-orphan"))

    def __repr__(self):
        return f"<Freebie {self.item_name} worth ${self.value}>"
