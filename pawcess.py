import json
import sys

fp = sys.argv[1]

with open(fp, 'r') as file:
    for line in file:
        jsonobj = json.loads(line)
        print(jsonobj)
        if jsonobj['data']['kind'] == "super-secure-person-with-significant-control" or jsonobj['data']['kind'] == "super-secure-beneficial-owner":
            continue

        if jsonobj['data']['kind'] == "legal-person-beneficial-owner":
            continue

        # print(jsonobj['data'])
        # if jsonobj['company_number'] == "07691187" or jsonobj['company_number'] == "11179285":
        #     continue
            
            
        print(jsonobj['company_number'])
        print(jsonobj['data']['address'])
        print(jsonobj['data']['etag'])
        print(jsonobj['data']['kind'])
        print(jsonobj['data']['name'])

        try:
            print(jsonobj['data']['natures_of_control'])
        except:
            pass

        print(jsonobj['data']['notified_on'])
        print(jsonobj['data']['links'])
        try:
            print(jsonobj['data']['is_sanctioned'])
        except:
            pass
        

        if jsonobj['data']['kind'] == "corporate-entity-person-with-significant-control" or \
            jsonobj['data']['kind'] == "legal-person-person-with-significant-control" or \
            jsonobj['data']['kind'] == "corporate-entity-beneficial-owner":
            print(jsonobj['data']['identification'])
            
        elif jsonobj['data']['kind'] == "individual-beneficial-owner" or jsonobj['data']['kind'] == "individual-person-with-significant-control":
            print(jsonobj['data']['name_elements'])
            try:
                print(jsonobj['data']['country_of_residence'])
            except:
                pass

            try:
                print(jsonobj['data']['date_of_birth'])
            except:
                pass

            try:
                print(jsonobj['data']['nationality'])
            except:
                pass
