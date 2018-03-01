# -*- coding: utf-8 -*-
# Code automatically generated by pycrate_asn1c

from pycrate_asn1rt.utils            import *
from pycrate_asn1rt.err              import *
from pycrate_asn1rt.glob             import make_GLOBAL, GLOBAL
from pycrate_asn1rt.dictobj          import ASN1Dict
from pycrate_asn1rt.refobj           import *
from pycrate_asn1rt.setobj           import *
from pycrate_asn1rt.asnobj_basic     import *
from pycrate_asn1rt.asnobj_str       import *
from pycrate_asn1rt.asnobj_construct import *
from pycrate_asn1rt.asnobj_class     import *
from pycrate_asn1rt.asnobj_ext       import *
from pycrate_asn1rt.init             import init_modules

class RFC1155_SMI:

    _name_  = 'RFC1155-SMI'
    _oid_   = []
    
    _obj_ = [
        'internet',
        'directory',
        'mgmt',
        'experimental',
        'private',
        'enterprises',
        'ObjectName',
        'ObjectSyntax',
        'SimpleSyntax',
        'ApplicationSyntax',
        'NetworkAddress',
        'IpAddress',
        'Counter',
        'Gauge',
        'TimeTicks',
        'Opaque',
        ]
    _type_ = [
        'ObjectName',
        'ObjectSyntax',
        'SimpleSyntax',
        'ApplicationSyntax',
        'NetworkAddress',
        'IpAddress',
        'Counter',
        'Gauge',
        'TimeTicks',
        'Opaque',
        ]
    _set_ = [
        ]
    _val_ = [
        'internet',
        'directory',
        'mgmt',
        'experimental',
        'private',
        'enterprises',
        ]
    _class_ = [
        ]
    _param_ = [
        ]
    
    #-----< internet >-----#
    internet = OID(name='internet', mode=MODE_VALUE)
    internet._val = (1, 3, 6, 1)
    
    #-----< directory >-----#
    directory = OID(name='directory', mode=MODE_VALUE)
    directory._val = (1, 3, 6, 1, 1)
    
    #-----< mgmt >-----#
    mgmt = OID(name='mgmt', mode=MODE_VALUE)
    mgmt._val = (1, 3, 6, 1, 2)
    
    #-----< experimental >-----#
    experimental = OID(name='experimental', mode=MODE_VALUE)
    experimental._val = (1, 3, 6, 1, 3)
    
    #-----< private >-----#
    private = OID(name='private', mode=MODE_VALUE)
    private._val = (1, 3, 6, 1, 4)
    
    #-----< enterprises >-----#
    enterprises = OID(name='enterprises', mode=MODE_VALUE)
    enterprises._val = (1, 3, 6, 1, 4, 1)
    
    #-----< ObjectName >-----#
    ObjectName = OID(name='ObjectName', mode=MODE_TYPE)
    
    #-----< ObjectSyntax >-----#
    ObjectSyntax = CHOICE(name='ObjectSyntax', mode=MODE_TYPE)
    _ObjectSyntax_simple = CHOICE(name='simple', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'SimpleSyntax')))
    _ObjectSyntax_application_wide = CHOICE(name='application-wide', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'ApplicationSyntax')))
    ObjectSyntax._cont = ASN1Dict([
        ('simple', _ObjectSyntax_simple),
        ('application-wide', _ObjectSyntax_application_wide),
        ])
    ObjectSyntax._ext = None
    
    #-----< SimpleSyntax >-----#
    SimpleSyntax = CHOICE(name='SimpleSyntax', mode=MODE_TYPE)
    _SimpleSyntax_number = INT(name='number', mode=MODE_TYPE)
    _SimpleSyntax_string = OCT_STR(name='string', mode=MODE_TYPE)
    _SimpleSyntax_object = OID(name='object', mode=MODE_TYPE)
    _SimpleSyntax_empty = NULL(name='empty', mode=MODE_TYPE)
    SimpleSyntax._cont = ASN1Dict([
        ('number', _SimpleSyntax_number),
        ('string', _SimpleSyntax_string),
        ('object', _SimpleSyntax_object),
        ('empty', _SimpleSyntax_empty),
        ])
    SimpleSyntax._ext = None
    
    #-----< ApplicationSyntax >-----#
    ApplicationSyntax = CHOICE(name='ApplicationSyntax', mode=MODE_TYPE)
    _ApplicationSyntax_address = CHOICE(name='address', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'NetworkAddress')))
    _ApplicationSyntax_counter = INT(name='counter', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'Counter')))
    _ApplicationSyntax_gauge = INT(name='gauge', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'Gauge')))
    _ApplicationSyntax_ticks = INT(name='ticks', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'TimeTicks')))
    _ApplicationSyntax_arbitrary = OCT_STR(name='arbitrary', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'Opaque')))
    ApplicationSyntax._cont = ASN1Dict([
        ('address', _ApplicationSyntax_address),
        ('counter', _ApplicationSyntax_counter),
        ('gauge', _ApplicationSyntax_gauge),
        ('ticks', _ApplicationSyntax_ticks),
        ('arbitrary', _ApplicationSyntax_arbitrary),
        ])
    ApplicationSyntax._ext = None
    
    #-----< NetworkAddress >-----#
    NetworkAddress = CHOICE(name='NetworkAddress', mode=MODE_TYPE)
    _NetworkAddress_internet = OCT_STR(name='internet', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'IpAddress')))
    NetworkAddress._cont = ASN1Dict([
        ('internet', _NetworkAddress_internet),
        ])
    NetworkAddress._ext = None
    
    #-----< IpAddress >-----#
    IpAddress = OCT_STR(name='IpAddress', mode=MODE_TYPE, tag=(0, TAG_APPLICATION, TAG_IMPLICIT))
    IpAddress._const_sz = ASN1Set(rv=[4], rr=[], ev=None, er=[])
    
    #-----< Counter >-----#
    Counter = INT(name='Counter', mode=MODE_TYPE, tag=(1, TAG_APPLICATION, TAG_IMPLICIT))
    Counter._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=4294967295)], ev=None, er=[])
    
    #-----< Gauge >-----#
    Gauge = INT(name='Gauge', mode=MODE_TYPE, tag=(2, TAG_APPLICATION, TAG_IMPLICIT))
    Gauge._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=4294967295)], ev=None, er=[])
    
    #-----< TimeTicks >-----#
    TimeTicks = INT(name='TimeTicks', mode=MODE_TYPE, tag=(3, TAG_APPLICATION, TAG_IMPLICIT))
    TimeTicks._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=4294967295)], ev=None, er=[])
    
    #-----< Opaque >-----#
    Opaque = OCT_STR(name='Opaque', mode=MODE_TYPE, tag=(4, TAG_APPLICATION, TAG_IMPLICIT))
    
    _all_ = [
        internet,
        directory,
        mgmt,
        experimental,
        private,
        enterprises,
        ObjectName,
        _ObjectSyntax_simple,
        _ObjectSyntax_application_wide,
        ObjectSyntax,
        _SimpleSyntax_number,
        _SimpleSyntax_string,
        _SimpleSyntax_object,
        _SimpleSyntax_empty,
        SimpleSyntax,
        _ApplicationSyntax_address,
        _ApplicationSyntax_counter,
        _ApplicationSyntax_gauge,
        _ApplicationSyntax_ticks,
        _ApplicationSyntax_arbitrary,
        ApplicationSyntax,
        _NetworkAddress_internet,
        NetworkAddress,
        IpAddress,
        Counter,
        Gauge,
        TimeTicks,
        Opaque,
    ]

class RFC1157_SNMP:

    _name_  = 'RFC1157-SNMP'
    _oid_   = []
    
    _obj_ = [
        'Message',
        'PDUs',
        'GetRequest-PDU',
        'GetNextRequest-PDU',
        'GetResponse-PDU',
        'SetRequest-PDU',
        'PDU',
        'Trap-PDU',
        'VarBind',
        'VarBindList',
        ]
    _type_ = [
        'Message',
        'PDUs',
        'GetRequest-PDU',
        'GetNextRequest-PDU',
        'GetResponse-PDU',
        'SetRequest-PDU',
        'PDU',
        'Trap-PDU',
        'VarBind',
        'VarBindList',
        ]
    _set_ = [
        ]
    _val_ = [
        ]
    _class_ = [
        ]
    _param_ = [
        ]
    
    #-----< Message >-----#
    Message = SEQ(name='Message', mode=MODE_TYPE)
    _Message_version = INT(name='version', mode=MODE_TYPE)
    _Message_version._cont = ASN1Dict([('version-1', 0)])
    _Message_community = OCT_STR(name='community', mode=MODE_TYPE)
    _Message_data = CHOICE(name='data', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1157-SNMP', 'PDUs')))
    Message._cont = ASN1Dict([
        ('version', _Message_version),
        ('community', _Message_community),
        ('data', _Message_data),
        ])
    Message._ext = None
    
    #-----< PDUs >-----#
    PDUs = CHOICE(name='PDUs', mode=MODE_TYPE)
    _PDUs_get_request = SEQ(name='get-request', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1157-SNMP', 'GetRequest-PDU')))
    _PDUs_get_next_request = SEQ(name='get-next-request', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1157-SNMP', 'GetNextRequest-PDU')))
    _PDUs_get_response = SEQ(name='get-response', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1157-SNMP', 'GetResponse-PDU')))
    _PDUs_set_request = SEQ(name='set-request', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1157-SNMP', 'SetRequest-PDU')))
    _PDUs_trap = SEQ(name='trap', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1157-SNMP', 'Trap-PDU')))
    PDUs._cont = ASN1Dict([
        ('get-request', _PDUs_get_request),
        ('get-next-request', _PDUs_get_next_request),
        ('get-response', _PDUs_get_response),
        ('set-request', _PDUs_set_request),
        ('trap', _PDUs_trap),
        ])
    PDUs._ext = None
    
    #-----< GetRequest-PDU >-----#
    GetRequest_PDU = SEQ(name='GetRequest-PDU', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('RFC1157-SNMP', 'PDU')))
    
    #-----< GetNextRequest-PDU >-----#
    GetNextRequest_PDU = SEQ(name='GetNextRequest-PDU', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('RFC1157-SNMP', 'PDU')))
    
    #-----< GetResponse-PDU >-----#
    GetResponse_PDU = SEQ(name='GetResponse-PDU', mode=MODE_TYPE, tag=(2, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('RFC1157-SNMP', 'PDU')))
    
    #-----< SetRequest-PDU >-----#
    SetRequest_PDU = SEQ(name='SetRequest-PDU', mode=MODE_TYPE, tag=(3, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('RFC1157-SNMP', 'PDU')))
    
    #-----< PDU >-----#
    PDU = SEQ(name='PDU', mode=MODE_TYPE)
    _PDU_request_id = INT(name='request-id', mode=MODE_TYPE)
    _PDU_error_status = INT(name='error-status', mode=MODE_TYPE)
    _PDU_error_status._cont = ASN1Dict([('noError', 0), ('tooBig', 1), ('noSuchName', 2), ('badValue', 3), ('readOnly', 4), ('genErr', 5)])
    _PDU_error_index = INT(name='error-index', mode=MODE_TYPE)
    _PDU_variable_bindings = SEQ_OF(name='variable-bindings', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1157-SNMP', 'VarBindList')))
    PDU._cont = ASN1Dict([
        ('request-id', _PDU_request_id),
        ('error-status', _PDU_error_status),
        ('error-index', _PDU_error_index),
        ('variable-bindings', _PDU_variable_bindings),
        ])
    PDU._ext = None
    
    #-----< Trap-PDU >-----#
    Trap_PDU = SEQ(name='Trap-PDU', mode=MODE_TYPE, tag=(4, TAG_CONTEXT_SPEC, TAG_IMPLICIT))
    _Trap_PDU_enterprise = OID(name='enterprise', mode=MODE_TYPE)
    _Trap_PDU_agent_addr = CHOICE(name='agent-addr', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'NetworkAddress')))
    _Trap_PDU_generic_trap = INT(name='generic-trap', mode=MODE_TYPE)
    _Trap_PDU_generic_trap._cont = ASN1Dict([('coldStart', 0), ('warmStart', 1), ('linkDown', 2), ('linkUp', 3), ('authenticationFailure', 4), ('egpNeighborLoss', 5), ('enterpriseSpecific', 6)])
    _Trap_PDU_specific_trap = INT(name='specific-trap', mode=MODE_TYPE)
    _Trap_PDU_time_stamp = INT(name='time-stamp', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'TimeTicks')))
    _Trap_PDU_variable_bindings = SEQ_OF(name='variable-bindings', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1157-SNMP', 'VarBindList')))
    Trap_PDU._cont = ASN1Dict([
        ('enterprise', _Trap_PDU_enterprise),
        ('agent-addr', _Trap_PDU_agent_addr),
        ('generic-trap', _Trap_PDU_generic_trap),
        ('specific-trap', _Trap_PDU_specific_trap),
        ('time-stamp', _Trap_PDU_time_stamp),
        ('variable-bindings', _Trap_PDU_variable_bindings),
        ])
    Trap_PDU._ext = None
    
    #-----< VarBind >-----#
    VarBind = SEQ(name='VarBind', mode=MODE_TYPE)
    _VarBind_name = OID(name='name', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'ObjectName')))
    _VarBind_value = CHOICE(name='value', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1155-SMI', 'ObjectSyntax')))
    VarBind._cont = ASN1Dict([
        ('name', _VarBind_name),
        ('value', _VarBind_value),
        ])
    VarBind._ext = None
    
    #-----< VarBindList >-----#
    VarBindList = SEQ_OF(name='VarBindList', mode=MODE_TYPE)
    _VarBindList__item_ = SEQ(name='_item_', mode=MODE_TYPE, typeref=ASN1RefType(('RFC1157-SNMP', 'VarBind')))
    VarBindList._cont = _VarBindList__item_
    
    _all_ = [
        _Message_version,
        _Message_community,
        _Message_data,
        Message,
        _PDUs_get_request,
        _PDUs_get_next_request,
        _PDUs_get_response,
        _PDUs_set_request,
        _PDUs_trap,
        PDUs,
        GetRequest_PDU,
        GetNextRequest_PDU,
        GetResponse_PDU,
        SetRequest_PDU,
        _PDU_request_id,
        _PDU_error_status,
        _PDU_error_index,
        _PDU_variable_bindings,
        PDU,
        _Trap_PDU_enterprise,
        _Trap_PDU_agent_addr,
        _Trap_PDU_generic_trap,
        _Trap_PDU_specific_trap,
        _Trap_PDU_time_stamp,
        _Trap_PDU_variable_bindings,
        Trap_PDU,
        _VarBind_name,
        _VarBind_value,
        VarBind,
        _VarBindList__item_,
        VarBindList,
    ]

init_modules(RFC1155_SMI, RFC1157_SNMP)