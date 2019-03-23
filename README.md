# twilio_example
This Python application is intended to support parents at school that can't remember the key dates coming up.

With this application active, simply send a text to your twilio number and if your phone number is recorded on the school records then it will identify your children, find the year they are in and then immediately text you back the upcoming dates for your children.

If your number is not known then you will get a message back telling you so.

You can always get details for any school year whether your number is recognised or not.  Simply text year followed by the school year(s) you would like to recieve e.g. "Year1" or "year R35".

Installation.

- Please copy all the files to your working directory.
- Ensure all dependent packages are installed by using the command: pip install -r requirements.txt  IT IS STRONGLY RECOMMENDED THIS IS DONE IN A VIRTUAL ENVIRONMENT
- run the sms_school_dates.py file
- In your Twilio account ensure your Twilio phone number has been configured so the web address of your server (including "/sms" on the end) is entered into Messaging: A MESSAGE COMES IN webhook field.

- This file includes sample data in YearDiary.csv and pupils.csv.  Naturally this will need to be updated with your data, or the code amended to link to your data sources.
