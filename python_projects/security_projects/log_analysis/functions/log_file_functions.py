#Functions for firewall analysis - Written by Eric Lovell

import re

def parse_log_entry(log_entry):
    """Function the parses a log entry and looks for patterns that match src/desc IP's and protocol
    Arguments:
        log_entry {String Value} - String Value that holds information regarding log entry
    Returns: 
        None - If no pattern is found | Source/Destination/Protocol Information"""
    
    #Regex for ip info
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*SRC=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*DST=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*PROTO=(\w+).*'
    match = re.match(pattern, log_entry)
    if match:
        timestamp = match.group(1)
        source_ip = match.group(2)
        destination_ip = match.group(3)
        protocol = match.group(4)

        return {
            'Timestamp': timestamp,
            'Source IP': source_ip,
            'Destination IP': destination_ip,
            'Protocol': protocol
        }
    return None



def parse_firewall_log(file_path):
    """Function the parses contents of a Firewall log and passes in to parse_log_entry().
    Arguments:
        file_path {String Value} - String Value that holds file path information for firewall log
    Returns: 
        log_entries {String Value} - String value that represents all the log entries in the fire wall log file"""
    
    with open(file_path, 'r') as log_file:
        log_data = log_file.readlines()

    log_entries = []

    # Parse each log entry
    for line in log_data:
        log_entry = parse_log_entry(line)
        if log_entry:
            log_entries.append(log_entry)

    return log_entries



def write_parsed_logs_to_file(log_entries, file_path):
    """Function that write the parsed firewall log entries to a text file
    Arguments: 
        log_entries {String Value} -- String values holding log entry information
        file_path {String Value} -- String values that hold file path to the firewall logs
    Returns:
        None -- Directly outputs information to a file"""
    
    with open(file_path, 'w') as output_file:
        for log in log_entries:
            output_file.write(f"Timestamp: {log['Timestamp']}\n")
            output_file.write(f"Source IP: {log['Source IP']}\n")
            output_file.write(f"Destination IP: {log['Destination IP']}\n")
            output_file.write(f"Protocol: {log['Protocol']}\n")
            output_file.write("\n")