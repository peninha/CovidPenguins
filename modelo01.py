
traitList = {
	"infectedStart": 0.01,
	"age": {
		"mean": 30,
		"sigma": 20,
		}
	}
	

def roll(trait):
	if isnumeric(traitList.get(trait)):
		return traitsList.get(trait)*numpy.random.rand()
	else:
		return traitList.get(trait).sigma*numpy.random.randn() + traitList.get(trait).mean


	

class person:
	infected = False
	age = 0
	
	def __init__(self):
		self.infected = roll("infectedStart")
		self.age = roll("age")

sivana = person()