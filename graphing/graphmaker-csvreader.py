import numpy as np
import matplotlib
import csv
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def parsecsvdata():
    summary = []
    with open("/home/student/mycode/graphing/2018summary.csv", "r") as downtime:
            downdata = csv.reader(downtime, delimiter=",")
            for row in downdata:
                rowdat = (row[0], row[1], row[2], row[3])
                summary.append(rowdat)
    return summary

def main():
    N = 4
    summary = parsecsvdata()
    localnetMeans = summary[0]
    wanMeans = summary[1]
    ind = np.arange(N)
    width = 0.35

    p1 = plt.bar(ind, localnetMeans, width)
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    plt.savefig("/home/student/mycode/graphing/2018summary.png")

if __name__ == "__main__":
    main()
