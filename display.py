from tabulate import tabulate

def print_report(data, report_name):
    headers = ['country', 'gdp']
    print(f"\nReport: {report_name.replace('-', ' ').title()}")
    print(tabulate(data, headers=headers, tablefmt="grid", floatfmt=".2f", showindex=range(1, len(data) + 1)))