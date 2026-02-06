import argparse
import sys
from data_loader import load_data
from reports import AverageGDPReport
from display import print_report

def main():
    parser = argparse.ArgumentParser(description='GDP data analysis')
    parser.add_argument('--files', nargs='+', required=True)
    parser.add_argument('--report', required=True)

    args = parser.parse_args()

    report_registry = {
        'average-gdp': AverageGDPReport(),
    }

    if args.report not in report_registry:
        print(f"Error: Report '{args.report}' not found")
        sys.exit(1)

    try:
        data = load_data(args.files)
        report_logic = report_registry[args.report]
        report_data = report_logic.generate(data)
        print_report(report_data, args.report)
    except Exception as e:
        print(f" An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()