import sys
import os

import json

sys.path.insert(1, os.getcwd())
from datasets.flickr30k import Flickr30kDataset
from models.flickr30k_vilt import Flickr30KVilt
from transformers import ViltProcessor
import torch.nn.functional as F
from visualizations.visualizegradient import *

# get the dataset
data = Flickr30kDataset("valid")
# set target sentence idx
target_idx = 0

# get the model
analysismodel = Flickr30KVilt(target_idx=target_idx)

# unimodal image gradient
"""
for instance_idx in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
    instance = data.getdata(instance_idx)

    # get the model predictions
    preds = analysismodel.forward(instance)

    # compute and print grad saliency with and without multiply orig:
    saliency = get_saliency_map(instance, analysismodel, 0)
    grads = saliency[0]

    t = normalize255(torch.sum(torch.abs(grads), dim=0), fac=255)
    heatmap2d(
        t,
        f"visuals/flickr30k-vilt-{instance_idx}-{target_idx}-saliency.png",
        instance[0],
    )
"""

target_ids_100 =  {0: '[CLS]', 1: 'a', 2: 'large', 3: 'bearded', 4: 'man', 5: 'flip', 6: '##s', 7: 'a', 8: 'cr', 9: '##ep', 10: '##e', 11: 'or', 12: 'om', 13: '##ele', 14: '##t', 15: 'in', 16: 'mid', 17: '##air', 18: 'with', 19: 'his', 20: 'fry', 21: '##ing', 22: 'pan', 23: '.', 24: '[SEP]', 25: '[PAD]', 26: '[PAD]', 27: '[PAD]', 28: '[PAD]', 29: '[PAD]', 30: '[PAD]', 31: '[PAD]', 32: '[PAD]', 33: '[PAD]', 34: '[PAD]', 35: '[PAD]', 36: '[PAD]', 37: '[PAD]', 38: '[PAD]', 39: '[PAD]'}
target_ids_150 = {0: '[CLS]', 1: 'a', 2: 'black', 3: 'dog', 4: 'with', 5: 'white', 6: 'facial', 7: 'and', 8: 'chest', 9: 'markings', 10: 'standing', 11: 'in', 12: 'chest', 13: 'high', 14: 'water', 15: '.', 16: '[SEP]', 17: '[PAD]', 18: '[PAD]', 19: '[PAD]', 20: '[PAD]', 21: '[PAD]', 22: '[PAD]', 23: '[PAD]', 24: '[PAD]', 25: '[PAD]', 26: '[PAD]', 27: '[PAD]', 28: '[PAD]', 29: '[PAD]', 30: '[PAD]', 31: '[PAD]', 32: '[PAD]', 33: '[PAD]', 34: '[PAD]', 35: '[PAD]', 36: '[PAD]', 37: '[PAD]', 38: '[PAD]', 39: '[PAD]'}



instance_text_target_ids_100 = {
    "100_1": {"ids": [2], "text": "large"},
    "100_2": {"ids": [3], "text": "bearded"},
    "100_3": {"ids": [4], "text": "man"},
    "100_4": {"ids": [8,9,10], "text": "crepe"},
    "100_5": {"ids": [12,13,14], "text": "omelet"},
    "100_6": {"ids": [20, 21, 22], "text": "frying pan"},
    "100_7": {"ids": [2, 3, 4], "text": "large bearded man"},
}
instance_text_target_ids_150 = {
    "150_1": {"ids": [2], "text": "black"},
    "150_2": {"ids": [3], "text": "dog"},
    "150_3": {"ids": [5], "text": "white"},
    "150_4": {"ids": [6], "text": "facial"},
    "150_5": {"ids": [8], "text": "chest"},
    "150_6": {"ids": [9], "text": "markings"},
    "150_7": {"ids": [10], "text": "standing"},
    "150_8": {"ids": [11], "text": "in"},
    "150_9": {"ids": [12], "text": "chest"},
    "150_10": {"ids": [13], "text": "high"},
    "150_11": {"ids": [14], "text": "water"},
    "150_12": {"ids": [2, 3], "text": "black dog"},
    "150_13": {"ids":[5, 6], "text": "white facial"},
    "150_14": {"ids": [5, 6, 7, 8, 9], "text": "white facial and chest markings"},
    "150_15": {"ids": [12, 13, 14], "text": "chest high water"}
}



id_to_tids = {
    100: instance_text_target_ids_100,
    150: instance_text_target_ids_150
}

for instance_idx, tid_dict in id_to_tids.items():
    for key, value in tid_dict.items():
        instance = data.getdata(instance_idx)
        # probs, _ = analysismodel.forward(instance)
        processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-flickr30k")
        grads, di, tids = analysismodel.getdoublegrad(
            instance, instance[-1], value["ids"]
        )

        # print(dict(enumerate(processor.tokenizer.convert_ids_to_tokens(tids[0].detach().cpu().numpy()))))
        
        grads = grads[0]
        t = normalize255(torch.sum(torch.abs(grads), dim=0), fac=255)
        heatmap2d(
            t,
            f"visuals/flickr30k-vilt-{key}-doublegrad.png",
            instance[0],
        )
