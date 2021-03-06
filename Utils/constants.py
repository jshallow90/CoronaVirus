rootRequest = "https://api.covid19api.com/"
UKSet = {'anguilla', 'bermuda', 'british virgin islands', 'cayman islands', 'turks and caicos islands', \
         'falkland islands (islas malvinas)', 'channel islands', 'gibraltar', 'isle of man', 'montserrat'}
FranceSet = {'new caledonia', 'martinique', 'saint barthelemy', 'french polynesia', 'mayotte', 'st martin', \
             'french guiana', 'reunion', 'guadeloupe'}
countriesWithProvinces = {'france', 'united-kingdom'}
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
countryTestCases = ['italy', 'spain', 'united-kingdom', 'us', 'france', 'germany', 'china']
countrySlugs = {
    'afghanistan', 'ala-aland-islands', 'albania', 'algeria', 'american-samoa', 'andorra', 'angola', 'anguilla',
    'antarctica', 'antigua-and-barbuda', 'argentina', 'armenia', 'aruba', 'australia', 'austria',
    'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bermuda',
    'bhutan', 'bolivia', 'bosnia-and-herzegovina', 'botswana', 'bouvet-island', 'brazil',
    'british virgin islands', 'british-indian-ocean-territory', 'british-virgin-islands', 'brunei', 'bulgaria',
    'burkina-faso', 'burundi', 'cambodia', 'cameroon', 'canada', 'cape-verde', 'cayman-islands',
    'central-african-republic', 'chad', 'channel islands', 'chile', 'china', 'christmas-island',
    'cocos-keeling-islands', 'colombia', 'comoros', 'congo-brazzaville', 'congo-kinshasa', 'cook-islands', 'costa-rica',
    'cote-divoire', 'croatia', 'cuba', 'cyprus', 'czech-republic', 'denmark', 'djibouti', 'dominica',
    'dominican-republic', 'ecuador', 'egypt', 'el-salvador', 'equatorial-guinea', 'eritrea', 'estonia', 'ethiopia',
    'falkland islands (islas malvinas)', 'falkland-islands-malvinas', 'faroe-islands', 'fiji', 'finland', 'france',
    'french guiana', 'french polynesia', 'french-guiana', 'french-polynesia', 'french-southern-territories', 'gabon',
    'gambia', 'georgia', 'germany', 'ghana', 'gibraltar', 'greece', 'greenland', 'grenada', 'guadeloupe',
    'guam', 'guatemala', 'guernsey', 'guinea', 'guinea-bissau', 'guyana', 'haiti',
    'heard-and-mcdonald-islands', 'holy-see-vatican-city-state', 'honduras', 'hong-kong-sar-china', 'hungary',
    'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'isle of man', 'israel', 'italy',
    'jamaica', 'japan', 'jersey', 'jordan', 'kazakhstan', 'kenya', 'kiribati', 'korea-north', 'korea-south', 'kosovo',
    'kuwait', 'kyrgyzstan', 'lao-pdr', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania',
    'luxembourg', 'macao-sar-china', 'macedonia', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta',
    'marshall-islands', 'martinique', 'mauritania', 'mauritius', 'mayotte', 'mexico',
    'micronesia', 'moldova', 'monaco', 'mongolia', 'montenegro', 'montserrat', 'morocco', 'mozambique',
    'myanmar', 'namibia', 'nauru', 'nepal', 'netherlands', 'netherlands-antilles', 'new caledonia', 'new-caledonia',
    'new-zealand', 'nicaragua', 'niger', 'nigeria', 'niue', 'norfolk-island', 'northern-mariana-islands', 'norway',
    'oman', 'pakistan', 'palau', 'palestine', 'panama', 'papua-new-guinea', 'paraguay', 'peru', 'philippines',
    'pitcairn', 'poland', 'portugal', 'puerto-rico', 'qatar', 'reunion', 'romania', 'russia', 'rwanda', 'réunion',
    'saint barthelemy', 'saint-barthélemy', 'saint-helena', 'saint-kitts-and-nevis', 'saint-lucia',
    'saint-martin-french-part', 'saint-pierre-and-miquelon', 'saint-vincent-and-the-grenadines', 'samoa', 'san-marino',
    'sao-tome-and-principe', 'saudi-arabia', 'senegal', 'serbia', 'seychelles', 'sierra-leone', 'singapore', 'slovakia',
    'slovenia', 'solomon-islands', 'somalia', 'south-africa', 'south-georgia-and-the-south-sandwich-islands',
    'south-sudan', 'spain', 'sri-lanka', 'st martin', 'sudan', 'suriname', 'svalbard-and-jan-mayen-islands',
    'swaziland', 'sweden', 'switzerland', 'syria', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'timor-leste',
    'togo', 'tokelau', 'tonga', 'trinidad-and-tobago', 'tunisia', 'turkey', 'turkmenistan', 'turks and caicos islands',
    'turks-and-caicos-islands', 'tuvalu', 'uganda', 'ukraine', 'united-arab-emirates', 'united-kingdom',
    'uruguay', 'us', 'us-minor-outlying-islands', 'uzbekistan', 'vanuatu', 'venezuela', 'vietnam',
    'virgin-islands', 'wallis-and-futuna-islands', 'western-sahara', 'yemen', 'zambia', 'zimbabwe'
}
statuses = {'deaths', 'confirmed', 'recovered'}
