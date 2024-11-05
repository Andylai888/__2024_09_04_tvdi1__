sql
'''
CREATE TABLE IF NOT EXISTS records (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	sitename TEXT NOT NULL,
	county TEXT,
	aqi INTEGER,
	status TEXT,
	pm25 NUMERIC,
	date TEXT,
	lat NUMERIC,
	lon NUMERIC,
    UNIQUE (sitename,date)
);
'''