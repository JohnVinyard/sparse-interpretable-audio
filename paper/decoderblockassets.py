import torch
from matplotlib import pyplot as plt
import numpy as np

def generate_noise_burst(n_samples: int, noise_duration: int):
    samples = torch.zeros(n_samples)
    noise = torch.hamming_window(noise_duration) * torch.zeros(noise_duration).uniform_(-1, 1)
    samples[:noise_duration] += noise
    return samples

def generate_damped_sinusoid(n_samples: int, frequency: float, exp: float):
    phase = torch.linspace(-np.pi, np.pi, n_samples)
    osc = torch.cos(phase * frequency)
    decay = torch.linspace(1, 0, n_samples) ** exp
    x = osc * decay
    return x
    

def generate_deformation(n_samples: int, n_channels: int):
    samples = torch.zeros(n_channels, n_samples).uniform_(-1, 1)
    sparse = torch.zeros_like(samples).bernoulli_(p=0.01)
    sparse = torch.cumsum(sparse, dim=-1)
    deformations = torch.softmax(sparse, dim=0)
    return deformations
    

def generate_mix():
    samples = torch.zeros(2).uniform_(-1, 1)
    samples = torch.softmax(samples, dim=-1)
    return samples[None, :]


if __name__ == '__main__':
    x = generate_damped_sinusoid(8192, 20, 10)
    plt.plot(x)
    plt.show()
    
    x = generate_noise_burst(2048, 512)
    plt.plot(x)
    plt.show()
    
    x = generate_deformation(128, 8)
    plt.matshow(x, cmap='gray')
    plt.show()
    
    x = generate_mix()
    plt.matshow(x, cmap='gray')
    plt.show()