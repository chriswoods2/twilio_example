# twilio_example
This Python application is intended to support parents at school that can't remember the important school dates coming up.

With this application active, your users can simply send a text to your Twilio number and if their phone number is recorded on the school records then it will identify their children, find the year they are in and then immediately text them back with the upcoming dates for their children.

If the number is not registered then a reply will be sent telling them so.

The user can always get details for any school year whether their number is recognised or not, by simply texting "year" followed by the school year(s) they would like to recieve e.g. "Year1" or "year R35".  Capitilisation and spacing after year does not matter.

Installation steps

- Please copy all the files to your working directory.
- Ensure all dependent packages are installed by using the command:
    pip install -r requirements.txt
  IT IS STRONGLY RECOMMENDED THIS IS DONE IN A VIRTUAL ENVIRONMENT
- run the file:
    sms_school_dates.py
- In your Twilio account ensure your Twilio number has been configured so the address of your server (including "/sms" on the end) is entered in Messaging:   A MESSAGE COMES IN    webhook field.
- This file includes sample data in YearDiary.csv and pupils.csv.  Naturally, this will need to be updated with your data, or the code amended to link to your data sources.
