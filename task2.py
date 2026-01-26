import os
import sys
import shutil

def backup_file(source_file, backup_dir):
    """Creates backup with .backup suffix and logs operation"""
    if not os.path.isfile(source_file):
        print(f"❌ Error: '{source_file}' does not exist")
        return False
    
    if not os.path.isdir(backup_dir):
        print(f"❌ Error: '{backup_dir}' is not a directory")
        return False
    
    filename = os.path.basename(source_file)
    backup_file = os.path.join(backup_dir, f"{filename}.backup")
    
    shutil.copy2(source_file, backup_file)
    
    user_id = os.getuid()
    full_path = os.path.abspath(backup_file)
    with open("backup.log", "a") as f:
        f.write(f"Backup created: {user_id}, {full_path}\n")
    
    print(f"✅ Backup created: {backup_file}")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 task2.py <source_file> <backup_dir>")
        sys.exit(1)
    
    backup_file(sys.argv[1], sys.argv[2])

