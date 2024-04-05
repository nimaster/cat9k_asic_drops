# cat9k_asic_drops

This script uses netmiko to ssh to a catalyst 9k switch and return the forwarding asic drop counters.
The data is parsed and reformatted into python dictionary/json format. 
The script also highlights non-zero drop counters

To run the script use the following format:
python3 cat9k_asicdrops.py <switch ip address> <username> <password>

for example:
python3 cat9k.asic_drops.py 10.1.1.1 cisco cisco

Sample output below:

[
  {
    "asic": 0,
    "core": 0,
    "drop_name": "NO_EXCEPTION",
    "drop_counter": 3543734
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "IPV4_CHECKSUM_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "ROUTED_AND_IP_OPTIONS_EXCEPTION",
    "drop_counter": 8
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "CTS_FILTERED_EXCEPTION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "SIA_TTL_ZERO",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "ALLOW_NATIVE_EXCEPTION_COUNT",
    "drop_counter": 1
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "ALLOW_DOT1Q_EXCEPTION_COUNT",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "ALLOW_PRIORITY_TAGGED_EXCEPTION_COUNT",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "ALLOW_UNKNOWN_ETHER_TYPE_EXCEPTION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "IP_SOURCE_GUARD_VIOLATION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "SECURE_L3IF_LEARNING_VIOLATION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "AUTH_DRIVEN_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "VLAN_LOADBALANCE_GROUP_DENY",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "RPF_UNICAST_FAIL",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "RPF_UNICAST_FAIL_SUPPRESS",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "RPF_UNICAST_CHECK_INCOMPLETE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "RPF_MULTICAST_FAIL",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "PKT_DROP_COUNT",
    "drop_counter": 10653
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "SOURCE_ROUTE_EXCEPTION",
    "drop_counter": 21
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "IGR_MISC_FATAL_ERROR",
    "drop_counter": 9053
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "BLOCK_FORWARD",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "POLICER_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "DENY_ROUTE",
    "drop_counter": 1961473
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "DENY_BRIDGE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "STATIC_MAC_VIOLATION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "STATIC_IP_VIOLATION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "FPM_DROP_PACKET",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "IGR_EXCEPTION_L4_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "IGR_EXCEPTION_L5_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "IGR_EXCEPTION_HARDWARE_PARSE_EXCEPTION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "IGR_EXCEPTION_INVALID_VLAN_DROP",
    "drop_counter": 1600
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "IGR_EXCEPTION_31",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "FRAGMENTING_IPV4_WITH_OPTIONS",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "FRAGMENTING_IPV6_WITH_EXTENSIONS",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "ICMP_REDIRECT",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "MTU_FAIL_PUNT_TO_CPU_NO_IP_UNREACHABLE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "LINK_LOCAL_CHECK_FAIL_NO_IP_UNREACHABLE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "IP_UNICAST_TTL_REACHED_ZERO",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "MISC_FATAL_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "STP_OR_FLEXLINK_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "PROTECTED_PORT_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "PVLAN_ISOLATED_CHECK_FAILED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "PVLAN_COMMUNITY_CHECK_FAILED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "DEJA_VU_CHECK_FAILED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "NOT_VLAN_LOAD_BALANCE_GROUP_ALLOWED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "RSPAN_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "SPLIT_HORIZON_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "SYSTEM_TTL_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "PRUNED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "DENY_NO_IP_UNREACHABLE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "IP_MULTICAST_TTL_REACHED_ZERO",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "MTU_FAIL_DROP_BRIDGED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "MTU_FAIL_DROP_BRIDGED_IP_ROUTED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "MTU_FAIL_ERSPAN",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "LINK_LOCAL_CHECK_FAIL_L3M_VALID",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "MTU_FAIL_PUNT_TO_CPU_NOT_NO_IP_UNREACHABLE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "LINK_LOCAL_CHECK_FAIL_NOT_NO_IP_UNREACHABLE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "COPY_TO_CPU",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "EGR_L3_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "EGR_L4_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "EGR_L5_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "EGR_HARDWARE_PARSE_EXCEPTION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "EGR_INVALID_REWRITE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 0,
    "drop_name": "SGT_CACHING_NEEDED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "NO_EXCEPTION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "IPV4_CHECKSUM_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "ROUTED_AND_IP_OPTIONS_EXCEPTION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "CTS_FILTERED_EXCEPTION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "SIA_TTL_ZERO",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "ALLOW_NATIVE_EXCEPTION_COUNT",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "ALLOW_DOT1Q_EXCEPTION_COUNT",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "ALLOW_PRIORITY_TAGGED_EXCEPTION_COUNT",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "ALLOW_UNKNOWN_ETHER_TYPE_EXCEPTION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "IP_SOURCE_GUARD_VIOLATION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "SECURE_L3IF_LEARNING_VIOLATION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "AUTH_DRIVEN_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "VLAN_LOADBALANCE_GROUP_DENY",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "RPF_UNICAST_FAIL",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "RPF_UNICAST_FAIL_SUPPRESS",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "RPF_UNICAST_CHECK_INCOMPLETE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "RPF_MULTICAST_FAIL",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "PKT_DROP_COUNT",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "SOURCE_ROUTE_EXCEPTION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "IGR_MISC_FATAL_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "BLOCK_FORWARD",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "POLICER_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "DENY_ROUTE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "DENY_BRIDGE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "STATIC_MAC_VIOLATION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "STATIC_IP_VIOLATION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "FPM_DROP_PACKET",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "IGR_EXCEPTION_L4_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "IGR_EXCEPTION_L5_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "IGR_EXCEPTION_HARDWARE_PARSE_EXCEPTION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "IGR_EXCEPTION_INVALID_VLAN_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "IGR_EXCEPTION_31",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "FRAGMENTING_IPV4_WITH_OPTIONS",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "FRAGMENTING_IPV6_WITH_EXTENSIONS",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "ICMP_REDIRECT",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "MTU_FAIL_PUNT_TO_CPU_NO_IP_UNREACHABLE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "LINK_LOCAL_CHECK_FAIL_NO_IP_UNREACHABLE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "IP_UNICAST_TTL_REACHED_ZERO",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "MISC_FATAL_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "STP_OR_FLEXLINK_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "PROTECTED_PORT_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "PVLAN_ISOLATED_CHECK_FAILED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "PVLAN_COMMUNITY_CHECK_FAILED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "DEJA_VU_CHECK_FAILED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "NOT_VLAN_LOAD_BALANCE_GROUP_ALLOWED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "RSPAN_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "SPLIT_HORIZON_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "SYSTEM_TTL_DROP",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "PRUNED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "DENY_NO_IP_UNREACHABLE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "IP_MULTICAST_TTL_REACHED_ZERO",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "MTU_FAIL_DROP_BRIDGED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "MTU_FAIL_DROP_BRIDGED_IP_ROUTED",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "MTU_FAIL_ERSPAN",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "LINK_LOCAL_CHECK_FAIL_L3M_VALID",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "MTU_FAIL_PUNT_TO_CPU_NOT_NO_IP_UNREACHABLE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "LINK_LOCAL_CHECK_FAIL_NOT_NO_IP_UNREACHABLE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "COPY_TO_CPU",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "EGR_L3_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "EGR_L4_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "EGR_L5_ERROR",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "EGR_HARDWARE_PARSE_EXCEPTION",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "EGR_INVALID_REWRITE",
    "drop_counter": 0
  },
  {
    "asic": 0,
    "core": 1,
    "drop_name": "SGT_CACHING_NEEDED",
    "drop_counter": 0
  }
]
The following drop counters are non-zero:
ASIC/CORE:   DROP_NAME:                                 COUNTER:
0/0          NO_EXCEPTION                               3543734
0/0          ROUTED_AND_IP_OPTIONS_EXCEPTION            8
0/0          ALLOW_NATIVE_EXCEPTION_COUNT               1
0/0          PKT_DROP_COUNT                             10653
0/0          SOURCE_ROUTE_EXCEPTION                     21
0/0          IGR_MISC_FATAL_ERROR                       9053
0/0          DENY_ROUTE                                 1961473
0/0          IGR_EXCEPTION_INVALID_VLAN_DROP            1600
