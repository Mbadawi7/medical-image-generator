# medical-image-generator
---

## 🧠 Dataset

This project uses the following dataset:

**[Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia?resource=download)**  
Created by **Paul Timothy Mooney** on Kaggle.

- **Total images:** 5,863  , only 1200 used for training and validation 
- **Categories:**  
  - Normal  
  - Pneumonia (Bacterial & Viral)
- **License:** Other (specified in dataset description)
- **Source Paper:** [Cell publication](http://www.cell.com/cell/fulltext/S0092-8674(18)30154-5)

The dataset is used for :
- **Synthetic image generation**
This project uses a deep Variational Autoencoder (VAE) to learn the underlying patterns of chest X-ray images and generate new, realistic samples.
The VAE architecture consists of an encoder, which compresses an input X-ray into a lower-dimensional latent space, and a decoder, which reconstructs an image from a point in that latent space.

During training, the model learns to balance image reconstruction quality and latent distribution regularization, enabling it to:
	•	Reconstruct chest X-rays from the dataset with high fidelity.
	•	Sample new synthetic X-rays that resemble real patient images but do not correspond to any actual person.
---

## ⚙️ Docker Environment

Everything runs inside Docker for full reproducibility.

### 🔧 Build the Image

```bash
docker build -t ai-medical-image-generator .
