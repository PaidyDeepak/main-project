import pandas as pd
import json

hist = [
    {"event": "login", "timestamp": "2025-07-05 12:00"},
    {"event": "upload", "timestamp": "2025-07-05 12:05"},
]

# Convert to DataFrame
df = pd.DataFrame(hist)

# Optional check
print("DataFrame:\n", df)

# Save as JSON
df.to_json("history.json", orient="records", indent=2)
