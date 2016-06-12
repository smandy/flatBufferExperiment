#import os
#import sys
#sys.path.append(os.path.join(os.path.dirname(__file__), '../python'))

import flatbuffers

from argo.ThingList import ThingList

buf = open('../things.fb','r').read()

thingList = ThingList.GetRootAsThingList(buf, 0)

print thingList.Title();

print "Have %s things" % thingList.ThingsLength()

for i in xrange(thingList.ThingsLength()):
    print thingList.Things(i).Name()



