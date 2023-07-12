#Stress vs Strain

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

MaxStressList = []
MaxStrainList = []
MaxLoadList = []
MaxTimeList = []
MaxElongationList = []

directory = r"C:\Users\Scott Lohman\Desktop\spreadsheet\7.3.23\(-1,1)\CSV"
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        with open(os.path.join(directory, filename)) as f:
            table = pd.read_csv(f).to_numpy()
            range = table.shape[0]

            Time = table[16:range, 0].astype(float)
            Load = table[16:range, 1].astype(float)

            Length = table[7, 1]
            Width = table[5, 1]
            Thickness = table[6, 1]

            Strain = table[16:range, 5].astype(float)
            Stress = table[16:range, 4].astype(float)
            Displacement = table[16:range, 3].astype(float)
            Elongation = table[16:range, 2].astype(float)

            MaxStrain = max(Strain)
            MaxStrainList.append(MaxStrain)

            MaxLoad = max(Load)
            MaxLoadList.append(MaxLoad)

            MaxStress = max(Stress)
            MaxStressList.append(MaxStress)

            MaxElongatoin = max(Elongation)
            MaxElongationList.append(MaxElongatoin)

            MaxTime = max(Time)
            MaxTimeList.append(MaxTime)

            print("Max Stress for " + filename + " is " +str(float(MaxTime)))
            print("Max Stress for " + filename + " is " +str(float(MaxLoad)))    
            print("Max Stress for " + filename + " is " +str(float(MaxStress)))
            print("Max Stress for " + filename + " is " +str(float(MaxStrain)))

            # Plot Time vs Load
            plt.figure(1)
            plt.plot(Time, Load)
            plt.xlabel('Time(s)')
            plt.ylabel('Force(N)')
            plt.title('Force vs Time')

            # Plot Stress vs Strain
            plt.figure(2)
            plt.plot(Strain, Stress, 'r')
            plt.xlabel('Strain')
            plt.ylabel('Stress(MPa)')
            plt.title('Stress vs Strain')

            # Display the plots
            plt.show()

            print("\n")

averageMaxStrain = sum(MaxStrainList)/len(MaxStrainList)
averageMaxStress = sum(MaxStressList)/len(MaxStressList)
averageMaxLoad = sum(MaxLoadList)/len(MaxLoadList)
averageMaxElongation = sum(MaxElongationList)/len(MaxElongationList)
averageMaxTime = sum(MaxTimeList)/len(MaxTimeList)

print("Average Max Load was " + str(float(averageMaxLoad)))
print("Average Max Stress was " + str(float(averageMaxStress)))
print("Average Max Strain was " + str(float(averageMaxStrain)))
print("Average Max Elongation was " + str(float(averageMaxElongation)))
print("Average Max Time was " + str(float(averageMaxTime)))



