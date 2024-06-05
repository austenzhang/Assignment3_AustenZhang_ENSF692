# school_data.py
# Austen Zhang
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022


def get_user_input(school_names_and_codes, selection):
    '''
    Returns the school code with passed in dictionary of school codes and names, as well as the user input.

    Parameters:
        school_names_and_codes: dictionary with school codes as keys, and school names as values.
        selection: The high school name or school code inputted by the user.

    Returns:
        int: The school code

    Raises:
        ValueError: if user input does not match any of the school codes or school names in school_names_and_codes dictionary.
    '''
    try:
        for code in school_names_and_codes.keys():
            if(code == int(selection)):
                return code
    except ValueError:
        pass

    for code, name in school_names_and_codes.items():
        if(selection == name):
            return code
    raise ValueError("Not a valid school name or school code. Please try again.")


def get_average_enrollment(enrollment_array, school_index, grade_index):
    '''
    Returns the average enrollment for a particular grade from a selected school over years 2013-2022. It ignores NaNs by using nanmean.

    Parameters:
        enrollment_array: The array containing enrollment information for 20 schools from 2013 to 2022.
        school_index: row index of the selected school in the enrollment_array.
        grade_index: the column index of the array which specifies grade of the enrollment data. Column index 0 is grade 10, index 1 is grade 11, and index 2 is grade 12.

    Returns:
        int: average enrollment for the particular grade over years 2013 to 2022.
    '''
    grade_enrollment = enrollment_array[:, school_index, grade_index] # get row of selected school by taking row of total enrollment data corresponding to school_index. Then index 0 is set for the column to indicate 10th grade. Then use np.nanmean to computer average, ignoring nans.
    average_enrollment = int(np.nanmean(grade_enrollment))
    return average_enrollment

def main():
    
    print("ENSF 692 School Enrollment Statistics")

    #enrollment_array created by creating an array of 2D arrays. 2D arrays are created using np.array and reshaping the imported data to 20 rows and 3 columns.
    enrollment_array = np.array(
        [np.array(year_2013).reshape(20,3),
        np.array(year_2014).reshape(20,3),
        np.array(year_2015).reshape(20,3),
        np.array(year_2016).reshape(20,3),
        np.array(year_2017).reshape(20,3),
        np.array(year_2018).reshape(20,3),
        np.array(year_2019).reshape(20,3),
        np.array(year_2020).reshape(20,3),
        np.array(year_2021).reshape(20,3),
        np.array(year_2022).reshape(20,3)])
    
    # printing 3D array properties using ndim and shape functions from numpy.
    print("Array has", enrollment_array.ndim, "dimensions.\nArray Shape:", enrollment_array.shape)

    #creating dictionary of school names and codes.
    school_names_and_codes = {1224:'Centennial High School',
                              1679:'Robert Thirsk School',
                              9626:'Louise Dean School',
                              9806:'Queen Elizabeth High School',
                              9813:'Forest Lawn High School',
                              9815:'Crescent Heights High School',
                              9816:'Western Canada High School',
                              9823:'Central Memorial High School',
                              9825:'James Fowler High School',
                              9826:'Ernest Manning High School',
                              9829:'William Aberhart High School',
                              9830:'National Sport School',
                              9836:'Henry Wise Wood High School',
                              9847:'Bowness High School',
                              9850:'Lord Beaverbrook High School',
                              9856:'Jack James High School',
                              9857:'Sir Winston Churchill High School',
                              9858:'Dr. E. P. Scarlett High School',
                              9860:'John G Diefenbaker High School',
                              9865:'Lester B. Pearson High School'}

    while True:
        try:
            selection = input("Please enter the high school name or school code: ")
            school_code = get_user_input(school_names_and_codes, selection)
        except ValueError as e:
            print(e)
            continue
        else:
            break

    #now that we have the school code, determine row index from school code
    school_index = [code for code in school_names_and_codes.keys()].index(school_code)

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    school_name = school_names_and_codes[school_code]
    print(f"School name: {school_name}\nSchool code: {school_code}")

    # using get_average_enrollment function to determine average grade 10 enrollment in selected school
    print(f"Average Grade 10 Enrollment: {get_average_enrollment(enrollment_array, school_index, 0)}")
    # using get_average_enrollment function to determine average grade 11 enrollment in selected school
    print(f"Average Grade 11 Enrollment: {get_average_enrollment(enrollment_array, school_index, 1)}")
    # using get_average_enrollment function to determine average grade 12 enrollment in selected school
    print(f"Average Grade 12 Enrollment: {get_average_enrollment(enrollment_array, school_index, 2)}")

    school_enrollment = enrollment_array[:, school_index, :] # obtaining all enrollment data regarding school.
    highest_enrollment = int(np.nanmax(school_enrollment)) # calculating highest enrollment by finding max of school_enrollment, ignoring nans with nanmax.
    print(f"Highest enrollment for a single grade for entire time period: {highest_enrollment}")
    lowest_enrollment = int(np.nanmin(school_enrollment)) # calculating lowest enrollment by finding min of school_enrollment, ignoring nans with nanmin.
    print(f"Lowest enrollment for a single grade for entire time period: {lowest_enrollment}")

    total_enrollment = 0 #initializing total enrollment sum, which will be added to in the below for loop
    no_of_years = 0
    for i in range(school_enrollment.shape[0]): # i indicates the year. school_enrollment.shape[0] indicates the row of this 2D array, which corresponds to the year. The [0] index is because the shape function returns a tuple, with the first value being the number of rows in the array.
        year_enrollment = int(np.nansum(school_enrollment[i,:])) #calculating enrollment of all grades for each year, then printing the number. Casting is used to have the result be integers because nansum and sum functions return floats.
        year = 2013 + i
        no_of_years += 1
        total_enrollment += year_enrollment #each loop adds to the total enrollment number. Once loop completes, it should have the total enrollment for the school across all 10 years.
        print(f"Total Enrollment in {year} was: {year_enrollment}")
    print(f"Total ten year enrollment: {total_enrollment}")

    # using nanmean to calculate average to ensure NaNs are not included in average calculation.
    yearly_enrollment_array = [gr_10 + gr_11 + gr_12 for gr_10, gr_11, gr_12 in school_enrollment]
    mean_yearly_enrollment = int(np.nanmean(yearly_enrollment_array))
    print(f"Mean total yearly enrollment over 10 years: {mean_yearly_enrollment}")

    # using school enrollment array which is the slice of the 3d array corresponding to all enrollment of the selected school.
    # using np.any to determine if any data is over 500. If not, print out No enrollments message. If so, using the np.nanmedian function to find median of all data greater than 500. The array of data greater than 500 is a 1D array obtained using masks.
    if np.any(school_enrollment > 500):
        median = int(np.nanmedian(school_enrollment[school_enrollment > 500])) #result will be floored to an integer.
        print(f"Median enrollments for all instances of enrollments greater than 500: {median}")
    else:
        print("No enrollments over 500")


    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    # taking slice of 3d array corresponding to 2013. Then averaging the data with np.nanmean to avoid nans.
    enrollment_2013 = enrollment_array[0,:,:]
    print(f"Mean enrollment in 2013 was {int(np.nanmean(enrollment_2013))}")
    # taking slice of 3d array corresponding to 2022. Then averaging the data with np.nanmean to avoid nans.
    enrollment_2022 = enrollment_array[9,:,:]
    print(f"Mean enrollment in 2022 was {int(np.nanmean(enrollment_2022))}")

    # To find sum of 2022 class, will find np.max of the slice of the enrollment array that corresponds to 2022 ('sheet' of index 9 of 3d array), and the column that corresponds with grade 12 (column of index 2). Every school should be included so all rows are included.
    graduating_class = enrollment_array[9,:,2]
    print(f"Total graduating class of 2022 across all schools was {int(np.nansum(graduating_class))}")

    # printing out highest enrollment by finding max of entire enrollment array
    print(f"Highest enrollment for a single grade within the entire time period (across all schools) was {int(np.nanmax(enrollment_array))}")
    # printing out lowest enrollment by finding min of entire enrollment array
    print(f"Lowest enrollment for a single grade within the entire time period (across all schools) was {int(np.nanmin(enrollment_array))}")


if __name__ == '__main__':
    main()

