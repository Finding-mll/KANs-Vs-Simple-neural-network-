import torch
import torch.nn as nn
import torch.nn.functional as F

class SplineActivation(nn.Module):
    def __init__(self, num_splines=10, init_range=0.5):
        super(SplineActivation, self).__init__()
        self.num_splines = num_splines
        self.weights = nn.Parameter(torch.randn(num_splines) * init_range)
        self.knots = nn.Parameter(torch.linspace(-1, 1, num_splines))
    
    def forward(self, x):
        # Apply spline functions to the input
        indices = torch.bucketize(x, self.knots)
        left_knots = torch.index_select(self.knots, 0, indices - 1)
        right_knots = torch.index_select(self.knots, 0, indices)
        left_weights = torch.index_select(self.weights, 0, indices - 1)
        right_weights = torch.index_select(self.weights, 0, indices)
        left_values = left_weights * (x - left_knots)
        right_values = right_weights * (right_knots - x)
        return left_values + right_values

class kAN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(kAN, self).__init__()
        self.hidden = nn.Linear(input_size, hidden_size)
        self.output = nn.Linear(hidden_size, output_size)
        self.spline_activation = SplineActivation()
    
    def forward(self, x):
        x = self.hidden(x)
        x = self.spline_activation(x)
        x = F.relu(x)  # You can add another activation here if needed
        x = self.output(x)
        return x

# Example usage
if __name__ == "__main__":
    model = kAN(input_size=2, hidden_size=10, output_size=2)
    example_input = torch.tensor([0.5, -0.5])
    output = model(example_input)
    print(output)
  
