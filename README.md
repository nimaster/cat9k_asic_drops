# cat9k_asic_drops

This script uses netmiko to ssh to a catalyst 9k switch and return the forwarding asic drop counters.
The data is parsed and reformatted into python dictionary/json format. 
The script also highlights non-zero drop counters

To run the script use the following format:
python3 cat9k_asicdrops.py <switch ip address> <username> <password>

for example:
python3 cat9k.asic_drops.py 10.1.1.1 cisco cisco
