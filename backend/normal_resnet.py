import os
import torch
import torchvision.transforms as transforms
from torchvision.models import resnet18
from PIL import Image

def classify_with_normal_resnet(input_folder, output_folder):
    model = resnet18(pretrained=True)
    model.eval()

    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
    ])

    results = []

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for img_name in os.listdir(input_folder):
        if img_name.endswith(('png', 'jpg', 'jpeg')):
            img_path = os.path.join(input_folder, img_name)
            img = Image.open(img_path)
            img_t = transform(img)
            batch_t = torch.unsqueeze(img_t, 0)

            out = model(batch_t)
            _, index = torch.max(out, 1)
            class_idx = index.item()

            class_folder = os.path.join(output_folder, str(class_idx))
            if not os.path.exists(class_folder):
                os.makedirs(class_folder)

            output_img_path = os.path.join(class_folder, img_name)
            img.save(output_img_path)
            results.append(f"{img_name} classified as {class_idx}")

    return results