import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt


def read_data(file_path):
    try:
        # Read the CSV file into a pandas DataFrame
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Function to generate a simple analysis (summary statistics)
def generate_analysis(data):
    summary = data.describe()  # Basic statistics for numerical columns
    return summary

# Function to create the PDF report
def create_pdf_report(file_path, data, summary):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, 'Automated Data Report', ln=True, align='C')
    
    # Add introduction text
    pdf.ln(10)  # Line break
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, 'This report contains an analysis of the data from the given file.')

    # Add data preview
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Data Preview (First 5 Rows):', ln=True)
    
    pdf.set_font('Arial', '', 10)
    for i, row in data.head().iterrows():
        pdf.cell(0, 10, str(row.to_list()), ln=True)

    # Add summary statistics
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Summary Statistics:', ln=True)
    
    pdf.set_font('Arial', '', 10)
    for column in summary.columns:
        pdf.cell(0, 10, f'{column}: {summary[column].to_dict()}', ln=True)
    
    # Save the PDF
    pdf.output(file_path)
    print(f"Report successfully saved to {file_path}")

# Function to generate a plot and save it as an image
def generate_plot(data, plot_file_path):
    plt.figure(figsize=(8, 6))
    data['column_name'].plot(kind='hist', bins=30, color='blue', alpha=0.7)
    plt.title('Histogram of Column')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(plot_file_path)
    plt.close()

# Main function
def main():
    # File paths
    data_file = 'data.csv'  # Input data file (CSV format)
    report_pdf = 'report.pdf'  # Output PDF report file
    plot_image = 'plot.png'  # Plot image file

    # Read data from file
    data = read_data(data_file)
    if data is not None:
        # Generate summary statistics
        summary = generate_analysis(data)

        # Generate plot (for example: histogram of a specific column)
        generate_plot(data, plot_image)

        # Create the PDF report
        create_pdf_report(report_pdf, data, summary)

if __name__ == "__main__":
    main()
