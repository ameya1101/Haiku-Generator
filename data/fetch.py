from urllib.request import urlopen

def flush_buffer(buf, f):
	for b in buf:
		f.write("%s\n"%b)
	return []


base = 'http://haiku.somebullshit.net/'
destination = open('haiku_reddit.tsv', 'w')

index = 1

buffer_size = 1000
haiku_buffer = []
total_haikus = 0


while index <= 2000:
	try:
		url = base+"%d.html"%index
		html = urlopen(url).read().decode('utf-8')
		items = html.split("<article class=\"card\">")[1:]
		for item in items:
			text = item.split("<p>")[1].split("</p>")[0].replace("\n", "")
			haiku_buffer.append(text)
			total_haikus = total_haikus + 1
		if len(haiku_buffer) > buffer_size:
			haiku_buffer = flush_buffer(haiku_buffer, destination)
	except Exception as e:
		print("Caught exception: ", e)
		print("Flushing Buffer...")
		flush_buffer(haiku_buffer, destination)
		print("Done.")
	index = index + 1

flush_buffer(haiku_buffer, destination)
print("\n\nDone.")
