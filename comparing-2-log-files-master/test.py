
  def extract():
    try:	    
        file1= open('bcgp_log.txt','r')
        content= file1.readlines()
        #print(content1)
        i=0
        lis =[]
        testcase= "Oem Config Testcase"
        while i<len(content):
            if testcase in content[i]:
                lis.append(content[i])
            i=i+1
        return content
    except Exception as e:
        print(e)

def registrylog_get_client():
  try:
    lis6 = []
    with open(bcgp_logfile, "r") as f:
      lines = f.readlines()
      for line in lines:
        if re.search("Registry Testcase::", line):
          lis6.append(line)
      f.close()
      return lis6

  except Exception as e:
    print("Error in registrylog_get_client()")
    print((str(e)))
    print((traceback.format_exc()))


def comp(list1,list2):
    try:
        #print(list1)
        x=0
        dict = {}
        while x<len(list1):
            y=0
            cases= list1[x].split(':: ')
            Testcase = cases[1].split(" : ")[0]
            Value= cases[1].split(" : ")[1].split("\n")[0]
            while y<len(list2):
                case= list2[y].split(":: ")
                Testcase1 = case[1].split(" : ")[0]
                Value1= case[1].split(" : ")[1].split("\n")[0]
                if Testcase == Testcase1:
                    if Value != Value1:
                        dict[Testcase] =  Value1+' *1'
                    else:
                        dict[Testcase]= Value1 +' *0'
                y=y+1
            
            x=x+1
        print(dict)
        return dict
    
    except Exception as e:
        print(e)
						
def create_tokens(list1):
    try:
      lines = list1
      f2 = ""
      for line in lines:
        t1 = line.split("::")
        t2 = t1[1]

        t3 = t2.split()
        len1 = len(t3)

        if t3[len1 - 1] == "PASS":
          t4 = ' '.join(t3[0:(len1 - 1)])
          t5 = t3[len1 - 1]
          f2 += t4
          f2 += "|"
          f2 += t5
          f2 += "\n"
        elif t3[len1 - 1] == "FAIL":
          t4 = ' '.join(t3[0:(len1 - 1)])
          t5 = t3[len1 - 1]
          f2 += t4
          f2 += "|"
          f2 += t5
          f2 += "\n"
        elif re.search('PASS', t3[len1 - 1]):
          t3[len1 - 1] = t3[len1 - 1].replace("PASS", "")
          t4 = ' '.join(t3[0:(len1)])
          t5 = "PASS"
          f2 += t4
          f2 += "|"
          f2 += t5
          f2 += "\n"
        elif re.search('FAIL', t3[len1 - 1]):
          t3[len1 - 1] = t3[len1 - 1].replace("FAIL", "")
          t4 = ' '.join(t3[0:(len1)])
          t5 = "FAIL"
          f2 += t4
          f2 += "|"
          f2 += t5
          f2 += "\n"
        elif re.search('Null', t3[len1 - 1]):
          t4 = ' '.join(t3[0:(len1)])
          t5 = "Null"
          f2 += t4
          f2 += "|"
          f2 += t5
          f2 += "\n"
        elif re.search('(x86)', t3[len1 - 1]):
          t4 = ' '.join(t3[0:(len1 - 3)])
          t5 = ' '.join(t3[(len1 - 3):(len1)])
          f2 += t4
          f2 += "|"
          f2 += t5
          f2 += "\n"
        else:
          t4 = ' '.join(t3[0:(len1 - 1)])
          t5 = t3[len1 - 1]
          f2 += t4
          f2 += "|"
          f2 += t5
          f2 += "\n"

      return f2

    except Exception as e:
      print("Error in create_tokens()")
      print((str(e)))
      print((traceback.format_exc()))

listx= registrylog_get_client()
print(listx)
x= create_tokens(listx)
print(x)
