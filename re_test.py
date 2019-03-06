import re
fileLocation = "C:\\dev_work\\svn-git\\repo1\\"
fileName = "a.txt"
targetFileName = "ch_a.txt"
pattern = '<author>(.*?)<\/author>'
 
class LogParser:
    def extractPattern(self, sFileLocation="C:/Users/", sTargetFileName = "hello.txt", sPattern = "1234"):
        with open(sFileLocation + fileName, mode="rt", encoding='utf-8') as f:
            string = f.read()
 
        pattern = re.compile(sPattern)
        findAll = pattern.findall(string)
        findSetList = list(set(findAll))

        for item in findSetList:
            with open(sFileLocation + sTargetFileName, mode="w+", encoding='utf-8') as f:
                f.write(item+' = ')
 
        print("success")
        
    def testCode(self, sample="<author>pi</author>\n<author>홍길동</author>"):
        pattern = re.compile("<author>(.*?)<\/author>")
        findAll = pattern.findall(sample)

        findSetList = list(set(findAll))
        for item in findSetList:
            print(item+' = ')
        
 
 
parser = LogParser()
#parser.testCode()
parser.extractPattern(fileLocation, targetFileName, pattern)
