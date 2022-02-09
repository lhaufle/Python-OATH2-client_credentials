import pandas as pd

class Transform:

    normal_values = ''

    def __init__(self, value):
        values = pd.DataFrame.from_dict(value['entries'])
        self.normal_values = values

    def chg_data_call_report(self):
        # change the data time from object to datetime
        self.normal_values['start_at'] = pd.to_datetime(
            self.normal_values['start_at'])
        self.normal_values['end_at'] = pd.to_datetime(
            self.normal_values['end_at'])
        # change any potential null values into 0 for types that are int
        self.normal_values['total_time'].fillna(0, inplace=True)
        self.normal_values['talk_time'].fillna(0, inplace=True)
        self.normal_values['wait_time'].fillna(0, inplace=True)
        self.normal_values['hold_time'].fillna(0, inplace=True)
        self.normal_values['abandon_time'].fillna(0, inplace=True)
        self.normal_values['total_ringing_time'].fillna(0, inplace=True)
        # drop any duplicates though this is not likely to happen.
        self.normal_values.drop_duplicates(inplace=True)
        # reset the index
        self.normal_values.reset_index()

    def clean_report(self):
        return self.normal_values
