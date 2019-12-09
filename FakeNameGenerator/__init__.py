import requests

class FakeNameGenerator():
    def __init__(self):
        self.html = ""

    def GenerateIdenity(self):
        self.html = requests.get("https://www.fakenamegenerator.com/",headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}).text
        self.name = {"completename":self.html.split('<div class="address">')[1].split('<h3>')[1].split('</h3>')[0],"first":self.html.split('<div class="address">')[1].split('<h3>')[1].split('</h3>')[0].split(" ")[0],"last":self.html.split('<div class="address">')[1].split('<h3>')[1].split('</h3>')[0].split(" ")[-1]}

        addy = self.html.split('<div class="adr">')[1].split("                                        ")[1].split("                                        </div>")[0]
        addynum = addy.split(" ")[0]
        streetlist = self.html.split('<div class="adr">')[1].split("                                        ")[1].split("                                        </div>")[0].split("<br />")[:1][0].split(" ")[1:]
        street = ""

        province = addy.split('<br />')[1].split(",")[0]
        ZIP = addy.split(", ")[1].split('   ')[0]
        for i in streetlist:
            street = street + " " + i
        self.addy = {"addynum":addynum,"street":street[1:],"province":province,"zip":ZIP}

        self.SSN = self.html.split('tal"><dt>SSN</dt><dd>')[1].split(' <div class="adtl">')[0]
        self.phone = self.html.split("<dt>Phone</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.phoneprefix = "+" + self.html.split("<dt>Country code</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        birthday = "+" + self.html.split("<dt>Birthday</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        Month = birthday.split(" ")[0].replace("+","")
        Day = birthday.split(" ")[1].replace(",","")
        Year = birthday.split(" ")[-1]
        self.birthday = {"Day":Day,"Month":Month,"Year":Year}
        self.age = self.html.split("<dt>Age</dt>")[1].split(" years old</dd>")[0].split("<dd>")[1]
        self.tropicalzodiac = self.html.split("<dt>Tropical zodiac</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.email = self.html.split('<dt>Email Address</dt>')[1].split('<dd>')[1].split('        ')[0]
        self.username = self.html.split("<dt>Username</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.password = self.html.split("<dt>Password</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.website = self.html.split("<dt>Website</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.useragent = self.html.split("<dt>Browser user agent</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.cardtype = self.html.split('<h3 class="hh3">Finance</h3>')[1].split('<dt>')[1].split('</dt>')[0]
        self.card = self.html.split(f"<dt>{self.cardtype}</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.exp = self.html.split("<dt>Expires</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        try:
            self.CVC = self.html.split("<dt>CVC2</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        except:
            self.CVC = self.html.split("<dt>CVV2</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.company = self.html.split("<dt>Company</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.job = self.html.split("<dt>Occupation</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.height = self.html.split("<dt>Height</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.weight = self.html.split("<dt>Weight</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.bloodtype = self.html.split("<dt>Blood type</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.UPSTrackingnum = self.html.split("<dt>UPS tracking number</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.MoneyGram = self.html.split("<dt>MoneyGram MTCN</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.WesternUnion = self.html.split("<dt>Western Union MTCN</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.favcolor = self.html.split("<dt>Favorite color</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.car = self.html.split("<dt>Vehicle</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.GUID = self.html.split("<dt>GUID</dt>")[1].split("</dd>")[0].split("<dd>")[1]


    def Test(self):
        self.GenerateIdenity()
        print(self.name["first"] + " " + self.name["last"])
        print(self.addy["addynum"] + " " + self.addy["street"] + " " + self.addy["province"] + " " + self.addy["zip"])
        print(self.SSN)
        print(self.phone)
        print(self.phoneprefix)
        print(self.birthday["Day"] + " " + self.birthday["Month"] + " " + self.birthday["Year"])
        print(self.age)
        print(self.tropicalzodiac)
        print(self.email)
        print(self.username)
        print(self.password)
        print(self.website)
        print(self.useragent)
        print(self.cardtype)
        print(self.card)
        print(self.exp)
        print(self.CVC)
        print(self.company)
        print(self.job)
        print(self.height)
        print(self.weight)
        print(self.bloodtype)
        print(self.UPSTrackingnum)
        print(self.MoneyGram)
        print(self.WesternUnion)
        print(self.favcolor)
        print(self.car)
        print(self.GUID)
