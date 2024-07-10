import torch
from torch.utils.data import Dataset

class NerfDataset(Dataset):
    def __init__(self, width, height, rays = torch.tensor([]), colors = torch.tensor([])):
        self.width = width
        self.height = height
        self.rays = rays
        self.colors = colors

    def __len__(self):
        return len(self.rays)
    
    def __getitem__(self, index):
        return self.rays[index], self.colors[index]
    
    def append (self, other): # other: NerfDataset
        assert self.width == other.width and self.height == other.height
        if len(self) <= 0:
            self.rays = other.rays.clone().detach()
            self.colors = other.colors.clone().detach()
        else:
            self.rays = torch.cat((self.rays, other.rays))
            self.colors = torch.cat((self.colors, other.colors))