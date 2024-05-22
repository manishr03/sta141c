
# Data Type Classifier

def data_type_classifier(df):
    '''
    This function takes a dataframe as input and returns a dictionary with the data type of each column in the dataframe.
    The data types are classified as Binary, Categorical, or Continuous.
    
    Parameters:
    df: A pandas dataframe
    
    Returns:
    data_type_dict: A dictionary with the data type of each column in the dataframe
    '''
    
    data_type_dict = dict()

    for i in df.columns:
        if df[i].nunique() == 2:
            data_type_dict[i] = 'Binary'
        elif df[i].nunique() > 2 and df_2[i].nunique() < 10:
            data_type_dict[i] = 'Categorical'
        else:
            data_type_dict[i] = 'Continuous'

    return data_type_dict

