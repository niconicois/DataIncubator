from urllib2 import Request, urlopen, URLError
import json 
from pprint import pprint
import numpy
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

perPage = 100

for i in range(0,3):
#    print i
    request = Request('https://api.data.gov/ed/collegescorecard/v1/schools.json?api_key=3DPbmuIkRoj2InqLbgd8iYrSMZM4JGC7EjomReHc&school.state_fips=26&_per_page=100&_page={0}&_fields=id,school.name,2013.student.size,2013.student.demographics.race_ethnicity.white,2013.student.demographics.race_ethnicity.black,2013.student.demographics.race_ethnicity.hispanic,2013.student.demographics.race_ethnicity.asian,2013.student.demographics.race_ethnicity.aian,2013.student.demographics.race_ethnicity.nhpi,school.state_fips,2013.admissions.sat_scores.average.overall,2013.student.demographics.race_ethnicity.two_or_more,2013.student.demographics.race_ethnicity.non_resident_alien,2013.student.demographics.race_ethnicity.unknown,1997.student.size,1997.student.demographics.race_ethnicity.white,1997.student.demographics.race_ethnicity.black,1997.student.demographics.race_ethnicity.hispanic,1997.student.demographics.race_ethnicity.asian,1997.student.demographics.race_ethnicity.aian,1997.student.demographics.race_ethnicity.nhpi,school.state_fips,1997.admissions.sat_scores.average.overall,1997.student.demographics.race_ethnicity.two_or_more,1997.student.demographics.race_ethnicity.non_resident_alien,1997.student.demographics.race_ethnicity.unknown'.format(i))    
    response = urlopen(request)
    data = response.read()
    with open('query' + str(i) + '.txt', 'w') as file:
        file.write(data)
    file.close()

studentSize2013 = []
sat = []
state = []
white = []
black = []
hispanic = []
asian = []
aian = []
nhpi = []
nrAlien = []
twoOrMore = []
unknown = []
white1997 = []
black1997 = []
hispanic1997 = []
asian1997 = []
aian1997 = []
nhpi1997 = []
nrAlien1997 = []
twoOrMore1997 = []
unknown1997 = []


schoolId = []
schoolName = []

for j in range(0,3):
    f = open('query' + str(j) + '.txt', 'r')
    results = json.loads(f.read())
    f.close()

    dataLength = results["metadata"]["total"]

    if j != 2:
        upperBound = perPage-1
    else:
        upperBound = dataLength - 2 * perPage
        upperBound

    for i in range(0,upperBound):
        if results["results"][i]["2013.student.size"] and results["results"][i]["2013.student.demographics.race_ethnicity.white"] and results["results"][i]["2013.student.demographics.race_ethnicity.black"] and results["results"][i]["2013.student.demographics.race_ethnicity.hispanic"] and results["results"][i]["2013.student.demographics.race_ethnicity.asian"] and results["results"][i]["2013.student.demographics.race_ethnicity.aian"] and results["results"][i]["2013.student.demographics.race_ethnicity.nhpi"] and results["results"][i]["2013.admissions.sat_scores.average.overall"] and results["results"][i]["school.state_fips"] == 26  is not None:
            studentSize2013.append(float(results["results"][i]["2013.student.size"]))
            white.append(float(results["results"][i]["2013.student.demographics.race_ethnicity.white"]))
            black.append(float(results["results"][i]["2013.student.demographics.race_ethnicity.black"]))
            hispanic.append(float(results["results"][i]["2013.student.demographics.race_ethnicity.hispanic"]))
            asian.append(float(results["results"][i]["2013.student.demographics.race_ethnicity.asian"]))
            aian.append(float(results["results"][i]["2013.student.demographics.race_ethnicity.aian"]))
            nhpi.append(float(results["results"][i]["2013.student.demographics.race_ethnicity.nhpi"]))
            nrAlien.append(float(results["results"][i]["2013.student.demographics.race_ethnicity.non_resident_alien"]))
            twoOrMore.append(float(results["results"][i]["2013.student.demographics.race_ethnicity.two_or_more"]))
            unknown.append(float(results["results"][i]["2013.student.demographics.race_ethnicity.unknown"]))
            state.append(float(results["results"][i]["school.state_fips"]))
            schoolId.append(float(results["results"][i]["id"]))
            schoolName.append(results["results"][i]["school.name"])
            
universityofMichiganAnnArbor2013 = []

for i,_ in enumerate(schoolId):
    if (schoolId[i] == 170976):
        print schoolName[i]
        universityofMichiganAnnArbor2013.append(white[i])
        universityofMichiganAnnArbor2013.append(black[i])
        universityofMichiganAnnArbor2013.append(hispanic[i])
        universityofMichiganAnnArbor2013.append(asian[i])
        universityofMichiganAnnArbor2013.append(aian[i])
        universityofMichiganAnnArbor2013.append(nhpi[i])
        universityofMichiganAnnArbor2013.append(nrAlien[i])
        universityofMichiganAnnArbor2013.append(twoOrMore[i])
        universityofMichiganAnnArbor2013.append(unknown[i])
        studentSize2013.append(studentSize2013[i])

print sum(universityofMichiganAnnArbor2013)


objects = ('White', 'Black', 'Hispanic', 'Asian', 'Aian', 'NHPI', 'Alien', '2 or more', 'Unknown')
y_pos = np.arange(len(objects))
ratioEthnicity = universityofMichiganAnnArbor2013

plt.bar(y_pos, ratioEthnicity, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylim([0,1])
plt.ylabel('Percentage')
plt.title('Percentage per Ethnicity at University of Michigan - Ann Arbor in 2013')
 
plt.show()       
    
    
    
