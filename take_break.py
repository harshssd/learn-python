import time
import webbrowser

total_breaks = 3
breaks_count = 0
break_time = 2 * 60 * 60
print("Take break starting at: " + time.ctime())
while(breaks_count < total_breaks):
    time.sleep(break_time)
    webbrowser.open("https://www.youtube.com/watch?v=YrVIK41RCjs")
    breaks_count = breaks_count + 1
