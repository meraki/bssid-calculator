# MerakiBssidGetter is a utility for calculating and exporting bssid information for an organization.
#
# Use it as an object and initialize with your dashboard api key:
#   bssid_getter = MerakiBssidGetter('your-api-key-here')
#
# Once initialized you can get your bssid information in memory or export it to a csv
#   working with it:
#   bssid_info = bssid_getter.get_org_bssids('org-id-here')
#
#   exporting to csv:
#   bssid_getter.export_org_bssids_to_csv('org-id-here','output-filename.csv')
#
# You'll need the id for the organization you want the bssid information for.  
# You can get this information by using the meraki lib function: meraki.myorgaccess('your-api-key')

from meraki import meraki
from meraki_bssid_calculator import MerakiBssidCalculator
import json
import csv

class Bssid:
    def __init__(self,ssid,ap,bssids):
        self.ssid = ssid
        self.ap = ap
        self.bssids = bssids

    def __str__(self):
        return "{ ssid: " + self.ssid + ", ap: " + self.ap + ", bssids: " + json.dumps(self.bssids) + " }"


class MerakiBssidGetter:
    def __init__(self,api_key):
        self.api_key = api_key

    def get_org_bssids(self,org_id):
        org_networks = meraki.getnetworklist(self.api_key,org_id,suppressprint=True)
        self.org_inventory = meraki.getorginventory(self.api_key,org_id,suppressprint=True)
        bssids = {}
        for network in org_networks:
            bssids[network['name']] = self.__get_bssids_for_network(network)
        return bssids

    def export_org_bssids_to_csv(self,org_id,filename='bssids.csv'):
        bssids = self.get_org_bssids(org_id)
        output = [
            ['Network name', 'SSID name', 'AP mac', '2.4 BSSID', '5 BSSID']
        ]
        for network in bssids:
            for bssid in bssids[network]:
                output_line = [
                    network,
                    bssid.ssid,
                    bssid.ap,
                    bssid.bssids['2.4'],
                    bssid.bssids['5']
                ]
                output.append(output_line)
        with open(filename,'w') as outfile:
            output_writer = csv.writer(
                outfile,
                lineterminator='\n'
            )
            for line in output:
                output_writer.writerow(line)

    def __get_bssids_for_network(self,network):
        aps = self.__get_aps_for_network(network)
        if (len(aps) > 0):
            ssids = self.__get_ssids_for_network(network)
        else:
            ssids = []
        bssids = []
        for ssid in ssids:
            for ap in aps:
                bssids.append(
                    Bssid(
                        ssid=ssid['name'],
                        ap=ap['mac'],
                        bssids=MerakiBssidCalculator.calculate(ap['model'],ap['mac'],ssid['number']+1)
                ))
        return bssids

    def __get_aps_for_network(self,network):
        aps = []
        for device in self.org_inventory:
            if ((device['model'][:2] == "MR") and (device['networkId'] == network['id'])):
                aps.append(device)
        return aps

    def __get_ssids_for_network(self,network):
        ssids = []
        if ('configTemplateId' in network):
            network_id = network['configTemplateId']
        else:
            network_id = network['id']
        for ssid in meraki.getssids(self.api_key,network_id,suppressprint=True):
            if (ssid['enabled'] == True):
                ssids.append(ssid)
        return ssids


