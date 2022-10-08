import torch 
from torch import nn,optim
from PIL import Image
from torchvision import models,transforms
from torchvision.utils import save_image

model = models.vgg19(pretrained=True).features

print(model)