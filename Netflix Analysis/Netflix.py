# Import Required Libraries
import warnings
warnings.filterwarnings("ignore")
import pandas as pd

# Load Dataset
data = pd.read_csv('netflix1.csv')

# Display First Few Rows of the Dataset
print(data.head())

# Display Dataset Information
print(data.info())

# Display Summary Statistics of the Dataset
print(data.describe())

# Check for Missing Values
print(data.isnull().sum())

# Drop duplicates if any
data.drop_duplicates(inplace=True)

# Convert 'date_added' to datetime.
data['date_added'] = pd.to_datetime(data['date_added'], 
    format='mixed', 
    dayfirst=True, 
    errors='coerce'
)

# Remove extra spaces from string columns.
for col in ['type', 'title', 'director', 'country', 
            'rating', 'duration', 'listed_in']:
    data[col] = data[col].str.strip()

# Date-Based Features
data['year_added'] = data['date_added'].dt.year
data['month_added'] = data['date_added'].dt.month
data['month_name'] = data['date_added'].dt.month_name()

# Duration Features
data['duration_mins'] = data['duration'].str.extract('(\d+)').astype(float)

# Country & Genre Insights
data['genre_count'] = data['listed_in'].str.split(',').apply(len)
data['primary_genre'] = data['listed_in'].str.split(',').str[0]

tableau_cols = [
    'show_id', 'type', 'title', 'director', 'country',
    'date_added', 'year_added', 'month_name',
    'release_year', 'rating', 'duration_mins', 'listed_in',
    'primary_genre', 'genre_count'
]

# Save the cleaned dataset for Tableau or Power BI
df_tableau = data[tableau_cols]
df_tableau.to_csv('netflix_tableau_ready.csv', index=False)
print("✅ Tableau-ready dataset saved successfully")





