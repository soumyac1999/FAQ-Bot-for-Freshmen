from rasa_nlu.model import Metadata, Interpreter

#Following lines are to ignore a FutureWarning raised by h5py
import warnings
warnings.simplefilter('ignore', FutureWarning)

#Load the trained model
print("Loading model... \nPlease Wait...")
interpreter = Interpreter.load("model")

#To let the user know that nlu is ready to classify
print("Hello!")

#Function to classify queries
def classify(query = None):
	warnings.simplefilter('ignore', DeprecationWarning) #To ignore DeprecationWarning raised by sklearn
	try:
		out = interpreter.parse(query)
		entities = {}
		for k in out['entities']:
			entities[k['entity']] = k['value']
		return out['intent']['name'], entities
	except:
		return "Could not classify", None #To handle cases where it is unable to load the model
