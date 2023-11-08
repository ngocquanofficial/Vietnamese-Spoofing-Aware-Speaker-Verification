import os
import sys 
sys.path.append(os.getcwd()) # NOQA

import random
import torch
from torch.utils.data import Dataset

from src.fusion.LCNN.vad.vad import voice_active_detection, vad_one_file
from src.fusion.feature import calc_stft, calc_cqt, calc_stft_one_file

# filenames = ["src/fusion/LCNN/vad/00000001.wav", "src/fusion/LCNN/vad/speech.wav"]
# file = "src/fusion/LCNN/vad/00000001.wav"
# print("DONE")
# one = vad_one_file(file)
# data = voice_active_detection(filenames)

# # print(calc_stft(data))

# print(calc_stft_one_file(one).shape)

# use the embedding vector implemented from 2 model AASIST(antispoof-model) and ECAPA(verification-model)
class TrainingDataLCNN(Dataset) :
    def __init__(self, path_list, type= "stft") :
        self.type = type
        self.path_list = path_list
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def __len__(self) :
        return len(self.path_list)

    def __getitem__(self, index) :
        audio_path = random.choice(self.path_list)
        audio_type = audio_path.split("/")[-2]
        if audio_type == "bonafide" :
            label = 1
        elif audio_type == "spoofed_replay" or audio_type == "spoofed_voice_clone" :
            label = 0
        else :
            print("ERROR Occur at Dataloader")
            label = None
        after_vad = vad_one_file(audio_path)
        
        
        
        
        
        

              