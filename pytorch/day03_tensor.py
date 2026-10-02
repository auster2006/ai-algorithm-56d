import torch


a = torch.tensor([
    [1,2,3],
    [4,5,6]
    ])

print(a)
print(a.shape)
print(a.dtype)
print(a.device)

c = torch.normal(2,3)
print(c)