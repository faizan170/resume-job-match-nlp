# Resume and Job Description Match
This is a Natural Language Project for Analyzing Job Description and Resume of User and show match score for Job Description.

It works with Spacy and NLTK for parsing resumes.

Here is sample output for a Resume and Job Description
```
{
  "totalScore": 47,
  "scores": {
    "skills": {
      "exists": 3,
      "not-exists": 8,
      "total": 11
    },
    "ats": {
      "exists": 10,
      "not-exists": 2,
      "total": 12
    },
    "rfindings": {
      "exists": 2,
      "not-exists": 2,
      "total": 4
    }
  },
  "ats": {
    "name": "FAIZAN AMIN",
    "email": "faizanfaizanamin@gmail.com",
    "mobileNumber": "+923045543201",
    "resumeSkillsMissing": 8,
    "jobTitleMatch": "notMatch",
    "jobTitle": "Learning Engineer",
    "educationMatch": {
      "required": false,
      "match": false
    },
    "headings": {
      "educationHeading": true,
      "workExperienceHeading": true
    },
    "dateFormatting": true,
    "fileFormat": {
      "format": "pdf",
      "noSpecialCharName": true,
      "nameReadable": true
    }
  },
  "recruiterFindings": {
    "length": {
      "current": 1423,
      "allowed": 1000
    },
    "measureableResults": null,
    "wordsToAvoid": null,
    "jobLevelMatch": true
  },
  "skillsData": {
    "pandas": {
      "ResumeCount": 1,
      "JobCount": 0,
      "wanted": false,
      "exists": true
    },
    "java": {
      "ResumeCount": 1,
      "JobCount": 0,
      "wanted": false,
      "exists": true
    },
    "ai": {
      "ResumeCount": 10,
      "JobCount": 1,
      "wanted": true,
      "exists": false
    },
    "cloud": {
      "ResumeCount": 2,
      "JobCount": 1,
      "wanted": true,
      "exists": false
    },
    "matplotlib": {
      "ResumeCount": 1,
      "JobCount": 0,
      "wanted": false,
      "exists": true
    },
    "php": {
      "ResumeCount": 1,
      "JobCount": 0,
      "wanted": false,
      "exists": true
    },
    "numpy": {
      "ResumeCount": 1,
      "JobCount": 0,
      "wanted": false,
      "exists": true
    },
    "programming": {
      "ResumeCount": 1,
      "JobCount": 1,
      "wanted": true,
      "exists": false
    },
    "machine learning": {
      "ResumeCount": 2,
      "JobCount": 1,
      "wanted": false,
      "exists": true
    },
    "docker": {
      "ResumeCount": 1,
      "JobCount": 0,
      "wanted": false,
      "exists": true
    },
    "tensorflow": {
      "ResumeCount": 2,
      "JobCount": 0,
      "wanted": false,
      "exists": true
    },
    "tkinter": {
      "ResumeCount": 1,
      "JobCount": 0,
      "wanted": false,
      "exists": true
    },
    "keras": {
      "ResumeCount": 2,
      "JobCount": 0,
      "wanted": false,
      "exists": true
    },
    "flask": {
      "ResumeCount": 1,
      "JobCount": 0,
      "wanted": false,
      "exists": true
    },
    "algorithms": {
      "ResumeCount": 0,
      "JobCount": 1,
      "wanted": true,
      "exists": false
    },
    "saas": {
      "ResumeCount": 0,
      "JobCount": 1,
      "wanted": true,
      "exists": false
    },
    "operations": {
      "ResumeCount": 0,
      "JobCount": 1,
      "wanted": true,
      "exists": false
    },
    "hypothesis": {
      "ResumeCount": 0,
      "JobCount": 1,
      "wanted": true,
      "exists": false
    },
    "testing": {
      "ResumeCount": 0,
      "JobCount": 1,
      "wanted": true,
      "exists": false
    },
    "system": {
      "ResumeCount": 0,
      "JobCount": 2,
      "wanted": true,
      "exists": false
    },
    "statistics": {
      "ResumeCount": 0,
      "JobCount": 1,
      "wanted": true,
      "exists": false
    },
    "pattern": {
      "ResumeCount": 0,
      "JobCount": 1,
      "wanted": true,
      "exists": false
    }
  },
  "meta": {
    "noOfPages": 1
  }
}
```
