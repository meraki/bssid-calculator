
from meraki_bssid_getter import MerakiBssidGetter

api_key = 'cc54e1f9520616813f654aab8e0dfc614e33c179 '

m = MerakiBssidGetter(api_key)
m.export_org_bssids_to_csv('549236','sandbox-bssids.csv')

