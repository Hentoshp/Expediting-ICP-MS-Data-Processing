 # Expediting heavy metals ICP-MS testing data transcription using Openpyxl and Pandas
    #### Video Demo:  https://youtu.be/VPX0jhXxzpY
    #### Description:
    Traditional data transcription of heavy metals testing using ICP-MS instrumentation typically uses manual manipulation of excel files to transfer data from its raw state into a more filtered data excel sheet. The issue with manual transcription of data is that it can become very tedious and time consuming to process. Manual transcription is also open to the possibility of user errors in transferring data. In my final project I have written a python script that automates the majority of the manual transcription of this process. I used Pandas and Openpyxl libraries in writing this script. The main function of the script is to take raw data from an excel sheet, filter it, and transcript it into a final excel sheet, while accounting for specific requested metals from mock clients. Below, I will explain in detail the functions defined in this script.


    ##### get_raw_data and get_sample_data
	The functions above use Pandas to first read a data frame of the raw data taken from a mock excel sheet. The mock excel sheet contains many random columns and rows that are not needed in the final cleaned excel sheet. The get_raw_data uses data frame manipulation (.drop) in Pandas to remove most of the unnecessary columns. The data frame is then returned and inputted into get_sample_data, which also uses data frame manipulation to exclude any unnecessary rows. get_raw_data raises a FileNotFoundError if the file path to the raw data excel sheet is not inputted correctly.

    ##### get_requested_metals(excel page)
	Heavy metals testing usually involves a client requesting a sample to be tested for heavy metals. Clients will not always want a result for every metal tested. This function checks the metals requested column of the final excel sheet and creates a dictionary. The key-value pairs of the dictionary are the sample #'s matched with the metals requested by each client. The function takes an argument for the path to the excel file, and uses Openpyxl load_workbook.


    ##### check_metals(sample_key, dict, col_value) and move_data(df, dict, excel page )
	move_data() uses Openpyxl to transfer the filtered data into the final excel sheet by looping over the sample_data data frame and replacing data not requested by the client with "NA" using the check_metals function. The check_metals function creates a list of the allowed metals from the column headers of the final excel sheet (i.e. all of the metals tested) This list is then compared to the values of the requested_metals dictionary (using the row names as the key). Check_metals then returns a logical variable, True or False depending on whether the client sample requested the specific metal. Using a conditional statement, the data point is either kept if True, or replaced with "NA".


#### Conclusion:
	While the script I wrote does furfill the inital requirements I planned, I do hope to add some more functionality to be able to input multiple excel sheets. This would require some editing to the functions above to either loop over each sheet, one at a time, or be able to handle multiple data frames at once. Looping over each sheet may be very slow from a coding perspective, but the data never gets so large that a regular computer would be unable to handle this process.

