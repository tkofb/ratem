import pandas as pd

def getTickers():

    nasdaq_df = pd.read_csv('tickers/nasdaqlisted.txt', sep='|', usecols=['Symbol'])
    other_df = pd.read_csv('tickers/otherlisted.txt', sep='|', usecols=['ACT Symbol', 'Exchange'])
    
    nasdaq_df['Exchange'] = "NAS"
    other_df['Exchange'] = other_df['Exchange'].apply(lambda x: x if x != 'N' else "NY")
    other_df.rename(columns={"ACT Symbol": "Symbol"}, inplace=True)
    
    symbols_to_remove = {"A", "DD", "AI"}
    
    combined_df = pd.concat([nasdaq_df, other_df], ignore_index=True)
    combined_df = combined_df[~combined_df['Symbol'].isin(symbols_to_remove)]
    
    return combined_df
