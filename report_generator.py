report_title = "Report: ACC TEST REPORT"
file_path=r'C:\Python_Course\Pycharm\Pycharm\Script\Py_Canoe_auto\pythonProject1\Reports\report.html'

def write_content(argument):

    flag = check_report_title()
    input_string_lower = argument.lower()

    with open(file_path, "a") as file:
     
        if flag == False:
            file.write("<h1 style='color: red;text-align: center;background: lightgrey; border-bottom: 2px solid black;border-radius: 8px;'> {} </h1>" .format(report_title))
            flag = True

        if "test case" in input_string_lower:
            file.write("<h2 style='color:black;background: yellow'> {} </h2>".format(argument))

        elif "pass" in input_string_lower:
            file.write("<h3 style='color:black;background: green'>{}</h3>".format(argument))

        elif "fail" in input_string_lower:
            file.write("<h3 style='color:black;background: red'>{}</h3>".format(argument))

        else:
            file.write("<h3 style='color:black;background: lightgrey'> {} </h3>".format(argument))

    return file

def check_report_title():
    with open(file_path, "r") as file:
        for line in file:
            if "<h1" in line and report_title in line:
                return True   
            break                                                     
    return False
