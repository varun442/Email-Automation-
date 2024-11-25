import pandas as pd

# Create lists of names and emails from LinkedIn data
names = [
    "Jayanth Narla",
]

emails = [
    "jayanth221b@gmail.com",
]

# Create DataFrame
df = pd.DataFrame({
    'Name': names,
    'Email': emails
})

# Save to CSV
df.to_csv('./data/recipients.csv', index=False)
print("CSV file 'recipients.csv' has been created successfully in data folder!")