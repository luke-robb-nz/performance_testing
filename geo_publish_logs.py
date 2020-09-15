import re
import datetime as dt
import pytimeparse
import os

regex_start = r"START"
regex_end = r"END"
start_list = []
end_list = []

regex_download_start = r"about to download"
regex_download_end = r"files unpacked"
download_start_list = []
download_end_list = []


def get_publish_timings(publish_log_file):
    if os.path.isfile(publish_log_file):
        with open(publish_log_file, 'r') as file:
            for line in file:
                if regex_start:
                    start_list.append(line)
                if regex_download_end:
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

                    print(f"Publish Duration: {duration}\n--------------------------------------------------------------")

    else:
        print(f"File not found, is {publish_log_file} the correct path?\n-----------------------------------------------")


def get_download_timings(download_log_file):
    if os.path.isfile(download_log_file):
        with open(download_log_file, 'r') as file:
            for line in file:
                if regex_download_start:
                    download_start_list.append(line)
                if regex_download_end:
                    download_end_list.append(line)

                r = re.search(regex_download_start, line)
                if r:
                    start = line.split(" ")[1].strip()
                    start = start.split(",")[0].strip()
                    print(f"Download Start:  {start}")
                    download_start = pytimeparse.parse(start)

                r = re.search(regex_download_end, line)
                if r:
                    end = line.split(" ")[1].strip()
                    end = end.split(",")[0].strip()
                    print(f"Download End:  {end}")
                    download_end = pytimeparse.parse(end)

                    duration_seconds = download_end - download_start
                    duration = dt.timedelta(seconds=duration_seconds)

                    print(f"Download Duration: {duration}")
                    break
    else:
        print(f"File not found, is {download_log_file} the correct path?")


if __name__ == "__main__":
    get_publish_timings(r"C:/Users/luke.robb/OneDrive - Seequent/Desktop/geo_publish_logs_here/Maia_Geo_publish_#2.log")
    get_download_timings(r"C:\Users\luke.robb\OneDrive - Seequent\Desktop\geo_download_logs/maia_geo_download.log")

