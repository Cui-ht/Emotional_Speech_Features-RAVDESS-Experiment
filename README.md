# Emotional Speech Features with RAVDESS

An experiment to find speech acoustic features related to emotions in speech using the RAVDESS.

## Goal

The direct goal is to find what acoustic features are most related to emotions in speech using machine learning algorithms. Hopefully, we can utilise the algorithms here combined with more data or/and experiments to gain deeper knowledge of the topic, for example what features are more closely related to one certain emotion? What are robust features in all or some emotions? What features are related to emotion intensity?

## Data

We use the 1440 speech audio files from [RAVDESS](https://zenodo.org/record/1188976) as the raw dataset. There are 8 emotions (neutral, calm, happy, sad, angry, fearful, disgust, surprised) and two intensity levels (normal and strong) for each emotion (no strong intensity for "neutral"). These information are coded in the filenames.

We use openSMILE to extract acoustic features, more specifically the [eGeMAPS](https://sail.usc.edu/publications/files/eyben-preprinttaffc-2015.pdf) configuration with 88 features. 

## Description

### [Bash script](https://github.com/Cui-ht/Emotional_Speech_Features-RAVDESS-Experiment/blob/main/smile_egemaps_loop.sh)

The script runs in terminal to process all .wav files in one fold with openSMILE feature extraction and save all results in one .csv file. 

It takes two arguments:

1. Directory where .wav files are stored;
2. Output Csv file.

Besides, the openSMILE paths needs to be replaced by where it is actually installed.

Example: `bash smile_egemaps_loop.sh ~/project_dir/all_audio_dir ~/project_dir/raw_output.csv`

A glimpse of the output:

<img width="709" alt="图片" src="https://user-images.githubusercontent.com/57549068/154889372-e6aead56-459b-4094-afe7-ec3fd9d89ab3.png">



### [data_preprocess.py](https://github.com/Cui-ht/Emotional_Speech_Features-RAVDESS-Experiment/blob/main/data_preprocess.py)

As the name suggests, this script preprocesses the output of openSMILE extraction result (by the above bash script) to the format which we can analyze. I.e. we retrieve the information coded in file names and assign them to new columns. 

Similarly, it also takes two commad-line options: an input csv (`-i`) and an output one (`-o`).

Example: `python data_preprocess.py -i project_dir/raw_output.csv -o project_dir/cooked_output.csv `

A glimpse of this output:

<img width="1088" alt="图片" src="https://user-images.githubusercontent.com/57549068/154889455-6b1d8f79-4a85-4c33-83f8-0919237a3cb9.png">



### [decision_tree_model.ipynb](https://github.com/Cui-ht/Emotional_Speech_Features-RAVDESS-Experiment/blob/main/decision_tree_model.ipynb)

Analysis of the correlation between emotions and speech features with a scikit-learn decision tree model. The current result of this model is that the most influential feature is "F0semitoneFrom27.5Hz_sma3nz_pctlrange0", yet its importance is only 0.0873 of all 88 features.

![feature_importance](https://user-images.githubusercontent.com/57549068/154889483-f5f3e117-f1da-48dd-ba32-7254c7e2f24f.png)
<p align="center"><i>Figure 1. Top 15 features by imporatance</i></p>  

  
If we first only take the highest score as input X, the accuracy score would be 0.1875, However, when we add the second most important feature, the score rises to 0.3542 which would continue to rise as we add the third, fourth ... most important features. The score peaks at 0.4722 when the 14th feature is added.

![accuracy-iteration](https://user-images.githubusercontent.com/57549068/154889507-e0651905-17f7-49c5-b8e0-421879ca6543.png)
<p align="center"><i>Figure 2. Best accuracy score in each iteration</i></p>  
<p align="center"><i>For clearer graphs please view in the original notebook.</i></p> 

## Reference and Acknowlegment
Thanks for Dr. Chris Carignan's kind instructions.  
  
Livingstone SR, Russo FA (2018) The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS): A dynamic, multimodal set of facial and vocal expressions in North American English. PLoS ONE 13(5): e0196391. https://doi.org/10.1371/journal.pone.0196391.
  
Eyben, F., Scherer, K., Schuller, B., Sundberg, J., Andre, E., Busso, C., . . . Truong, K. (2016). The Geneva Minimalistic Acoustic Parameter Set (GeMAPS) for Voice Research and Affective Computing. IEEE Transactions on Affective Computing, 7(2), 190-202.  
  
## Author
Haotian Cui,  
21-2-2022
