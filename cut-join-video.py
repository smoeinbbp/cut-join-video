#!/usr/env python

# Simple script for joining two videos and cutting videos based on start
# and end time

# by Moein Babapour

from subprocess import Popen, PIPE
import time


def cut(vi, st, en, nv):
    print(time.strftime("%H:%M:%S", time.localtime()), "cutting video...")
    p = Popen(['ffmpeg', '-i', vi, '-ss', st, '-t',
               en, '-vcodec', 'copy', '-acodec', 'copy', nv], stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()


def join(vi1, t1, vi2, t2, fv, to):
    print(time.strftime("%H:%M:%S", time.localtime()), "Preparing first Video...")
    p1 = Popen(['ffmpeg', '-i', vi1, '-qscale:v',
                '1', t1], stdout=PIPE, stderr=PIPE)
    stdout1, stderr1 = p1.communicate()

    print(time.strftime("%H:%M:%S", time.localtime()),
          "Preparing second video...")
    p2 = Popen(['ffmpeg', '-i', vi2, '-qscale:v',
                '1', t2], stdout=PIPE, stderr=PIPE)
    stdout2, stderr2 = p2.communicate()

    print(time.strftime("%H:%M:%S", time.localtime()), "Joining videos...")
    conc = 'concat:' + t1 + '|' + t2
    pout = Popen(['ffmpeg', '-i', conc, '-c',
                  'copy', to], stdout=PIPE, stderr=PIPE)
    stdoutout, stderrout = pout.communicate()

    print(time.strftime("%H:%M:%S", time.localtime()),
          "Preparing your new video...")
    pfinal = Popen(['ffmpeg', '-i', to, '-qscale:v', '2',
                    fv], stdout=PIPE, stderr=PIPE)
    stdoutfin, stderrfin = pfinal.communicate()

    print(time.strftime("%H:%M:%S", time.localtime()),
          "removing temporary files...")
    prm = Popen(['rm', '-f', t1, t2, to], stdout=PIPE, stderr=PIPE)
    stdoutrm, stderrrm = prm.communicate()


def main():
    inp = input(
        "CUT or JOIN? \n1 for cutting video \n2 for joining two videos\n\n")

    if (inp == "1"):
        video = input("Enter your video file name. ex: myVideo.mp4\n")

        start = input("Enter start time: hh:mm:ss\n")
        end = input("Enter end time: hh:mm:ss\n")

        newVideo = input("Enter new video file name. ex: myNewVideo.mp4\n")

        cut(video, start, end, newVideo)

        print(time.strftime("%H:%M:%S", time.localtime()), "bye bye...")

    elif (inp == "2"):
        video1 = input(
            "Enter your first video file name. ex: firstVideo.mp4\n")
        tmp1 = video1 + "tmp.mpg"

        video2 = input(
            "Enter your second video file name. ex: secondVideo.mp4\n")
        tmp2 = video2 + "tmp.mpg"

        finalVideo = input("Enter new video file name. ex: myNewVideo.mp4\n")
        tmpout = video1 + video2 + "tmp.mpg"

        join(video1, tmp1, video2, tmp2, finalVideo, tmpout)
        print(time.strftime("%H:%M:%S", time.localtime()), "bye bye...")

    else:
        print("Unknown input\n")
        main()

if __name__ == "__main__":
    main()
