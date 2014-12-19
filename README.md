Lyrics
======

A-Z lyrics Scraping

This is a simple Python script that retreives songs given an artist, gets the lyrics given those songs, and stores the lyrics into
a pickle file. A-Z makes it really easy to grab lyrics, but it's also fairly easy to get banned--hence why my code
includes a place for proxies.

I also included the analysis file, which takes the pickle files and analyzes things like top words, unique words, and 
total words. The end of the file converts the data into a Pandas DataFrame and plots it using ggplot.  

I wrote this code for this blog post:

https://brianchesley.wordpress.com/2014/12/12/largest-vocabulary-in-rock/

