import pandas as pd


class DataProcessor:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.df1 = None
        self.df2 = None

    def load_data(self):
        """
        Load Excel files into DataFrames.
        """
        self.df1 = pd.read_excel(self.file1)
        self.df2 = pd.read_excel(self.file2)

    def clean_data(self):
        """
        Clean and preprocess the data.
        """
        # Handle missing values
        self.df1.fillna({'Assigned to': 'Unassigned', 'Tags': 'No Tags'}, inplace=True)
        self.df2.fillna({'Assignee': 'Unassigned', 'Notes': 'No Notes'}, inplace=True)

        # Drop unnecessary columns
        self.df1.drop(['User ID', 'Parent Incident', 'Last_updated_by_QC', 'last_updated_days'], axis=1, inplace=True)
        self.df2.drop(['Release Note?', 'st.login', 'User Country'], axis=1, inplace=True)

        # Standardize column names
        self.df1.columns = self.df1.columns.str.strip().str.lower().str.replace(' ', '_')
        self.df2.columns = self.df2.columns.str.strip().str.lower().str.replace(' ', '_')

    def preprocess_dates(self):
        """
        Convert date columns to datetime format.
        """
        date_columns_df1 = ['actual_start', 'actual_end', 'opened_time', 'created', 'closed', 'resolved']
        date_columns_df2 = ['creation_time', 'run_date']

        for col in date_columns_df1:
            self.df1[col] = pd.to_datetime(self.df1[col], errors='coerce')

        for col in date_columns_df2:
            self.df2[col] = pd.to_datetime(self.df2[col], errors='coerce')

    def remove_duplicates(self):
        """
        Remove duplicate entries in the DataFrames.
        """
        self.df1.drop_duplicates(subset=['incident_number'], keep='first', inplace=True)
        self.df2.drop_duplicates(subset=['noteid', 'unique_id'], keep='first', inplace=True)

    def standardize_columns(self):
        """
        Standardize specific columns.
        """
        self.df1['incident_number'] = self.df1['incident_number'].str.strip().str.upper()
        self.df2['unique_id'] = self.df2['unique_id'].str.strip().str.upper()

    def add_period_columns(self):
        """
        Add a 'period' column for aligning data by year.
        """
        self.df1['date'] = pd.to_datetime(self.df1['created'])
        self.df2['date'] = pd.to_datetime(self.df2['creation_time'])
        self.df1['period'] = self.df1['date'].dt.to_period('Y')
        self.df2['period'] = self.df2['date'].dt.to_period('Y')

    def process(self):
        """
        Run all preprocessing steps.
        """
        self.load_data()
        self.clean_data()
        self.preprocess_dates()
        self.remove_duplicates()
        self.standardize_columns()
        self.add_period_columns()
        return self.df1, self.df2
