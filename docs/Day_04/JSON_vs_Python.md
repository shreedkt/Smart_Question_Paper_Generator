**What is JSON?**
JSON stand for javaScript Object Notation.   
**Why do we use JSON?**
JSON is simple text used for storing the data and sending the data.
**What is a Key?**
Key is unique name which is used for identifying the data item. In JSON the key must be string and in double quote. 
{
    "name"= "deepak",
    "age"= 26,
    "isfaculty"= true
}
"name", "age", "isfaculty" all are the key 
**What is a Value?**
The actual data which is assigned to key example 
{
    "name"= "deepak",
    "age"= 26,
    "isfaculty"= true
}
"deepak", 26, true all are the value 
**Why is pathlib better than writing "config/settings.json" directly?**
because pathlib detect the Operating system automatically. It also lets join folder with /(forward slace) in mac or linux  in window \(backward slace) and give built in tools to to check if file exist, read date and delete items. one of the major advantage is that it remove the dependency of same computer like where I have create the project we may also run on other devices.  
pathlib creates operating-system-independent paths, making the application portable across Windows, Linux, and macOS.
**What does json.load() return?**
json.load() basically reads data from json file and convert it into the corresponding python object. 