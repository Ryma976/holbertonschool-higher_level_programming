#!/usr/bin/python3
"""Lists all State objects and corresponding City objects using a single query."""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying State and City using outerjoin creates a SINGLE SQL query with proper ordering
    results = (
        session.query(State)
        .outerjoin(City)
        .order_by(State.id.asc(), City.id.asc())
        .all()
    )

    for state in results:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
