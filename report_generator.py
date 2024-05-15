def write_content(argument, file):
    print("argument: " +argument)
    input_string_lower = argument.lower()
    # file = open(r'D:\services-workspace\python-scripts\git\html_generator\ACC_Reports copy.html', "w")

    if "report" in input_string_lower:
        file.writelines("<h1 style='color: red;text-align: center;background: lightgrey; border-bottom: 2px solid black;border-radius: 8px;'> {} </h1>" .format(argument))

    if "pass" in input_string_lower:
        file.writelines("<h2 style='color:black;background: green'>{}</h2>".format(argument))
    elif "fail" in input_string_lower:
        file.writelines("<h2 style='color:black;background: red'>{}</h2>".format(argument))
    else:
        file.writelines("<h2 style='color:black;background: lightgrey'> {} </h2>".format(argument))

    print(f"HTML report generated successfully: {file}")
    return file
