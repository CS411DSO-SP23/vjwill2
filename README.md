# vjwill2

1. Title: Exploring Publications
2. Purpose: This app's purpose is to look more into publications based on keywords. This is for users who would like to find publications based off of their interests and be able to get more information about publications and whether they might be the right fit.
3. Demo:
4. Installation: You can run the application using the command py app.py inside of the project folder.
5. Usage: At the top are two graphs to visualize popular keywords and popular publications. Below is a place where you can search publications by keyword and submit the form. This will give the top publications by the keyword. Similarly, there is a search by publication title, which will give the user all of the keywords associated with that publication. At the bottom, you can edit a publication's name in the format "Prior publication name, new publication name". You can also edit an existing keyword name in the format "PreviousKeywordName,NewKeywordName".
6. Design: There is a main app.py that utilizes dash and other Python imports. There is helper py classes for Neo4j, SQL, and MongoDB.
7. Implementation: I used many different Python imports such as Dash, Pandas, Plotly.express, and GraphDatabase. Of course, HTML, CSS, Bootstrap, and Python were also utilized. I also utilized all of the imports for the different database technologies.
8. Database Techniques: I've implemented view by creating a SQL view that I can query from. I also created prepared statements where I was able to plug in a variable string for quick usage. Lastly, I implemented a stored procedure that retrieves the number of publications quickly.
9. Extra-Credit Capabilities: N/A
10. Contributions: N/A
