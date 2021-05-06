import json


def statistic(filepath="datasets/FC-TF/train_data.json", res=None):
    with open(filepath, "r", encoding="utf8") as fr:
        data = json.load(fr)
        for rel, l in data.items():
            for item in l:
                text = item["sentence"]
                doc = nlp(text)
                for t in doc:
                    if (t.dep_, t.dep) not in res:
                        res.append((t.dep_, t.dep))


if __name__ == '__main__':


    res = []
    statistic(res, filepath="datasets/FC-TF/train_data.json")
    statistic(res, filepath="datasets/FC-TF/val_data.json")
    statistic(res, filepath="datasets/FC-TF/test_data.json")
    with open("d.txt", "w", encoding="utf8") as fw:
        for pair in res:
            line = "{}: {}\n".format(pair[0], pair[1])
            fw.write(line)
    print("done!")