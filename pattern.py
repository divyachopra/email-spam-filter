# -*- coding: utf-8 -*-
#from collections import defaultdict
import os
import random
vocab= {}
wordWeight = {}
deltaWrdWght = {}
trainSpamCount = {}
trainHamCount = {}
testSpamCount = {}
testHamCount = {}
spamAcc = 0
hamAcc = 0
netAcc = 0
correctSpamCount = 0
correctHamCount = 0
netSpamCount = 0
netHamCount = 0
learningRate = 0.1
maxIterations = 2000
bias = 1

def get_train_spamail(path):
    filelist = os.listdir(path)
    filelist = filter(lambda x: x != 'cmds', filelist)
    all_msgs =[get_train_smail(os.path.join(path, f)) for f in filelist]
    #print trainSpamCount
    #for i in trainSpamCount:
    #   print "==============================================="        
     #   print i.name 
      #  print trainSpamCount[i]
    #    print "==============================================="
   #.....................................................Word punctuation complete.
    return all_msgs
def get_train_smail(path):    
    with open(path, 'rU') as f:
      tempcount = {}
    # print f  
   # print "==============================================="
      for msg in f :
       words = msg.split()
       #print msg
       for word in words :
         #print word#
         if word in tempcount :
             tempcount[word] += 1
             #print "old word"
         else :
             tempcount[word] = 1
         if word in vocab :
             vocab[word] += 1
             #print "old word"
         else :
             vocab[word] = 1
    trainSpamCount[f] = tempcount


   #print tempcount
  # print "===============checked tempcount general value.....=========="

   #return word,spamcount[word]  
   #print  spamcount[f]

def get_train_hamail(path):
    filelist = os.listdir(path)
    filelist = filter(lambda x: x != 'cmds', filelist)
    all_msgs =[get_train_hmail(os.path.join(path, f)) for f in filelist]
    #for i in trainHamCount:
        #print "==============================================="        
        #print i.name 
        #print trainHamCount[i]
        #print "==============================================="
    return all_msgs
    
def get_train_hmail(path): 
    #print('path: ', path)   
    with open(path, 'rU') as k :
      tempcount = {}
      #print k 
      #print "==============================================="
      for msg in k :
       words = msg.split()
       #print msg
       for word in words :
         #print word#
         if word in tempcount :
             tempcount[word] += 1
             #print "old word"
         else :
             tempcount[word] = 1
        
         if word in vocab :
             vocab[word] += 1
             #print "old word"
         else :
             vocab[word] = 1
    trainHamCount[k]= tempcount

  #print tempcount
   #print "==============================================="

   #return word,spamcount[word]  
   #print  hamcount[k]
def createVocab(spath,hpath):
    tempvocab = {}
    with open(spath, 'rU') as k :
      tempcount = {}
      #print k 
      #print "==============================================="
      for msg in k :
       words = msg.split()
       #print msg
       for word in words :
         #print word#
         if word in tempvocab :
             tempvocab[word] += 1
             #print "old word"
         else :
             tempvocab[word] = 1
    with open(hpath, 'rU') as k :
      tempcount = {}
      #print k 
      #print "==============================================="
      for msg in k :
       words = msg.split()
       #print msg
       for word in words :
         #print word#
         if word in tempcount :
             tempcount[word] += 1
             #print "old word"
         else :
             tempcount[word] = 1
    return tempvocab     
#vocab = createVocab(train_spam_path,train_ham_path)
def initWeights():
    #print random.random()
    for w in vocab:
        wordWeight[w] = (random.random())
        deltaWrdWght[w] = 0.0

def trainPerceptron ():
    for i in range(0,maxIterations):
        #for Spam messages
        destClass = 1
        for fl in trainSpamCount:
            weightedSum = bias
            calcClass=0            
            for word in trainSpamCount[fl]:
                count = trainSpamCount[fl][word]
                vWght = float(wordWeight[word])
                vWght = vWght + deltaWrdWght[word]
                wordWeight[word] = vWght 
                weightedSum = weightedSum + (count*vWght)

            if(weightedSum > 0 ):
                calcClass = 1                
            else:
                calcClass = 0
                
            for word in trainSpamCount[fl]:
                vCount = trainSpamCount[fl][word]
                deltaW = learningRate * (destClass - calcClass) * (vCount)
                deltaWrdWght[word] = deltaW

        #For ham messages        
        destClass = 0
        for fl in trainHamCount:
            weightedSum = bias
            calcClass=0            
            for word in trainHamCount[fl]:
                count = trainHamCount[fl][word]
                vWght = wordWeight[word]
                vWght = vWght + deltaWrdWght[word]
                wordWeight[word] = vWght 
                weightedSum = weightedSum + (count*vWght)

            if(weightedSum > 0 ):
                calcClass = 1                
            else:
                calcClass = 0
                
            for word in trainHamCount[fl]:
                vCount = trainHamCount[fl][word]
                deltaW = learningRate * (destClass - calcClass) * (vCount)
                deltaWrdWght[word] = deltaW            
    #print wordWeight
    #print "dummy checked"             
    
  

def get_test_spamail(path):
    filelist = os.listdir(path)
    filelist = filter(lambda x: x != 'cmds', filelist)
    all_msgs =[get_test_smail(os.path.join(path, f)) for f in filelist]
    #print trainSpamCount
    #for i in trainSpamCount:
    #   print "==============================================="        
     #   print i.name 
      #  print trainSpamCount[i]
    #    print "==============================================="
   #
    return all_msgs
def get_test_smail(path):    
    with open(path, 'rU') as f:
      tempcount = {}
    # print f  
   # print "==============================================="
      for msg in f :
       words = msg.split()
       #print msg
       for word in words :
         #print word#
         if word in vocab :
            if word in tempcount :
                 tempcount[word] += 1
                 #print "old word"
            else :
                 tempcount[word] = 1
    testSpamCount[f] = tempcount


   #print tempcount
  # print "==============================================="

   #return word,spamcount[word]  
   #print  spamcount[f]

def get_test_hamail(path):
    path = 'C:\Users\Divya Chopra\Downloads\Exam\pattern_proj'
    filelist = os.listdir(path)
    print('filelist',filelist)
    filelist = filter(lambda x: x != 'cmds', filelist)
    print('path: ', path)  
    all_msgs =[get_test_hmail(os.path.join(path, f)) for f in filelist]
    #for i in trainHamCount:
        #print "==============================================="        
        #print i.name 
        #print trainHamCount[i]
        #print "==============================================="
    return all_msgs
    
def get_test_hmail(path):    
    with open(path, 'rU') as k :
      tempcount = {}
      #print k 
      #print "==============================================="
      for msg in k :
       words = msg.split()
       #print msg
       for word in words :
         #print word#
        if word in vocab :
            if word in tempcount :
                 tempcount[word] += 1
                 #print "old word"
            else :
                 tempcount[word] = 1
        
      testHamCount[k]= tempcount
    #print testHamCount[k]

def testPerceptron ():
    #for i in range(0,maxIterations):
    spamAcc = 0.0
    hamAcc = 0.0
    netAcc = 0.0
    correctSpamCount = 0
    correctHamCount = 0
    netSpamCount = 0
    netHamCount = 0
    
    #for Spam messages
    destClass = 1
    for fl in testSpamCount:
        weightedSum = bias
        calcClass=0            
        for word in testSpamCount[fl]:
            count = testSpamCount[fl][word]
            vWght = float(wordWeight[word])
            weightedSum = weightedSum + (count*vWght)

        if(weightedSum > 0 ):
            calcClass = 1                
        else:
            calcClass = 0
        if(calcClass == destClass):
            correctSpamCount+=1.0
        netSpamCount+=1.0    
    #For ham messages        
    destClass = 0
    for fl in testHamCount:
        weightedSum = bias
        calcClass=0            
        for word in testHamCount[fl]:
            count = testHamCount[fl][word]
            vWght = wordWeight[word]
            weightedSum = weightedSum + (count*vWght)

        if(weightedSum > 0 ):
            calcClass = 1                
        else:
            calcClass = 0
        if(calcClass == destClass):
            correctHamCount = correctHamCount + 1.0
        netHamCount+=1.0
                
    #print wordWeight
    netAcc = (correctSpamCount + correctHamCount)/(netSpamCount + netHamCount)
    print "__correctSpamCount = " + str(correctSpamCount)
    print "__correctHamCount = "  + str(correctHamCount)
    print "__netSpamCount = "  + str(netSpamCount)
    print "__netHamCount = " + str(netHamCount)
    print "__netAccuracy = " + str(netAcc*100)

#File Paths
train_ham_path = 'C:\Users\Divya Chopra\Downloads\Exam\pattern_proj'
train_spam_path = 'C:\Users\Divya Chopra\Downloads\Exam\pattern_proj'
train_spam_messages = get_train_spamail(train_spam_path)    
train_ham_messages =get_train_hamail(train_ham_path)  
print"*****SPAM FILTER********************"
print "total vocabulary length :",len(vocab)  #dummy added to make sure the component is loaded.
print "Filtering.. "
initWeights()
trainPerceptron()
print "***********************************************"
print "Test Results for Dataset-1 " 
print "***********************************************"
print "__LearningRate="+str(learningRate)
print "__Iterations="+str(maxIterations)
test_ham_path = os.path.abspath(os.path.join('.',''))  
test_spam_path = 'C:\Users\Divya Chopra\Downloads\Exam\pattern_proj'
test_spam_messages = get_test_spamail(test_spam_path)    
test_ham_messages =get_test_hamail(test_ham_path)  
testPerceptron()
