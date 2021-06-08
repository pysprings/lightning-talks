#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script shows an example of using Fernet encryption on a database column
(aka "encryption at rest").
https://github.com/fernet/spec/blob/master/Spec.md

Fernet uses "symmetric encryption" (kinda like a password) to encrypt data.
https://cryptography.io/en/latest/fernet/

We can use this with the functionality provided by sqlalchemy_utils.

The use case presented in this script is to protect PII (personal identifiable information).

https://www.dhs.gov/privacy-training/what-personally-identifiable-information
> DHS defines personally identifiable information or PII as any information that
> permits the identity of an individual to be directly or indirectly inferred,
> including any information that is linked or linkable to that individual, regardless
> of whether the individual is a U.S. citizen, lawful permanent resident, visitor
> to the U.S., or employee or contractor to the Department.
"""
import os

from cryptography.fernet import Fernet
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import FernetEngine

# Boilerplate to create the database and connect sqlalchemy
engine = create_engine("sqlite:///fernet-test.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# This is the key used for encryption/decryption:
FERNET_KEY = "A1THRr76-8BUNRAA4iBtI2bf8emHg1Zt-U0ExXl12VE="


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, nullable=False)

    # username will be stored in plain text
    username = Column(String, nullable=False)

    # email will be stored encrypted and automatically decrypted when used by
    # sqlalchemy.
    # https://sqlalchemy-utils.readthedocs.io/en/latest/_modules/sqlalchemy_utils/types/encrypted/encrypted_type.html
    email = Column(
        StringEncryptedType(String, FERNET_KEY, FernetEngine),
        nullable=False,
    )


# Initialize the database will any class that inherits from `Base`.
Base.metadata.create_all(bind=engine)


def generate_keys():
    """Sample method of generating some Fernet from which to choose."""
    for _ in range(10):
        print(Fernet.generate_key().decode("utf-8"))


def init_db():
    """Remove any existing data from the database, and populate the database with sample data."""
    session = SessionLocal()
    session.add_all(
        [
            Profile(username="Donkey", email="kong@nintendo.com"),
            Profile(username="Peach", email="peach@nintendo.com"),
            Profile(username="Mario", email="mario@nintendo.com"),
        ]
    )
    session.commit()

    print("Database has been initialized")


def show_profiles():
    """Iterate through all profiles to show that the app doesn't have to care about encryption"""
    if not os.path.isfile("fernet-test.db"):
        init_db()

    session = SessionLocal()
    for profile in session.query(Profile).all():
        print(f"username: {profile.username}; email: {profile.email}")

    # The side affect is that you cannot query on the encrypted field.
    donkey = session.query(Profile).where(Profile.email == "kong@nintendo.com").first()
    assert not donkey


def search_email(email: str):
    """Iterate through all profiles and look for an encrypted email."""
    session = SessionLocal()
    for profile in session.query(Profile).all():
        # NOTE: This works because sqlalchemy is decrypting the `Profile` field(s).
        if profile.email == email:
            print(f"user {profile.username} has the email of {email}")
            break
    else:
        print(f"No user found with an email of {email}")


if __name__ == "__main__":
    generate_keys()
    # init_db()
    # show_profiles()
    # search_email("kong@nintendo.com")
