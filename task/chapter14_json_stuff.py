import json, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

#parse json str to python dic
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
jsonDataAsPythonVal = json.loads(stringOfJsonData)
print(jsonDataAsPythonVal['name'])
#parse python dic to json str
#str = json.dumps(jsonDataAsPythonVal)
