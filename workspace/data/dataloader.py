import sys
import os

from PIL import Image
import torch
from torchvision import transforms
from torch.utils.data import DataLoader

trans2tensor = transforms.ToTensor()

def load(path2img):
    img = Image.open(path2img)
    img_t = trans2tensor(img).unsqueeze(0)
    print('img_t:', img_t.size())
    return img_t

class DataLoader(DataSet):
    def __init__(self):
        super(DataLoader, self).__init__()
    def __getitem__(self, index):


def main():
    path2img = 'data/test_img.png'
    load(path2img)

main()

