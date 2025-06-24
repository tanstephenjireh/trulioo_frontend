# streamlit_frontend_only.py
"""
Frontend-only version of Trulioo Contract Extractor
Clean UI code with dummy data imported from separate file
"""

import pandas as pd
import streamlit as st
import time
from datetime import datetime

# Import all dummy data functions
from dummy_data import (
    create_dummy_contract_data,
    create_dummy_subscription_data, 
    create_dummy_line_item_data,
    create_dummy_consumption_schedule,
    create_dummy_consumption_rate,
    dummy_google_folders,
    dummy_pdf_files,
    create_dummy_extraction_results,
    main_pipeline_dummy,
    to_excel_dummy
)

# Streamlit page configuration
st.set_page_config(
    page_title="Trulioo Contract Extractor",
    page_icon="🛠️",
    initial_sidebar_state="auto"
)


def show_auth_page():
    """Display the authentication page with dummy authentication"""
    
    st.title("🔐 Login to Trulioo Contract Extractor")
    st.caption("Please Login to access the Contract extraction tool")
    
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.subheader("Login")
        with st.form("login_form"):
            username = st.text_input("Email")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login", use_container_width=True)
            
            if login_button:
                if username and password:
                    # Allow any username and password for frontend testing
                    with st.spinner("Logging in..."):
                        time.sleep(0)  # Simulate login delay
                    st.success("Login successful!")
                    # Set session state for demo
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Please enter both username and password")
    
    with tab2:
        st.subheader("Register New Account")
        with st.form("register_form"):
            reg_email = st.text_input("Email", key="reg_email")
            reg_password = st.text_input("Password", type="password", key="reg_password")
            reg_password_confirm = st.text_input("Confirm Password", type="password", key="reg_password_confirm")
            register_button = st.form_submit_button("Register", use_container_width=True)
            
            if register_button:
                if reg_email and reg_password and reg_password_confirm:
                    # Allow any email for frontend testing - no domain restrictions
                    if reg_password == reg_password_confirm:
                        if len(reg_password) >= 8:
                            with st.spinner("Creating account..."):
                                time.sleep(2)  # Simulate registration
                            st.success("Registration successful! Please check your email for verification.")
                            st.session_state.pending_confirmation = reg_email
                        else:
                            st.error("Password must be at least 8 characters long")
                    else:
                        st.error("Passwords do not match")
                else:
                    st.error("Please fill in all fields")
        
        # Email verification section
        if 'pending_confirmation' in st.session_state:
            st.subheader("📧 Email Verification")
            st.info(f"Please check your email and enter the verification code below.")
            with st.form("confirm_form"):
                confirmation_code = st.text_input("Enter verification code from your email")
                confirm_button = st.form_submit_button("Verify Email", use_container_width=True)
                
                if confirm_button:
                    if confirmation_code:
                        with st.spinner("Verifying email..."):
                            time.sleep(2)
                        # Dummy verification - accept any 6-digit code
                        if len(confirmation_code) == 6 and confirmation_code.isdigit():
                            st.success("Email verified successfully!")
                            del st.session_state.pending_confirmation
                            st.info("You can now login with your credentials!")
                        else:
                            st.error("Please enter a valid 6-digit verification code")
                    else:
                        st.error("Please enter the verification code")


def show_google_drive_tab():
    """Display Google Drive multiple extraction interface"""
    
    st.title("🛠️ Trulioo Contract Extractor - Google Drive")
    st.caption("Extract from multiple PDFs stored in Google Drive")

    # Initialize Google Drive session state
    if 'google_authenticated' not in st.session_state:
        st.session_state.google_authenticated = False
    if 'google_selected_folder' not in st.session_state:
        st.session_state.google_selected_folder = None
    if 'google_extraction_results' not in st.session_state:
        st.session_state.google_extraction_results = []
    
    # Sub tabs for Google Drive functionality
    google_tab1, google_tab2, google_tab3 = st.tabs(["🔐 Connect Google Drive", "📁 Select Folder", "📄 Extract Contracts"])
    
    with google_tab1:
        st.subheader("Step 1: Connect to Google Drive")
        
        if not st.session_state.google_authenticated:
            st.info("To access your Google Drive files, you need to authenticate first.")
            
            st.markdown("""
            **Please follow these steps:**
            1. Click the button below to authorize the application
            2. You'll be redirected back automatically after authorization
            """)
            
            # Dummy Google OAuth button
            if st.button("🔗 Connect to Google Drive", type="primary"):
                with st.spinner("Connecting to Google Drive..."):
                    time.sleep(3)  # Simulate connection
                st.session_state.google_authenticated = True
                st.success("Successfully connected to Google Drive!")
                st.rerun()
            
        else:
            st.success("✅ Successfully connected to Google Drive!")
            if st.button("🔄 Disconnect Google Drive"):
                st.session_state.google_authenticated = False
                st.session_state.google_selected_folder = None
                st.session_state.google_extraction_results = []
                st.rerun()
    
    with google_tab2:
        st.subheader("Step 2: Select PDF Folder")
        
        if not st.session_state.google_authenticated:
            st.warning("Please connect to Google Drive first.")
        else:
            st.info("Select the folder containing your PDF files for extraction.")
            
            # Use dummy folders
            folders = dummy_google_folders()
            folder_names = [folder['name'] for folder in folders]
            
            selected_folder_name = st.selectbox(
                "Choose a folder:",
                options=["Select a folder..."] + folder_names,
                key="google_folder_select"
            )
            
            if selected_folder_name != "Select a folder...":
                selected_folder = next(f for f in folders if f['name'] == selected_folder_name)
                st.session_state.google_selected_folder = selected_folder
                
                # Show folder info and PDF count with dummy data
                pdfs = dummy_pdf_files()
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Selected Folder", selected_folder_name)
                with col2:
                    st.metric("PDF Files Found", len(pdfs))
                
                st.markdown("**PDF Files in folder:**")
                pdf_df = pd.DataFrame([
                    {
                        "Name": pdf['name'],
                        "Size": f"{int(pdf.get('size', 0)) / 1024:.1f} KB",
                        "Modified": pdf.get('modifiedTime', 'Unknown')[:10]
                    }
                    for pdf in pdfs
                ])
                st.dataframe(pdf_df, use_container_width=True)
    
    with google_tab3:
        st.subheader("Step 3: Extract Contract Information")
        
        if not st.session_state.google_authenticated:
            st.warning("Please connect to Google Drive first.")
        elif not st.session_state.google_selected_folder:
            st.warning("Please select a folder first.")
        else:
            folder = st.session_state.google_selected_folder
            pdfs = dummy_pdf_files()
            
            st.info(f"Ready to extract from {len(pdfs)} PDF files in '{folder['name']}'")
            
            col1, col2 = st.columns([2, 1])
            with col1:
                if st.button("🚀 Start Google Drive Extraction", type="primary", use_container_width=True):
                    # Create progress bar
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    extraction_results = create_dummy_extraction_results()
                    
                    # Simulate processing each file
                    for i, pdf in enumerate(pdfs[:3]):  # Only process first 3 for demo
                        status_text.text(f"Processing: {pdf['name']} ({i+1}/{len(pdfs)})")
                        time.sleep(1)  # Simulate processing time
                        
                        # Update progress
                        progress_bar.progress((i + 1) / len(pdfs))
                    
                    st.session_state.google_extraction_results = extraction_results
                    status_text.text("Extraction completed!")
                    st.success(f"Successfully extracted information from {len(extraction_results)} files!")
            
            with col2:
                if st.session_state.google_extraction_results:
                    # Download results as CSV
                    df = pd.DataFrame(st.session_state.google_extraction_results)
                    csv = df.to_csv(index=False)
                    
                    st.download_button(
                        label="📥 Download Results (CSV)",
                        data=csv,
                        file_name=f"google_drive_extraction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
            
            # Display results
            if st.session_state.google_extraction_results:
                st.markdown("### Extraction Results")
                
                results_df = pd.DataFrame(st.session_state.google_extraction_results)
                st.dataframe(results_df, use_container_width=True)
                
                # Summary statistics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Files Processed", len(st.session_state.google_extraction_results))
                with col2:
                    st.metric("Successful Extractions", len(st.session_state.google_extraction_results))
                with col3:
                    st.metric("Average Text Length", "1,250 chars")


def show_single_extraction_tab():
    """Display single file extraction interface"""
    
    st.title("🛠️ Trulioo Contract Extractor")
    st.caption("Easily extract person match details from a single order form")

    # File upload
    uploaded_file = st.file_uploader(
        "Upload an order form",
        accept_multiple_files=False, 
        type=['pdf'],
        help="Upload your order form in pdf format"
    )

    if uploaded_file is not None:
        
        # Process button
        if st.button("🔄 Extract", type="primary", use_container_width=True):
            try:
                # Create progress bar and status text
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                def update_progress(progress_value, status_message):
                    """Callback function to update progress bar and status"""
                    progress_bar.progress(progress_value)
                    status_text.text(status_message)
                
                # Use the dummy main pipeline with progress callback
                response = main_pipeline_dummy(
                    uploaded_file, 
                    "dummy_endpoint", 
                    "dummy_token",
                    progress_callback=update_progress
                )
                
                # Clear the status text after completion
                status_text.empty()
                progress_bar.empty()
                
                # Process the response
                res = response['output_records']
                
                # Arrange dataframes
                df_contract = pd.DataFrame(res[0]["data"])
                df_subscription = pd.DataFrame(res[1]["data"])
                df_lineitemsource = pd.DataFrame(res[2]["data"])
                df_subconsumptionschedule = pd.DataFrame(res[3]["data"])
                df_subconsumptionrate = pd.DataFrame(res[4]["data"])
                df_lisconsmptionschedule = pd.DataFrame(res[5]["data"])
                df_lisconsumptionrate = pd.DataFrame(res[6]["data"])

                # Create Excel file
                df_xlsx = to_excel_dummy(
                    df_contract=df_contract, 
                    df_subscription=df_subscription,
                    df_lineitemsource=df_lineitemsource,
                    df_subconsumptionschedule=df_subconsumptionschedule,
                    df_subconsumptionrate=df_subconsumptionrate,
                    df_lisconsmptionschedule=df_lisconsmptionschedule,
                    df_lisconsumptionrate=df_lisconsumptionrate
                )

                st.success("✅ Extraction completed successfully!")
                
                # Show preview of data
                with st.expander("📊 Preview Excel File", expanded=True):
                    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
                        "📋 Contract Data", 
                        "📊 Subscription Data",
                        "📄 Line Item Source",
                        "📅 Sub Consumption Schedule", 
                        "💰 Sub Consumption Rate",
                        "📋 LIS Consumption Schedule",
                        "💸 LIS Consumption Rate"
                    ])
                    
                    with tab1:
                        st.dataframe(df_contract, use_container_width=True, height=400)
                    
                    with tab2:
                        st.dataframe(df_subscription, use_container_width=True, height=400)      

                    with tab3:
                        st.dataframe(df_lineitemsource, use_container_width=True, height=400) 

                    with tab4:
                        st.dataframe(df_subconsumptionschedule, use_container_width=True, height=400) 

                    with tab5:
                        st.dataframe(df_subconsumptionrate, use_container_width=True, height=400) 

                    with tab6:
                        st.dataframe(df_lisconsmptionschedule, use_container_width=True, height=400) 

                    with tab7:
                        st.dataframe(df_lisconsumptionrate, use_container_width=True, height=400) 

                # Download button
                st.download_button(
                    label='📥 Download Result',
                    data=df_xlsx,
                    file_name='Legacy_Data_Line_Items.xlsx',
                    use_container_width=True
                )

            except Exception as e:
                st.error(f"❌ Error processing response: {str(e)}")


def main_app():
    """Main application interface"""

    # Sidebar with user info and logout
    with st.sidebar:
        username_display = st.session_state.username.split('@')[0] if st.session_state.username else "User"
        st.write(f"👤 **Welcome, {username_display}!**")

        if st.button("🚪 Logout", use_container_width=True):
            # Clear session state
            for key in ['authenticated', 'username', 'google_authenticated', 'google_selected_folder', 'google_extraction_results']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    # Create tabs for Multiple and Single Extraction
    tab1, tab2 = st.tabs(["Multiple Extraction", "Single Extraction"])

    with tab1:
        show_google_drive_tab()

    with tab2:
        show_single_extraction_tab()


def main():
    """Main function that handles authentication flow"""
    # Initialize session state
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
        
    # Check if user is authenticated
    if st.session_state.authenticated:
        main_app()
    else:
        show_auth_page()


if __name__ == "__main__":
    main()