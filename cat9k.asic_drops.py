from netmiko import ConnectHandler
import json
import sys

def get_cli(ip_addr, user, pwd):
    switch = ConnectHandler(ip=f'{ip_addr}', username=f'{user}', password=f'{pwd}', device_type='cisco_ios')
    result = switch.send_command('show platform hardware fed switch active fwd-asic drops exceptions | exclude ==|ASIC|current')
    result = format_data(result)
    return result

def format_data(result):
    new_list = []
    result_list = result.split('\n')
    result_list = result_list[1:-1]
    for i in result_list:
        if len(i) > 0:
            temp_list = i.split()
            temp_dict = {'asic' : int(temp_list[0]), 'core' : int(temp_list[1]), 'drop_name' : f'{temp_list[2]}', 'drop_counter' : int(temp_list[4])}
            new_list.append(temp_dict)
    return new_list

def highlight_drops(drops):
    print('The following drop counters are non-zero:')
    print('ASIC/CORE:   DROP_NAME:                                 COUNTER:')
    for drop in drops:
        if drop['drop_counter'] != 0:
            print(f"{drop['asic']}/{drop['core']:<10} {drop['drop_name']:<42} {drop['drop_counter']}")

drops = get_cli(sys.argv[1], sys.argv[2], sys.argv[3])

highlight_drops(drops)

print('\nComplete Drop Counter Data:')
print(json.dumps(drops, indent=2))
