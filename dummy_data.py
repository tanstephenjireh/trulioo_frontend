# dummy_data.py
"""
Dummy data functions for frontend testing
Contains all test data generators for the Trulioo Contract Extractor
"""

import pandas as pd
import time
from io import BytesIO


def create_dummy_contract_data():
    """Create dummy contract data for frontend testing"""
    return pd.DataFrame({
        'Contract ID': ['CNT-001', 'CNT-002', 'CNT-003'],
        'Client Name': ['ABC Corporation', 'XYZ Industries Ltd', 'Global Tech Solutions'],
        'Contract Value': [50000, 75000, 120000],
        'Start Date': ['2024-01-01', '2024-02-01', '2024-03-01'],
        'End Date': ['2024-12-31', '2025-01-31', '2025-02-28'],
        'Status': ['Active', 'Active', 'Pending'],
        'Contract Type': ['Service Agreement', 'Licensing Deal', 'Partnership Agreement']
    })


def create_dummy_subscription_data():
    """Create dummy subscription data for frontend testing"""
    return pd.DataFrame({
        'Subscription ID': ['SUB-001', 'SUB-002', 'SUB-003'],
        'Service Type': ['Premium Identity Verification', 'Standard Background Check', 'Enhanced Due Diligence'],
        'Monthly Fee': [299.99, 199.99, 449.99],
        'Status': ['Active', 'Active', 'Trial'],
        'Start Date': ['2024-01-15', '2024-02-01', '2024-03-10'],
        'Billing Cycle': ['Monthly', 'Quarterly', 'Annual']
    })


def create_dummy_line_item_data():
    """Create dummy line item data"""
    return pd.DataFrame({
        'Line Item ID': ['LI-001', 'LI-002', 'LI-003', 'LI-004'],
        'Description': ['Identity Verification - Basic', 'Background Check - Standard', 'Document Verification', 'AML Screening'],
        'Quantity': [100, 50, 75, 25],
        'Unit Price': [2.99, 5.99, 3.49, 8.99],
        'Total Amount': [299.00, 299.50, 261.75, 224.75],
        'Category': ['Verification', 'Screening', 'Document', 'Compliance']
    })


def create_dummy_consumption_schedule():
    """Create dummy consumption schedule data"""
    return pd.DataFrame({
        'Schedule ID': ['SCH-001', 'SCH-002', 'SCH-003'],
        'Period': ['Q1 2024', 'Q2 2024', 'Q3 2024'],
        'Allocated Units': [1000, 1200, 1500],
        'Used Units': [850, 900, 1100],
        'Remaining Units': [150, 300, 400],
        'Usage Percentage': ['85%', '75%', '73%']
    })


def create_dummy_consumption_rate():
    """Create dummy consumption rate data"""
    return pd.DataFrame({
        'Rate ID': ['RT-001', 'RT-002', 'RT-003', 'RT-004'],
        'Service': ['Basic Verification', 'Enhanced Check', 'Document Scan', 'Real-time Monitoring'],
        'Rate per Unit': [1.99, 3.99, 2.49, 5.99],
        'Tier': ['Standard', 'Premium', 'Standard', 'Enterprise'],
        'Min Volume': [100, 500, 200, 1000],
        'Max Volume': [999, 1999, 999, 9999]
    })


def dummy_google_folders():
    """Return dummy Google Drive folders"""
    return [
        {
            'id': 'folder_001',
            'name': 'Contracts 2024',
            'parents': ['root']
        },
        {
            'id': 'folder_002', 
            'name': 'Legal Documents',
            'parents': ['root']
        },
        {
            'id': 'folder_003',
            'name': 'Client Files - Q1',
            'parents': ['root']
        },
        {
            'id': 'folder_004',
            'name': 'Service Agreements',
            'parents': ['root']
        }
    ]


def dummy_pdf_files():
    """Return dummy PDF files"""
    return [
        {
            'id': 'pdf_001',
            'name': 'Contract_ABC_Corporation.pdf',
            'size': '2048000',
            'modifiedTime': '2024-01-15T10:30:00Z'
        },
        {
            'id': 'pdf_002',
            'name': 'Agreement_XYZ_Industries.pdf',
            'size': '1536000',
            'modifiedTime': '2024-01-20T14:45:00Z'
        },
        {
            'id': 'pdf_003',
            'name': 'Service_Contract_GlobalTech.pdf',
            'size': '3072000',
            'modifiedTime': '2024-02-01T09:15:00Z'
        },
        {
            'id': 'pdf_004',
            'name': 'Partnership_Agreement_TechCorp.pdf',
            'size': '2560000',
            'modifiedTime': '2024-02-10T16:20:00Z'
        },
        {
            'id': 'pdf_005',
            'name': 'Licensing_Deal_InnovateAI.pdf',
            'size': '1792000',
            'modifiedTime': '2024-02-15T11:10:00Z'
        }
    ]


def create_dummy_extraction_results():
    """Create dummy Google Drive extraction results"""
    return [
        {
            'filename': 'Contract_ABC_Corporation.pdf',
            'contract_date': '2024-01-15',
            'party_1': 'ABC Corporation',
            'party_2': 'Trulioo Inc.',
            'contract_value': '$50,000',
            'contract_type': 'Service Agreement',
            'status': 'Active'
        },
        {
            'filename': 'Agreement_XYZ_Industries.pdf',
            'contract_date': '2024-01-20',
            'party_1': 'XYZ Industries Ltd',
            'party_2': 'Trulioo Inc.',
            'contract_value': '$75,000',
            'contract_type': 'Licensing Deal',
            'status': 'Active'
        },
        {
            'filename': 'Service_Contract_GlobalTech.pdf',
            'contract_date': '2024-02-01',
            'party_1': 'Global Tech Solutions',
            'party_2': 'Trulioo Inc.',
            'contract_value': '$120,000',
            'contract_type': 'Partnership Agreement',
            'status': 'Pending'
        }
    ]


def main_pipeline_dummy(pdf_path, url, jwt_token, progress_callback=None):
    """
    Dummy version of main_pipeline with progress callbacks
    Simulates the real pipeline with realistic progress updates
    """
    # 1. Reading the Order Form
    if progress_callback:
        progress_callback(0.1, "📄 Reading PDF file...")
    time.sleep(0.5)  # Simulate processing time
    
    if progress_callback:
        progress_callback(0.5, "✍️ PDF content extracted successfully")
    time.sleep(0.5)
    
    # 2. Extracting Order Form Details
    if progress_callback:
        progress_callback(0.6, "🔍 Analyzing document content...")
    time.sleep(0.8)
    
    if progress_callback:
        progress_callback(0.8, "⚙️ Processing contract details...")
    time.sleep(0.7)
    
    if progress_callback:
        progress_callback(1.0, "✅ Extraction completed!")
    time.sleep(0.3)
    
    # Return dummy response structure matching the real API response
    return {
        'output_records': [
            {"data": create_dummy_contract_data().to_dict('records')},
            {"data": create_dummy_subscription_data().to_dict('records')},
            {"data": create_dummy_line_item_data().to_dict('records')},
            {"data": create_dummy_consumption_schedule().to_dict('records')},
            {"data": create_dummy_consumption_rate().to_dict('records')},
            {"data": create_dummy_consumption_schedule().to_dict('records')},  # LIS schedule
            {"data": create_dummy_consumption_rate().to_dict('records')}       # LIS rate
        ]
    }


def to_excel_dummy(df_contract, df_subscription, df_lineitemsource, 
                   df_subconsumptionschedule, df_subconsumptionrate, 
                   df_lisconsmptionschedule, df_lisconsumptionrate):
    """
    Convert dataframes to Excel file - dummy version
    Creates a functional Excel file with all the required sheets
    """
    output = BytesIO()
    
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        # Write each dataframe to its respective sheet
        df_contract.to_excel(writer, index=False, sheet_name='Contract')
        df_subscription.to_excel(writer, index=False, sheet_name='Subscription')
        df_lineitemsource.to_excel(writer, index=False, sheet_name='LineItemSource')
        df_subconsumptionschedule.to_excel(writer, index=False, sheet_name='subConsumptionSchedule')
        df_subconsumptionrate.to_excel(writer, index=False, sheet_name='subConsumptionRate')
        df_lisconsmptionschedule.to_excel(writer, index=False, sheet_name='lisConsmptionSchedule')
        df_lisconsumptionrate.to_excel(writer, index=False, sheet_name='lisConsumptionRate')
        
        # Optional: Format the sheets (you can expand this for better styling)
        workbook = writer.book
        currency_format = workbook.add_format({'num_format': '$#,##0.00'})
        
        # Apply formatting to relevant columns if needed
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            worksheet.set_column('A:Z', 15)  # Set default column width
    
    return output.getvalue()


# Configuration constants for frontend testing
DUMMY_ALLOWED_DOMAINS = ["any-domain.com"]  # Not used anymore, but kept for reference
DUMMY_USER_CREDENTIALS = {
    "any_username": "any_password"  # Frontend accepts any credentials
}