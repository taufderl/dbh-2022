GET /key_1.txt HTTP/1.1
lbYldJw9Gg
6c62596c644a77394767

GET /key_2.txt HTTP/1.1
ESQqIBrRQk
4553517149427252516b

GET /key_3.txt HTTP/1.1
bCdNmpTZNS
6243644e6d70545a4e53

GET /key_2.txt HTTP/1.1
ESQqIBrRQk

key_combined
lbYldJw9GgESQqIBrRQkbCdNmpTZNS
6c62596c644a773947674553517149427252516b6243644e6d70545a4e53


# keyserver / DNS server
MAC:  00:0c:29:4d:70:17
IPv4: -
IPv6: fd15:4ba5:5a2b:1004:fda5:3d88:bf5e:bec2


# key requestor
MAC:  00:0c:29:8d:98:33
IPv4: 172.16.93.128
IPv6: fd15:4ba5:5a2b:1004:7fc5:bcc5:95ba:260a


# c2 infra

c2.mlwreprvt.de: type AAAA, class IN, addr eda4:3872:65ec:4d47:32bd:7038:6d00:a3e8
No such name AAAA c3.mlwreprvt.de SOA f.nic.de
No such name AAAA control-infr.atc1.mlwreprvt.de


tcp.stream eq 9!!

953	91.533319025	44.232.89.39	172.16.93.128	TLSv1.2			9	85	Application Data


554	35.072627146	172.16.93.128	172.217.18.98	TLSv1.3	pagead2.googlesyndication.com		5	571	Client Hello
808	52.900054836	172.16.93.128	18.66.192.13	TLSv1.2	firefox.settings.services.mozilla.com		6	272	Client Hello
836	53.472092272	172.16.93.128	18.66.192.21	TLSv1.2	content-signature-2.cdn.mozilla.net		7	270	Client Hello
905	86.564631561	172.16.93.128	34.117.237.239	TLSv1.3	contile.services.mozilla.com		8	571	Client Hello
1094	172.939772659	172.16.93.128	108.138.36.100	TLSv1.2	services.addons.mozilla.org		10	262	Client Hello
1154	174.369782803	172.16.93.128	108.138.36.44	TLSv1.2	versioncheck-bg.addons.mozilla.org		11	269	Client Hello
1176	174.378130020	172.16.93.128	108.138.36.44	TLSv1.2	versioncheck-bg.addons.mozilla.org		12	269	Client Hello
1174	174.377607103	172.16.93.128	108.138.36.44	TLSv1.2	versioncheck-bg.addons.mozilla.org		13	269	Client Hello
1172	174.376482031	172.16.93.128	108.138.36.44	TLSv1.2	versioncheck-bg.addons.mozilla.org		14	269	Client Hello
1169	174.374964074	172.16.93.128	108.138.36.44	TLSv1.2	versioncheck-bg.addons.mozilla.org		15	269	Client Hello
1167	174.374492069	172.16.93.128	108.138.36.44	TLSv1.2	versioncheck-bg.addons.mozilla.org		16	269	Client Hello
1386	174.615524918	172.16.93.128	108.138.36.53	TLSv1.3	addons.mozilla.org		17	571	Client Hello
1389	174.619423407	172.16.93.128	108.138.36.53	TLSv1.3	addons.mozilla.org		18	571	Client Hello
1406	174.631044663	172.16.93.128	108.138.36.53	TLSv1.3	addons.mozilla.org		19	571	Client Hello
1400	174.628613238	172.16.93.128	108.138.36.53	TLSv1.3	addons.mozilla.org		20	571	Client Hello
1395	174.624921865	172.16.93.128	108.138.36.53	TLSv1.3	addons.mozilla.org		21	571	Client Hello
1393	174.622710966	172.16.93.128	108.138.36.53	TLSv1.3	addons.mozilla.org		22	571	Client Hello
2771	175.489276046	172.16.93.128	35.244.181.201	TLSv1.2	aus5.mozilla.org		23	251	Client Hello
12419	379.827764087	172.16.93.128	34.120.208.123	TLSv1.2	incoming.telemetry.mozilla.org		28	265	Client Hello
12478	380.540651936	172.16.93.128	34.120.115.102	TLSv1.3	contile-images.services.mozilla.com		29	571	Client Hello


http://[fd15:4ba5:5a2b:1004:fda5:3d88:bf5e:bec2]:8000/key_3.txt