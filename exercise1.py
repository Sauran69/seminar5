try:
   sako=open('mailbox.txt')
except:
   print('Faila net')
   exit()

lines=sako.readlines()
Sauran=open ('output.txt','w')

for line in lines:
   if '(GMT)' in line:
      ind=line.find(',')
      en_ind=line.find('+')
      word=line[ind+2:en_ind-10]
      print(word)
      Sauran.write(word)
      Sauran.write('\n')
sako.close()
