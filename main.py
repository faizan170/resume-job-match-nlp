from pyresparser import ResumeParser
import numpy as np
import time
import json
from pdfTextExtract import extract_text_from_pdf
from find_job_titles import FinderAcora
skillsData = np.load("finalDataTags.npy")

data = ResumeParser("demo.docx").get_extracted_data()

import docx


def checkEducation(txt):
    edu = ["Education", "Degree"]
    for e in edu:
        if e.lower() in txt.lower():
            return True
    return False

def checkExperience(txt):
    exp = ["Experience", "Work Experience"]
    for e in exp:
        if e.lower() in txt.lower():
            return True
    return False

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
    
def getOtherResults(ResumePath, JobPath):
    text = ""
    meta = {}
    for page in extract_text_from_pdf(ResumePath):
        text += ' ' + page
    meta["length"] = len(text)
    textJob = getText(JobPath)
    print(type(text))
    finder = FinderAcora()
    jobTitle = finder.findall(textJob)
    if len(jobTitle) != 0:
        jobTitle = jobTitle[0].match
        meta["jobTitle"] = jobTitle
        meta["jobTitleResume"] = "no-exists"
        if jobTitle in text:
            meta["jobTitleResume"] = "exists"
    
    meta["eductationHeading"] = True if checkEducation(text) else False    
    meta["workExperienceHeading"] = True if checkExperience(text) else False
    
    meta["educationRequirements"] = True if checkEducation(textJob) else False

    print("Meta:", meta)



def parseSkills(skills):
    skillsFinal = []
    for skill in skills:
        lowerSkill = skill.lower()
        if lowerSkill in skillsData:
            skillsFinal.append(skill)
    return skillsFinal


def checkSkillsScore(resumeSkills, JobSkills):
    resumeSkills = [skill.lower() for skill in resumeSkills]

    JobSkills = [skill.lower() for skill in JobSkills]
    eScore = 0
    for jSkill in JobSkills:
        if jSkill in resumeSkills:
            eScore += 1
    return eScore, len(JobSkills) - eScore


def finalizeSkillsDisplay(resumeSkills, JobSkills):
    fSkills = {}
    resumeSkills = [skill.lower() for skill in resumeSkills]

    JobSkills = [skill.lower() for skill in JobSkills]
    eSkills = 0
    for skill in resumeSkills:
        if skill not in JobSkills:
            fSkills[skill] = {
                "wanted": False,
                "exists": True
            }
        else:
            eSkills += 1
            fSkills[skill] = {
                "wanted": True,
                "exists": True
            }
    for skill in JobSkills:
        if skill not in resumeSkills:
            fSkills[skill] = {
                "wanted": True,
                "exists": False
            }
        else:
            fSkills[skill] = {
                "wanted": True,
                "exists": False
            }
    print(eSkills, len(resumeSkills) - eSkills)
    return fSkills

def getResults(resumePath, jobPath):
    old = time.time()
    resumeData = ResumeParser(resumePath).get_extracted_data()
    resumeData["skills"] = parseSkills(resumeData["skills"])
    print("Resume Skills:", resumeData["skills"])

    jobData = ResumeParser(jobPath).get_extracted_data()
    jobData["skills"] = parseSkills(jobData["skills"])
    print("Job Skills:", jobData["skills"])

    skillsRes = finalizeSkillsDisplay(resumeData["skills"], jobData["skills"])
    resumeData["skillsData"] = skillsRes
    miscResults = getOtherResults(resumePath, jobPath)
    resumeData["socres"] = {
        "skills": checkSkillsScore(resumeData["skills"], jobData["skills"])
    }
    print(json.dumps(resumeData, indent=2, sort_keys=True))

getResults("C:/Users/Faizan/Documents/Resume (1).pdf", "demo.docx")
