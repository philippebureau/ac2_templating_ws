# Installation Instructions and Details for GDL Office

## Site Type campus

___

***Last Updated: November 13, 2024 at 11:04 AM***
<br>
Smarthands at GDL Office: Rupert Pupkin
<br>
<br>![Appliance](./images/ORDR_S2000_Sensor.jpg)
<br>
<br>
| ITEM               | Value                     |
|--------------------|---------------------------|
| LOCATION TYPE              |   campus   |
| MODEL              |   S2000   |
| APPLIANCE FQDN        |   gdl-sec-app01.uwaco.net    |
| APPLIANCE IP       |   192.168.1.4 |
| MGMT VLAN          |   31    |
| MGMT Subnet Gateway        |   192.168.1.1    |
| MGMT Subnet Mask        |   255.255.255.248  |
| MGMT Subnet CIDR        |   192.168.1.0/29    |
| MGMT Subnet Gateway Device       |   gdl-core01    |
| MGMT SWITCH         |   gdl-as01   |
| SWITCH INTERFACE       |   GigabitEthernet1/0/21    |
| SPAN VLAN RANGE        |   7XX   |
| SPAN INTERFACE        |   TenGigabitEthernet1/1/17 on gdl-core01   |
| NOTES       |   Plenty of room above the core device in Rack 5    |
| Recommended Install RU       |   31    |
| Smart Hands Name      |   Rupert Pupkin    |
| Smart Hands Email      |   rupert@king-of-comedy.net    |
| Smart Hands Phone      |   payphone 3 located in Times Square 555-555-5555    |
<br>
---



## Installing a S2000

The S2000 is a full width 19" 1RU appliance that comes with mounting ears.
Please attach the mounting ears to install in Rack 5  RU 5


### Notes
Plenty of room above the core device in Rack 5

### Management Connection
Please connect the appliance mgmt interface to switch gdl-as01 using interface GigabitEthernet1/0/21
This interface has already been configured for vlan 31.

### Data Connection (SPAN/RSPAN)
Please connect the appliance mgmt interface to switch gdl-core01 using interface TenGigabitEthernet1/1/17
This interface has already been configured to support the appliance.

### Device Network Configuration
Tip:  It might be easier to configure the IP, Mask, and Gateway prior to taking to the IDF.

For appliance  please use the following network configuration details:
Management subnet: 192.168.1.0/29
Management Vlan:   31
Appliance IP: GigabitEthernet1/0/21
Appliance MASK: 255.255.255.248
Appliance Gateway: gdl-as01
Appliance Primary DNS: 8.8.8.8
Appliance Secondary DNS: 9.9.9.9

### Labeling
The appliance should have been sent with an envelope containing two labels.
Please affix one label to the front of the unit and one to the back.
Labels must be visible from front and back.

### Power
Please connect the single power supply to an empty NEMA 5-15

