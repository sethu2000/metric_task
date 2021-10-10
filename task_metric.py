from sys import argv
import os.path
import json
from pdfminer import high_level
import re

def isFile(fileName):
    try:
        if(not os.path.isfile(fileName)):
            print("file not found")
            exit()
    except Exception as e:
        print(e)
    
def main():
    try:
        fileName=argv[1]
        isFile(fileName)
        Pdf_extract(fileName)
        pass
    except Exception as e:
        print("No name for inputfile",e)
        

def Pdf_extract(filename):
    try:
   
        dict_save = {}
        local_pdf_filename = filename
        pages = [0] # just the first page
        extracted_text = high_level.extract_text(local_pdf_filename, "", pages)
        json_dumped = json.dumps(extracted_text)
        json_loaded = json.loads(json_dumped)
        first_word = json_loaded.split('\n')[0]
        dict_save.update({"name":first_word})
        
        for word in json_loaded.split('\n'):
            if "@gmail.com" in word:
                if "|" in word :
                    word = word.split()
                    address = word[1]
               
                dict_save.update({"address":address , "email":word[3]})
                

        Education = re.findall(r'Education(.*?)Leadership Experience',json_dumped)
        Education = "".join(Education).replace('\\n','').replace('_','').replace('  ','')


        Leadership_Experience = re.findall(r'Leadership Experience(.*?)Professional Experience',json_dumped)
        Leadership_Experience = "".join(Leadership_Experience).replace('\\n','').replace('_','').replace('  ','')
       
        Professional_Experience = re.findall(r'Professional Experience(.*?)Additional Projects',json_dumped)
        Professional_Experience = "".join(Professional_Experience).replace('\\n','').replace('_','').replace('  ','')
       

        Additional_Projects = re.findall(r'Additional Projects(.*?)Skills & Interests',json_dumped)
        Additional_Projects = "".join(Additional_Projects).replace('\\n','').replace('_','').replace('  ','')
        
        Technical = re.findall(r'Skills & Interests(.*?)Technical:',json_dumped)
        Technical = "".join(Technical).replace('\\n','').replace('_','').replace('  ','')
        Technical = "Technical:"+Technical
        

        Language = re.findall(r'Language:(.*?)\\u200b',json_dumped)
        Language = "".join(Language).replace('\\n','').replace('_','').replace('  ','')
        Language = "Language :"+Language
        

        Interests = re.findall(r'\\u200b(.*?)Interests:',json_dumped)
        Interests = "".join(Interests).replace('\\n','').replace('_','').replace('  ','')
        Interests = Interests.split('u200b')
        Interests = "Interests :" + Interests[1]
       

        SkillsInterests = Technical+Language+Interests
        
        dict_save.update({"Education":Education , "Leadership Experience":Leadership_Experience,
                            "Professional Experience": Professional_Experience,"Additional Projects":Additional_Projects,
                            "Skills & Interests":SkillsInterests})

        
        save_json(dict_save)
    except Exception as e:
        print(e)

    
    
def save_json(dict_save):
        json_file_name = argv[2]
        with open(json_file_name, "w") as outfile:
            json.dump(dict_save, outfile,indent=4)

main()