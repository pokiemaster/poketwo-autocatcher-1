with open("data/config.json", "a") as file:
    print("Input your discord authorization token:OTc1NDU2NzE2MjgyMDM2MzE1.G8JeWp.hKDb0LrmiJw0vPimyM-OFzfJQfpVown_mGsDe0")
    auth_token = input()
    file.write("{\n")
    file.write(f'   "user_token" : "{auth_token}",\n')
    print("Now, input the preferred Channel ID for spamming and catching:1000896531018305587")
    channel_id = input()
    file.write(f'   "channel_id" : "{channel_id}"\n')
    file.write("}")

print("Setup completed. Please run the bot using the correct command:\nPlease see the GitHub repo for help on this.")
