import json

def group_json():
    Dict = {}  # 定义一个字典
    str_file = 'test_16.json'
    with open(str_file, 'r') as f:
        r = json.load(f)

    keys = list(r['results'].keys())
#    keys = list(r.keys())
    for j in keys:
        s = ''
        for i in r['results'][j]:
            s = s + i['sentence'].capitalize()
        Dict[j] = {
            'caption': s
        }

 #   for j in keys:
 #       s = ''
 #       for i in r[j]['sentences']:
#            s = s + i
 #       m, n, p, q = j.split('_', 3)
 #       Dict[n] = {
  #          'caption': s
  #      }

    jsObj = json.dumps(Dict, ensure_ascii=False)

    fileObject = open('test_16_caption.json', 'w')
    fileObject.write(jsObj)
    fileObject.close()
    f.close()

if __name__ == "__main__":
    group_json()