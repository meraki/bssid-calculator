
from meraki_bssid_getter import MerakiBssidGetter

api_key = 'e2aca9806dff8a983e8e21590e2e95416986ee9b'

m = MerakiBssidGetter(api_key)
m.export_org_bssids_to_csv('549236','sandbox-bssids.csv')

