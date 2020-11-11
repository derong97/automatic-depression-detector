# ellie

## DAIC-WOZ Database Description

This database is part of a larger corpus, the Distress Analysis Interview Corpus (DAIC) (Gratch et al.,2014), that contains clinical interviews designed to support the diagnosis of psychological distress conditions such as anxiety, depression, and post-traumatic stress disorder. These interviews were collected as part of a larger effort to create a computer agent that interviews people and identifies verbal and nonverbal indicators of mental illness (DeVault et al., 2014). Data collected include audio and video recordings and extensive questionnaire responses; this part of the corpus includes the Wizard-of-Oz interviews, conducted by an animated virtual interviewer called Ellie, controlled by a human interviewer in another room. Data has been transcribed and annotated for a variety of verbal and non-verbal features.

## Project Aim

To predict whether the participant is depressed using interview transcripts and audio data.

Due to non-disclosure, we will not be sharing the dataset. For more information, please refer to their [website](http://dcapswoz.ict.usc.edu).

## Set up

1. Download all the neccessary files from my [Google Drive](https://drive.google.com/drive/folders/1yuLqv8IrJNQr_JAuFyAlVaPYRA0ejydZ?usp=sharing). Only authorized members are allowed to perform this operation.
2. Create `ellie/data` directory and copy the `Y_data.csv` file over. The file contains all the labeled data for every participant.
3. Copy the `Transcript` folder into `ellie/preprocessing` directory. The folder contains all the transcript files from every participant.
