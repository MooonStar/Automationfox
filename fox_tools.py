import inspect
import json


def add_new_testcase(json_value, json_url=''):
    """ Add a new item to json"""
    json_dict = {"id": json_value, "url": json_url}

    with open('config/testcase_ids') as outfile:
        data = json.load(outfile)

        if dupliacte_entry(data, json_dict['id']):
            print "Cannot set duplicated name."
            return False

        data['list'].append(json_dict)

    with open('config/testcase_ids', 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    return True


def update_entry(old, new):
    """ Item properties has changed. Update json."""

    with open('config/testcase_ids') as outfile:
        data = json.load(outfile)

        for i in data['list']:
            # if item exists in the list
            if i['id'] == old:
                i['id'] = new

    with open('config/testcase_ids', 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4, ensure_ascii=False)


def dupliacte_entry(data, key):
    """ Check if given key is a duplicate in json"""
    for i in data['list']:
        if i['id'] == key:
            return True
    return False


def get_item_url():
    temp = []

    with open('config/testcase_ids') as outfile:
        data = json.load(outfile)

        for i in data['list']:
            temp.append(i['url'])

    return temp


def load_json():
    """ Load json file """
    temp = []

    with open('config/testcase_ids') as outfile:
        data = json.load(outfile)

        for i in data['list']:
            temp.append(i['id'])

    return temp


# ----------------------------------------------------------------------

def delete_entry(entry2delete):
    """ Delete entry from json"""
    with open('config/testcase_ids') as outfile:
        data = json.load(outfile)

        x = 0

        for i in data['list']:

            # if item exists in the list
            if i['id'] == entry2delete:
                del data['list'][x]
                return True
            x = x + 1

    return False


def count_tests(module_name):
    """dynamic import module to count amount of tests in that module"""

    mod = __import__(module_name, fromlist=['Test'])
    klass = getattr(mod, 'Test')
    return inspect.getmembers(klass, predicate=inspect.ismethod)
