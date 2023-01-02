url = "https://github.com/flowlord/Multiple-Substitution-Encryption/blob/main/README.md"

version_actuelle = "0011211548862 - 33221 - 145205932375L"

import urllib.request

try:
	data = urllib.request.urlopen(url)

	data = data.read().decode('utf-8')

	if version_actuelle not in data:
		print("\t** [ Version obsolète, mise à jour nécessaire. ] **")

except urllib.error.URLError:
	pass

