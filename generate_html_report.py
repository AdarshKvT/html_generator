def generate_html_report(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    fields = [line.strip() for line in lines]

    html = """
    <html>
    <body>
    <h1>HTML Report</h1>
    <table border="1">
    <tr>
    <th>Field</th>
    <th>Value</th>
    </tr>
    """

    for i, field in enumerate(fields, start=1):
        html += f"""
        <tr>
        <td>Field {i}</td>
        <td>{field}</td>
        </tr>
        """

    html += """
    </table>
    </body>
    </html>
    """

    with open(output_file, 'w') as f:
        f.write(html)

generate_html_report('input.txt', 'output.html')