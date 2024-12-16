import requests
from  concurrent.futures import ProcessPoolExecutor

files = [
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Edet, Theophilus - Node.js Mastery_ A Comprehensive Guide to Server-Side JavaScript-CompreQuest Books (2023).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Seok, Jiho - The Complete Node.js Guide_ A Detailed Guide to Learning Node.js, Featuring In-Depth Explanations, Practical Examples, and Best Practices for Professional Developers-Jiho Seok (2024).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Nate Phoetean - Full-Stack Development with MEAN Stack_ MongoDB, Express.js, Angular, and Node.js-Independently Published (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Bethany Griggs, Manuel Spigolon - Node.js Cookbook_ Practical recipes for building server-side web applications with Node.js 22-Packt Publishing (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Ulises Gascón - Node.js for Beginners - A comprehensive guide to building efficient, full-featured web applications with Node.js-Packt Publishing Ltd. (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Real-Time Twilio and Flybase Build Real-Time Web Apps Using Twilio and Flybase with Node.js (Roger Stringer) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Node.js  Novice to Ninja (Craig Buckler) (Z-Library) (1).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Full Stack GraphQL Applications With React, Node.js, and Neo4j (MEAP V09) (William Lyon) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Node.js  Novice to Ninja (Craig Buckler) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Distributed Systems with Node.js (Thomas Hunter II) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Getting the Most out of Node.js Frameworks The Essential Tools and Libraries (Sufyan Bin Uzayr) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Procedural 3D Modeling Using Geometry Nodes in Blender (Siemen Lens) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Sufyan bin Uzayr - Getting the Most out of Node.js Frameworks_ The Essential Tools and Libraries-CRC Press (2022).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Pinakin Ashok Chaubal - Mastering MEAN Stack_ Build full stack applications using MongoDB, Express.js, Angular, and Node.js (English Edition)-BPB Publications (2023).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\(2024 Collection_ Forging Ahead in Tech and Programming) O., Adeolu - Essential Guide to Node.js for All Levels (2024 Collection_ Forging Ahead in Tech and Programming)-Independently Published (2023).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Jon Wexter - Node.js Projects-O'Reilly Media, Inc. (2024).epub",
    
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Edet, Theophilus - Node.js Mastery_ A Comprehensive Guide to Server-Side JavaScript-CompreQuest Books (2023).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Seok, Jiho - The Complete Node.js Guide_ A Detailed Guide to Learning Node.js, Featuring In-Depth Explanations, Practical Examples, and Best Practices for Professional Developers-Jiho Seok (2024).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Nate Phoetean - Full-Stack Development with MEAN Stack_ MongoDB, Express.js, Angular, and Node.js-Independently Published (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Bethany Griggs, Manuel Spigolon - Node.js Cookbook_ Practical recipes for building server-side web applications with Node.js 22-Packt Publishing (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Ulises Gascón - Node.js for Beginners - A comprehensive guide to building efficient, full-featured web applications with Node.js-Packt Publishing Ltd. (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Real-Time Twilio and Flybase Build Real-Time Web Apps Using Twilio and Flybase with Node.js (Roger Stringer) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Node.js  Novice to Ninja (Craig Buckler) (Z-Library) (1).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Full Stack GraphQL Applications With React, Node.js, and Neo4j (MEAP V09) (William Lyon) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Node.js  Novice to Ninja (Craig Buckler) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Distributed Systems with Node.js (Thomas Hunter II) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Getting the Most out of Node.js Frameworks The Essential Tools and Libraries (Sufyan Bin Uzayr) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Procedural 3D Modeling Using Geometry Nodes in Blender (Siemen Lens) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Sufyan bin Uzayr - Getting the Most out of Node.js Frameworks_ The Essential Tools and Libraries-CRC Press (2022).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Pinakin Ashok Chaubal - Mastering MEAN Stack_ Build full stack applications using MongoDB, Express.js, Angular, and Node.js (English Edition)-BPB Publications (2023).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\(2024 Collection_ Forging Ahead in Tech and Programming) O., Adeolu - Essential Guide to Node.js for All Levels (2024 Collection_ Forging Ahead in Tech and Programming)-Independently Published (2023).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Jon Wexter - Node.js Projects-O'Reilly Media, Inc. (2024).epub",
    
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Edet, Theophilus - Node.js Mastery_ A Comprehensive Guide to Server-Side JavaScript-CompreQuest Books (2023).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Seok, Jiho - The Complete Node.js Guide_ A Detailed Guide to Learning Node.js, Featuring In-Depth Explanations, Practical Examples, and Best Practices for Professional Developers-Jiho Seok (2024).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Nate Phoetean - Full-Stack Development with MEAN Stack_ MongoDB, Express.js, Angular, and Node.js-Independently Published (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Bethany Griggs, Manuel Spigolon - Node.js Cookbook_ Practical recipes for building server-side web applications with Node.js 22-Packt Publishing (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Ulises Gascón - Node.js for Beginners - A comprehensive guide to building efficient, full-featured web applications with Node.js-Packt Publishing Ltd. (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Real-Time Twilio and Flybase Build Real-Time Web Apps Using Twilio and Flybase with Node.js (Roger Stringer) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Node.js  Novice to Ninja (Craig Buckler) (Z-Library) (1).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Full Stack GraphQL Applications With React, Node.js, and Neo4j (MEAP V09) (William Lyon) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Node.js  Novice to Ninja (Craig Buckler) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Distributed Systems with Node.js (Thomas Hunter II) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Getting the Most out of Node.js Frameworks The Essential Tools and Libraries (Sufyan Bin Uzayr) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Procedural 3D Modeling Using Geometry Nodes in Blender (Siemen Lens) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Sufyan bin Uzayr - Getting the Most out of Node.js Frameworks_ The Essential Tools and Libraries-CRC Press (2022).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Pinakin Ashok Chaubal - Mastering MEAN Stack_ Build full stack applications using MongoDB, Express.js, Angular, and Node.js (English Edition)-BPB Publications (2023).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\(2024 Collection_ Forging Ahead in Tech and Programming) O., Adeolu - Essential Guide to Node.js for All Levels (2024 Collection_ Forging Ahead in Tech and Programming)-Independently Published (2023).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Jon Wexter - Node.js Projects-O'Reilly Media, Inc. (2024).epub",
    
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Edet, Theophilus - Node.js Mastery_ A Comprehensive Guide to Server-Side JavaScript-CompreQuest Books (2023).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Seok, Jiho - The Complete Node.js Guide_ A Detailed Guide to Learning Node.js, Featuring In-Depth Explanations, Practical Examples, and Best Practices for Professional Developers-Jiho Seok (2024).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Nate Phoetean - Full-Stack Development with MEAN Stack_ MongoDB, Express.js, Angular, and Node.js-Independently Published (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Bethany Griggs, Manuel Spigolon - Node.js Cookbook_ Practical recipes for building server-side web applications with Node.js 22-Packt Publishing (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Ulises Gascón - Node.js for Beginners - A comprehensive guide to building efficient, full-featured web applications with Node.js-Packt Publishing Ltd. (2024).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Real-Time Twilio and Flybase Build Real-Time Web Apps Using Twilio and Flybase with Node.js (Roger Stringer) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Node.js  Novice to Ninja (Craig Buckler) (Z-Library) (1).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Full Stack GraphQL Applications With React, Node.js, and Neo4j (MEAP V09) (William Lyon) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Node.js  Novice to Ninja (Craig Buckler) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Distributed Systems with Node.js (Thomas Hunter II) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Getting the Most out of Node.js Frameworks The Essential Tools and Libraries (Sufyan Bin Uzayr) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Procedural 3D Modeling Using Geometry Nodes in Blender (Siemen Lens) (Z-Library).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Sufyan bin Uzayr - Getting the Most out of Node.js Frameworks_ The Essential Tools and Libraries-CRC Press (2022).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Pinakin Ashok Chaubal - Mastering MEAN Stack_ Build full stack applications using MongoDB, Express.js, Angular, and Node.js (English Edition)-BPB Publications (2023).pdf",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\(2024 Collection_ Forging Ahead in Tech and Programming) O., Adeolu - Essential Guide to Node.js for All Levels (2024 Collection_ Forging Ahead in Tech and Programming)-Independently Published (2023).epub",
    r"C:\Users\91930\Documents\books\javascript\Nodejs\Jon Wexter - Node.js Projects-O'Reilly Media, Inc. (2024).epub",
]
# filename1 = r'/home/paradox/Documents/permute_brackets.py'
# filename2 = r"/home/paradox/Downloads/Python for Probability, Statistics, and Machine Learning ( PDFDrive ).pdf"
# files = [filename1] * 1001

# URL
url = 'http://127.0.0.1:9000/v1/u/m/'

def upload(file, url=url):
    # uploadfile = {'file': open(file, 'rb')}
    counter = 1
    uploads = {}
    for f in files:
        uploads[f"file{counter}"] = open(f, 'rb')
        counter+=1
        
        
    r = requests.post(url=url, files=uploads) 
    return r.json()


def main():
    with ProcessPoolExecutor() as executor:
        for index, json in enumerate(executor.map(upload, files)):
            print(index, json)
            
if __name__ == "__main__":
    main()