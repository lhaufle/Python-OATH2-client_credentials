# Python-OATH2-client_credentials
api.pi: includes a class called TD_API, which takes the client_id, secret_id, and base url in the constructor. 
These values are used to submit for authorization and retrieve the token for later reqeusts. 
  There is a method called create_report that allows for the report_type, start_date, end_date and name to be passed as parameters. These 
values are used either to build the url or to added to the body of the post request. Once the job is completed, a message is printed to the
console and the job_id is stored.
  The last method to use--at this time--is called get_report, and this doesn't take any aurguments but uses some of the value stored from the prior methods. 
 The job type and job_id are used to build the url, and the token is used in the header to pass into the request. One the report request is made, it is not 
 instantly finished, so a while loop is used to check the status. If it is not completed then it will sleep for 3 second to prevent sending too many requests
 to the server, and then it will check it again. One the report shows finished, the json response will be returned
 
 
 
 ---future feature and changes coming
 1) Error handling is yet to be added
 2) Another class called normal.py will be created using pandas, to grabe the data values to clean the data and
    and write the data to a spreadsheet
 3) A logging feature will be added that will write to a seperate file whenever an exception/error takes place. 
