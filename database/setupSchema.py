tables = [
    '''
    CREATE TABLE agency(
        a_id SERIAL PRIMARY KEY,
        name VARCHAR(25),
        street VARCHAR(25),
        city VARCHAR(30),
        state CHAR(2),
        zip integer,
        commission NUMERIC(2, 2)
        )
    ''',
    '''
    CREATE TABLE client(
        c_id SERIAL PRIMARY KEY,
        name VARCHAR(25),
        address TEXT,
        active BOOLEAN DEFAULT false NOT NULL,
        notes TEXT,
        a_id INTEGER,
        commission NUMERIC(2, 2)
    )
    '''
]

