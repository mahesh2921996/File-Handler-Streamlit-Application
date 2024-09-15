import streamlit as st
import shutil
import os
import glob
import time

# Function to handle file actions
def handle_file_action(src_path, dst_path, action, file_exts):

    # Validation of source and destination path
    if not os.path.exists(src_path):
        st.error(f"Source path '{src_path}' does not exist.")
        return

    if not os.path.isdir(dst_path):
        st.error(f"Destination path '{dst_path}' is not a valid directory.")
        return
    
    # Collect all file extensions by their respective categories.
    exist_file_exts_dic = {}
    for file_ext in file_exts:

        if file_ext == 'CSV':
            exist_file_exts_dic[file_ext] = ['*.csv']
        elif file_ext == 'Excel':
            exist_file_exts_dic[file_ext] = ['*.xlx', '*.xlsx']
        elif file_ext == 'Text':
            exist_file_exts_dic[file_ext] = ['*.txt']
        elif file_ext == 'Image':
            exist_file_exts_dic[file_ext] = ['*.gif', '*.jpg' , '*.jpeg' , '*.jfif' , '*.pjpeg' , '*.pjp', '*.png', '*.svg']
        elif file_ext == 'Audio':
            exist_file_exts_dic[file_ext] = ['*.mp3', '*.wav', '*.flac', '*.aac', '*.ogg', '*.m4a', '*.wma', '*.alac', '*.aiff', '*.opus']
        elif file_ext == 'Video':
            exist_file_exts_dic[file_ext] = ['*.mp4', '*.avi', '*.mov', '*.mkv', '*.wmv', '*.flv', '*.webm', '*.mpeg', '*.mpg', '*.3gp', '*.ogv']
        elif file_ext == 'PDF':
            exist_file_exts_dic[file_ext] = ['*.pdf', '*.pdfa', '*.pdfx']
        else:
            st.error("Unsupported file extension.")
            return
    
    # List to store the found files
    found_files_dic = {}

    # Iterate through each pattern
    for file_type, file_exts in exist_file_exts_dic.items():

        found_file_list = []
        for file_ext in file_exts:

            # Create a search pattern that includes subdirectories
            search_pattern = os.path.join(src_path, '**', file_ext)
            
            # Use glob to find all matching files (recursive search)
            files = glob.glob(search_pattern, recursive=True)

            found_file_list.extend(files)
            
        if len(found_file_list) == 0:
            continue

        # Add the found files to the list
        found_files_dic[file_type] = found_file_list

    # Check files 
    for file_list in list(found_files_dic.values()):
        if len(file_list)>0:
            break
    else:
        st.warning("No files found in the source path.")
        return
    
    print("found_files_dic", found_files_dic)

    for key, value in found_files_dic.items():
        dst_folder = os.path.join(dst_path, f"{key}_Files")

        # Create folders based on file types.
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)

        for file in value:
            file_name = os.path.basename(file)
            dst_file = os.path.join(dst_folder, file_name)

            try:
                if action == 'Copy':
                    shutil.copy(file, dst_file)

                elif action == 'Move':
                    shutil.move(file, dst_file)

            except Exception as e:
                st.error(f"An error occurred: {e}")

        # Inform the user when the task is complete.
        if action == 'Copy':
            st.success(f"{key}'s files copied successfully.")
        elif action == 'Move':
            st.success(f"{key}'s files moved successfully.")

    time.sleep(2)

    reset_state()

    st.experimental_rerun()  # Rerun the app to reflect changes immediately
        
# # Streamlit UI
# st.title('File Extracter')

# # Input fields
# src_path = st.text_input('File Path', '')
# dst_path = st.text_input('Output Path', '')

# # Action selection
# action = st.selectbox('Choose Action', ['Copy', 'Move'])

# # File extension selection (multiple selection)
# file_exts = st.multiselect('Select File Extensions', ['Text', 'PDF', 'Image', 'Audio', 'Video', 'CSV', 'Excel'])

# # Submit button
# if st.button('Submit'):
#     handle_file_action(src_path, dst_path, action, file_exts)

# Define a function to reset the state
def reset_state():
    st.session_state['src_path'] = ''
    st.session_state['dst_path'] = ''
    st.session_state['action'] = 'Copy'
    st.session_state['file_exts'] = []

# Initialize session state values if not already set
if 'src_path' not in st.session_state:
    st.session_state['src_path'] = ''
if 'dst_path' not in st.session_state:
    st.session_state['dst_path'] = ''
if 'action' not in st.session_state:
    st.session_state['action'] = 'Copy'
if 'file_exts' not in st.session_state:
    st.session_state['file_exts'] = []

# Set page configuration
st.set_page_config(
    page_title="File Handler",
    page_icon="📁",  # File folder emoji
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Streamlit UI
st.title('File Handler Application')
st.write('Manage and organize your files efficiently.')

# Input fields
src_path = st.text_input('File Path', value=st.session_state['src_path'])
dst_path = st.text_input('Output Path', value=st.session_state['dst_path'])

# Action selection
action = st.selectbox('Choose Action', ['Copy', 'Move'], index=['Copy', 'Move'].index(st.session_state['action']))

# File extension selection (multiple selection)
file_exts = st.multiselect('Select File Extensions', ['Text', 'PDF', 'Image', 'Audio', 'Video', 'CSV', 'Excel'], default=st.session_state['file_exts'])

# Save inputs to session state
st.session_state['src_path'] = src_path
st.session_state['dst_path'] = dst_path
st.session_state['action'] = action
st.session_state['file_exts'] = file_exts

# Create a row with two columns
col1, _, col2 = st.columns(3)

with col1:
    if st.button('Submit'):
        handle_file_action(src_path, dst_path, action, file_exts)

with col2:
    if st.button('Reset'):
        reset_state()
        st.experimental_rerun()  # Rerun the app to reflect changes immediately
        