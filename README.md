# [TweeStat]
![Result for Iphone 6](https://camo.githubusercontent.com/ccbfc174e5ac3f1b218e709841a992e93b7e5c5a/687474703a2f2f74776565737461742e61752d7379642e6d79626c75656d69782e6e65742f7374617469632f646f6e616c647472756d702e706e67)

An Analytical view of Tweets for deducing public opinion on any trending topic

##Youtube promo video link
[![ScreenShot](https://i9.ytimg.com/vi/uFOC2bvIPYg/mqdefault.jpg?sqp=CNzPrd0F&rs=AOn4CLCgMyihvwv6DY6cduGtrv5v9eUEag&time=1537960142369)](https://www.youtube.com/watch?v=rTM2HZAULik)
## How to Run the app locally

1. Download and extract the code
2. cd into the app directory
3. Run `python server.py`
4. Access the running app in a browser at http://localhost:8000

#What is Tweetstat:

Tweestat originates from the name Tweets Statistics or Stats. This is a web app which aims to provide E commerce companies information on what people think about them, their products and services.
                   Here we extract tweets based on demography, time-durationn, favorite or retweet count. We find similar hashtags trending on the days and then after processing it we apply IBM Watson Alchemy API to dig inside the actual sentiment of the person writing the tweet. 
              So, you just have to go to [TweeStat] and enter the product/service of your interest. Tweestat will do all the analysis and will give the stats of public opinion on that query!
            
[TweeStat]:http://tweestat.au-syd.mybluemix.net/
#Where does data come from? What is inside the system?
Tweestat deals with real-time data from Twitter, and get results of public opinion with the help of [Alchemy API from IBM] Watson. Tweestat = Twitter (source of data) + Stat (statistics)

[Alchemy API from IBM]:http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/alchemy-language.html
#What kind of searches can be made:
Basically all kinds of sentences are perfect candidate for analysis by [Alchemy API] which is currently limited to English, French and few other languages. Currently we are using only English tweets further we are planning to integrate Google translator to increase the spectrum of tweets specially for the countries like India.
[Alchemy API]:http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/alchemy-language.html

#Why is it unique and who would use it when solved? 
From big companies to a general user anyone can use Tweestat for their work. This is the first such kind of attempt in this area which not only focuses on providing cognitive sentiment analysis to corporate but to general public as well.

#Privacy: 
In the whole course of developing Tweestat we have not used profile based research. All the works have been done anonymously. We even don't store profile details with tweets for further development. 
