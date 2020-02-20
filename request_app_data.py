from urllib.request import urlopen

# f = open("app_ranking_list.json", "wb")

check = "https://sensortower.com/api/ios/rankings/get_category_rankings?category=0&country=US&date=2020-02-01T00%3A00%3A00.000Z&device=IPHONE&limit=50&offset=0"


base_url = "https://sensortower.com/api/ios/rankings/get_category_rankings?"
rankingsCategory = 0
rankingsCountry = "US"
rankingsDate = "2020-02-01"
rankingsTime = "T00%3A00%3A00.000Z"
rankingsDevice = "IPHONE"
rankingsLimit = 50
rankingsOffset = 0

rankingsUrl = base_url + "category=" + str(rankingsCategory) + "&"
rankingsUrl += "country=" + str(rankingsCountry) + "&"
rankingsUrl += "date=" + str(rankingsDate)
rankingsUrl += str(rankingsTime) + "&"
rankingsUrl += "device=" + str(rankingsDevice) + "&"
rankingsUrl += "limit=" + str(rankingsLimit) + "&"
rankingsUrl += "offset=" + str(rankingsOffset)
print(rankingsUrl == check)
#rankingsUrl = "https://sensortower.com/api/ios/rankings/get_category_rankings?category=0&country=US&date=2020-02-01T00%3A00%3A00.000Z&device=IPHONE&limit=50&offset=0"
#response = urlopen(rankingsUrl)

# f.write(response.read())

# f.close()
