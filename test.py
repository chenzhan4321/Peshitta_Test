import numpy as np
import torch
import torch.nn.functional as F

res = []
X = np.array([[4, 5, 6], [7, 8, 9]])
res=F.softmax(torch.tensor(X, dtype=torch.float), dim=-1).numpy()

print(res)