import pyttsx

with open('results.txt', 'r') as f:
    first_line = f.readline()
print(first_line)

print(type(first_line))
engine = pyttsx.init()
engine.say("I am pretty sure you are superman", first_line)
engine.runAndWait()