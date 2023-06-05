import requests
import numpy as np

# Sample input data for testing
data = {"instances": np.random.randint(low=1, high=6, size=(10, 25)).tolist()}

# Send a POST request to the TensorFlow Serving REST API
response = requests.post('http://localhost:8501/v1/models/my_model:predict', json=data)
predictions = response.json()

# Convert predictions to numpy array
predictions = np.array(predictions["predictions"])

# Get the indices of the maximum values using argmax
argmax_indices = np.argmax(predictions, axis=1)

print(argmax_indices)