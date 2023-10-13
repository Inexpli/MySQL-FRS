import os
import shutil
from tkinter import filedialog, messagebox
import tkinter as tk
import sys

def ask_path():
    new_path = filedialog.askdirectory(title="Select MySQL directory")
    return os.path.normpath(new_path) if new_path else None

def main():
    root = tk.Tk()
    root.withdraw()

    new_path = ask_path()
    if new_path:
        PATH = new_path
    else:
        messagebox.showerror("Error", "Directory hasn't been provided")
        sys.exit()

    data_folder = os.path.join(PATH, "data")
    new_data_folder = data_folder + "_old"
    backup_folder = os.path.join(PATH, "backup")

    if os.path.exists(new_data_folder):
        shutil.rmtree(new_data_folder)

    shutil.copytree(data_folder, new_data_folder)

    os.walk(data_folder)

    folders_to_delete = ['mysql', 'performance_schema', 'phpmyadmin', 'test']

    for folder_name in folders_to_delete:
        folder_path = os.path.join(data_folder, folder_name)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)

    file_to_ignore = "ibdata1"
    for root, dirs, files in os.walk(data_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name != file_to_ignore:
                os.remove(file_path)

    for root, dirs, files in os.walk(backup_folder):
        for dir_name in dirs:
            src_dir = os.path.join(root, dir_name)
            dest_dir = os.path.join(data_folder, os.path.relpath(src_dir, backup_folder))
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

        for file_name in files:
            src_file = os.path.join(root, file_name)
            dest_file = os.path.join(data_folder, os.path.relpath(src_file, backup_folder))
            if file_name != file_to_ignore:
                shutil.copy2(src_file, dest_file)

    messagebox.showinfo("Operation done", "Your database has been repaired")
    sys.exit()

if __name__ == "__main__":
    main()