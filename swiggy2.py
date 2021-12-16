swiggy=[{"a2b":[{"area":"adayar","rating":"4.0","most rated":"vegitarian"} ],
 "anjappar":[{"area":"ashoknagar","rating":"4.2","most rated":"non veg"}],
 "thalapakatti":[{"area":"tiruvottiyur","rating":"4.5","most rated":"briyani"},],
 "ss hyderabad":[{"area":"kolathur","rating":"4.3","most rated":"briyani"}],
 "pushpa":[{"area":"koyambedu","rating":"3.8","most rated":"masalapoori"}],
 "locofeast":[{"area":"nungambakkam","rating":"4.1","most rated":"grillchcken"}],
 "bbq":[{"area":"tnagar","rating":"4.9","most rated":"unlimited buffet"}],
 "haunted":[{"area":"annanagar tower","rating":"4.9","most rated":"potato nuggets"}],
 "kfc":[{"area":"mambalam","rating":"3.5","most rated":"chicken popcorn"}],
 "yamohideen":[{"area":"velacherry","rating":"4.5","most rated":" beefbriyani"}],
 "bismillah":[{"area":"kathipara","rating":"4.3","most rated":"dumbriyani"}],
 "althaf":[{"area":"velacherry","rating":"4.7","most rated":"pepperchicken"}],
 "pizzahut":[{"area":"royapuram","rating":"4.9","most rated":"cheese pizza"}],
 "rideus":[{"area":"adampakkam","rating":"4.5","most rated":"chicken65"}],
 "rasavid":[{"area":"kalmandapam","rating":"4.5","most rated":"non veg"}],
 "oyalo":[{"area":"tolgate","rating":"3.5","most rated":"butter pizza"}],
 "pandiyas":[{"area":"tiruvottiyur","rating":"4.5","most rated":"briyani"}],
 "chettinad":[{"area":"talambur","rating":"3.8","most rated":"meals"}],
 "alif":[{"area":"mount","rating":"4.4","most rated":"briyani"}],
 "waterffalls":[{"area":"vadapalani","rating":"4.5","most rated":"combo"}],
 "thoppivapa":[{"area":"taramani","rating":"4.5","most rated":"chilliparotta"}],
 "ecrfastfood":[{"area":"triplicane","rating":"4.5","most rated":"chickenrice"}]}]

for i in swiggy:
    if (i["a2b"][0]["area"]=="adayar"):
        print("order food")
    if (i["althaf"][0]["area"]=="velacherry"):
        print("order rice")
    if (i["oyalo"][0]["area"]=="tolgate"):
        print("order pizza")

