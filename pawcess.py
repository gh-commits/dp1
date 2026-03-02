import json
import sys

fp = sys.argv[1]

with open(fp, 'r') as file:
    for line in file:
        jsonobj = json.loads(line)
        print(jsonobj)
        if jsonobj['data']['kind'] == "super-secure-person-with-significant-control":
            continue
        # print(jsonobj['data'])
        print(jsonobj['company_number'])
        print(jsonobj['data']['address'])
        print(jsonobj['data']['etag'])
        print(jsonobj['data']['kind'])
        print(jsonobj['data']['name'])
        print(jsonobj['data']['natures_of_control'])
        print(jsonobj['data']['notified_on'])
        print(jsonobj['data']['links'])

        if jsonobj['data']['kind'] == "corporate-entity-person-with-significant-control" or jsonobj['data']['kind'] == "legal-person-person-with-significant-control":
            print(jsonobj['data']['identification'])
        else:
            print(jsonobj['data']['country_of_residence'])

            try:
                print(jsonobj['data']['date_of_birth'])
            except:
                pass

            print(jsonobj['data']['nationality'])
            print(jsonobj['data']['name_elements'])
