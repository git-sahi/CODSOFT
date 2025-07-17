MY LEARNINGS

1. I have defined various functions (PassEasy , PassMed , PassHard , PasswordGenerator) to improve readbility and it will be easy this way 
to maintain the code. The logic i used for password generation is simple. Easy passwords onlly contain a randomly generated number pattern,
medium password contain both numbers and letter, and hard password contain numbers, letters and special characters.

2. I used try and expect block to handle any exceptions if user inputs Negative/Zero value for length.

3. I implemented upper() to make ensure that input for 'complexity' is normalised.

4. The user interface is user friendly

5. I have a learned a better more efficient way of navigating through the password generation problem... 

instead of my initial logic to generate passswords, which was lenghty, complex and used up more space

def PassHard(length):  #password including numbers, letter and symbols
    Hardpwd = ''
    num = range(48,123)
    chrlst = r.sample(num , length)
    for i in chrlst:
        i = chr(i)
        Hardpwd += str(i)
    return Hardpwd

I came up with a more time efficient, simple logic which gave me more control over my code.

def PassHard(length):  #numbers, letter and symbols
    characters = s.ascii_letters + s.digits + s.punctuation
    Hardpwd =  ''.join(r.choice(characters) for i in range(length))
    return Hardpwd

6. Lastly, I used Tkinter to create a GUI version of the program.
   So now I have two versions:

   * One that runs on the command line

   * Another with a more interactive GUI interface

