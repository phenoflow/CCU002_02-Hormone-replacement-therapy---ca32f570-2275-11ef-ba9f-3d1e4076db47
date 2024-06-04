# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"0604011D0AAALAL","system":"bnf"},{"code":"0604011G0AABLBL","system":"bnf"},{"code":"0604011G0BUACBA","system":"bnf"},{"code":"0604011G0BUADBH","system":"bnf"},{"code":"0604011G0BUAABR","system":"bnf"},{"code":"0604011D0AAAAAA","system":"bnf"},{"code":"0604011D0AAAWAW","system":"bnf"},{"code":"0604011G0AABEBE","system":"bnf"},{"code":"0604011G0AABHBH","system":"bnf"},{"code":"0604011G0BUAEBL","system":"bnf"},{"code":"0604011G0AABABA","system":"bnf"},{"code":"0604011G0AABRBR","system":"bnf"},{"code":"0604011G0AABGBG","system":"bnf"},{"code":"0604011D0AAACAC","system":"bnf"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-hormone-replacement-therapy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-hormone-replacement-therapy-hrt-75microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-hormone-replacement-therapy-hrt-75microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-hormone-replacement-therapy-hrt-75microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
