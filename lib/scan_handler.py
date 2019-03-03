class Scan(object):
    """Handles the scan data"""

    def __init__(self, con, db, lHandler, root, xHandler):
        
        ## Add services now
        for svc in lHandler.sList:
            db.execute('INSERT INTO\
                            `svc_list`\
                        VALUES(?,\
                                ?,\
                                ?,\
                                ?,\
                                ?);',\
                                (svc[0],\
                                svc[1],\
                                svc[2],\
                                svc[3],\
                                svc[4]))

        ## Notate the data for the individual hosts
        hostList = root.findall('host')
        
        ## Parse results
        
        for host in hostList:
            eList = host.iter()
            eDict = {}
            for elem in eList:
                eDict.update({elem.tag: elem})
            address = eDict.get('address').attrib.get('addr')
            addrtype = eDict.get('address').attrib.get('addrtype')
            
            ### Can really expand here
            if xHandler.xmlType == 'nmap':
                for port in eDict.get('ports'):
                    protocol = port.attrib.get('protocol')
                    portid = port.attrib.get('portid')
                    state = port.find('state').attrib.get('state')
                    reason = port.find('state').attrib.get('reason')
                    if port.find('service') is not None:
                        name = port.find('service').attrib.get('name')
                        banner = port.find('service').attrib.get('product')
                    else:
                        name = ''
                        banner = ''
                    ## Add the host to DB
                    db.execute('INSERT OR IGNORE INTO\
                                    `ip_list`\
                                VALUES(?,\
                                        ?,\
                                        ?,\
                                        ?,\
                                        ?,\
                                        ?,\
                                        ?,\
                                        ?);',\
                                        (address,\
                                        addrtype,\
                                        protocol,\
                                        portid,\
                                        state,\
                                        reason,\
                                        name,\
                                        banner))     

            elif xHandler.xmlType == 'masscan':
                protocol = eDict.get('port').attrib.get('protocol')
                portid = eDict.get('port').attrib.get('portid')
                state = eDict.get('state').attrib.get('state')
                reason = eDict.get('state').attrib.get('reason')
                if 'service' in eDict:
                    name = eDict.get('service').attrib.get('name')
                    banner = eDict.get('service').attrib.get('banner')
                else:
                    name = ''
                    banner = ''

            ## Add the host to DB
            db.execute('INSERT OR IGNORE INTO\
                            `ip_list`\
                        VALUES(?,\
                                ?,\
                                ?,\
                                ?,\
                                ?,\
                                ?,\
                                ?,\
                                ?);',\
                                (address,\
                                addrtype,\
                                protocol,\
                                portid,\
                                state,\
                                reason,\
                                name,\
                                banner))       
