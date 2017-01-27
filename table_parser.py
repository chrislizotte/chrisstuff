import csv
no_tables = 4 #total number of tables to be created by the script
print "Number of tables: " + str(no_tables)
table_names = ['department', 'equipment', 'sold_by', 'models', 'makes'] #list of table names to be created
print "Tables to be created: "  + str(table_names)
table_schema = [['id', 'department'], ['id', 'year', 'department_id', 'soldby_id'], ['id', 'model', 'make_id'], ['id', 'make']]#list of lists containing schemata in order corresponding to tables to be created
for i in range (no_tables):
        print "Table " + table_names[i] + " contains the following columns: " + str(table_schema[i])
#create a new file object called f that represents the existing .csv I want to read from
filename = 'U:\\GEOG 465 Winter \'17\\sold_fleet.csv'
f = open(filename)
print "Original file: " + filename
# loop runs as many times as there are tables to be created, with the same origin table each time. A new .csv file will be created and populated according to
# the above list of table names and table schemas
for i in range (0, no_tables - 1):
        my_dreader = csv.DictReader(f, 'r') #create DictReader object to take in rows from original table
        cur_table = open('U:\\465_test_tables\\' + table_names[i] + '.csv', 'w')#create new .csv file to represent the newly created table
        print "Creating table " + str(table_names[i])
        columnnames = table_schema[i] #list of column names 
        my_dwriter = csv.DictWriter(cur_table, fieldnames = columnnames) #DictWriter object to write row captured by DictReader to new table
        my_dwriter.writeheader() #write list of column names to file as headers
        new_dict_list = []#create list that will eventually hold dictionaries, each representing a row that will be written to the table
        j = 1 #counting variable if needed for incremented id values
        value_list = []#this will eventually hold a list of dictionaries, each dictionary representing a row from the original file
        for row in my_dreader:#procedes row by row from original table
                temp_dict = {} #temporary dictionary to hold the key-value pairs for each row
                for k in range (len(table_schema[i])): #need to iterate over each individual list of schemata - which themselves are stored in a list
                        #problem is that in order to properly iterate, I can only grab one key: value pair at a time - each iteration should go down one row and
                        #then across all columns
                        print str(len(table_schema[i]))
                        print str(temp_dict)
                        print str(table_schema[i][k])
                        print row
                        if str(row[str(table_schema)[i][k]]) == 'id':
                                temp_dict['id'] = j
                        else:
                                temp_dict[str(table_schema[i][k])] = row[str(table_schema[i][k])]#pairs column name k with the appropriate value
                value_list.append(temp_dict)
                new_dict_list.append({value_list}) #dictionary of key-value (column-value) pairs
                #use row object from Dict Reader i.e. row['<columnname>']
                j =+ 1 #increment j by 1 to act as a primary key value
        my_dwriter.writerows(new_dict_list) #write list of dictionaries to .csv file
        
