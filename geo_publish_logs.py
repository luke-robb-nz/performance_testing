import re
import datetime as dt
import pytimeparse
import os

# log_file = r"C:/Users/luke.robb/OneDrive - Seequent/Desktop/geo_publish_logs_here/Maia_Geo_publish_#2.log"
regex_start = r"START"
regex_end = r"END"
start_list = []
end_list = []


def get_publish_timeings(Publish_log_file):
    if os.path.isfile(Publish_log_file):
        with open(Publish_log_file, 'r') as file:
            for line in file:
                if regex_start:
                    start_list.append(line)
                if regex_end:
                    end_list.append(line)

                r = re.search(regex_start, line)
                if r:
                    start = line.split(" ")[1].strip()
                    start = start.split(",")[0].strip()
                    print("Publish Start: ", start)
                    publish_start = pytimeparse.parse(start)

                r = re.search(regex_end, line)
                if r:
                    end = line.split(" ")[1].strip()
                    end = end.split(",")[0].strip()
                    print("Publish End: ", end)
                    publish_end = pytimeparse.parse(end)

                    duration_seconds = publish_end - publish_start
                    duration = dt.timedelta(seconds=duration_seconds)

                    print("Publish Duration:", duration)
                    break
    else:
        print(f"File not found, is {Publish_log_file} the correct path")


def get_download_timeings():
    pass


if __name__ == "__main__":
    get_publish_timeings(r"C:/Users/luke.robb/OneDrive - Seequent/Desktop/geo_publish_logs_here/Maia_Geo_publish_#2.log")
