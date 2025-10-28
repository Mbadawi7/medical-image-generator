import torch
import numpy as np
from PIL import Image

# TODO: adjust import to your actual model module/file
# from Model.resnet_vae import ResVAE

class DummyModel(torch.nn.Module):
    # Temporary fallback if you haven't wired the real model yet
    def __init__(self, latent_dim=128):
        super().__init__()
        self.latent_dim = latent_dim
    def decode(self, z):
        # Returns a [-1,1] grayscale 128x128 tensor as a demo
        return torch.tanh(torch.randn(1, 128, 128))

class ImageGenerator:
    def __init__(self, weight_path="Model/vae_resnet_latest.pt", device="cpu", use_dummy=True):
        self.device = torch.device(device)
        if use_dummy:
            self.model = DummyModel().to(self.device)
        else:
            # model = ResVAE(latent_dim=128).to(self.device)
            # model.load_state_dict(torch.load(weight_path, map_location=self.device))
            # self.model = model
            raise NotImplementedError("Wire your actual model & weights, or use_dummy=True.")
        self.model.eval()

    def generate_image(self, seed=None, size=(128, 128)):
        if seed is not None:
            torch.manual_seed(seed)
            np.random.seed(seed)
        with torch.no_grad():
            z = torch.randn(1, 128).to(self.device)
            img = self.model.decode(z).cpu().squeeze().numpy()  # [-1,1], shape [H,W]
            img = ((img + 1) / 2 * 255).astype(np.uint8)        # [0,255]
            pil_img = Image.fromarray(img).resize(size)
            return np.array(pil_img)
