# ![Logo](https://s13.postimg.org/thnfbvzc7/www.png) IANA TopLevelDomain Scraper

Extracting top-level-domain information from Internet Assigned Numbers
Authority (IANA) website.

### List of all TopLevelDomains
```python
iana = Iana.tld_list()
print(iana)
```

```javascript
[
    <TLD: aaa>,
    <TLD: aarp>,
    <TLD: abarth>,
    <TLD: abb>,
    <TLD: abbott>,
]
```

### TLD Object
```python
print(vars(iana[0]))
```

```javascript
{
    'name': 'aaa',
    'idna': 'aaa',
    'type': 'generic',
    'description': 'American Automobile Association, Inc.',
    'nameservers': [],
    'last_update': None,
    'registration': None
}
```

### Fetching details (nameserver, registration) for TLD object
```python
iana[0].details()
print(vars(iana[0]))
```

```javascript
{
    'name': 'aaa',
    'idna': 'aaa',
    'type': 'generic',
    'description': 'American Automobile Association, Inc.',
    'nameservers': [
        ('ns6.dns.nic.aaa', '156.154.158.2 2610:a1:1076:0:0:0:0:2'),
        ('ns4.dns.nic.aaa', '156.154.156.2 2610:a1:1074:0:0:0:0:2'),
        ('ns2.dns.nic.aaa', '156.154.145.2 2610:a1:1072:0:0:0:0:2'),
        ('ns3.dns.nic.aaa', '156.154.159.2 2610:a1:1073:0:0:0:0:2'),
        ('ns1.dns.nic.aaa', '156.154.144.2 2610:a1:1071:0:0:0:0:2'),
        ('ns5.dns.nic.aaa', '156.154.157.2 2610:a1:1075:0:0:0:0:2')],
    'last_update': datetime.date(2016, 11, 8),
    'registration': datetime.date(2015, 8, 13)
}
```
