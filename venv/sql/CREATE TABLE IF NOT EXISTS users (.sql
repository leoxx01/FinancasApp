CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL ,
    date_created TEXT DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS entries   (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nameEntries TEXT NOT NULL,
    value TEXT NOT NULL ,
    id_user TEXT NOT NULL ,
    date_created TEXT DEFAULT CURRENT_TIMESTAMP
    
);

CREATE TABLE IF NOT EXISTS leaves   (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nameLeave TEXT NOT NULL,
    value TEXT NOT NULL,
    installments TEXT NOT NULL ,
    pays_installments TEXT NOT NUll,
    pays_finish TEXT NOT NULL,
    id_user TEXT NOT NULL ,
    date_created TEXT DEFAULT CURRENT_TIMESTAMP
    
);

CREATE TABLE IF NOT EXISTS investments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_Investiments TEXT NOT NULL,
    type_investments TEXT NOT NULL, 
    value TEXT NOT NULL,
    profitability text NOT NULL,
    id_user TEXT NOT NULL ,
    date_created TEXT DEFAULT CURRENT_TIMESTAMP
    
);

