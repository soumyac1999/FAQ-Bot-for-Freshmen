rep = {'greet':'Hi!',\
'affirm':'Thank you!',\
'goodbye':'See you soon.',\
'Hostel Allotment':'All freshers are alloted room in hostels 15 and 16 a few days before reporting. All rooms are alloted on a twin sharing basis and no changes are allowed normally.',\
'Hostel Mattress':'Students have to get their own mattress. Stall will be selling them and other items during the first few days near the hostels.',\
'Hostel Furnishing':'All rooms have a table, a chair and a cupboard for each student.',\
'Hostel Laundry':'All floors have a washing machine and a dryer which can be used by students. Also, hostel 15 has a laundry.',\
'Hostel Pests':'There is not too much a problem from pests but it is advisable to keep mosquito repellant and bed-bug sprays.',\
'Minors':'All information related to minors can be found in the Course Info Booklet at https://gymkhana.iitb.ac.in/~ugacademics/Docs/CourseInfo_Booklet.pdf',\
'Course Info':'All freshers have to complete several common courses which are fixed. Information about courses in later years can be found at https://gymkhana.iitb.ac.in/~ugacademics/Docs/CourseInfo_Booklet.pdf',\
'Branch Change':'The rules for change of branch can be found at http://www.iitb.ac.in/newacadhome/RulesforChangeofBranch201312March.pdf',\
'Classes':'Classes are conducted in various slots througout the starting from 8:30 am to 8:30 pm which lunch and evening breaks. Lecture slots are usually 1 to 1-1/2 hours long which labs are 3 hours long.',\
'Placements':'???',\
'Fees':'Fees are to paid at portal.iitb.ac.in/asc preferably for SBI / Canara Bank NetBanking.',\
'Vaccination':'All students are supposed to be vaccinated against common diseases. One can also get vaccinations done from IIT Bombay Hospital.',\
'Laptop':'It is recommended to have a laptop for reading lecture slides and CS101.',\
'Wallets':'Mobile wallets (mainly PayTM) are accepted throuout campus but it is good to have some cash too.',\
'Registration':'???'\
}

def reply(intent):
	t = rep[intent]
	if t == '???':
		return 'I don\'t know about this.'
	else:
		return t