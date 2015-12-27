'''
Created on Dec 27, 2015

@author: karam
'''
'''
Created on Dec 27, 2015

@author: karam
'''
class Process :
    def __init__(self,state=1,channel=""):
        self.state=state
        self.channel=channel
    def subWords(self,length=None) :
        subWordList =[]
        channel = self.channel
        channelLength = len(channel)
        if length== None : length=channelLength
        for i in range(1,length+1):
            for j in range(0,channelLength-i+1):
                subWordList.append(channel[j:j+i])
        return subWordList
    def subProcesses(self,length):
        subProcessList=[]
        state = self.state
        if length==None : length = len(self.channel)
        subWordList= self.subWords(length)
        for i in range(0,len(subWordList)):
            subProcessList.append(Process(state,subWordList[i]))
        return subProcessList
    def __eq__(self,other):
        if self.state == other.state and self.channel==other.channel : return True
        return False
    def __str__(self):
        return "["+str(self.state)+",\""+self.channel+"\"]"
class LCSystem:
    def __init__(self,sendProcess=Process(),recieveProcess=Process()):
        self.sendProcess = sendProcess
        self.recieveProcess = recieveProcess
    def alpha(self,K):
        viewsList=[]
        sendProcess = self.sendProcess
        recievedProcess = self.recieveProcess
        sendProcessesList = sendProcess.subProcesses(K)
        recieveProcessesList = recievedProcess.subProcesses(K)
        for i in range(0,len(sendProcessesList)):
            for j in range(0,len(recieveProcessesList)):
                view = LCSystem(sendProcessesList[i],recieveProcessesList[j])
                if view not in viewsList:
                    viewsList.append(view)
        return viewsList
    def __eq__(self,other):
        if self.sendProcess == other.sendProcess and self.recieveProcess == other.recieveProcess :
            return True
        return False
    
    def __str__(self):
        return "["+str(self.sendProcess.state) + ","+str(self.recieveProcess.state) \
            +","+"\""+self.sendProcess.channel+"\""+","+"\""+self.recieveProcess.channel+"\"]"
    
        
p = LCSystem()
p.sendProcess.channel = "111"
p.recieveProcess.channel = "110"
list = p.alpha(2)
for i in range(0,len(list)):
    print list[i]