import glob
import os


def rename(folder, pattern):
    """
    Function: rename
    Summary: replaces all gaps in file names with underscores, for files matching passed pattern inside specific folder
    Examples: 'old file name' -> 'old_file_name'
    :param folder:
    :param pattern:
    """

    for pathAndFilename in glob.iglob(os.path.join(folder, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        new_s = title.replace(" ", "_")
        os.rename(pathAndFilename, os.path.join(folder, new_s + ext))


if __name__ == "__main__":
    rename("path_to_folder", "*.*")
