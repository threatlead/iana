from .context import iana
import unittest


class TestIana(unittest.TestCase):

    def test_tld_list(self):
        tlds = iana.Iana.tld_list()
        self.assertGreater(len(tlds), 1500, 'Found a total of {0} threat types'.format(len(tlds)))
        self.assertEqual(tlds[0].__class__.__name__, 'Tld', 'Incorrect object returned')

    def test_tld_details(self):
        zw = iana.Tld(name='zw')
        zw.details()
        self.assertGreater(len(zw.nameservers), 1, 'Tld details failed to fetch nameservers')
        self.assertTrue(zw.last_update, 'TLd details failed to fetch last_update')


if __name__ == '__main__':
    unittest.main()
