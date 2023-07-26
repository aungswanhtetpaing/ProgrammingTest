import os

def count_csv_files(folder_path):
    csv_count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                csv_count += 1
    return csv_count

if __name__ == "__main__":
    folder_path = "gw_test/Question1/Dataset"
    csv_files_count = count_csv_files(folder_path)
    print(f"CSV File Count: {csv_files_count} files")

