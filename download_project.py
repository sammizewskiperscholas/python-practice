# Program to automate to clear my downloads folder

import os
from pprint import pprint
import collections

video_extension = ['mp4','mpg', 'mpeg', 'avi', 'mov', 'flv', 'mwv', 'm4v', 'mkv', 'h264']
audio_extension = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
image_extension = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'tif', 'tiff' ]
document_extension = ['txt','pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx','html', 'odt', 'tex', 'ppt', 'pptx', 'log']
compression_extension = ['zip', 'z', 'tar', '7z', 'rar', 'gz', 'bz', 'rpm', 'pkg', 'deb']
install_extension = ['dmg', 'exe', 'iso']

# step 1 - (Optional) Create directories where we want to store the files
base_path = os.path.expanduser("~")
print(base_path)
dest_dirs = ['video_folder', 'audio_folder', 'image_folder', 'document_folder', 'compression_folder', 'other_folder']

for d in dest_dirs:
    dir_path = os.path.join(base_path, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
       
download_path = os.path.join(base_path, 'Downloads')
files_mapping = collections.defaultdict(list)
files_list = os.listdir(download_path)

# Step 2 - Map files from Downloads folder based on their file extension
for filename in files_list:
    if filename != '.':
        file_ext = filename.split('.')[-1]
        files_mapping[file_ext].append(filename)

pprint(files_mapping)

# Step 3 - Move all files given a file extension to a target directory
for f_ext, f_list in files_mapping.items():
    if f_ext in video_extension:
        for file in f_list:
            os.rename(os.path.join(download_path, file), os.path.join(base_path, 'video_folder', file))
    if f_ext in audio_extension:
        for file in f_list:
             os.rename(os.path.join(download_path, file), os.path(base_path, 'audio_folder', file))
    elif f_ext in image_extension:
        for file in f_list:
            os.rename(os.path.join(download_path, file), os.path(base_path, 'image_folder', file))
    elif f_ext in document_extension:
        for file in f_list:
            os.rename(os.path.join(download_path, file), os.path(base_path, 'document_folder', file))
    elif f_ext in compression_extension:
        for file in f_list:
            os.rename(os.path.join(download_path, file), os.path(base_path, 'compression_folder', file))
    elif f_ext in install_extension:
        for file in f_list:
            os.rename(os.path.join(download_path, file), os.path(base_path, 'installation_folder', file))
    else:
        for file in f_list:
            os.rename(os.path.join(download_path, file), os.path.join(base_path, 'other_folder', file))   
