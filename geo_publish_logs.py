import re
import datetime as dt
import pytimeparse

log_file = r"C:/Users/luke.robb/OneDrive - Seequent/Desktop/geo_publish_logs_here/Maia_Geo_publish_#2.log"
regex_start = r"START"
regex_end = r"END"
start_list = []
end_list = []


def read_log(log_file):
    with open(log_file, 'r') as file:
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
                pstart = pytimeparse.parse(start)

            r = re.search(regex_end, line)
            if r:
                end = line.split(" ")[1].strip()
                end = end.split(",")[0].strip()
                print("Publish End: ", end)
                pend = pytimeparse.parse(end)

                duration_seconds = pend - pstart
                duration = dt.timedelta(seconds=duration_seconds)

                print("Publish Duration:", duration)








read_log(log_file)



