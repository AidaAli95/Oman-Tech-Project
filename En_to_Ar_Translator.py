#Import pipeline library
from transformers import pipeline

#Choose models
model= ["mobarmg/Marian-en-ar", "anibahug/marian-finetuned-kde4-en-to-ar", "Helsinki-NLP/opus-mt-en-ar", "marefa-nlp/marefa-mt-en-ar"]

#English phrase to be translated
en_phrase1= "His majesty Sultan Haitham bin Tariq, may god protect him, has issued his royal orders to declare offical mourning, lower flag, and suspend work"
en_phrase2= "\ndue to the death of prince of Kuwait, starting from Saturday, December 16,2023, with official work resuming on Tuesday"
en_phrase= en_phrase1 + en_phrase2

i = 0
while i < len(model):
  #Print model name
  print("Model: "+ model[i]+ "\n")

  #Apply the translation with the choosen model
  ph_translate = pipeline("translation", model[i])
  
  #Get the translated arabic phrase
  print(ph_translate(en_phrase))
  print()

  #Go to the next model
  i = i + 1
