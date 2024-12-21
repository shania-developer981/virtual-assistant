# import pyttsx4
# engine=pyttsx4.init()
# engine.say( "hey,my self shania ")
# engine.runAndWait() 

# import pyttsx4
# import speech_recognition as sr
# def listen() :
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print("listening...")
#         audio=r.listen(source)
#         text=r.recognize_google(audio)
#     return text


 ##### libraries webscout #####    

# text= listen()    
# print(text) 

# text= listen():
# if "joke in text":

# import pyttsx4
# from webscout import Meta
# from rich import print
# # **For unauthenticated usage**
# meta_ai = Meta()

# # Simple text prompt
# response = meta_ai.chat("What is the capital of France?")
# print(response)

# # Streaming response
# for chunk in meta_ai.chat("Tell me a story about a cat."):
#     print(chunk, end="", flush=True)

# # **For authenticated usage (including image generation)**
# fb_email = "abcd@abc.com"
# fb_password = "qwertfdsa"
# meta_ai = Meta(fb_email=fb_email, fb_password=fb_password)

# # Text prompt with web search
# response = meta_ai.ask("what is currently happning in bangladesh in aug 2024")
# print(response["message"]) # Access the text message
# print("Sources:", response["sources"]) # Access sources (if any)

# Image generation
# response = meta_ai.ask("Create an image of a cat wearing a hat.") 
# print(response["message"]) # Print the text message from the response
# for media in response["media"]:
#     print(media["url"])  # Access image URLs  


# import requests
# import json
# response = requests.get('https://dummyjson.com/products')
# print (response.json())
# result =response.json()
# with open ("product.json","w") as file:
#     json.dump(result, file)


