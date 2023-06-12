import pyshorteners

url = input("Enter URL which you want to Shorten : \n")

print("URL After Shortening :- ", pyshorteners.Shortener().tinyurl.short(url))
# This above line prints the Shorten url of your entered long URL.
