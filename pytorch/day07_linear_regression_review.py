import torch
import torch.nn as nn

x = torch.rand(100,1)*10-5
noise = torch.randn(100,1)
class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1,1)

    def forward(self,x):
        return self.linear(x)

model = LinearRegression()

y = 3 * x + 2 + noise

criterion = nn.MSELoss()

optimizer = torch.optim.SGD(model.parameters(),lr = 0.01)

for epoch in range(1000):
    optimizer.zero_grad()
    y_pred = model(x)
    loss = criterion(y_pred,y)
    loss.backward()
    optimizer.step()


loss = criterion(y_pred,y)


print(model.linear.weight.item())
print(model.linear.bias.item())
print(loss.item())