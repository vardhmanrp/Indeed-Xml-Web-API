import urllib2
import time
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
intialvalue = 0
offset = 25
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

baseUrl = "http://api.indeed.com/ads/apisearch?"
publisher = "publisher=3660210929802644"
query = "&q="+ ""
location = "&l="
sort = "&sort="
radiusSearch = "&radius="
siteType = "&st=" + "employer"
jobType = "&jt="
start = "&start="
limit = "&limit=50"
backDate = "&fromage="
duplicatejobFilter = "&filter="
country = "&co=us"
channel = "&chnl="
userip= "&userip=1.2.3.4"
useragent = "&useragent=Mozilla/%2F4.0%28Firefox%29&v=2"

# URL Header created
urlHead = baseUrl + publisher +query + location +sort + radiusSearch + siteType + jobType

# URL TAIL created
startTime = time.time()
urlTail = limit +backDate + duplicatejobFilter +country + channel + userip + useragent
for i in range(0,1000,25):
    urlCreated = urlHead + start + str(i) + urlTail
    print urlCreated
    tempStart = time.time()
    response = urllib2.urlopen(urlCreated).read()
    print str(i) + " executed in " + str(time.time() - tempStart)
    f = open(str(i)+".xml","w")
    f.write(response)
    f.close()
##    if i==100:
##        break
print "Completed in " + str(time.time() - startTime)