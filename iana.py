from pyquery import PyQuery
import re
from datetime import datetime


class Iana:
    """
    Iana website scraper
    """
    base_url = 'http://www.iana.org'
    # todo - add parser for port numbers
    # port_numbers = 'http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml'

    @classmethod
    def tld_list(cls):
        """
        Get list of TLDs
        :return: list of TLDs
        """
        root_db_url = '{0}/domains/root/db'.format(cls.base_url)
        pq = PyQuery(url=root_db_url)
        tlds = []
        for row in pq.find('table#tld-table > tbody > tr').items():
            tld = row('td').eq(0).find('span > a').attr['href']
            tld = tld.replace('/domains/root/db/', '').replace('.html', '').strip()
            tld_type = row('td').eq(1).text().strip()
            desc = row('td').eq(2).text().strip()
            tlds.append(Tld(name=tld, tld_type=tld_type, description=desc))
        return tlds


class Tld:
    RE_LAST_UPDATE = re.compile('Record\s+last\s+updated\s+(.*?)\.', re.IGNORECASE)
    RE_REGISTERATION = re.compile('Registration\s+date\s+(.*?)\.', re.IGNORECASE)

    def __init__(self, name, tld_type=None, description=None):
        self.name = name.encode('idna').decode('idna')
        self.idna = self.name.encode('idna').decode('utf-8')
        self.type = tld_type
        self.description = description
        self.nameservers = []
        self.last_update = None
        self.registration = None

    def __repr__(self):
        return '<TLD: {0}>'.format(self.name)

    def details(self, ):
        url = '{0}/domains/root/db/{1}.html'.format(Iana.base_url, self.idna)
        pq = PyQuery(url=url)
        # -- nameserver
        for row in pq.find('table.iana-table > tbody > tr').items():
            nameserver = row('td').eq(0).text().strip()
            ipaddress = row('td').eq(1).text().strip()
            self.nameservers.append((nameserver, ipaddress))
        # -- dates
        date_items = pq('div#main_right > p > i').text()
        match = Tld.RE_LAST_UPDATE.search(date_items)
        if match:
            self.last_update = datetime.strptime(match.groups()[0], '%Y-%m-%d').date()
        match = Tld.RE_REGISTERATION.search(date_items)
        if match:
            self.registration = datetime.strptime(match.groups()[0], '%Y-%m-%d').date()
