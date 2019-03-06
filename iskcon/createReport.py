'''
Created on 18-Feb-2019

@author: aagoyal
'''
import sys 
import codecs
import datetime
import re
import json
from datetime import datetime, timedelta
from asyncore import write
import re

reload(sys)
sys.setdefaultencoding('utf-8')
FILENAME = "D:\\userdata\\aagoyal\\Desktop\\temp\\WhatsApp Chat with Radha Asthmi Diksha JPS.txt"
PROCESSEDFILE = "D:\\userdata\\aagoyal\\Desktop\\temp\\WhatsApp Chat with Radha Asthmi Diksha JPS Final.txt"

report = {} 
startDate = ""
phonebookNameToProperName = {
    "Sunayana Dewal Jps Initiation 2019" : "Sunayana mataji",
    "Gauranga Pr Jps 2019" : "Gauranga pr",
    "Bhadra Nitai Pr 2019 Jps" : "Bhadra Nitai pr",
    "P Jitu" : "Jitu pr",
    "Mitesh Pr Jps 2019" : "Mitesh pr",
    "Jyothi Jps 2019" : "Jyoti mataji",
    "BV Manohar" : "Manohar pr",
    "Jm Jaya Mataji" : "Jaya mataji",
    "Soniya Jps 2019" : "Soniya mataji",
    }
#structure ->
# devotee name/Number
#     date 
#         rounds
#         finish time
#         book reading

ROUNDS = "rounds"
CHANTINGFINISHTIME = "time"
READING = "reading"

def processInputFile():
    fs = codecs.open(PROCESSEDFILE, "w+")
          
    with codecs.open(FILENAME) as f:
        input = f.read()
        for line in input.split("\n"):
            dateOthers = line.split(",")
            try:
                datetime.strptime(dateOthers[0].strip(),"%d/%m/%y")
                fs.write("\n" + line)
            except:
                fs.write(" " + line)
    fs.close()

def analyzeWhatsappComment(line):
    global startDate
    dateOthers = line.split(",")
    if ": " in line: #catch it
        dateval = (dateOthers[0]).strip()
        timeOthers = (dateOthers[1]).split("-")
        timeval = timeOthers[0].strip()
        nameOthers = timeOthers[1].split(":")
        name = nameOthers[0].strip()
        if name in phonebookNameToProperName.keys():
            name = phonebookNameToProperName[name]
#         if(hasNumbers(name)):
#             print "before ", name
#             name = name.replace(" ", "")
#             name = [char for char in name if char.isdigit()]
#             name = ''.join(name)
#             print "after, "name
        sadhna = nameOthers[1]
        sadhnadict = processSadhnaFromComments(sadhna, name, timeval)
        if sadhnadict != {}:
            updateReport(name, dateval, sadhnadict)
            
        if startDate == "":
            startDate = dateval
    else:
        print "line ignored -> ", line

def processSadhnaFromComments(sadhna, name, timeval):
    sadhnadict = {}
    if "16" in sadhna and "Manohar" in name:
        sadhnadict[ROUNDS] = '16'
        sadhnadict[CHANTINGFINISHTIME] = timeval
    
    sadhnaOrig = sadhna
    sadhna = sadhna.replace(" ","").replace(".","")
    
    if ("rounds" in sadhna.lower() or "round" in sadhna.lower()):
        rounds = re.findall(r'\d+', sadhna)
        if len(rounds) == 1 and "yesterday" not in sadhna.lower():
            if rounds[0] != "16":
                sadhnadict[ROUNDS] = rounds[0] + " done and pending " + str(16-int(rounds[0]))
            else:
                sadhnadict[ROUNDS] = rounds[0]
            sadhnadict[CHANTINGFINISHTIME] = timeval
        elif "16" in rounds and "yesterday" not in sadhna.lower():
            sadhnadict[ROUNDS] = "16"
            sadhnadict[CHANTINGFINISHTIME] = timeval
        else:
            print "Check this prabhu -> ", name, ": ", sadhnaOrig.strip(), rounds
    
    if READING in sadhnaOrig.lower() or "read" in sadhnaOrig.lower():
        sadhnadict[READING] = re.sub(r'[^\x00-\x7F]+','', sadhnaOrig)   #remove non ascii code
        
    return sadhnadict

def updateReport(name, date, val):
    if name not in report.keys():
        report[name] = {}
    
    if date not in (report[name]).keys():
        report[name][date] = {}
    
    daysdata = report[name][date]
    
    for key in [ROUNDS, CHANTINGFINISHTIME, READING]:
        if key not in daysdata.keys() and key in val.keys():
            daysdata[key] = val[key]        
        
def saveToFile():
    global report, startDate
    
    writeType = "csv"
    fp = ""
    
    if writeType == "normal":
        fp = open('SadhnaReportJson.txt', 'w')
        fp.write(json.dumps(report))
        print "See it as yaml at https://www.json2yaml.com/"
    elif writeType == "csv":
        i = 0
        fp = open('SadhnaReport.csv', 'w')    
        fp.write("Date, Rounds, EndTime, Reading\n")
        for name in report.keys():
            if name == "Akshay Gaursundar Das" or name == "Radhapati Gopinath Prabhu":
                continue
            i = i+1
            fp.write("\n" + str(i) + ". " + name + "\n")
            dateList = generateListOfDates(startDate)

            for date in dateList:
                if date not in report[name].keys():
                    fp.write(date + ",PENDING,PENDING,PENDING\n")
                    continue
                if writeType == "normal":
                    fp.write("    " + date + " -> " + str(report[name][date]) + "\n")
                elif writeType == "csv":
                    sadhna = date + ","
                    for key in [ROUNDS, CHANTINGFINISHTIME, READING]:
                        if key in report[name][date].keys():
                            sadhna = sadhna + report[name][date][key].strip() + ","
                        else:
                            sadhna = sadhna + "PENDING,"
                    fp.write(sadhna + "\n")
    fp.close()        
    
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def generateListOfDates(startDate):
    start = datetime.strptime(startDate, "%d/%m/%y")
    end = datetime.strptime(datetime.today().strftime('%d/%m/%y'), "%d/%m/%y")
    date_generated = [start + timedelta(days=x) for x in range(1, (end-start).days + 1)]
    
    dateList = []
    for date in date_generated:
        dateList.append(date.strftime("%d/%m/%y"))
        
    return dateList

def insertExceptions():
    updateReport("Sunayana mataji", "20/02/19", {READING: "Verse  2.46 to 2.55 done"})
    updateReport("Jitu pr", "20/02/19", {READING: "Hare Krishna....4.10 to 4.31"})
    updateReport("Gauranga pr", "24/02/19", {ROUNDS: "16", CHANTINGFINISHTIME: "06:00 pm"})
    updateReport("Bhadra Nitai pr", "24/02/19", {ROUNDS: "16", CHANTINGFINISHTIME: "06:00 pm"})
    updateReport("Mitesh pr", "23/02/19", {ROUNDS: "16", CHANTINGFINISHTIME: "late night"})
    updateReport("Mitesh pr", "25/02/19", {ROUNDS: "10", CHANTINGFINISHTIME: "01:04 pm"})
    updateReport("Soniya mataji", "24/02/19", {ROUNDS: "16", CHANTINGFINISHTIME: "10:56 pm"})

if __name__ == '__main__':
    processInputFile()
    with codecs.open(PROCESSEDFILE) as f:
        input = f.read()
        for val in input.split("\n"):
            analyzeWhatsappComment(val)
    insertExceptions()
    print report
    saveToFile()
