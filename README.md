# mazona

File py_to_postgresql_amazon_data.py is useful for adding and removing tables to a PostGreSQL database.

This function began with a desire to monitor prices and reviews on Amazon. Python was the choice language, as all of my scrapers had been written with it (using Python2.7), and PostGreSQL seemed like a worthwhile database to explore (which turned out to be great).  The default values for table creation came out of determining the most informative data that items listed in the Amazon marketplace contained.

This is a useful way of inserting data into your PostGreSQL database using a method that can be closely tied to your webscraper.  Oh right, I should post the webscraper!
