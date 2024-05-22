
# Data Type Classifier
def data_type_classifier(df, distinguish_numeric = False):
    '''
    This function takes a dataframe as input and returns a dictionary with the data type of each column in the dataframe.
    The data types are classified as Binary, Categorical, and Continuous. Uncomment secondary block of code to distinguish if we are
    making the distinction between Discrete (integer) and Continuous numerical variables.
    
    Parameters:
    df: A pandas dataframe

    distinguish_numeric: Distinguishes between discrete or continuous numerical variables
        False - No distinguishment
        True - Distinguish "Continuous" into "Integer" and "Coninuous"
    
    Returns:
    data_type_dict: A dictionary with the data type of each column in the dataframe
    '''
    
    data_type_dict = dict()

    if distinguish_numeric == False:    
        for i in df.columns:
            if df[i].nunique() == 2:
                data_type_dict[i] = 'Binary'
            elif df[i].nunique() > 2 and df[i].nunique() <= 10:
                data_type_dict[i] = 'Categorical'
            else:
                if data_type_dict[i]
                data_type_dict[i] = 'Continuous'

        return data_type_dict
    
    else:
        for column in df.columns:
            if df[column].nunique() == 2:
                    data_type_dict[column] = 'Binary'
            elif df[column].nunique() > 2 and df[column].nunique() <= 10:
                data_type_dict[column] = 'Categorical'
            elif pd.api.types.is_numeric_dtype(df[column]):
                if all(df[column].astype(int) == df[column]):  # Check for integer-like values
                    data_type_dict[column] = 'Integer'
                else:
                    data_type_dict[column] = 'Continuous'  
        return data_type_dict