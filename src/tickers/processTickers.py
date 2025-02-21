import pandas as pd

# df = pd.read_csv('nasdaqlisted.txt', sep='|')
nasdaq_df = pd.read_csv('src/tickers/nasdaqlisted.txt', sep='|')
other_df = pd.read_csv('src/tickers/otherlisted.txt', sep='|')

nasdaq_df = pd.read_csv('src/tickers/nasdaqlisted.txt', sep='|', usecols=['Symbol'])
other_df = pd.read_csv('src/tickers/otherlisted.txt', sep='|', usecols=['ACT Symbol', 'Exchange'])

nasdaq_df['Exchange'] = "NAS"
other_df['Exchange'] = other_df['Exchange'].apply(lambda x: x if x != 'N' else "NY")
other_df.rename(columns={"ACT Symbol": "Symbol"}, inplace=True)

combined_df = pd.concat([nasdaq_df, other_df], ignore_index=True)
