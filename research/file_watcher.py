import argparse
import os
import fnmatch
import sys
from os.path import join
import shutil
import multiprocessing


def move_matching_criteria_files(criteria, watch_list,sleep_time,dest):
    if os.path.exists(dest):
        while criteria:
            for directory in watch_list:
                if os.path.exists(directory):
                    result= []
                    for item in criteria:
                        file_list =  fnmatch.filter(os.listdir(directory), item)


                        if len(file_list)> 0:
                            result.append(item)
                            for file in file_list:
                                try:
                                    shutil.move(join(directory,file), join(dest, file))
                                    print(f"Moving {join(directory,file)} to {join(dest, file)}")
                                except PermissionError:
                                    SystemExit(1)
                    for item in result:
                        criteria.remove(item)
            if len(criteria) != 0:
                time.sleep(sleep_time)


if __name__ == '__main__':
    time = 7200
    sleep_time= 60
    parser = argparse.ArgumentParser(description="Move file to destination with given filename and given directories to watch")
    parser.add_argument('-c','--criteria',help='Filename to search',required=True)
    parser.add_argument('-w', '--watch', help='Directories to watch', required=True)
    parser.add_argument('-t', '--time', help='Time to watch(seconds)', required=False)
    parser.add_argument('-s','--sleep',help='Sleep or suspend time',required=False)
    parser.add_argument('-d', '--dest', help='Destination directory', required=True)
    args = parser.parse_args()
    print("criteria: %s" % args.criteria)
    print("Directories to watch: %s" % args.watch)
    print("Time to watch(seconds): %s" % args.time)
    print("Sleep or suspend time: %s" % args.sleep)
    print("Destination directory: %s" % args.dest)
    criteria = args.criteria
    criteria = criteria.split(" ")
    watch_list = args.watch
    watch_list = watch_list.split(" ")
    dest = args.dest
    if args.time:
        time = int(args.time)
    if args.sleep:
        sleep_time = int(args.sleep)

    p = multiprocessing.Process(target=move_matching_criteria_files, args=(criteria,watch_list,sleep_time,dest))
    p.start()
    # wait for 7200 seconds or until the process finishes
    p.join(time)

    # If thread is still active
    if p.is_alive():
        print("Process is still running.. killing it now")
        # Terminate
        p.terminate()
        p.join()
        sys.exit(1)