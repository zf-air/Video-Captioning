from densevid_eval3.evaluate2018 import main as eval2018
from densevid_eval3.evaluate2021 import main as eval2021

def eval_dvc(json_path, reference, no_lang_eval=False, topN=1000, version='2018'):
    args = type('args', (object,), {})()
    args.submission = json_path
    args.max_proposals_per_video = topN
    args.tious = [0.3,0.5,0.7,0.9]
#    args.verbose = False     #原先的设置
    args.verbose = True    #验证时设为True
    args.no_lang_eval = no_lang_eval
    args.references = reference
    eval_func = eval2018 if version=='2018' else eval2021
    score = eval_func(args)
    return score

if __name__ == '__main__':
    p = '../save/workoutuow18_tsp_pdvc/2022-02-21-20-07-21_workoutuow18_tsp_pdvc_epoch16_num324_alpha1.0.json_rerank_alpha1.0_temp2.0.json'
    ref = ['../data/workoutuow18/captiondata/test.json']
    score = eval_dvc(p, ref, no_lang_eval=False, version='2018')
    print(score)