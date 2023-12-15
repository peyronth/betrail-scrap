import scripts.chronorace as chronorace
import scripts.kikourou as kikourou
import scripts.sportmaniacs as sportmaniacs
import scripts.eventicom as eventicom
import scripts.ultratiming as ultratiming
import scripts.utmb as utmb
import scripts.yakachrono as yakachrono
import scripts.livetrail as livetrail

supportedWebsites = {
    'chronorace' : {"script": chronorace.chronorace, "exampleUrl": "https://prod.chronorace.be/Classements/Classement.aspx?eventId=1188318666566175&IdClassement=17573"},
    'eventicom' : {"script": eventicom.eventicom, "exampleUrl": "https://eventicom.fr/resultats/TrailNoel2023/10%C3%A8me%20Trail%20de%20No%C3%ABl.clax" },
    'kikourou' : {"script": kikourou.kikourou, "exampleUrl": "http://www.kikourou.net/resultats/resultat-154252-la_course_nature_des_3_etangs_-_18_km-2020.html"},
    'livetrail' : {"script": livetrail.livetrail, "exampleUrl": "https://livetrail.net/histo/kosciuszko_2023/classement.php?course=100k&cat=scratch"},
    'sportmaniacs' : {"script": sportmaniacs.sportmaniacs, "exampleUrl": "https://sportmaniacs.com/es/races/gtpe-2023-gran-trail-picos-de-europa/64976d6e-e580-48b6-ba51-6641ac1f1c02/results#rankings"},
    'ultratiming' : {"script": ultratiming.ultratiming, "exampleUrl": "https://www.ultratiming.be/evenement/trail-du-hoyoux-2023/epreuve/34km/resultats"},
    'utmb world' : {"script": utmb.utmbworld, "exampleUrl": "https://kosciuszko.utmb.world/runners/results?year=2023&raceUri=33948.ultra-trailkosciuszkobyutmbkoscimiler.2023"},
    'yakachrono (pdf)' : {"script": yakachrono.yakachrono_pdf, "exampleUrl": "https://www.ganatrail.com/_files/ugd/a39524_982ab77c9b054edc83fe4b4085e22de6.pdf"}
}