from flask import Flask, request, redirect
import pandas as pd
from twilio.twiml.messaging_response import MessagingResponse
#     Message,
#     Body
# )

calendar = pd.read_csv("YearDiary.csv", dtype=str)
pupil_list = pd.read_csv("pupils.csv", dtype=str)
school_years = ["R", "1", "2", "3", "4", "5", "6"]

app =Flask(__name__)

@app.route("/sms", methods=['POST'])
def search():
    """This function reads the inbound SMS message and determines how it should be routed"""
    
    #Get information from the inbound SMS
    inbound_num = request.form['From']
    inbound_message = request.form['Body']

    # if the text message starts with "year" then send the years requested.
    if inbound_message.lower()[0:4]=="year":
    	year_list=[]
    	for char in school_years:
    		if char in inbound_message.upper()[4:]:
    			year_list.append(char.upper())
    	# if there are years included in the message send themm, if not continue to phone number lookup
    	if len(year_list)>0:
    		year_list = pd.DataFrame(year_list, columns=["Year"])
    		return send_dates(year_list)

    # if message does not start with year, look up the phone number and send the years the parents children are in
    pupil_match = pupil_list[pupil_list["PhoneNumber"]==inbound_num][["Year", "Parent_Name"]]
    if len(pupil_match) == 0:
        return send_phone_number_not_found()
    else:
        parent_name = pupil_match["Parent_Name"].iloc[0] # Parent name taken from first record that matches phone number
        year_list = pd.DataFrame(pupil_match["Year"].unique(),columns=["Year"]).sort_values("Year") # unique years

        return send_dates(year_list, parent_name)


def send_phone_number_not_found():
    """Message to send if the text message did not start "year" and includes a year group(s)
    and the phonenumber the message was sent from is not on the pupil records""" 

    response = MessagingResponse()
    response.message("Your phone number is not known.  Please text Year follwed by the school year you need e.g. Year 1 or Year R 5 6")
    return str(response)

def send_dates(year_list, parent_name=""):
    """Message to send if the number is matched to pupil records
     or the messsage started with "year" and includes a year group(s)
    year_list: must be a dataframe object containg the year values.
    parent_name: (optional) must be a string containing the parents name if known."""

    response = MessagingResponse()
    #create a a dataframe with the events for the years included in year_list
    result = pd.merge(year_list, calendar, on = 'Year')
    
    #Tailor SMS reply opening depending on if a parent name is known.
    if parent_name == "":
    	output = "The school calendar dates requested are:\n"
    else:
    	output = f"Dear {parent_name},\nThe school calendar dates for your children are:\n"

    #Add the contents of the dataframe to the message
    for event in result.index:
        output += "Year "
        for info in result.columns:
            output +=f"{result[info].loc[event]}, "
        output +="\n"
    output += "For any other year please text Year followed by the school year you need e.g. Year 1 or Year R 5 6"
    response.message(output)
    return str(response)

if __name__ == '__main__':

    app.run(debug=True)