RFC1155 = {'RFC1155-SMI': {'extensibility-implied': False,
                 'imports': {},
                 'object-classes': {},
                 'object-sets': {},
                 'types': {'ApplicationSyntax': {'members': [{'name': 'address',
                                                              'optional': False,
                                                              'type': 'NetworkAddress'},
                                                             {'name': 'counter',
                                                              'optional': False,
                                                              'type': 'Counter'},
                                                             {'name': 'gauge',
                                                              'optional': False,
                                                              'type': 'Gauge'},
                                                             {'name': 'ticks',
                                                              'optional': False,
                                                              'type': 'TimeTicks'},
                                                             {'name': 'arbitrary',
                                                              'optional': False,
                                                              'type': 'Opaque'}],
                                                 'type': 'CHOICE'},
                           'Counter': {'restricted-to': [(0, 4294967295)],
                                       'tag': {'class': 'APPLICATION',
                                               'kind': 'IMPLICIT',
                                               'number': 1},
                                       'type': 'INTEGER'},
                           'Gauge': {'restricted-to': [(0, 4294967295)],
                                     'tag': {'class': 'APPLICATION',
                                             'kind': 'IMPLICIT',
                                             'number': 2},
                                     'type': 'INTEGER'},
                           'IpAddress': {'size': [4],
                                         'tag': {'class': 'APPLICATION',
                                                 'kind': 'IMPLICIT',
                                                 'number': 0},
                                         'type': 'OCTET STRING'},
                           'NetworkAddress': {'members': [{'name': 'internet',
                                                           'optional': False,
                                                           'type': 'IpAddress'}],
                                              'type': 'CHOICE'},
                           'ObjectName': {'type': 'OBJECT IDENTIFIER'},
                           'ObjectSyntax': {'members': [{'name': 'simple',
                                                         'optional': False,
                                                         'type': 'SimpleSyntax'},
                                                        {'name': 'application-wide',
                                                         'optional': False,
                                                         'type': 'ApplicationSyntax'}],
                                            'type': 'CHOICE'},
                           'Opaque': {'size': None,
                                      'tag': {'class': 'APPLICATION',
                                              'kind': 'IMPLICIT',
                                              'number': 4},
                                      'type': 'OCTET STRING'},
                           'SimpleSyntax': {'members': [{'name': 'number',
                                                         'optional': False,
                                                         'type': 'INTEGER'},
                                                        {'name': 'string',
                                                         'optional': False,
                                                         'size': None,
                                                         'type': 'OCTET '
                                                                 'STRING'},
                                                        {'name': 'object',
                                                         'optional': False,
                                                         'type': 'OBJECT '
                                                                 'IDENTIFIER'},
                                                        {'name': 'empty',
                                                         'optional': False,
                                                         'type': 'NULL'}],
                                            'type': 'CHOICE'},
                           'TimeTicks': {'restricted-to': [(0, 4294967295)],
                                         'tag': {'class': 'APPLICATION',
                                                 'kind': 'IMPLICIT',
                                                 'number': 3},
                                         'type': 'INTEGER'}},
                 'values': {'directory': {'type': 'OBJECT IDENTIFIER',
                                          'value': ['internet', 1]},
                            'enterprises': {'type': 'OBJECT IDENTIFIER',
                                            'value': ['private', 1]},
                            'experimental': {'type': 'OBJECT IDENTIFIER',
                                             'value': ['internet', 3]},
                            'internet': {'type': 'OBJECT IDENTIFIER',
                                         'value': ['iso',
                                                   ('org', 3),
                                                   ('dod', 6),
                                                   1]},
                            'mgmt': {'type': 'OBJECT IDENTIFIER',
                                     'value': ['internet', 2]},
                            'private': {'type': 'OBJECT IDENTIFIER',
                                        'value': ['internet', 4]}}}}