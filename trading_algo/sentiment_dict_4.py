# region imports
from AlgorithmImports import *
# endregion


class WordScoreChunk4:
    words = {"pityingly": -1.0, "pityriasis": -0.8, "play": 1.4, "played": 1.4, "playful": 1.9, "playfully": 1.6, "playfulness": 1.2, "playing": 0.8, "plays": 1.0, "pleasant": 2.3, "pleasanter": 1.5, "pleasantest": 2.6, "pleasantly": 2.1, "pleasantness": 2.3, "pleasantnesses": 2.3, "pleasantries": 1.3, "pleasantry": 2.0, "please": 1.3, "pleased": 1.9, "pleaser": 1.7, "pleasers": 1.0, "pleases": 1.7, "pleasing": 2.4, "pleasurability": 1.9, "pleasurable": 2.4, "pleasurableness": 2.4, "pleasurably": 2.6, "pleasure": 2.7, "pleasured": 2.3, "pleasureless": -1.6, "pleasures": 1.9, "pleasuring": 2.8, "poised": 1.0, "poison": -2.5, "poisoned": -2.2, "poisoner": -2.7, "poisoners": -3.1, "poisoning": -2.8, "poisonings": -2.4, "poisonous": -2.7, "poisonously": -2.9, "poisons": -2.7, "poisonwood": -1.0, "pollute": -2.3, "polluted": -2.0, "polluter": -1.8, "polluters": -2.0, "pollutes": -2.2, "poor": -2.1, "poorer": -1.5, "poorest": -2.5, "popular": 1.8, "popularise": 1.6, "popularised": 1.1, "popularises": 0.5, "popularising": 1.2, "popularities": 1.6, "popularity": 2.1, "popularization": 1.3, "popularizations": 0.9, "popularize": 1.3, "popularized": 1.9, "popularizer": 1.8, "popularizers": 1.0, "popularizes": 1.4, "popularizing": 1.5, "popularly": 1.8, "positive": 2.6, "positively": 2.4, "positiveness": 2.3, "positivenesses": 2.2, "positiver": 2.3, "positives": 2.4, "positivest": 2.9, "positivism": 1.6, "positivisms": 1.8, "positivist": 2.0, "positivistic": 1.9, "positivists": 1.7, "positivities": 2.6, "positivity": 2.3, "possessive": -0.9, "postpone": -0.9, "postponed": -0.8, "postpones": -1.1, "postponing": -0.5, "poverty": -2.3, "powerful": 1.8, "powerless": -2.2, "praise": 2.6, "praised": 2.2, "praiser": 2.0, "praisers": 2.0, "praises": 2.4, "praiseworthily": 1.9, "praiseworthiness": 2.4, "praiseworthy": 2.6, "praising": 2.5, "pray": 1.3, "praying": 1.5, "prays": 1.4, "prblm": -1.6, "prblms": -2.3, "precious": 2.7, "preciously": 2.2, "preciousness": 1.9, "prejudice": -2.3, "prejudiced": -1.9, "prejudices": -1.8, "prejudicial": -2.6, "prejudicially": -1.5, "prejudicialness": -2.4, "prejudicing": -1.8, "prepared": 0.9, "pressure": -1.2, "pressured": -0.9, "pressureless": 1.0, "pressures": -1.3, "pressuring": -1.4, "pressurise": -0.6, "pressurised": -0.4, "pressurises": -0.8, "pressurising": -0.6, "pressurizations": -0.3, "pressurize": -0.7, "pressurized": 0.1, "pressurizer": 0.1, "pressurizers": -0.7, "pressurizes": -0.2, "pressurizing": -0.2, "pretend": -0.4, "pretending": 0.4, "pretends": -0.4, "prettied": 1.6, "prettier": 2.1, "pretties": 1.7, "prettiest": 2.7, "pretty": 2.2, "prevent": 0.1, "prevented": 0.1, "preventing": -0.1, "prevents": 0.3, "prick": -1.4, "pricked": -0.6, "pricker": -0.3, "prickers": -0.2, "pricket": -0.5, "prickets": 0.3, "pricking": -0.9, "prickle": -1.0, "prickled": -0.2, "prickles": -0.8, "pricklier": -1.6, "prickliest": -1.4, "prickliness": -0.6, "prickling": -0.8, "prickly": -0.9, "pricks": -0.9, "pricky": -0.6, "pride": 1.4, "prison": -2.3, "prisoner": -2.5, "prisoners": -2.3, "privilege": 1.5, "privileged": 1.9, "privileges": 1.6, "privileging": 0.7, "prize": 2.3, "prized": 2.4, "prizefight": -0.1, "prizefighter": 1.0, "prizefighters": -0.1, "prizefighting": 0.4, "prizefights": 0.3, "prizer": 1.0, "prizers": 0.8, "prizes": 2.0, "prizewinner": 2.3, "prizewinners": 2.4, "prizewinning": 3.0, "proactive": 1.8, "problem": -1.7, "problematic": -1.9, "problematical": -1.8, "problematically": -2.0, "problematics": -1.3, "problems": -1.7, "profit": 1.9, "profitabilities": 1.1, "profitability": 1.1, "profitable": 1.9, "profitableness": 2.4, "profitably": 1.6, "profited": 1.3, "profiteer": 0.8, "profiteered": -0.5, "profiteering": -0.6, "profiteers": 0.5, "profiter": 0.7, "profiterole": 0.4, "profiteroles": 0.5, "profiting": 1.6, "profitless": -1.5, "profits": 1.9, "profitwise": 0.9, "progress": 1.8, "prominent": 1.3, "promiscuities": -0.8, "promiscuity": -1.8, "promiscuous": -0.3, "promiscuously": -1.5, "promiscuousness": -0.9, "promise": 1.3, "promised": 1.5, "promisee": 0.8, "promisees": 1.1, "promiser": 1.3, "promisers": 1.6, "promises": 1.6, "promising": 1.7, "promisingly": 1.2, "promisor": 1.0, "promisors": 0.4, "promissory": 0.9, "promote": 1.6, "promoted": 1.8, "promotes": 1.4, "promoting": 1.5, "propaganda": -1.0, "prosecute": -1.7, "prosecuted": -1.6, "prosecutes": -1.8, "prosecution": -2.2, "prospect": 1.2,
             "prospects": 1.2, "prosperous": 2.1, "protect": 1.6, "protected": 1.9, "protects": 1.3, "protest": -1.0, "protested": -0.5, "protesters": -0.9, "protesting": -1.8, "protests": -0.9, "proud": 2.1, "prouder": 2.2, "proudest": 2.6, "proudful": 1.9, "proudhearted": 1.4, "proudly": 2.6, "provoke": -1.7, "provoked": -1.1, "provokes": -1.3, "provoking": -0.8, "pseudoscience": -1.2, "puke": -2.4, "puked": -1.8, "pukes": -1.9, "puking": -1.8, "pukka": 2.8, "punish": -2.4, "punishabilities": -1.7, "punishability": -1.6, "punishable": -1.9, "punished": -2.0, "punisher": -1.9, "punishers": -2.6, "punishes": -2.1, "punishing": -2.6, "punishment": -2.2, "punishments": -1.8, "punitive": -2.3, "pushy": -1.1, "puzzled": -0.7, "quaking": -1.5, "questionable": -1.2, "questioned": -0.4, "questioning": -0.4, "racism": -3.1, "racist": -3.0, "racists": -2.5, "radian": 0.4, "radiance": 1.4, "radiances": 1.1, "radiancies": 0.8, "radiancy": 1.4, "radians": 0.2, "radiant": 2.1, "radiantly": 1.3, "radiants": 1.2, "rage": -2.6, "raged": -2.0, "ragee": -0.4, "rageful": -2.8, "rages": -2.1, "raging": -2.4, "rainy": -0.3, "rancid": -2.5, "rancidity": -2.6, "rancidly": -2.5, "rancidness": -2.6, "rancidnesses": -1.6, "rant": -1.4, "ranter": -1.2, "ranters": -1.2, "rants": -1.3, "rape": -3.7, "raped": -3.6, "raper": -3.4, "rapers": -3.6, "rapes": -3.5, "rapeseeds": -0.5, "raping": -3.8, "rapist": -3.9, "rapists": -3.3, "rapture": 0.6, "raptured": 0.9, "raptures": 0.7, "rapturous": 1.7, "rash": -1.7, "ratified": 0.6, "reach": 0.1, "reached": 0.4, "reaches": 0.2, "reaching": 0.8, "readiness": 1.0, "ready": 1.5, "reassurance": 1.5, "reassurances": 1.4, "reassure": 1.4, "reassured": 1.7, "reassures": 1.5, "reassuring": 1.7, "reassuringly": 1.8, "rebel": -0.6, "rebeldom": -1.5, "rebelled": -1.0, "rebelling": -1.1, "rebellion": -0.5, "rebellions": -1.1, "rebellious": -1.2, "rebelliously": -1.8, "rebelliousness": -1.2, "rebels": -0.8, "recession": -1.8, "reckless": -1.7, "recommend": 1.5, "recommended": 0.8, "recommends": 0.9, "redeemed": 1.3, "reek": -2.4, "reeked": -2.0, "reeker": -1.7, "reekers": -1.5, "reeking": -2.0, "refuse": -1.2, "refused": -1.2, "refusing": -1.7, "regret": -1.8, "regretful": -1.9, "regretfully": -1.9, "regretfulness": -1.6, "regrets": -1.5, "regrettable": -2.3, "regrettably": -2.0, "regretted": -1.6, "regretter": -1.6, "regretters": -2.0, "regretting": -1.7, "reinvigorate": 2.3, "reinvigorated": 1.9, "reinvigorates": 1.8, "reinvigorating": 1.7, "reinvigoration": 2.2, "reject": -1.7, "rejected": -2.3, "rejectee": -2.3, "rejectees": -1.8, "rejecter": -1.6, "rejecters": -1.8, "rejecting": -2.0, "rejectingly": -1.7, "rejection": -2.5, "rejections": -2.1, "rejective": -1.8, "rejector": -1.8, "rejects": -2.2, "rejoice": 1.9, "rejoiced": 2.0, "rejoices": 2.1, "rejoicing": 2.8, "relax": 1.9, "relaxant": 1.0, "relaxants": 0.7, "relaxation": 2.4, "relaxations": 1.0, "relaxed": 2.2, "relaxedly": 1.5, "relaxedness": 2.0, "relaxer": 1.6, "relaxers": 1.4, "relaxes": 1.5, "relaxin": 1.7, "relaxing": 2.2, "relaxins": 1.2, "relentless": 0.2, "reliant": 0.5, "relief": 2.1, "reliefs": 1.3, "relievable": 1.1, "relieve": 1.5, "relieved": 1.6, "relievedly": 1.4, "reliever": 1.5, "relievers": 1.0, "relieves": 1.5, "relieving": 1.5, "relievo": 1.3, "relishing": 1.6, "reluctance": -1.4, "reluctancy": -1.6, "reluctant": -1.0, "reluctantly": -0.4, "remarkable": 2.6, "remorse": -1.1, "remorseful": -0.9, "remorsefully": -0.7, "remorsefulness": -0.7, "remorseless": -2.3, "remorselessly": -2.0, "remorselessness": -2.8, "repetitive": -1.0, "repress": -1.4, "repressed": -1.3, "represses": -1.3, "repressible": -1.5, "repressing": -1.8, "repression": -1.6, "repressions": -1.7, "repressive": -1.4, "repressively": -1.7, "repressiveness": -1.0, "repressor": -1.4, "repressors": -2.2, "repressurize": -0.3, "repressurized": 0.1, "repressurizes": 0.1, "repressurizing": -0.1, "repulse": -2.8, "repulsed": -2.2, "rescue": 2.3, "rescued": 1.8, "rescues": 1.3, "resent": -0.7, "resented": -1.6, "resentence": -1.0, "resentenced": -0.8, "resentences": -0.6, "resentencing": 0.2, "resentful": -2.1, "resentfully": -1.4, "resentfulness": -2.0, "resenting": -1.2, "resentment": -1.9, "resentments": -1.9, "resents": -1.2, "resign": -1.4, "resignation": -1.2, "resignations": -1.2, "resigned": -1.0, "resignedly": -0.7, "resignedness": -0.8, "resigner": -1.2, "resigners": -1.0, "resigning": -0.9, "resigns": -1.3}
