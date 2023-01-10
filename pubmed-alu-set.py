attributes_list = [
    'PMID',
	'OWN',
	'STAT',
	'DCOM',
	'LR',
	'IS',
	'VI',
	'IP',
	'DP',
	'TI',
	'PG',
	'LID',
	'AB',
	'FAU',
	'AU',
	'AD',
	'AUID',
	'LA',
	'PT',
	'DEP',
	'TA',
	'JT',
	'JID',
	'RN',
	'SB',
	'MH',
	'PMC',
	'OTO',
	'OT',
	'COIS',
	'EDAT',
	'MHDA',
	'CRDT',
	'PHST',
	'AID',
	'PST',
	'SO',
	'PL',
	'CI',
	'GR',
	'PMCR',
	'CIN',
	'MID',
	'SI',
	'CN',
	'FIR',
	'IR',
	'CON',
	'EIN',
	'TT',
	'OAB',
	'OABL',
	'OID',
	'EFR',
	'RIN',
	'CRI',
	'CRF',
	'ROF',
	'IRAD',
]

def create_base_structure():
    data = {}
    for attribute_name in attributes_list:
        data[attribute_name] = None
    return data

def process_line(selected_line, line_number, input_file, previous_data):
    if len(selected_line) >= 5 and selected_line[4] == "-":
        attribute_name = selected_line[0:4].strip()
        if attribute_name == "PMID":
            current_data = create_base_structure()
            insert_previous = True
        else:
            if previous_data == None:
                print(selected_line)
            current_data = previous_data
            insert_previous = False
        attribute_value = selected_line[5:].strip()
        # print("Attribute Value: " + str(attribute_value))
        current_line = input_file.tell()
        next_line = input_file.readline()
        if len(next_line) < 5 or next_line[4] == "-":
            # print(attribute_name + ": " + attribute_value)
            input_file.seek(current_line)
        else:
            while True:
                attribute_value = attribute_value + " " + next_line[5:].strip()
                current_line = input_file.tell()
                next_line = input_file.readline()
                if not next_line or len(next_line) < 5 or next_line[4] == "-":
                    input_file.seek(current_line)
                    break
            # print(attribute_name + ": " + attribute_value)
        if current_data[attribute_name] == None:
            # print("Setting current_data['" + attribute_name + "'] = " + str(attribute_value))
            current_data[attribute_name] = attribute_value
            # print(current_data)
        else:
            current_data[attribute_name] = current_data[attribute_name] + ";" + attribute_value
        return (current_data, previous_data, insert_previous, line_number)
    else:
        # print("Basic Conditions Violated. Skipping Line " + selected_line)
        return (None, previous_data, True, line_number)

input_file = open('pubmed-Alu-set.txt', 'r')
count = 0
previous_data = None
final_data = []
while True:
    count = count + 1
    line = input_file.readline()

    if not line:
        break

    (current_data, previous_data, insert_previous, count) = process_line(line, count, input_file, previous_data)
    if insert_previous and previous_data != None:
        # if previous_data['PMID'] == None:
            # print("\n\nInserting " + str(previous_data))
        final_data.append(previous_data)

    previous_data = current_data
    # print(previous_data)
    # break

print(",".join(attributes_list))
for data_entry in final_data:
    attribute_count = 1
    data_entry_string = ""
    for attribute_name in attributes_list:
        attribute_value = data_entry[attribute_name]
        if attribute_value == None:
            attribute_value = ""
        if attribute_count > 1:
            data_entry_string = data_entry_string + ",\"" + attribute_value.replace("\"", "\"\"") + "\""
        else:
            data_entry_string = "\"" + attribute_value.replace("\"", "\"\"") + "\""
        attribute_count = attribute_count + 1
    print(data_entry_string)