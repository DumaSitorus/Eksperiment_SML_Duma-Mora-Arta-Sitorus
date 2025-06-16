import pandas as pd

def hapus_outlier_tinggi(df, kolom='Tinggi Badan (cm)'):
    Q1 = df[kolom].quantile(0.25)
    Q3 = df[kolom].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[kolom] >= lower_bound) & (df[kolom] <= upper_bound)]
    return df

def encoding_data(df):
    # Encoding Jenis Kelamin
    df['Jenis Kelamin'] = df['Jenis Kelamin'].map({'laki-laki': 0, 'perempuan': 1})
    
    # Encoding Status Gizi
    df['Status Gizi'] = df['Status Gizi'].map({'severely stunted': 0, 'stunted': 1, 'normal': 2, 'tinggi': 3})
    
    return df

def preprocess_data(path_csv):
    # Load data
    df = pd.read_csv(path_csv)

    # Menghapus duplikat
    df = df.drop_duplicates()

    # Menghapus outlier pada kolom Tinggi Badan
    df = hapus_outlier_tinggi(df, kolom='Tinggi Badan (cm)')

    # Encoding data kategorikal
    df = encoding_data(df)

    # Reset index agar rapi
    df = df.reset_index(drop=True)

    return df
