


# Purpose
# demo python regex name group functionality



import re



s = """
iPerfRemote\,10.0.16.63\,ethaddr=00C017330EAA\,2.2.170\,1000\,PS90.697141\,PS845.299335\,EtherTypeCDP\,DeviceIDAP_1702i_01_00f6.6378.3270.minions.lab\,Addresses010.000.001.003\,PlatformciscoAIR-CAP1702I-B-K9\,PortIDGigabitEthernet0\,VlanID
"""



__ = re.search(r'Addresses(?P<IP>(([0-9]{3}\.){3}[0-9]{3}))', s)

if not __ is None:
    print('IP = {}'.format(__.group('IP')))

__ = re.search(r'ethaddr=(?P<MAC>(([0-9A-F])+))\\\,(?P<V>([0-9]+(\.)?){3})', s)

if not __ is None:
    print('MAC = {}'.format(__.group('MAC')))
    print('VERSION = {}'.format(__.group('V')))
