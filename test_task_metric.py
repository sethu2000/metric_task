
import unittest
import sys
import json
class TestMethods(unittest.TestCase):
    
    def test(self):
       
        self.input_file = "Interview_sample_data.pdf"
        self.output_file = "sample.json"
    
   
    def test_isFile(self):
        if self.input_file == None:
            self.assertFalse(self.input_file)

        else:
            self.assertTrue(self.input_file)
        
   
    # def test_split(self):        
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     with self.assertRaises(TypeError):
    #         s.split(2)



    def test_save_json(self):
        json_file_name = self.output_file
        dict_save = {
                    "name": "Burk Lee ",
                    "address": "XXX-XXX",
                    "email": "burk.lee@gmail.com",
                    "Education": " University of California, Berkeley Intended: Bachelor of Arts in PsychologyBalboa High School, San Francisco High School DiplomaRelevant Coursework: program development, research methods ",
                    "Leadership Experience": " data analysis, child development and adolescence, public services, administration,May 2023 GPA: 3.7June 2019ASUC Student Union Event Services \\u2013 Berkeley, CA Event Planning Assistant August 2019-Present\\u25cf Assist with the quality of services for students and staff at UC Berkeley campus.\\u25cf Organize and prepare the materials and equipment needed for events serving over 100+ guests.\\u25cf Maintain a positive guest experience by ensuring all event requests were met in a timely manner. Barany Consulting- Berkeley, CA Externship December 2019-January 2020 \\u25cf Explored work environments aligned to personal career and educational goals in social services by participating in training, presentations, and workshops to enhance communication skills.\\u25cf Assisted staff to complete administrative projects: emails, phone transfers, printing, scanning. \\u25cf Connected with alumni to explore opportunities for personal and professional growth within the consulting industry. ",
                    "Professional Experience": "Target- San Francisco, CA Sales Associate ",
                    "Additional Projects": " May 2018- June 2019\\u25cf Monitored inventory and restocked items as requested by store manager and team.\\u25cf Provided memorable customer service by assisting with merchandise to meet demands of company.\\u25cf Multitasked in a face pace environment to produce high volume of sales to meet weekly benchmarks. \\u25cf Operated computerized cash register and processed membership accounts.Child Development ResearchJune 2018\\u25cf Collected data from online reports to analyze the findings to present a 15-page research paper.\\u25cf Interviewed with students on campus to record over 50 responses to gain insight of their perceptions on the developmental stages of children. \\u25cf Presented a 10-minute presentation while facilitating a Q&A panel regarding research results. ",
                    "Skills & Interests": "Technical: Proficient with Microsoft Suite, Adobe Photoshop and Illustrator, Google PlatformsLanguage : Basic Tagalog (written and verbal)Interests :Community Service with over 100+ volunteer hours, traveler to over 5 countries in Asia."
                }
        self.assertTrue(dict_save, self.output_file)


        

  
if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestMethods.input_file = sys.argv[1]
        TestMethods.output_file = sys.argv[2]
        del(sys.argv[1],sys.argv[0])
        
    unittest.main()