import json


if __name__ == '__main__':
    PATH = '../appReq/status_filters.json'
else:
    PATH = './appReq/status_filters.json'


def filter_options(filepath = PATH):
    with open(filepath,'r') as json_file:
        content = json_file.read()
    data= json.loads(content)
    data_values = list(data.values())[0]
    return data_values




if __name__ == '__main__':
    print(filter_options())

