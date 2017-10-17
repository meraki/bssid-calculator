# MerakiBssidCalculator is a utility for figuring out a bssid for your Meraki AP's
# 
# Full documentation on how these calculations are made can be found in Meraki's online documentation:
# https://documentation.meraki.com/MR/WiFi_Basics_and_Best_Practices/Calculating_Cisco_Meraki_BSSID_MAC_Addresses
# 
# Based on that document, the calculator defines 3 families of access points that have unique bssid calculations.
# To calculate the bssid, each octet of the AP's mac is offset by a value defined per oui per radio per ssid 
#
# These are statically configured as 'offset_families' and combined with a provided ap mac and ssid number
#
# Use the calculator as a stateless function:
# MerakiBssidCalculator.calculate(ap_model,ap_mac,ssid_number)
#
# For example:
# MerakiBssidCalculator.calculate("MR53","0c:8d:db:00:00:00",12)
#
# will output the bssid for each radio:
# {'2.4': '22:8d:db:00:00:00', '5': '22:8d:cb:00:00:00'}

class MerakiBssidCalculator:
    offset_families = {
        1: {
            "00:18:0a": {
                "2.4": {
                    1: {1:0x00,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    2: {1:0x06,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    3: {1:0x0a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    4: {1:0x0e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    5: {1:0x12,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    6: {1:0x16,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    7: {1:0x1a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    8: {1:0x1e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    9: {1:0x22,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    10: {1:0x26,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    11: {1:0x2a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    12: {1:0x2e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    13: {1:0x32,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    14: {1:0x36,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    15: {1:0x3a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00}
                },
                "5": {
                    1: {1:0x02,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    2: {1:0x06,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    3: {1:0x0a,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    4: {1:0x0e,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    5: {1:0x12,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    6: {1:0x16,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    7: {1:0x1a,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    8: {1:0x1e,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    9: {1:0x22,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    10: {1:0x26,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    11: {1:0x2a,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    12: {1:0x2e,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    13: {1:0x32,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    14: {1:0x36,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    15: {1:0x3a,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00}
                }
            },
            "88:15:44": {
                "2.4": {
                    1: {1:0x00,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    2: {1:0x06,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    3: {1:-0x06,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    4: {1:-0x02,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    5: {1:0x12,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    6: {1:0x16,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    7: {1:0x0a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    8: {1:0x0e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    9: {1:0x22,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    10: {1:0x26,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    11: {1:0x1a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    12: {1:0x1e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    13: {1:0x32,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    14: {1:0x36,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    15: {1:0x2a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00}
                },
                "5": {
                    1: {1:0x02,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    2: {1:0x06,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    3: {1:-0x06,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    4: {1:-0x02,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    5: {1:0x12,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    6: {1:0x16,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    7: {1:0x0a,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    8: {1:0x0e,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    9: {1:0x22,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    10: {1:0x26,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    11: {1:0x1a,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    12: {1:0x1e,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    13: {1:0x32,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    14: {1:0x36,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    15: {1:0x2a,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00}
                }
            }
        }, 2: {
            "00:18:0a": {
                "2.4": {
                    1: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x00},
                    2: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x01},
                    3: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x02},
                    4: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x03},
                    5: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x04},
                    6: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x05},
                    7: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x06},
                    8: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x07},
                    9: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x08},
                    10: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x09},
                    11: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x0A},
                    12: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x0B},
                    13: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x0C},
                    14: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x0D},
                    15: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x0E} 
                },
                "5": {
                    1: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x00},
                    2: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x01},
                    3: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x02},
                    4: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x03},
                    5: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x04},
                    6: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x05},
                    7: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x06},
                    8: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x07},
                    9: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x08},
                    10: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x09},
                    11: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x0A},
                    12: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x0B},
                    13: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x0C},
                    14: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x0D},
                    15: {1:0x02,2:0x00,3:0x50,4:0x00,5:0x00,6:0x0E} 
                }
            },
            "88:15:14": {
                "2.4": {
                    1: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x00},
                    2: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x01},
                    3: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x02},
                    4: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x03},
                    5: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x04},
                    6: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x05},
                    7: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x06},
                    8: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x07},
                    9: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x08},
                    10: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x09},
                    11: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x0A},
                    12: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x0B},
                    13: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x0C},
                    14: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x0D},
                    15: {1:0x02,2:0x00,3:-0x40,4:0x00,5:0x00,6:0x0E}
                },
                "5": {
                    1: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x00},
                    2: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x01},
                    3: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x02},
                    4: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x03},
                    5: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x04},
                    6: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x05},
                    7: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x06},
                    8: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x07},
                    9: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x08},
                    10: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x09},
                    11: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x0A},
                    12: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x0B},
                    13: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x0C},
                    14: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x0D},
                    15: {1:0x02,2:0x00,3:-0x30,4:0x00,5:0x00,6:0x0E}
                }
            },
            "e0:55:3d": {
                "2.4": {
                    1: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x00},
                    2: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x01},
                    3: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x02},
                    4: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x03},
                    5: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x04},
                    6: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x05},
                    7: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x06},
                    8: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x07},
                    9: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x08},
                    10: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x09},
                    11: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x0A},
                    12: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x0B},
                    13: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x0C},
                    14: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x0D},
                    15: {1:0x02,2:0x00,3:0x40,4:0x00,5:0x00,6:0x0E}
                },
                "5": {
                    1: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x00},
                    2: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x01},
                    3: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x02},
                    4: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x03},
                    5: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x04},
                    6: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x05},
                    7: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x06},
                    8: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x07},
                    9: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x08},
                    10: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x09},
                    11: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x0A},
                    12: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x0B},
                    13: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x0C},
                    14: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x0D},
                    15: {1:0x02,2:0x00,3:0x30,4:0x00,5:0x00,6:0x0E}
                }
            }
        }, 3: {
            "88:15:44": {
                "2.4": {
                    1: {1:0x00,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    2: {1:0x06,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    3: {1:-0x06,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    4: {1:-0x02,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    5: {1:0x12,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    6: {1:0x16,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    7: {1:0x0a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    8: {1:0x0e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    9: {1:0x22,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    10: {1:0x26,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    11: {1:0x1a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    12: {1:0x1e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    13: {1:0x32,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    14: {1:0x36,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    15: {1:0x2a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00}
                },
                "5": {
                    1: {1:0x02,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    2: {1:0x06,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    3: {1:-0x06,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    4: {1:-0x02,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    5: {1:0x12,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    6: {1:0x16,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    7: {1:0x0a,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    8: {1:0x0e,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    9: {1:0x22,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    10: {1:0x26,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    11: {1:0x1a,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    12: {1:0x1e,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    13: {1:0x32,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    14: {1:0x36,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00},
                    15: {1:0x2a,2:0x00,3:0x10,4:0x00,5:0x00,6:0x00}
                }
            },
            "e0:55:3d": {
                "2.4": {
                    1: {1:0x00,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    2: {1:0x06,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    3: {1:0x0a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    4: {1:0x0e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    5: {1:0x12,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    6: {1:0x16,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    7: {1:0x1a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    8: {1:0x1e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    9: {1:-0x1e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    10: {1:-0x1a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    11: {1:-0x16,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    12: {1:-0x12,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    13: {1:-0x0e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    14: {1:-0x0a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    15: {1:-0x06,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00}
                },
                "5": {
                    1: {1:0x02,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    2: {1:0x06,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    3: {1:0x0a,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    4: {1:0x0e,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    5: {1:0x12,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    6: {1:0x16,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    7: {1:0x1a,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    8: {1:0x1e,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    9: {1:-0x1e,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    10: {1:-0x1a,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    11: {1:-0x16,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    12: {1:-0x12,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    13: {1:-0x0e,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    14: {1:-0x0a,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    15: {1:-0x06,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00}
                }
            },
            "0c:8d:db": {
                "2.4": {
                    1: {1:0x00,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    2: {1:-0x02,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    3: {1:-0x06,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    4: {1:-0x0a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    5: {1:0x12,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    6: {1:0x0e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    7: {1:0x0a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    8: {1:0x06,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    9: {1:0x22,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    10: {1:0x1e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    11: {1:0x1a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    12: {1:0x16,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    13: {1:0x32,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    14: {1:0x2e,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00},
                    15: {1:0x2a,2:0x00,3:0x00,4:0x00,5:0x00,6:0x00}
                },
                "5": {
                    1: {1:0x02,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    2: {1:-0x02,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    3: {1:-0x06,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    4: {1:-0x0a,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    5: {1:0x12,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    6: {1:0x0e,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    7: {1:0x0a,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    8: {1:0x06,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    9: {1:0x22,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    10: {1:0x1e,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    11: {1:0x1a,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    12: {1:0x16,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    13: {1:0x32,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    14: {1:0x2e,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00},
                    15: {1:0x2a,2:0x00,3:-0x10,4:0x00,5:0x00,6:0x00}
                }
            }
        }
    }
    ap_families = {
        "MR12": 1,
        "MR16": 1,
        "MR18": 1,
        "MR24": 1,
        "MR62": 1,
        "MR66": 1,
        "MR32": 2,
        "MR34": 2,
        "MR26": 2,
        "MR72": 2,
        "MR30H": 3,
        "MR33": 3,
        "MR42": 3,
        "MR52": 3,
        "MR53": 3,
        "MR74": 3,
        "MR84": 3
    }
    def ap_offset(ap_model):
        return MerakiBssidCalculator.offset_families[MerakiBssidCalculator.ap_families[ap_model]]
    def calculate(ap_model,ap_mac,ssid_number):
        bssids = { 
            "2.4": MerakiBssidCalculator.calculate_bssid(
                ap_mac,
                MerakiBssidCalculator.ap_offset(ap_model)[ap_mac[:8]]["2.4"][ssid_number]
            ),
            "5": MerakiBssidCalculator.calculate_bssid(
                    ap_mac,
                    MerakiBssidCalculator.ap_offset(ap_model)[ap_mac[:8]]["5"][ssid_number]
            )
        }
        return bssids
    def calculate_bssid(ap_mac,offsets):
        ap_octets = ap_mac.split(":")
        bssid_octets = []
        for i,octet in enumerate(ap_octets):
            bssid_octets.append(MerakiBssidCalculator.calculate_octet(octet,offsets[i+1]))
        return ":".join(bssid_octets)
    def calculate_octet(octet,offset):
        return hex(int(octet,16) + offset)[2:].zfill(2)



