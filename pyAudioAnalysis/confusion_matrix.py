import os
import glob
import seaborn as sns
import numpy
import matplotlib.pyplot as plt
from pyAudioAnalysis import audioTrainTest as aT
from sklearn.metrics import accuracy_score, confusion_matrix

# =============================================================================


def show_confusion_matrix(y_test, y_predict):
    #    model.fit(Xtrain, ytrain)
    #    y_model = model.predict(Xtest)
    print('accuracy_score = {: .2f}%'.format(
        accuracy_score(ytest, y_predict)*100))

    table_confusion = confusion_matrix(ytest, y_predict)
    sns.heatmap(table_confusion, square=True, annot=True, cbar=False)
    plt.xlabel('predicted value "Y_Predict"')
    plt.ylabel('true value' "Y_Test")
    plt.text(0.0, -.25, '"0" for non-standard pronunciation', fontsize=12)
    plt.text(0.0, -.10, '"1" for ASE - American Standard English', fontsize=12)
    plt.show()


# =============================================================================
inputFolder = './data/speechPronunciation/test'
model_name = './data/spModel'
model_type = 'svm'
files = "*.wav"

if os.path.isdir(inputFolder):
    strFilePattern = os.path.join(inputFolder, files)
else:
    strFilePattern = inputFolder + files

wavFilesList = []
wavFilesList.extend(glob.glob(strFilePattern))
wavFilesList = sorted(wavFilesList)

if len(wavFilesList) == 0:
    print("No WAV files found!")

ypredict = []
for wavFile in wavFilesList:
    R, regressionNames = aT.fileRegression(wavFile, model_name, model_type)
    ypredict.append(R)

ypredict = numpy.array(ypredict)
ypredict = ypredict[:, 0]

bar = numpy.genfromtxt(
    './data/speechPronunciation/train/sayit.csv', delimiter=',')
ytest = bar[:, 1]
# =============================================================================
#show_confusion_matrix(ytest, ypredict)
show_confusion_matrix(ytest, ytest)
# =============================================================================
