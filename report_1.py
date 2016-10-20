import sqlite3

fragment = input("Return all addresses in New York City containing: ")
conn = sqlite3.connect("mth4320.db")
c = conn.cursor()
results = []
for borough in ["MN", "BK", "QN", "BX", "SI"]:
	results += c.execute("SELECT ADDRESS, BOROUGH, NUMFLOORS, BLDGCLASS, YEARBUILT FROM {0} WHERE Address LIKE '%{1}%'".format(borough, fragment)).fetchall()

borough_dict = {
	"MN": "Manhattan",
	"BK": "Brooklyn",
	"QN": "Queens",
	"BX": "The Bronx",
	"SI": "Staten Island"
}
class_dict = {
	"A": "One-Family Dwelling",
	"B": "Two-Family Dwelling",
	"C": "Walk-Up Apartment",
	"D": "Elevator Apartment",
	"E": "Warehouse",
	"F": "Factory Building",
	"G": "Garage",
	"H": "Hotel",
	"I": "Health Center",
	"J": "Theater",
	"K": "Store",
	"L": "Loft",
	"M": "Religious Facility",
	"N": "Asylum",
	"O": "Office",
	"P": "Place of Assembly",
	"Q": "Outdoor Facility",
	"R": "Condominium",
	"S": "Mixed-Use Residence",
	"T": "Transp. Facility",
	"U": "Utility Facility",
	"V": "Vacant Property",
	"W": "Education Center",
	"Y": "Gov. Installation",
	"Z": "Misc. Installation"
}

for (address, borough, numfloors, bldgclass, yearbuilt) in results:
	address = address.strip()
	if yearbuilt == 0:
		yearbuilt = "UNKNOWN"
	try:
		borough = borough_dict[borough]
	except:
		pass
	try:
		bldgclass = class_dict[bldgclass[:1]]
	except:
		pass
	print("{0} is a {2}-story {3} in {1} from {4}.".format(address, borough, int(numfloors), bldgclass.lower(), yearbuilt))