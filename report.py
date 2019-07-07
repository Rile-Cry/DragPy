# Module Title: Report
# Created By: Rile_Cry
# Created On: 24 June 2019
# Description: This module is focused on creating a report from the
# DragPy's simulation. All results from the simulation, if allowed, are
# recreated in file form as a report.

# Main Class


class Report:
    '''
    Class: Report
    Params:
        filename: [str] A name for the file that will contain the report
        rep_type: [str] Type of report {'report', 'log'}
    Functions:
        None
    '''

    # Class Setup

    def __init__(self, filename: str='report.txt',
                 rep_type: str='report') -> None:
        # Set the class variables
        self.rep_type = rep_type
        self.filename = filename
        self.data = ''

    # Utility Functions

    def convert(self, data) -> str:
        '''
        Function: convert
        Params:
            data: [any] The data to be converted to string
        Description:
            convert takes in data and checks if the data isn't already a
            a string. If it is, then the data is converted to a string,
            else the data is just returned as itself.
        '''

        # Check if the data is a string at all and returns the string
        # version of the data.
        if type(data) != str:
            return str(data)
        return data

    def setData(self, data) -> None:
        '''
        Function: setData
        Params:
            data: [any] The data to be set to the instance
        Description:
            setData takes in a set of data and places it within the instance.
        '''

        # Set instance's data variable to the new data
        self.data = data

    def report(self) -> None:
        '''
        Function: report
        Params:
            None
        Description:
            report utilizes the instance's variables to determine the report
            type and the file name, along with what data to write.
        '''

        # Create a variable to hold the final reported data.
        reported_data = ''

        # Checks what type of data is currently being utilized
        if type(self.data) in [tuple, dict, list]:
            if self.rep_type == 'log':
                if type(self.data) == dict:
                    for key in self.data.keys():
                        string = key + ': ' + self.convert(self.data[key])
                        reported_data += string + '\n'
                else:
                    for item in self.data:
                        reported_data += self.convert(item) + '\n'
            else:
                if type(self.data) == dict:
                    data = list(self.data.items())[len(self.data) - 1]
                    reported_data = self.convert(data)
                else:
                    reported_data = self.convert(self.data[len(self.data) - 1])
        else:
            reported_data = self.convert(self.data)

        # Generate the report
        with open(self.filename, 'w') as file:
            file.write(reported_data)


# Test

if __name__ == '__main__':
    # Create an instance of the class
    rep = Report()

    # Set some arbitrary data
    rep.setData({'data': [1, 2, 3, 4, 5], 'creator': 'Rile_Cry'})

    # Generate the report
    rep.report()

    # Recreate the instance
    rep = Report(filename='log.txt', rep_type='log')

    # Using the same arbitrary data
    rep.setData({'data': [1, 2, 3, 4, 5], 'creator': 'Rile_Cry'})

    # Generate the new data
    rep.report()