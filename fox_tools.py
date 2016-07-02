import json
from testcase_1 import Test
import inspect
from pydoc import locate


def add_new_testcase(json_value):
    json_dict = {"id": json_value}

    with open('config/testcase_ids') as outfile:
        data = json.load(outfile)
        data['list'].append(json_dict)

    with open('config/testcase_ids', 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4, ensure_ascii=False)


def get_item_url():
    temp = []

    with open('config/testcase_ids') as outfile:
        data = json.load(outfile)

        for i in data['list']:
            temp.append(i['url'])

    return temp


def load_json():
    temp = []

    with open('config/testcase_ids') as outfile:
        data = json.load(outfile)

        for i in data['list']:
            temp.append(i['id'])

    return temp


def update_entry(self, win, old):
    temp = []
    print("OLD = " + old)
    with open('config/testcase_ids') as outfile:
        data = json.load(outfile)

        for i in data['list']:
            if i['id'] == old:
                # data.remove(i['id'])
                i['id'] = self.new_test_var.get()
                # del data['list'][i['id']]
    print(data['list'])

    with open('config/testcase_ids', 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    #win.destroy()


# ----------------------------------------------------------------------

def delete_entry(self, win):
    temp = []

    with open('config/testcase_ids') as outfile:
        data = json.load(outfile)

        for i in range(len(data['list'])):
            if data['list'][i]['id'] == "\"id\":" + "\"" + self.new_test_var.get() + "\"":
                # data.remove(i['id'])
                del data['list']
                # del data['list'][i['id']]
    print(data['list'])

    with open('config/testcase_ids', 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    # self.testcases.append(self.new_test_var.get())
    # self.w['values'] = self.testcases

    win.destroy()


def count_tests(module_name):

    """dynamic import module to count amount of tests in that module"""

    mod = __import__(module_name, fromlist=['Test'])
    klass = getattr(mod,'Test')
    return inspect.getmembers(klass,predicate=inspect.ismethod)


