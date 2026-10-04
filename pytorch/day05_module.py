import torch
import torch.nn as nn

class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1,1)

    def forward(self,x):
        return self.linear(x)

y_pred = model(x)
loss = criterion(y_pred, y)

import torch
import torch.nn as nn

torch.manual_seed(42)

x = torch.rand(100, 1) * 10 - 5
noise = torch.randn(100, 1)
y = 3 * x + 2 + noise

# 1. 定义 LinearRegression(nn.Module)
#    __init__ 里使用 nn.Linear(1, 1)
#    写 forward
class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1,1)

    def forward(self,x):
        return self.linear(x)
# 2. 创建 model
model = LinearRegression()

# 3. 创建 MSELoss 和 SGD
#    lr = 0.01
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr = 0.01)

# 4. 训练 100 个 epoch
#    zero_grad
#    forward
#    loss
#    backward
#    step
for epoch in range(100):
    optimizer.zero_grad()
    y_pred = model(x)
    loss = criterion(y_pred,y)
    loss.backward()
    optimizer.step()

print("w =", model.linear.weight.item())
print("b =", model.linear.bias.item())
print("loss =", loss.item())




import torch
import torch.nn as nn

torch.manual_seed(42)

x = torch.rand(200, 1) * 6 - 3
noise = torch.randn(200, 1) * 0.2
y = x ** 2 + noise

class MLP(nn.Module):
    def __init__(self):
        super().__init__()

        # 在这里定义三个东西：
        self.layer1 = nn.Linear(1,16)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(16,1)

    def forward(self, x):
        # 依次：
        # x 经过 layer1
        x = self.layer1(x)
        # 再经过 relu
        x = self.relu(x)
        # 再经过 layer2
        x = self.layer2(x)
        # 最后 return
        return x

model = MLP()

criterion = nn.MSELoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

for epoch in range(500):
    optimizer.zero_grad()
    y_pred = model(x)
    loss = criterion(y_pred,y)
    loss.backward()
    optimizer.step()
    if epoch % 50 == 0:
        print(epoch, loss.item())