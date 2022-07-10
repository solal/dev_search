# from gettext import install
import sqlite3
import datetime
import uuid
import os
# import grequests


class InstallData:
    def __init__(self):
        self.install_id = self.__get_install_id()

    def __fetch_one(self, sql_query):
        domains_db_path = os.path.dirname(__file__) + '/domains.db'
        con = sqlite3.connect(domains_db_path)
        cur = con.cursor()
        cur.execute(sql_query)
        data = cur.fetchone()
        con.close()
        return data[0]


    def __get_install_id(self):
        install_id = self.__fetch_one("SELECT install_id FROM install_data")

        if install_id is None or install_id == "":
            self.__set_install_id()

        return install_id


    def __get_whitelist_version(self):
        return self.__fetch_one("SELECT whitelist_version FROM install_data")


    def __set_install_id(self):
        now_ms     = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-000%f')
        install_id = str(uuid.uuid4()) + "-" + now_ms

        domains_db_path = os.path.dirname(__file__) + '/domains.db'
        con = sqlite3.connect(domains_db_path)
        cur = con.cursor()
        cur.execute("UPDATE install_data SET install_id = ? WHERE id = 1", (install_id,))
        con.commit()
        con.close()
        return install_id


    def async_check_whitelist_version(self):
        import requests
        requests.post(
            'http://127.0.0.1:5000/check-whitelist-version',
            data={'install_id': self.__get_install_id()}
        )
        # urls   = ['http://127.0.0.1:5000/check-whitelist-version']
        # params = {
        #     'whitelist_version': self.__get_whitelist_version(),
        #     'install_id': self.__get_install_id()
        # }

        # rs = (grequests.post(u, data=params) for u in urls)
        # grequests.map(rs)
