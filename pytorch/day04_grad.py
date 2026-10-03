import torch

X = torch.tensor([
    [1., 2.],
    [3., 4.]
])

W = torch.tensor([1., 2.], requires_grad=True)

y = torch.tensor([4., 10.])

y_pred = X @ W 
loss = torch.sum((y - y_pred)**2)
print(y_pred)
print(loss)

loss.backward()
print(W.grad)