

#README GRAZIOSO SOFTWARE AAC DATABASE 
<br/>
Developed in 2023 for my Client Server Development course (CS340) at Southern New Hampshire University
<br/>
<br/>
**About the Project/Project Title**
<br/>
This application allows a user to access the AAC database, which is a database of animals in the AAC shelter. Users can create, read, update, and delete animals from the database as needed using an intuitive dashboard created with the DASH framework. 
<br/>
<br/>
**Motivation**
<br/>
This program was designed so that users can better manage the animals within their shelter so that all parties get the best possible outcomes possible. I’ve implanted a CRUD method that can be used with an intuitive and user-friendly dashboard to keep track of the data base as the user pleases.
<br/>
<br/>
**Getting Started**
<br/>
To get started, run the mongoimport command in a Linux terminal to import the aac_shelter_outcomes.csv file. 
<br/>
![Picture19](https://github.com/JessicaDuft/Client_Server_Development_CS340/assets/130928718/17847783-70c3-4f80-b643-3c4bccafde85)
<br/>
<br/>
Then run the application using JuPyther, click the dashboard link at the bottom of the page: 
<br/>
<br/>

![Picture20](https://github.com/JessicaDuft/Client_Server_Development_CS340/assets/130928718/8e387fc3-d1b8-4126-81e4-3fa53a019f4a)
<br/>
<br/>
 This brings you to the main dashboard, which is intuitive and user friendly. See more about the dashboard and it’s functionality later in this #README file. 
 <br/>
 <br/>
**Installation**
<br/>
<br/>
You need to have a Linux operating system installed, Python should be downloaded and usable along with some shell such as JuPYter, MongoDB shall be installed in order to access the database. The Python driver for MONGODB, PyMONGO, is also used for this project. PyMongo is a user friendly, easy to use, and intuitive way to access and manipulate databases and collections. The AAC database will need constant manipulation, making PyMongo an excellent tool for meeting the program requirements. Finally all of this is brought together to create a final product using the DASH framework. 
<br/>
<br/>
**Usage**
<br/>
<br/>
 User logs in with authenticated user name and password. The user profile created here, aacuser, has full read/write abilities and can only be used by an authorized user who has proper credentials.Once a user is authenticated, they can access the database and make changes to the database by using the code in the next section of this document or by using the intuitive dashboard documented later on. 
 <br/>
 <br/>
 ![Picture21](https://github.com/JessicaDuft/Client_Server_Development_CS340/assets/130928718/1f432c6e-9873-4cb2-a257-2b69460c7971)
 <br/>
 <br/>
 **Code Example**
 <br/>
The code allows users to create and read data within the database. 
<br/>
An example of the code is the following create method, which allows a user to create new data in the database.
<br/>
If item is successfully create a Boolean value will be returned, otherwise an error will be thrown. 
<br/>
 def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  # data should be dictionary
            if insert!=0:
                return True
            else:
                return False    
        else:
            raise Exception("Nothing to save, because data parameter is empty")

 <br/>
 <br/>
            


**Tests**
<br/>
To test the function above, you would simply call the create method into a class that correlates to the database you are working with. You would then call the read method to view the object that you created or added into your database. 
<br/>
There is a full CRUD program implemented into this database so not only can users create new objects, they can also read , update and delete objects. To do so you would simply call the read, update or delete function followed by the read function to confirm changes. Examples of each are shown in the screenshots below. 
<br/>
<br/>
**Screenshots**
<br/>
		Calls the create and read method
  <br/>
  <br/>
![Picture22](https://github.com/JessicaDuft/Client_Server_Development_CS340/assets/130928718/34dd992f-b007-47db-a3dc-fe073d784b98)
 <br/>
  <br/>

  
Calls the update and read method- Below you can see where the animal_id was successfully changed from TEST123 to TEST_UPDATE_123
<br/>
<br/>


![Picture23](https://github.com/JessicaDuft/Client_Server_Development_CS340/assets/130928718/8a402f7a-6763-4065-8a00-ef9b75827548)

<br/>
<br/>
Here we call the delete function followed by the read function to confirm that our test animal with animal_id TEST_UPDATE_123 is no longer in the database
<br/>
<br/>

![Picture24](https://github.com/JessicaDuft/Client_Server_Development_CS340/assets/130928718/f77409b9-bdbe-4bb7-adb2-6034382421b0)




<br/>
<br/>
**Functionality:**
<br/>
<br/>
In addition to creating and testing the CRUD methods above , I’ve created a dashboard using the DASH framework that meets all of the client’s specified requirements.  The client’s requirements and proof of functionality are listed below : 
<br/>
•	The client wants a company logo displayed on the dashboard with an anchor tag to www.snhu.edu , see also the required unique identifier in the below screen shot. 
<br/>
<br/>


<img width="468" alt="Picture25" src="https://github.com/JessicaDuft/Client_Server_Development_CS340/assets/130928718/2e5f0af8-49c9-41b5-bbaf-970b3215b2d7">
<br/>
<br/>
•	Interactive filter options (buttons, drop-downs) to filter the Austin Animal Center Outcomes data set by: Water Rescue, Mountain or Wilderness Rescue, Disaster Rescue or Individual Tracking, and a RESET filter option. See screenshot below of the selectable filter buttons that appropriately filters the data selected by the user: In this screenshot, I’ve pre-selected the Disaster Rescue or Individual Tracking filter option
<br/>
<br/>


![Picture26](https://github.com/JessicaDuft/Client_Server_Development_CS340/assets/130928718/aeb0e622-9a89-4a0c-984b-667c54090587)
<br/>
<br/>
•	A Data table which dynamically responds to filter options. See the screenshot below of the data table I created which responds to the radio button filter options shown at the top of the chart. The data can be filtered by breed, color, date of birth, and many other options. In the screenshot below, I have the data from above filtered by color in the screenshot below: 
<br/>
<br/>

![Picture27](https://github.com/JessicaDuft/Client_Server_Development_CS340/assets/130928718/198fccfc-92ff-49be-bcab-6ed096a9cd98)
<br/>
<br/>

•	A geolocation graph that shows the filtered data. In the screenshot below I’ve selected Zeke, one of the Disaster or Individual Tracking dog from the screenshot above. The geolocation chart shows the user where Zeke is currently located using latitude and longitude values entered by the user upon creation of the animal in the database. 
<br/>
<br/>



![Picture28](https://github.com/JessicaDuft/Client_Server_Development_CS340/assets/130928718/cad74af7-896f-4c16-87b0-00c5ca3f6c29)
<br/>
<br/>
•	A second chart, of the developer’s choice, which displays filtered data. I chose to use a histogram graph. The graph will display the data that is currently shown in the data table. Using the same data from above, the Disaster or Individual Tracking filter option, see how the histogram sorts the 4 dogs from our chosen filter by breed:
<br/>
<br/>

![Picture29](https://github.com/JessicaDuft/Client_Server_Development_CS340/assets/130928718/c4faabb6-c4a7-4580-8379-7b72676c6f0b)
<br/>
<br/>
**Challenges:**
<br/>
When creating this dashboard, my first challenge was finding the appropriate port numbers. Port numbers can be notoriously difficult, but after troubleshooting the issue I was finally able to find the correct port number so that the DASH application would actually run. My next challenge was that PLOTLY was not installed in my lab environment. After some minor research I was able to get PLOTLY installed so that my data table, charts, and graphs would load appropriate data. My final challenges were mostly just minor syntax errors, and moving things around so that they looked good on the dashboard. These challenges are expected when developing any program or application. 
<br/>
<br/>


Contact
<br/>
Jessica Duft – jessica_duft@yahoo.com






















<br/>
<br/>
Reflection on my time in Client Server Development -CS340

•	How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
<br/>
 Writing programs that are maintainable, readable, and adaptable is extremely important in development so as code can easily be understood and subsequently appropriately replicated. In order to do this, I create code that has inline comments explaining functionality of the code, clear and easy to read variable names and functions, and I ensure that my functions can easily be modified to use with other programs or databases if necessary. Creating the CRUD method in project one in a clear and re-usable way was so beneficial when implementing the same functions in my dashboard. I didn’t have to rewrite any create, read, update, delete methods. I simply imported my already written python file and called the pre-written functions in my new file. 

 <br/>
 <br/>
 
•	How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
<br/>
The problems with my dashboard were mostly technical issues : things like finding the correct port number, ensuring proper extensions were downloaded in my environment, etc.. all of which required technical troubleshooting. As far as my actual code goes, I had to edit my read functions in the CRUD file to include a read_all function so that all of the data could be pulled from the database instead of just some data. After that my main issues were just with placement on dashboard. Trial and error with moving things around until I was visually satisfied with the dashboard is what worked best for me. As for a computer scientist, I think that solving problems comes down to frequent debugging, trial and error, and lots and lots of testing. I would use these same strategies in the future. 
<br/>
<br/>

•	What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
<br/>
Computer scientists automate previous manual requirements. Where there was once a pencil and paper process, computer scientists are able to step in and automate the process by creating an intuitive, easy to use, and accurate program that allows an authorized user to complete the task much more efficiently. For a company like Grazioso Salvare, this program will allow the company to operate in a more efficient and accurate manner saving the company time and resources on a daily basis. 
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

[View my Eportfolio here](https://github.com/JessicaDuft/EPortfolio)

