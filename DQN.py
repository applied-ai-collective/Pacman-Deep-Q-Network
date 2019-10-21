import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

# architecture used for layout smallGrid
""" Deep Q Network """
class DQN(nn.Module):
    def __init__(self, num_inputs=6, num_actions=4):
        super(DQN, self).__init__()

        self.conv1 = nn.Conv2d(num_inputs, 32, kernel_size=3, stride=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=2, stride=1)
        self.fc3 = nn.Linear(1024, 512)
        self.fc4 = nn.Linear(512, num_actions)
        
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.fc3(x.view(x.size(0), -1)))
        return self.fc4(x)


# architecture used for layout mediumClassic
#class DQN(nn.Module):
    #def __init__(self, num_inputs=6, num_actions=4):
        #super(DQN, self).__init__()
        
        #self.conv1 = nn.Conv2d(num_inputs, 32, kernel_size=3, stride=1)
        #self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1)
        #self.fc3 = nn.Linear(7 * 16 * 64, 512)
        #self.fc4 = nn.Linear(512, num_actions)
        
    #def forward(self, x):
        #x = F.relu(self.conv1(x))
        #x = F.relu(self.conv2(x))
        #x = F.relu(self.fc3(x.view(x.size(0), -1)))
        #return self.fc4(x)
