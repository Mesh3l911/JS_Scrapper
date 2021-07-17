import requests , sys , re , optparse 
from bs4 import BeautifulSoup

def logo():
    print('''\033[2;31m
                                      010                                       
                                      010                                       
                            000000000 010 000000000                             
                       00000000000000 010 00000000000000                        
                    00000000000000000 010 00000000000000000                     
                 00000000000000       010        0000000000000                  
               00000000000       0    010    0          0000000000                
             00000000          00             00           000000000              
           00000000           000             000            00000000            
          00000000           0000             0000             00000000          
         0000000             0000   1111111   0000              00000000         
       0000000                0000111111111110000                0000000        
       000000                 0011111111111111100                 0000000       
      000000                   11111111111111111                   0000000      
     000000                   1111111111111111111                   000000      
     000000                  111111111111111111111                   000000     
    000000                  11111111111111111111111                  000000     
    000000         0000000011111111111111111111111110000000           00000     
    00000       00000000001111111111111111111111111110000000000       000000    
00000000000000 00000000000111111111111111111111111111100000000000 000000000000000
00000000000000           11111111111111111111111111111            000000000000000
    00000                11111111111111111111111111111                00000    
    000000         00000001111111111111111111111111111000000          00000     
    000000       0000000 11111111111111111111111111111 00000000      000000     
     000000    0000000   11111111111111111111111111111   0000000     00000    
     000000    00         111111111111111111111111111         00    000000      
      000000            00001111111111111111111111100000           000000       
       0000000        00000001111111111111111111110000000         0000000       
        0000000      000000  111111111111111111111   000000     00000000        
         0000000    000        11111111111111111        000    0000000          
          00000000                 111111111                 00000000           
            000000000                                      000000000            
             0000000000                                 000000000              
                00000000000           010           000000000000                
                  000000000000000     010     000000000000000                   
                     0000000000000000 010 0000000000000000                      
                         000000000000 010 0000000000000                         
                              0000000 010 0000000                               
                                      010                                       
                                      010                                      

                   -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                   +      ..| JS_Scrapper v1.0 |..        +
                   -                                      -
                   -              By: Mesh3l              -
                   +         Twitter: Mesh3l_911          +
                   -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                                 
\033[1;m''')

#Colores:
sRed   , eRed   = "\033[1;31m" , "\033[1;m"
sWhite , eWhite = "\033[1;37m" , "\033[1;m"
sGray  , eGray  = "\033[1;90m" , "\033[1;m"

JS = []
Session = requests.session()
def Scrapper(Path):
    with open(Path, 'r') as urls:

        for url in urls.read().splitlines():
            print("\n"+sWhite+"JS for"+eWhite+" \033[1;31m{}\033[1;m : \n".format(url))
            Source = Session.get(url).text.replace('!--','').replace('/*','').replace('*/','')
            Soup = BeautifulSoup(Source, 'html.parser')
            Src = Soup.find_all('script')
            Href = Soup.find_all('link')
            splittedUrl = url.rsplit('/',-1)[2]
            urlScheme = url.rsplit('/',-1)[0]

            for _ in Src:
                if 'src="' in str(_) and '.js' in str(_) and '.json' not in str(_):
                    Scrapped = re.search(r'src="(.+)"', str(_)).group(1).rsplit('.js',-1)[0]+'.js'
                    if splittedUrl in Scrapped:
                        JS.append(Scrapped)
                    elif 'https://' not in Scrapped and 'http://' not in Scrapped:
                        pathChecker = Session.get(url+Scrapped).text.lower()
                        Status = Session.get(url+Scrapped).status_code
                        if Status == 200:
                            JS.append(url+Scrapped)
                        elif Status== 404:
                            JS.append(urlScheme+'//'+splittedUrl+Scrapped)
                        else:
                            JS.append(Scrapped)
                else:
                    pass
                
            for _ in Href:
                if 'href=' in str(_) and '.js' in str(_) and '.json' not in str(_):
                    Scrapped = re.search(r"href=(.+)", str(_)).group(1).rsplit('.js',-1)[0]+'.js'
                    if splittedUrl in Scrapped:
                        JS.append(Scrapped)
                    elif 'https://' not in Scrapped and 'http://' not in Scrapped:
                        pathChecker = Session.get(url+Scrapped).text.lower()
                        Status = Session.get(url+Scrapped).status_code
                        if Status == 200:
                            JS.append(url+Scrapped)
                        elif Status== 404:
                            JS.append(urlScheme+'//'+splittedUrl+Scrapped)
                        else:
                            JS.append(Scrapped)
                    else:
                        pass
                else:
                    pass


            for js in JS:
                print(sGray+js+eGray)

            JS.clear()




def Args():
    Parser = optparse.OptionParser()
    Parser.add_option("--p", "--path", dest="listPath", help="urls path")
    (arguments, values) = Parser.parse_args()
    return arguments

def main():
    arguments = Args()
    if len(sys.argv) == 3:
        logo()
        try:
            Scrapper(arguments.listPath)
        except (requests.exceptions.MissingSchema , ConnectionError) as error:
            print("\n"+sWhite+"Please check ur list urls ( 1-alive , 2-has a Sheme e.g. https:// or http:// )"+eWhite+"\n")
    else:
        logo()
        print(""+sWhite+"\nUsage:"+eWhite+" \n"+sRed+"python3 JS_Scrapper.py --path <listPath>"+sRed+"\n")


  
if __name__ == '__main__':
    main()          


