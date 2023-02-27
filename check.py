import random
import sys
import time


while True:
    result = random.randint(0, 5)
    announce_action = 'announce' if result > 2 else 'withdraw'
    announce_network = "172.31.0.89/32"
    announce_line = "{} route {} next-hop self\n".format(announce_action, announce_network)
    sys.stdout.write(announce_line)
    sys.stdout.flush()
    time.sleep(0.5)
