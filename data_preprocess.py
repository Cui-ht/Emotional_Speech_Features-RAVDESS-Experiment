from re import L
import pandas as pd
import numpy as np
import argparse

# preprocesses openSMILE extrated features to transform the original file names to columns according to their meanings. See descriptions in the original source:

# Livingstone SR, Russo FA (2018) The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS): A dynamic, multimodal set of facial and vocal expressions in North American English. PLoS ONE 13(5): e0196391. https://doi.org/10.1371/journal.pone.0196391.

# uses command-line options.

def preprocess(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df = df.drop(columns=['frameTime'])
    names = [i.split('.')[0] for i in df['name']]
    name_list = [i.split('-') for i in names]
    name_matrix = np.array(name_list)
    df.insert(1, 'Emotion', name_matrix[:, 2])
    df.insert(2, 'Intensity', name_matrix[:, 3])
    df.insert(3, 'Statement', name_matrix[:, 4])
    df.insert(4, 'Repetition', name_matrix[:, 5])
    df.insert(5, 'Speaker', name_matrix[:, 6])
    
    # get sex by ID parity
    
    sex_array = np.array(['f' if int(i)%2 == 0 else 'm' for i in name_matrix[:, 6]])
    df.insert(6, 'Sex', sex_array)

    df.to_csv(output_csv, index=False)
    
# preprocess('/Users/haotiancui/Desktop/RAVDESS_audio/test.csv')

parser = argparse.ArgumentParser(description = "Preprocess openSMILE extrated features")
parser.add_argument("-i", "--input_csv", help="input csv path and file")
parser.add_argument("-o", "--output_csv", help="output csv path and file")
args = parser.parse_args()

if __name__ == "__main__":
    preprocess(args.input_csv, args.output_csv)