import torch
from matplotlib import pyplot as plt
import numpy as np

def generate_noise_burst(n_samples: int, noise_duration: int):
    samples = torch.zeros(n_samples)
    noise = torch.hamming_window(noise_duration) * torch.zeros(noise_duration).uniform_(-1, 1)
    samples[:noise_duration] += noise
    return samples

def noise_burst_plot(n_samples: int, noise_duration: int):
    nb = generate_noise_burst(n_samples, noise_duration)
    plt.plot(nb)
    plt.show()

def generate_damped_sinusoid(n_samples: int, frequency: float, exp: float, n_elements: int):
    phase = torch.linspace(-np.pi, np.pi, n_samples)
    frequencies = torch.zeros(n_elements).uniform_(0, 1) * frequency
    decays = torch.zeros(n_elements).uniform_(2, 40)
    osc = torch.cos(phase[None, :] * frequencies[:, None])
    decay = torch.linspace(1, 0, n_samples)[None, :] ** decays[:, None]
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


def plot_damped_sinusoids(n_samples: int, frequency: float, exp: float, n_elements: int):
    x = generate_damped_sinusoid(n_samples, frequency, exp, n_elements)
    fig, ax = plt.subplots(nrows=n_elements, ncols=1)
    for i, s in enumerate(x):
        ax[i].set_axis_off()
        ax[i].plot(s)
    
    plt.tight_layout()
    plt.show()
    

if __name__ == '__main__':
    
    n_samples = 512
    max_freq = 160
    max_decay = 20
    n_deformations = 8
    
    plot_damped_sinusoids(n_samples, max_freq, max_decay, n_deformations)


    noise_burst_plot(n_samples, 128)
        
    # x = generate_noise_burst(512, 32)
    # ax = plt.plot(x)
    # ax.set_axis_off()
    # plt.show()
    
    x = generate_deformation(128, 8)
    ax = plt.matshow(x, cmap='hot')
    plt.show()
    