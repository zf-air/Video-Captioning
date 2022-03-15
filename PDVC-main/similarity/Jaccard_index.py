from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import json

def jaccard_similarity(s1, s2):
    def add_space(s):
        return ' '.join(s)

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # print(cv.get_feature_names())
    # print(vectors)
    # 求交集
    numerator = np.sum(np.min(vectors, axis=0))
    # print(np.min(vectors, axis=0))
    # 求并集
    denominator = np.sum(np.max(vectors, axis=0))
    # print(np.max(vectors, axis=0))
    # 计算杰卡德系数
    return 1.0 * numerator / denominator

def acc():
    real_path = 'real_caption.json'
    test_path = 'test_16_caption.json'
    with open(real_path, 'r') as f:
        real = json.load(f)
    with open(test_path, 'r') as f1:
        test = json.load(f1)

    real_keys = list(real.keys())
    test_keys = list(test.keys())
    all_number = 0
    acc_number = 0
    wrong_list = []
    for i in test_keys:
        score_max = 0
        max_name = ''
        test_caption = test[i]['caption']
        for j in real_keys:
            real_caption = real[j]['caption']
            score = jaccard_similarity(test_caption, real_caption)
            if score_max < score:
                score_max = score
                max_name = j
        a1, a2, a3, a4 = i.split("_", 3)
        if a2 == max_name:
            acc_number = acc_number + 1
        else:
            wrong_list.append(i)
        all_number = all_number + 1
    print(acc_number)
    print(all_number)
    f_w = open('test_16_wrong_list.txt', 'w')
    f_w.writelines(wrong_list)
    f_w.close()
    return acc_number / all_number
if __name__ == "__main__":
    acc = acc()
    print(acc)



