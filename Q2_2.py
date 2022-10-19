import re
generic_urls = ["https://www.genericdomain.com/abc/def/1290aodwb23-ghi.img", 
                "https://www.genericdomain.com/ab-c/31287bdwakj-jkl.img",
                "https://www.genericdomain.com/19unioawd02-jkl.img"
                ]
pattern_matching = "(?<=\/)(\d[a-zA-Z0-9_]*)(?=\-)"

for url in generic_urls:
    match_found = re.findall(pattern_matching, url)
    special_sequence = match_found[0]
    print(special_sequence)