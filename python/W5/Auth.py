secret = 'swordfish'
pw = ''

auth = False
count = 0
max_attempt = 4  # number of attemps is 4!

while pw != secret:
    count += 1  # increasing number of attemps every single try (iteration)
    if count > max_attempt: break  # break will break all the way out of the loop and skip the else clause
    if count == 2: continue  # continue will shortcut the loop and go back up to the test without finishing the body of the loop (so we will skip the second iteration)
    pw = input(f"{count}: What's the secret word?\n ")
else:  # else clause only gets executed when the condition is no longer true and the loop exits normally
    auth = True

print('Nice job!' if auth else "Calling the FBI ...")