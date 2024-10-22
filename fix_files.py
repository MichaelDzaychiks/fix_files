import os

def rename_images_sequentially(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.png')]

    files.sort()

    for index, file_name in enumerate(files, start=1):
        new_file_name = f"{index}.png"
        new_file_path = os.path.join(directory, new_file_name)

        current_file_path = os.path.join(directory, file_name)

        os.rename(current_file_path, new_file_path)

    print("Renaming completed!")

anime_directory = 'data/Anime'
cartoon_directory = 'data/Cartoon'

rename_images_sequentially(anime_directory)
rename_images_sequentially(cartoon_directory)
