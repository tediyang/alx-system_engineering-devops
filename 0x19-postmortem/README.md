# IMADECORP LOAD BALANCER OUTAGE INCIDENT REPORT

<img src=./meme.jpg width=50%>

## Issue Summary
Request to imadecorp.tech resulted in 500 error response messages from 10:03 AM to 10:17 AM WAT. This also resulted in error messages coming from APIs that needed it services. The acme of this resulted to 100% downtime and traffic requests not served. The root cause of this outage was a configuration involving the installation of the software that prevented the access to a port.

## Timeline (West African Time)

-	10:02 AM: Configuration push was made.
-	10:03 AM: Outage begins.
-	10:03 AM: Pagers alerted teams.
-	10:03 AM – 10:10 AM: The network engineering team worked on the server.
-	10:10 AM - 10:14 AM: Successfully installed the software program and stop it service on the load balancer server.
-	10:15 AM: Server restarts begin.
-	10:17 AM: 100% of traffic back online.

## Root Cause and Resolution

A new configuration was made at 10:02 AM WAT, which was released to the wrong production environment. The change installed a software program which was forced to listen to the port the load balancer was specified to. This led to a situation where the load balance service couldn’t start because it was also configured to redirect requests from port 80 to web servers. This situation made the load balancing service to be unavailable thereby responding a 500 error to users.
At 10:03 AM WAT, the monitoring systems alerted our engineers who investigated and quickly escalated the issue. They observed that a newly installed program from the configuration uploaded to the wrong server was preventing the load balancing software from directing the users’ requests.

At 10:10 – 10:14 AM WAT, we attempted to uninstall the problematic software program which was successful. At 10:15 AM WAT, the server was restarted and at 10:17AM WAT 100% traffic was back online.


## Corrective and Preventative Measures

-	Increase precision.
-	Improve process for auditing all high-risk configuration options.
