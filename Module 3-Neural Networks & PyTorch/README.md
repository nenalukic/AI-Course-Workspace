# Module 3: Neural Networks & PyTorch

## Overview
This module explores the mathematics and architecture behind Deep Learning. It transitions from theoretical concepts like Perceptrons and Gradient Descent into practical implementation using **PyTorch**, the industry-leading framework for building AI models.

## Setup Instructions
Ensure your virtual environment (`venv`) is activated, then install PyTorch and its vision library:
```bash
pip install torch torchvision
```

## Key Takeaways
**Tensors vs Arrays**: PyTorch Tensors act like NumPy arrays but have the crucial ability to track their own gradients and run on GPUs.

**The Training Loop**: Every deep learning training step involves 4 phases: 1) Forward Pass (Predict), 2) Calculate Loss (Error), 3) Backward Pass (Calculate Gradients), 4) Optimizer Step (Update Weights).