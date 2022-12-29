import os
from pprint import pprint
import collections
video_extension=['mp4','mpg','mpeg','avi','mov','flv','mwv','mkv','m4v','h264']
audio_extension=['mp3','wav','raw','wma','mid','midi']
image_extension=['png','jpg','jpeg','gif','svg','bmp','psd','tif','tiff']
document_extension=['txt','pdf','csv','xls','xlsx','ods','doc','docx','html','odt','tex','ppt','pptx','log']
compression_extension=['zip','z','tar','7z','gz','bz','rar','rpm','pkg','deb']
install_extension=['dmg','exe','iso']

base_path=os.path.expanduser('~')
dest_dirs=['Video_folder','Audio_folder','Image_folder','Document_folder','Compression_folder','Other_folder']
for d in dest_dirs:
    dir_path=os.path.join(base_path,d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

download_path=os.path.join(base_path,"Downloads")
files_mapping=collections.defaultdict(list)
file_list=os.listdir(download_path)


for filename in file_list:
    if filename != '.':
        file_ext=filename.split('.')[-1]
        files_mapping[file_ext].append(filename)
pprint(files_mapping)

for f_ext,f_list in files_mapping.items():
   if f_ext in video_extension:
        for file in f_list:
            os.rename(os.path.join(download_path,file),os.path.join(base_path,'Video_folder',file))
   elif f_ext in audio_extension:
        for file in f_list:
            os.rename(os.path.join(download_path,file),os.path.join(base_path,'Audio_folder',file))
   elif f_ext in image_extension:
        for file in f_list:
            os.rename(os.path.join(download_path,file),os.path.join(base_path,'Image_folder',file))
   elif f_ext in document_extension:
        for file in f_list:
            os.rename(os.path.join(download_path,file),os.path.join(base_path,"Document_folder",file))
   elif f_ext in compression_extension:
        for file in f_list:
            os.rename(os.path.join(download_path,file),os.path.join(base_path,"Compression_folder",file))
   elif f_ext in install_extension:
        for file in f_list:
            os.rename(os.path.join(download_path,file),os.path.join(base_path,"Installation_folder",file))
   else:
        for file in f_list:
            os.rename(os.path.join(download_path,file),os.path.join(base_path,"Other_Folder",file))
    






