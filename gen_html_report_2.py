def generate_html_report(data):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Report</title>
        <style>
            table {
                font-family: Arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h2>Report</h2>
        <table>
            <tr>
                <th>Part</th>
                <th>Serial No</th>
                <th>Test Result</th>
            </tr>
    """

    for item in data:
        html_content += "<tr>"
        for field, value in item.items():
            html_content += f"<td>{value}</td>"
        html_content += "</tr>"

    html_content += """
        </table>
    </body>
    </html>
    """

    return html_content

def read_input_file(filename):
    data = []
    with open(filename, 'r') as file:
        entry = {}
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                field, value = parts
                entry[field.strip()] = value.strip()
            elif len(parts) == 1:
                # Assume it's the start of a new entry
                data.append(entry)
                entry = {}
        if entry:  # Append the last entry if it exists
            data.append(entry)
    return data

def main():
    input_filename = 'input.txt'
    output_filename = 'report.html'

    data = read_input_file(input_filename)
    html_content = generate_html_report(data)

    with open(output_filename, 'w') as file:
        file.write(html_content)

    print(f"HTML report generated successfully: {output_filename}")

if __name__ == "__main__":
    main()
