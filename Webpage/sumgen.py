import sys
import pymysql


def getTerms():
	terms = sys.argv[1]
	ent = terms.split(',')
	#print ent
	#terms = [e.lower().replace(' ', '_') for e in ent]
	# terms
	return ent

def genSum(terms):
	#Set the right password
	connection = pymysql.connect(host='localhost', user='root', password='....', db='teknowbase', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
	connection.autocommit(True)
	#print connection

	out_sum = ""
	terms_o = terms
	terms = [e.lower().replace(' ', '_') for e in terms]
	#print terms
	for term in terms:
		#print "here2"
		cursor = connection.cursor()
		sql = 'SELECT `smmry`, `det_def` FROM `main` WHERE `term` like %s'
		#print sql%term
		cursor.execute(sql, (term))
		#print "here3"
		result = cursor.fetchone()
		#print result
		if result is not None:
			#print result
			sql = 'SELECT term, link from links where term like "%s"'
			cursor.execute(sql, term)
			tag_terms_d = cursor.fetchall()
			tag_terms = [d['link'].replace('_', ' ').split('(', 1)[0].rstrip() for d in tag_terms_d]
			out_sum += '<br/><h3>%s</h3><br/>'%term
			out_sum += result['smmry']
			for x in tag_terms:
				if x in out_sum.lower():
					out_sum = out_sum.replace(x, '<b>'+x+'</b>')

			
			if len(result['det_def']) >= 3:
				out_sum += "<br><h4>Formal Definition:</h4><br/>"
				out_sum += result['det_def']
			
			out_sum += "\n\n"

			# for i in range(len(tag_terms)):
			# 	poes = None
			# 	poes = tag_terms[i].find('(')
			# 	if poes is not None:
			# 		tag_terms[i] = tag_terms[i][0:poes+1]
		#print "here " + str(len(result))
	#cursor = connection.cursor()
	#sql = 'SELECT `term` as t1 FROM `temp2` t1, `temp2` t2 WHERE `smmry` LIKE \"{}\" + \"{}\" + \"{}\" '.format('%', result['smmry'], '%')
	#print sql
	#print cursor.execute(sql, result['smmry'])


	connection.close()

	out_sum = out_sum.rstrip('\n\n')
	


	for term in terms_o:
		#print term
		out_sum = out_sum
	#print "here5"
	return out_sum

def main():
	terms  = getTerms()
	#print terms
	summary = genSum(terms)

	#print 'asdf'
	print summary
	#print 'basdf'

if __name__ == '__main__':
	#print "here1", sys.argv[1:]
	main()