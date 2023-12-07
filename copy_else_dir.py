import shutil


def create_folder(source_folder, destination_folder, folder_name):
    try:
        shutil.copytree(source_folder, destination_folder + folder_name)
        print(f"{folder_name} created")
    except Exception as e:
        print(f"An error occurred in creating the : {e}")
