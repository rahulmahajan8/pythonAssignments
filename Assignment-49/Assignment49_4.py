import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])

# Distance before scaling
distance_before = np.linalg.norm(data[0] - data[1])

# Apply StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Distance after scaling
distance_after = np.linalg.norm(
    scaled_data[0] - scaled_data[1]
)

print("Distance before scaling:", distance_before)
print("Distance after scaling:", distance_after)