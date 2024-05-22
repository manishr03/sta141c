
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
    
# Function to compute Phi Coefficient matrix - binary variables
def compute_phi_matrix(df):
    corr_matrix = pd.DataFrame(np.zeros((df.shape[1], df.shape[1])), columns=df.columns, index=df.columns)
    for i in range(df.shape[1]):
        for j in range(i, df.shape[1]):
            if i == j:
                corr_matrix.iloc[i, j] = 1.0
            else:
                corr, _ = scipy.stats.pearsonr(df.iloc[:, i], df.iloc[:, j])
                corr_matrix.iloc[i, j] = corr
                corr_matrix.iloc[j, i] = corr
    return corr_matrix

# Function to get top 5 most correlated predictors
def get_top_correlated_predictors(corr_matrix, predictor, top_n=5):
    if predictor not in corr_matrix.columns:
        raise ValueError(f"Predictor '{predictor}' not found in the DataFrame.")
    # Get the correlations for the specified predictor
    predictor_correlations = corr_matrix[predictor]
    # Drop the predictor itself to avoid self-correlation
    predictor_correlations = predictor_correlations.drop(predictor)
    # Get the top N most correlated predictors
    top_predictors = predictor_correlations.abs().nlargest(top_n)
    return top_predictors

# Function to put top 5 most correlated predictors in a dataframe
def top_correlated_predictors_df(corr_matrix, top_n=5):
    all_top_correlations = {}
    for predictor in corr_matrix.columns:
        top_correlations = get_top_correlated_predictors(corr_matrix, predictor, top_n)
        all_top_correlations[predictor] = top_correlations.index.tolist()
    
    # Create a DataFrame for the top correlated predictors
    top_correlations_df = pd.DataFrame.from_dict(all_top_correlations, orient='index', columns=[f'{i+1}' for i in range(top_n)])
    return top_correlations_df

# Function to compute Cramer's V for categorical variables
def cramers_v(x, y):
    contingency_table = pd.crosstab(x, y)
    chi2, p, dof, expected = scipy.stats.chi2_contingency(contingency_table)
    n = contingency_table.sum().sum()
    phi2 = chi2 / n
    r, k = contingency_table.shape
    return np.sqrt(phi2 / min(k-1, r-1))

# generate a correlation matrix for categorical variables - not relevant 
def compute_cramers_v_matrix(df):
    corr_matrix = pd.DataFrame(np.zeros((len(df.columns), len(df.columns))), 
                               index=df.columns, columns=df.columns)
    
    for col1 in df.columns:
        for col2 in df.columns:
            if col1 == col2:
                corr_matrix.loc[col1, col2] = 1.0
            else:
                corr_matrix.loc[col1, col2] = cramers_v(df[col1], df[col2])
    return corr_matrix

# generate a dataframe of the top correlated categorical variables
def top_correlated_categorical_all(df, top_n=5):
    all_top_correlations = {}
    for target_var in df.columns:
        correlations = {}
        for col in df.columns:
            if col != target_var:
                correlations[col] = cramers_v(df[target_var], df[col])
        
        # Sort by correlation values and get top N
        sorted_correlations = sorted(correlations.items(), key=lambda item: item[1], reverse=True)
        top_correlated = [var for var, _ in sorted_correlations[:top_n]]
        all_top_correlations[target_var] = top_correlated

    # Create a DataFrame for the top correlated predictors
    top_correlations_df = pd.DataFrame.from_dict(all_top_correlations, orient='index')
    top_correlations_df.columns = [f'{i+1}' for i in range(top_n)]
    return top_correlations_df

# Generate a dataframe of the top correlated continuous variables
def top_correlated_continuous_all(corr_matrix, top_n=5):
    all_top_correlations = {}
    for target_var in corr_matrix.columns:
        correlations = corr_matrix[target_var].drop(target_var)
        top_correlated = correlations.abs().nlargest(top_n).index.tolist()
        all_top_correlations[target_var] = top_correlated

    # Create a DataFrame for the top correlated predictors
    top_correlations_df = pd.DataFrame.from_dict(all_top_correlations, orient='index')
    top_correlations_df.columns = [f'Top_{i+1}' for i in range(top_n)]
    return top_correlations_df