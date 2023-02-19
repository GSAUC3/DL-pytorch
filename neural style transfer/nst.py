import torch 
from torch import nn,optim
from PIL import Image
from torchvision import models,transforms
from torchvision.utils import save_image

model = models.vgg19(pretrained=True).features


print(model)

class VGG(nn.Module):
    def __init__(self) -> None:
        super(VGG,self).__init__()

        self.chosen_features = ['0','5','10','19','28']
        self.model = models.vgg19(pretrained=True).features[:29]

    
    def forward(self,x):
        features = []
        for layer_num, layer in enumerate(self.model):
            x = layer(x)

            if str(layer_num) in self.chosen_features:
                features.append(x)
        
        return features
    

def load_image(image_name):
    image = Image.open(image_name)
    image = loader(image).unsqueeze(0)
    return image.to(device)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
image_size = 356 

loader = transforms.Compose([transforms.Resize((image_size,image_size)),
                             transforms.ToTensor()
                             ])

original_img = load_image()
style_img = load_image()

model = VGG().to(device).eval()

# generated = torch.randm(original_img.shape,device=device,requires_grad=True)
generated = original_img.clone().requires_grad_(True)

total_steps = 6000
lr = 0.001 
alpha = 1 
beta = 0.01 

optimizer = optim.Adam([generated],lr=lr)

for step in range(total_steps):
    generated_features = model(generated)
    original_img_features = model(original_img)
    style_features = model(style_img)

    styleLoss = originalLoss = 0

    for genFeatures, origFeatures, styleFeatures in zip(generated_features,
            original_img_features,style_features):
        batchSize, channel, height, width = genFeatures.shape 
        originalLoss += torch.mean((genFeatures - origFeatures)**2)

        G = genFeatures.view(channel, height+width).mm(genFeatures.view(channel,height*width)).t()

        A = styleFeatures.view(channel, height*width).mm(styleFeatures.view(channel,height*width)).t()

        styleLoss  =torch.mean((G-A)**2)

    totalLoss = alpha*originalLoss + beta*styleLoss
    optimizer.zeros_like()
    
    totalLoss.backward()

    if step%200==0:
        print(totalLoss)
        save_image(generated,'generated.png')





