# Foreign keys:
#           a_id: agency.id
#           b_id: broadcast.id
#           c_id: client.id
#           con_id: contact.id
#           ep_id episode.id
#           inv_id invoice.id
#           l_id
#           m_id: media.id
#           o_id order.id
#           od_id order_day.id
#           odwk_id order_week.id
#           s_id


tables = [
    '''
    CREATE TABLE agency(
        id SERIAL PRIMARY KEY,
        name VARCHAR(25),
        street VARCHAR(25),
        city VARCHAR(30),
        state CHAR(2),
        zip INTEGER,
        commission NUMERIC(2, 2)
        )
    ''',
    '''
    CREATE TABLE broadcast_calendar(
        id SERIAL PRIMARY KEY,
        month CHAR(10),
        start DATE,
        stop DATE
    )
    ''',
    '''
    CREATE TABLE client(
        id SERIAL PRIMARY KEY,
        name VARCHAR(25),
        address TEXT,
        active BOOLEAN DEFAULT false NOT NULL,
        notes TEXT,
        a_id INTEGER,
        commission NUMERIC(2, 2)
    )
    ''',
    '''
    CREATE TABLE contacts(
        id SERIAL PRIMARY KEY,
        first_name CHAR(20),
        last_name CHAR(20),
        email VARCHAR(35),
        r_id INTEGER,
        c_id INTEGER,
        phone BIGINT,
        fax BIGINT,
        type CHAR(6),
        a_id INTEGER
   )
    ''',
    '''
    CREATE TABLE core(
        id SERIAL PRIMARY KEY,
        media VARCHAR(4) DEFAULT 'TV',
        product VARCHAR(4),
        estimate VARCHAR(4),
        access VARCHAR(4),
        markt VARCHAR(4),
        station VARCHAR(5) DEFAULT 'VIBRA',
        band VARCHAR,
        header VARCHAR,
        const INTEGER DEFAULT 0,
        program VARCHAR(4),
        type VARCHAR(4) DEFAULT 'POST',
        m_id INTEGER,
        syscode VARCHAR(4),
        active BOOLEAN DEFAULT false NOT NULL
    )
    ''',
    '''
    CREATE TABLE exact(
        id SERIAL PRIMARY KEY,
        c_id INTEGER,
        m_id INTEGER,
        s_id INTEGER,
        ep_id INTEGER,
        l_id INTEGER,
        run_day CHAR(2),
        run_date DATE,
        run_time TIME,
        inv_id INTEGER,
        rate MONEY,
        o_id INTEGER,
        od_id INTEGER,
        odwk_id INTEGER,
        paid BOOLEAN DEFAULT false NOT NULL,
        pi BOOLEAN DEFAULT false
    )
    ''',
    '''
    CREATE TABLE genre(
        id SERIAL PRIMARY KEY,
        s_id INTEGER,
        genre VARCHAR(40),
        description TEXT
    )
    ''',
    '''
    CREATE TABLE media(
        id SERIAL PRIMARY KEY,
        prey VARCHAR(60),
        title VARCHAR(60),
        number VARCHAR(12),
        isci VARCHAR(30),
        length SMALLINT,
        c_id INTEGER,
        active BOOLEAN DEFAULT true NOT NULL,
        catNum VARCHAR(4),
        ul BOOLEAN DEFAULT false NOT NULL,
        advertiser CHAR(30),
        product CHAR(20),
        p_description CHAR(50),
        sep INTEGER DEFAULT 3600,
        txt BOOLEAN DEFAULT true,
        pdf BOOLEAN DEFAULT false,
        csv BOOLEAN DEFAULT false,
        excel BOOLEAN DEFAULT false
    )
    ''',
    '''
    CREATE TABLE order_head(
        id SERIAL PRIMARY KEY,
        c_id INTEGER,
        m_id INTEGER,
        con_id INTEGER,
        start DATE,
        stop DATE,
        rev INTEGER DEFAULT 0,
        pi BOOLEAN DEFAULT false,
        change TEXT,
        inv BOOLEAN DEFAULT true
    )
    ''',
    '''
    CREATE TABLE order_det(
       id SERIAL PRIMARY KEY,
       start_t TIME,
       end_t TIME,
       rate MONEY,
       line INTEGER,
       days VARCHAR,
       o_id INTEGER,
       change TEXT
    )
    ''',
    '''
    CREATE TABLE order_det_wk(
        id SERIAL PRIMARY KEY,
        o_id INTEGER,
        od_id INTEGER,
        wo DATE,
        times INTEGER,
        line INTEGER,
        change TEXT
    )
    '''
]

