# Magic Embed Bot.
This bot was written for the purpose of sending embeds as messages on Discord. 

# Requirements:
- python 3.4+ (download it if you haven't).
- [discord.py](https://github.com/Rapptz/discord.py).
- Discord Application.

# Instructions.
1. Download this repository by clicking the green download button on the top right and choose the .ZIP option. Open the .ZIP file and drag the extracted folder to your Desktop.
2. Go to the [python dowloads page](https://www.python.org/downloads/) and install the latest version of Python 3. **DON'T INSTALL PYTHON 2.** Once the installation is complete, open your Applications folder (on your dock); open the Python 3.6 folder, then click the "Install Ce...ommand". Wait for it to complete.

3. Open the Command Line, (Terminal) on your laptop, and copy+paste the following code:
```
python3 -m pip install -U discord.py[voice]
```
4. Open `config.txt`
5. Open the Discord App, move your mouse to the top of the screen, then click; View > Developer > Toggle Developer Tools.
6. Click the '>>' and select 'Application'.
7. Click "Local Storage" on the left sidebar then click 'https://discordapp.com'. Go to the line that says 'token' and triple click the table cell to the right and copy the token.
8. Replace `your_token_here` with the token you just copied. **GET RID OF THE SPEECH MARKS".
9. On `config.txt`, replace `your_username_here` with your Discord Username. **(Include hashtags and numbers).**
10. Finally, select your desired colour from the colour wheel [here](https://www.google.com.au/search?q=%23ffffff&oq=%23ffffff&aqs=chrome..69i57.6998j0j4&sourceid=chrome&ie=UTF-8&safe=active&ssui=on).
11. Go to http://www.binaryhexconverter.com/hex-to-decimal-converter and input the hex value, (the one with the hashtag), and click, 'Convert'. Then, copy the number value.
12. Then, re-open `config.txt` and replace `your_colour_here` with the number value you copied.
13. Save the file, then go back to Terminal, and copy+paste the following line:
```
cd ~/Desktop/EmbeddingBot-master
python3 bot.py
```
14. When the bot prints out your Discord Credentials on the Terminal, it means that it is running. Enjoy.
