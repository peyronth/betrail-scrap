import scripts.chronorace as chronorace
import scripts.kikourou as kikourou
import scripts.sportmaniacs as sportmaniacs

supportedWebsites = {
    'chronorace' : {"script": chronorace.chronorace, "exampleUrl": "https://prod.chronorace.be/Classements/Classement.aspx?eventId=1188318666566175&IdClassement=17573"},
    'kikourou' : {"script": kikourou.kikourou, "exampleUrl": "http://www.kikourou.net/resultats/resultat-154252-la_course_nature_des_3_etangs_-_18_km-2020.html"},
    'sportmaniacs' : {"script": sportmaniacs.sportmaniacs, "exampleUrl": "https://sportmaniacs.com/es/races/gtpe-2023-gran-trail-picos-de-europa/64976d6e-e580-48b6-ba51-6641ac1f1c02/results#rankings"}
}