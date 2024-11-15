# Verification Mini Project
## STP Verification Report App

This mini project is an example of how to use observability tools for verification.

We will use SuzieQ to verify spanning tree for selected vlans.

In addition, we will show how simple it is to create a very user friendly Web App that can be run locally to mitigate issues with data entry.

### Use Case - Vlan and STP Verification

 A common activity in networking is the deployment of vlans (either new across an infrastructure or existing on to additional infrastructure).

Manual configuration and verification is always problematic.  As good as you are,  something often gets missed that results in a user having issues and a call late at night.

I've been automating this activity in some form or fashion for many years.

| Version | Strategy                                                     | Outcome                                                      |      |
| ------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 1       | Automation generates a "configlet" for each switch which needs to be updated.<br />A network engineer copies the configuration on to the switch and executes the custom verification commands. | - verification commands entered but not "read"<br /> - no way to tell if a switch was missed |      |
| 2       | Version 1 + Netmiko script to check spanning tree status for each switch | - Much more thorough verification <br />- Faulty reporting when STP priority not set on switches (solution: added STP priority if net new vlan)<br />- Faulty reporting for nested switches |      |
| 3       | Version 1 <br />+ SuzieQ query to highlight nested switches <br />+ SuzieQ STP verification<br /> | - 99% Reduction in user issues due to LAN Configuration issues<br /> |      |
| 4       | Version 3 <br />+ Script to test for SVI DHCP Lease          | - Exposed DHCP Scope issues<br />- Management interruption if default-gateway not set |      |
| 5       | Version 4<br />+ DHCP Default domain configuration check <br />+ Default Gateway check | 100% reduction in management interruption<br />95% reduction in default DHCP domain issues |      |
| 6       | Version 4<br />+ SuzieQ Default domain configuration check via ASSERT<br />+ SuzieQ STP verification via ASSERT | 80% Reduction in code                                        |      |



## Usage

To run the app locally enter the following command via CLI from the 06_VerificationReport directory

```bash
% streamlit run stp_verification_app.py 
```

CTRL-C to stop

```
(venv-ac2jinja) claudiadeluna in ~/Indigo Wire Networks Dropbox/Claudia de Luna/scripts/python/2024/ac2_templating_workshop/06_VerificationReport on main
% streamlit run stp_verification_app.py 

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.1.10.26:8501
```

This will automatically launch your default browser. 

Note:   Problematic with DuckDuckGo