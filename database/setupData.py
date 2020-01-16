# skipping core, exact, genre, all order

data = [
    '''
    INSERT INTO agency(
        name, street, city, state, zip, commission
    )
    VALUES(
        'Huntington',
        '990 Grove',
        'Evanston',
        'IL',
        60201,
        0.15
    )
    ''',
    '''
    INSERT INTO client(
        name, address, a_id, commission
    )
    VALUES(
        'ABC Client', 
        '1345 W. Housten St.',
        1,
        0.15
    )
    ''' ,
    '''
    INSERT INTO contacts(
        first_name,
        last_name,
        email,
        r_id,
        c_id,
        phone,
        fax,
        type
    )
    VALUES(
        'Jane',
        'Doe',
        'jd@ABC.com',
        1,
        1,
        1112223333,
        5556667777,
        'CLIENT'
    )
    ''',
    '''
    INSERT INTO media(
        prey,
        title,
        number,
        isci,
        length,
        c_id,
        catNum
    )
    VALUES(
        'WNDF890',
        'WONDERFUL PRODUCT',
        8009997654,
        'WNDF890-7654',
        60,
        1,
        'H001'
    )
    '''
]
