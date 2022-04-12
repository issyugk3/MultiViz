"""Implements dataloaders for IMDB dataset to return raw (image, text) data"""

from PIL import Image
import json
import h5py
import os
import numpy as np
import torch
import random
import torchvision.transforms as transforms


class IMDBDataset:
    
    def __init__(self, split, raw_data_path, dataset=None, table_path=None):
        """Initialize IMDBDataset object.

        Args:
            dataset (h5py.File): Raw IMDB data table
            split (str): Type of split
            raw_data_path (str): Path to raw IMDB data dir
            vgg16 : torch model for VGG16
            word2vec: Google word2vec
            table_path: path to IMDB data table
        """
        
        if split == 'train':
            self.start_ind = 0
            self.end_ind = 15552
        elif split == 'val':
            self.start_ind = 15552
            self.end_ind = 18160
        elif split == 'test':
            self.start_ind = 18160
            self.end_ind = 25959
        else:
            raise NotImplementedError

        self.size = self.end_ind - self.start_ind
        if dataset == None:
            assert table_path != None, 'Enter valid path for IMDB data'
            self.dataset = h5py.File(table_path, 'r')
        else:
            self.dataset = dataset

        self.raw_imdb_root_path = raw_data_path

        self.image_preprocess = transforms.Compose([
                                    transforms.Resize(256),
                                    transforms.CenterCrop(224)
                                ])

    def getdata(self, ind):
        imdb_id = self.dataset['imdb_ids'][ind].decode('utf-8')
        data = _process_data(imdb_id, self.raw_imdb_root_path)
        labels = self.dataset['genres'][ind]
        text = data['plot']
        image = np.asarray(self.image_preprocess(data['image']))
        return text, image, labels
        

    def length(self):
        return self.size

    def classnames(self):
        raise NotImplementedError

    def sample(self, num):

        sampled=[]
        nums = list(range(self.length()))
        random.shuffle(nums)
        idx = 0
        while(len(sampled) < num):
            a = self.getdata(nums[idx])
            sampled.append(a)
            idx += 1
        return sampled


def _process_data(filename, root_path):
    '''Process raw IMDB data'''
    data = {}
    filepath = os.path.join(root_path, filename)
    data['imdb_id'] = filename

    # process image
    with Image.open(filepath + ".jpeg") as f:
        raw_img = f.convert("RGB")
        data["image"] = raw_img
        # preprocess = transforms.Compose([
        #     transforms.Resize(256),
        #     transforms.CenterCrop(224),
        #     transforms.ToTensor(),
        #     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        # ])
    # input_tensor = preprocess(f.convert('RGB'))
    # data['image_tensor'] = input_tensor

    # process text
    with open(filepath + ".json", "r") as f:
        info = json.load(f)
        plot = info["plot"]
        plot_id = np.array([len(p) for p in plot]).argmax()
        data["plot"] = plot[plot_id]

    return data