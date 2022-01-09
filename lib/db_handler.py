class Database(object):
    """Handles any database preparation, pre-processing"""

    def __init__(self, db):
        self.db = db


    def scan_prep(self):
        """Prep the scan table"""
        self.db.execute("""
                        CREATE TABLE IF NOT EXISTS
                            `ip_list`("ip" TEXT,
                                      "protocol" TEXT,
                                      "portid" INT,
                                      "state" TEXT,
                                      "reason" TEXT,
                                      "name" TEXT,
                                      "banner" TEXT);
                                             """)


    def svc_prep(self):
        """Prep the services table"""
        self.db.execute('CREATE TABLE IF NOT EXISTS\
                            `svc_list`("name" TEXT,\
                                       "portid" INT,\
                                       "proto" TEXT,\
                                       "freq" TEXT,\
                                       "cmt" TEXT);')
