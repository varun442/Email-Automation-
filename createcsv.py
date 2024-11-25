import pandas as pd

# Create lists of names and emails from LinkedIn data
names = [
    "Christina Murphy",
    "Shaun Drawdy"
]

emails = [
    "cmurphy@saia.com",
    "sdrawdy@saia.com"
]

# Create DataFrame
df = pd.DataFrame({
    'Name': names,
    'Email': emails
})

# Save to CSV
df.to_csv('recipients.csv', index=False)
print("CSV file 'recipients.csv' has been created successfully!")