import os
import time
import logging

# Configure logging
logging.basicConfig(
    filename='cleanup_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def cleanup_old_files(directory, days_threshold, dry_run=True):
    """
    Deletes files older than a given threshold (in days) inside the directory.
    If dry_run=True, only previews deletions without removing files.
    Logs actions into cleanup_log.txt
    """
    seconds_threshold = days_threshold * 24 * 60 * 60
    current_time = time.time()
    deleted_files_count = 0

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_mod_time = os.path.getmtime(file_path)
            file_age = current_time - file_mod_time

            if file_age > seconds_threshold:
                if dry_run:
                    print(f"[DRY RUN] Would delete: {file_path}")
                    logging.info(f"[DRY RUN] Would delete: {file_path}")
                else:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    logging.info(f"Deleted: {file_path}")
                deleted_files_count += 1

    return deleted_files_count

if __name__ == "__main__":
    directory_to_cleanup = "./test_directory"   # Directory to clean
    days_to_keep = 30                           # Threshold in days
    dry_run_mode = True                         # Change to False to actually delete

    deleted_count = cleanup_old_files(directory_to_cleanup, days_to_keep, dry_run=dry_run_mode)
    if dry_run_mode:
        print(f"[DRY RUN] Total files that would be deleted: {deleted_count}")
    else:
        print(f"Total files deleted: {deleted_count}")
