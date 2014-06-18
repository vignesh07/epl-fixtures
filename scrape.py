import csv
import urllib2
from bs4 import BeautifulSoup


html = urllib2.urlopen('http://www.premierleague.com/en-gb/matchday/matches.html?paramClubId=ALL&paramComp_100=true&view=.dateSeason').read()
soup = BeautifulSoup(html)
soup.prettify()

all_tables = soup.find_all('table')    #finding all the tables -- there are 2 in this case content table and league table


op_file = open("fixtures.csv",'a')   	#opening a csv file to write

op_file.write("BPL 2014-15 schedule Home vs Away format (time in GMT)")

for table in all_tables:
	 if(table['class'][0]=="contentTable"):   	#content table is the classname; other being league table
	 	header = table.find('th')
	 	print header.text
	 	op_file.write('\n')
	 	op_file.write(header.text)		#header contains the day (sample: Saturday August 16 2014)
	 	op_file.write('\n')

	 	data = table.find_all('td')		#collects all data present in the table
	 	for chunk in data:
	 		if(chunk['class'][0] =="time"):		#we need this class of data that has the details of the game's starting time 
	 			print "time is " + str(chunk.string) 	
	 			op_file.write(chunk.string)
	 			op_file.write('\t')
	 			

	 		if(chunk['class'][0]=="clubs"):	  #we need this class of data that has the names of the clubs
	 			name=chunk.find('a')
	 			print "match is between "+ str(name.string)
	 			op_file.write(name.string)
				op_file.write('\n')
	 			


op_file.close()


	 		





