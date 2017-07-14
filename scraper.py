#MODIFY LINE 52 TO UPDATE THE MYSQL PASSWORD BEFORE RUNNING THIS SCRIPT
import wikipedia
import random
import time
import pymysql
import sys

def getWikiPara(term):
	#print "here"
	try:
		try:
			page = wikipedia.page(term)
			#print "here1"
		except:
			f = open("fail.txt", "a")
			print "page retrieve error for ",term 
			f.write(term)
			f.close()
		smmry = page.summary.replace("\n", " ")
		print page.summary
		#print page.sections
		#def_section = [section for section in page.sections if (u'definition' in section.lower() or u'description' in section.lower()) ]
		sections = page.sections
		pos = None
		for i in range(len(page.sections)):
			#print "here2"
			curr_section =  sections[i].lower()
			#print curr_section
			if 'definition' in curr_section or 'description' in curr_section:
				#print curr_section
				pos = i
				if page.section(sections[i]) != u'':
					break


		#Check if there's a definition or a formal definition page
		text = "-"
		if pos is not None:
			text = page.section(sections[pos]).replace("\n", " ")
		#print page.section('Technical description')
		return [term, smmry.encode('utf-8').rstrip(), text.encode('utf-8').rstrip()]
	except:
		print "error return"
		return [term, "-", "-"]

def main():

	#csvfile = open("out.csv", "a")
	#writer = csv.writer(csvfile)
	i = 0
	
	connection = pymysql.connect(host='localhost', user='root', password='.....', db='teknowbase', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
	connection.autocommit(True)

	index = sys.argv[1]

	with open("newEntities"+index, "r") as f:
		for term in f:
			if term[0] != '<':
				#print "here2"
				x = getWikiPara(term.rstrip())
				print x
				#try:
		        # Create a new record
		        try:
					cursor = connection.cursor()
					sql = "INSERT INTO `defns` (`term`, `smmry`, `det_def`) VALUES (%s, %s, %s)"
					cursor.execute(sql, (x[0], x[1], x[2]))
			except:
				print "sql write error for ", term
				f = open("failsq.txt", "a")
				f.write(term)
				f.close
				#print "committed"
			#time.sleep(random.randint(5, 10))
	#csvfile.close()
	connection.close()



if __name__ == "__main__":
	main()
