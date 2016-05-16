import requests
api_base_url = 'https://ja.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
wiki_data = requests.get(api_base_url, params=api_params)
fo = open('/Users/Yoshi/Desktop/wiki.html', 'w')
fo.write(wiki_data.text)
fo.close()
