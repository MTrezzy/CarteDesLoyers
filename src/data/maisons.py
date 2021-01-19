from . import *

RAW_DATA_FILE = ROOTDIR / 'data' / 'raw' / 'indicateurs-loyers-maisons.csv'

def download_dataset():
	URL = 'https://www.data.gouv.fr/fr/datasets/r/cf39b7e5-12fb-48e9-9ee7-b7e5496dcb75'
	download = requests.get(URL)

	decoded_content = download.content.decode('latin-1')

	# Save the csv raw dataset
	with open(RAW_DATA_FILE, 'w') as raw_file:
	    raw_file.writelines(decoded_content)


def read_dataset():
    df = pd.read_csv(RAW_DATA_FILE, sep=';', decimal=',')
    return df


def pipeline():
    download_dataset()
    df = read_dataset()
    outfn = ROOTDIR / 'data' / 'interim' / 'indicateurs-loyers-maisons.parquet'
    df.to_parquet(outfn)
