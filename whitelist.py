import sqlite3
import os


class Whitelist:
    def __init__(self, results):
        self.raw_domains_list = self.__extract_domains(results)


    def get_domain_whitelist_dict(self):
        white_list_dict = {}
        for domain in self.__check_results_domains(self.raw_domains_list):
            white_list_dict[domain[0]] = domain[0]

        return white_list_dict


    def __extract_domains(self, results):
        domains = []
        for result in results:
            try:
                domains.append(result['domain'])
            except:
                continue

        return domains


    def __check_results_domains(self, raw_domains_list):
        """Check which domains are in whitelist
        Args:
            List:String:Domains retrieved on search results page
        Returns:
            List:Tuple:A single item tuple with a domain name
        """
        domains_db_path = os.path.dirname(__file__) + '/domains.db'
        con = sqlite3.connect(domains_db_path)
        cur = con.cursor()
        cur.execute("SELECT name FROM domain WHERE name IN ({0})"
            .format(", ".join("?" for _ in raw_domains_list)),
            raw_domains_list
        )

        return cur.fetchall()
