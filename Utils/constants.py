rootRequest = "https://api.covid19api.com/"
UKSet = {'anguilla', 'bermuda', 'british virgin islands', 'cayman islands', 'turks and caicos islands', \
         'falkland islands (islas malvinas)', 'channel islands', 'gibraltar', 'isle of man', 'montserrat'}
FranceSet = {'new caledonia', 'martinique', 'saint barthelemy', 'french polynesia', 'mayotte', 'st martin', \
             'french guiana', 'reunion', 'guadeloupe'}
countriesWithProvinces = {'france', 'united-kingdom'}
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
countryTestCases = ['italy', 'spain', 'united-kingdom', 'us', 'france', 'germany', 'china']
countrySlugs = {'bangladesh', 'cameroon', 'cape-verde', 'guinea', 'macao-sar-china', 'bahamas', 'mozambique',
                'new-zealand', 'poland', 'japan', 'georgia', 'guyana', 'malta', 'martinique', 'moldova', 'somalia',
                'brunei', 'jersey', 'bhutan', 'aruba', 'cayman-islands', 'french-guiana', 'french-polynesia', 'gabon',
                'saint-martin-french-part', 'netherlands', 'burundi', 'ghana', 'greenland', 'vanuatu', 'barbados',
                'uruguay', 'cambodia', 'faroe-islands', 'germany', 'denmark', 'british-indian-ocean-territory', 'china',
                'india', 'monaco', 'niger', 'kiribati', 'kosovo', 'thailand', 'turks-and-caicos-islands', 'anguilla',
                'mali', 'panama', 'saint-lucia', 'united-arab-emirates', 'bosnia-and-herzegovina',
                'french-southern-territories', 'malawi', 'mauritania', 'haiti', 'kyrgyzstan', 'sierra-leone',
                'svalbard-and-jan-mayen-islands', 'korea-south', 'romania', 'russia', 'spain', 'zambia',
                'cocos-keeling-islands', 'lebanon', 'norway', 'saint-pierre-and-miquelon', 'solomon-islands',
                'south-africa', 'congo-brazzaville', 'british-virgin-islands', 'central-african-republic',
                'cote-divoire', 'tunisia', 'angola', 'antigua-and-barbuda', 'mayotte', 'turkmenistan', 'mongolia',
                'virgin-islands', 'ireland', 'congo-kinshasa', 'gibraltar', 'falkland-islands-malvinas', 'guernsey',
                'honduras', 'new-caledonia', 'tuvalu', 'ethiopia', 'iran', 'senegal', 'uganda', 'andorra', 'guadeloupe',
                'hungary', 'jordan', 'azerbaijan', 'burkina-faso', 'djibouti',
                'south-georgia-and-the-south-sandwich-islands', 'uzbekistan', 'antarctica', 'armenia', 'chad',
                'liechtenstein', 'heard-and-mcdonald-islands', 'latvia', 'samoa', 'tokelau', 'luxembourg', 'iraq',
                'swaziland', 'dominica', 'guam', 'guatemala', 'mexico', 'grenada', 'estonia', 'fiji', 'jamaica',
                'pakistan', 'cuba', 'eritrea', 'slovakia', 'bahrain', 'botswana', 'norfolk-island', 'australia',
                'colombia', 'kazakhstan', 'papua-new-guinea', 'portugal', 'micronesia', 'saint-barthélemy', 'croatia',
                'turkey', 'yemen', 'ecuador', 'vietnam', 'christmas-island', 'lao-pdr', 'lesotho', 'tanzania',
                'western-sahara', 'korea-north', 'belize', 'palau', 'united-states', 'zimbabwe', 'canada', 'nepal',
                'tajikistan', 'belgium', 'marshall-islands', 'montenegro', 'niue', 'sao-tome-and-principe', 'kenya',
                'kuwait', 'nicaragua', 'saudi-arabia', 'united-kingdom', 'israel', 'peru',
                'saint-vincent-and-the-grenadines', 'macedonia', 'bulgaria', 'el-salvador', 'gambia', 'serbia',
                'iceland', 'france', 'bermuda', 'bouvet-island', 'dominican-republic', 'indonesia', 'switzerland',
                'wallis-and-futuna-islands', 'albania', 'maldives', 'nauru', 'paraguay', 'san-marino', 'slovenia',
                'suriname', 'tonga', 'afghanistan', 'mauritius', 'rwanda', 'seychelles', 'timor-leste', 'lithuania',
                'italy', 'montserrat', 'togo', 'finland', 'bolivia', 'cyprus', 'equatorial-guinea', 'palestine',
                'american-samoa', 'réunion', 'egypt', 'guinea-bissau', 'hong-kong-sar-china', 'myanmar', 'oman',
                'south-sudan', 'brazil', 'isle-of-man', 'libya', 'netherlands-antilles', 'northern-mariana-islands',
                'puerto-rico', 'saint-kitts-and-nevis', 'sri-lanka', 'sudan', 'taiwan', 'trinidad-and-tobago', 'greece',
                'argentina', 'austria', 'venezuela', 'belarus', 'costa-rica', 'qatar', 'comoros', 'cook-islands',
                'madagascar', 'us-minor-outlying-islands', 'algeria', 'malaysia', 'morocco', 'saint-helena', 'syria',
                'ukraine', 'benin', 'liberia', 'philippines', 'singapore', 'ala-aland-islands', 'namibia', 'nigeria',
                'pitcairn', 'sweden', 'czech-republic', 'holy-see-vatican-city-state', 'chile'}
statuses = {'deaths', 'confirmed', 'recovered'}
