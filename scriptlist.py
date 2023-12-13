import scripts.chronorace as chronorace
import scripts.kikourou as kikourou
import scripts.sportmaniacs as sportmaniacs
import scripts.eventicom as eventicom
import scripts.ultratiming as ultratiming

supportedWebsites = {
    'chronorace' : {"script": chronorace.chronorace, "exampleUrl": "https://prod.chronorace.be/Classements/Classement.aspx?eventId=1188318666566175&IdClassement=17573"},
    'eventicom' : {"script": eventicom.eventicom, "exampleUrl": "https://eventicom.fr/resultats/TrailNoel2023/10%C3%A8me%20Trail%20de%20No%C3%ABl.clax" },
    'kikourou' : {"script": kikourou.kikourou, "exampleUrl": "http://www.kikourou.net/resultats/resultat-154252-la_course_nature_des_3_etangs_-_18_km-2020.html"},
    'sportmaniacs' : {"script": sportmaniacs.sportmaniacs, "exampleUrl": "https://sportmaniacs.com/es/races/gtpe-2023-gran-trail-picos-de-europa/64976d6e-e580-48b6-ba51-6641ac1f1c02/results#rankings"},
    'ultratiming' : {"script": ultratiming.ultratiming, "exampleUrl": "https://www.ultratiming.be/evenement/trail-du-hoyoux-2023/epreuve/34km/resultats"}
}