import torch


a = torch.tensor([
    [1,2,3],
    [4,5,6]
    ])

print(a)
print(a.shape)
print(a.dtype)
print(a.device)

c = torch.randn(2,3)
print(c)

a = torch.tensor([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a[2,1])
print(a[1,:])
print(a[:,2])
print(a[0:2,0:2])

x = torch.from_numpy(a)

a = x.numpy()

x = x.to("cuda")

x = torch.randn(3,3)

print(x.device)

x = x.to("cuda")

print(x.device)

x = torch.tensor(2.0,requires_grad=True)

y = 3*x**2 + 2*x + 1

y.backward()

print(x.grad)





import torch 

true_w = 3
true_b = 2
lr = 0.01

x = torch.rand(100)*10-5
noise = torch.randn(100)
y = true_w*x + true_b + noise


w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)


for epoch in range(100):
    y_pred = w*x + b
    loss = torch.mean((y - y_pred) ** 2)
    loss.backward()
    with torch.no_grad():
        w -= lr*w.grad
        b -= lr*b.grad

    w.grad.zero_()
    b.grad.zero_()

with torch.no_grad():
    y_pred = w * x + b
    loss = torch.mean((y - y_pred) ** 2)

print(loss)
print(y_pred[:5])
print("new w =", w)
print("new b =", b)