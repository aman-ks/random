"""Your inbuilt text to speech engine(On Ubuntu 12.04). Very Handy."""


import speechd
client = speechd.SSIPClient('test')
client.set_output_module('festival')
client.set_language('en')
client.set_punctuation(speechd.PunctuationMode.SOME)
client.speak("a")
client.speak("b")
client.speak("eight")
client.speak("0")
client.speak("I can speak anything")
client.close()
