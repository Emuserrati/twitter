# importing modules [tweepy for access credentials, random for the random values, PIL for the image creation]
# can be installed used pip install command or using conda

import tweepy
import time, random
from PIL import Image, ImageDraw


#size in pixels of the image
size = (1000,1000)
wait = 20

# they can be created with a Twitter developer account and creating a new application
consumer_key = "INSERT CONSUMER KEY"
consumer_secret = "INSERT CONSUMER SECRET KEY"
access_token="INSERT ACCESS TOKEN"
access_token_secret = "INSERT SECRET ACCESS TOKEN"

# CREDIT: authentication code [next 10 lines] copied from the documents on Github by: https://gist.github.com/szolotykh/e4924159d79ddbaa12c6

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.me()


#function running continously in order to have intervalled output
while True:
    grid_size = (random.randint(1,101), random.randint(1, 101))
    image = Image.new('RGB', size, color = 'white')
    draw = ImageDraw.Draw(image)

    previous = (0,0)
    
    # function for the creation of the image, coloring the grid
    for i in range(1, grid_size[1]+1):
        for f in range(1, grid_size[0]+1):
            draw.rectangle([previous, (previous[0] + size[0]/grid_size[0], previous[1]+ size[1]/grid_size[1])], fill = (random.randint(0,256), random.randint(0,256), random.randint(0,256)))
            previous = (previous[0] + size[0]/grid_size[0],previous[1])

        previous = (0, previous[1] + size[1]/grid_size[1])
    
    #save the image to PC
    imagePath = 'img.png'
    image.save(imagePath) 
   
  
    seed = random.randint(0, 222222)
    # text for the tweet, random number test case and the size of the grid 
    text = 'Test case #{0} \n Grid size: {1} x {2} \n #random #art #squares #grid'.format(seed, grid_size[0], grid_size[1])
    

    # Send the tweet with the image
    api.update_with_media(imagePath, text)
    print(text)

    time.sleep(wait)
