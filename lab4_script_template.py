import sys 
import os 
import re 
import pandas as pd 

def main():
    log_file = get_log_file_path_from_cmd_line()
    records = filter_log_by_regex(log_file, 'sshd', print_summary=True)


def get_log_file_path_from_cmd_line(param_num):
    """_summary_

    Args:
        param_num (int): Paramter number

    Returns:
        str: Full path of the log file
    """
    num_params = len(sys.argv) -1 
    if num_params >= param_num:
        log_file_path = sys.argv[param_num]
        if os.path.isfile(log_file_path):
            return os.path.abspath(log_file_path)
        else:
            print('Error: Log file does not exist.')
            sys.exit(1)
    else:
        print('Error: Missing log file.')
        sys.exit(1)





   

# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex

    Args:
        log_file (str): Path of the log file
        regex (str): Regex filter
        ignore_case (bool, optional): Enable case insensitive regex matching. Defaults to True.
        print_summary (bool, optional): Enable printing summary of results. Defaults to False.
        print_records (bool, optional): Enable printing all records that match the regex. Defaults to False.

    Returns:
        (list, list): List of records that match regex, List of tuples of captured data
    """
    records = []
    captured_data = []
    
    regex_flags = re.IGNORECASE if ignore_case else 0 

    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(regex, line)
            if match:
                records.append(line)
                if match.lastindex:
                    captured_data.append(match.groups())
    
    if print_records is True:
        print(*records, sep='')

    if print_summary is True:
        print(f'The log file contains {len(records)} records that case-insensitive match the regex' {regex})

from log_anatlytics import get_log_file_path_from_cmd_line, filter_log_by_regex

def main():
    log_file = get_log_file_path_from_cmd_line(1)
    #records = filter_log_by_regex(log_file, 'SRC=(.*?) DST=(.*?) LEN=(.*?)', print_summary=True, print_records=True)
    pass

  
                

# TODO: Step 8
def tally_port_traffic(log_file):
    dest_port_logs = filter_log_by_regex(log_file, 'DPT=(.*?)')[1]

    dpt_tally = {}
    for dpt_tuple in dest_port_logs:
        dpt_num = dpt_tuple[0]
        dpt_tally[dpt_num] = dpt_tally.get(dpt_num, 0) + 1 

    return dpt_tally

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):

    regex = r"^(.{6}) (.{8}).*SRC=(.+?) DST=(.+?) .*SPT=(.+?) " + f"DPT=({port_number}) " 
    captured_data = filter_log_by_regex(log_file, regex)[1]

    report_df = pd.DataFrame(captured_data)
    report_header = ('Date', 'Time', 'Source IP Addess', 'Destination IP Address', 'Source Port', 'Destination Port')
    report_df.to_csv(f'destination_por_{port_number}_report.csv', index=False, header=report_header)
    
    
    return



# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()