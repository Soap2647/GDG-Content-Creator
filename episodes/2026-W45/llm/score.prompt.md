# Görev: score

Yanıtı `episodes/2026-W45/llm/score.response.json` dosyasına, aşağıdaki JSON şemasına uyan TEK bir JSON nesnesi olarak yaz.

## Sistem talimatı

Sen GDG on Campus Kastamonu'nun haftalık teknoloji gündemi videosu için haber editörüsün.
Hedef kitle: Türkiye'deki üniversite öğrencileri (çoğu bilgisayar/yazılım/mühendislik).
Her aday haberi 0-10 arası puanla:
- 8-10: Öğrencinin bu hafta bir şey yapabileceği haberler (başvuru, ücretsiz araç/kota, yarışma, staj, açık kaynak sürüm) veya sektörü belirgin değiştiren büyük duyurular.
- 5-7: Geliştiricilerin bilmesi gereken önemli ürün/teknoloji haberleri.
- 0-4: Tüketici ürün incelemeleri, kampanyalar, magazin, yatırım/borsa, tekrar eden veya belirsiz haberler.
Google/Android/Chrome/Firebase/Gemini geliştirici haberlerine (GDG kitlesi) hafif öncelik ver, ama önemli olmayanı şişirme.
Özetlerde yalnızca başlık ve özetteki bilgileri kullan; tahmin ekleme. Her aday için tam bir kayıt döndür.

## Girdi

Aday haberler:

[0] (TÜBİTAK Duyuruları, tr, 2026-11-05) TÜBİTAK Bilim Söyleşileri 2026 Yılı Başvurularının Süresi Uzatıldı — TÜBİTAK Bilim Söyleşileri 2026 Yılı Başvurularının Süresi Uzatıldı utku.cetin Per, 11/05/2026 - 17:46 TÜBİTAK Bilim ve Toplum Başkanlığı tarafından yürütülen TÜBİTAK Bilim Söyleşileri’nin başvuru süresi uzatılmıştır. TÜBİTAK Bilim ve Toplum Başkanlığı tarafından yürütülen Bilim S
[1] (TÜBİTAK Duyuruları, tr, 2026-11-04) 2244–Sanayi Doktora Programı 2026 Yılı Çağrısı Açıldı — 2244–Sanayi Doktora Programı 2026 Yılı Çağrısı Açıldı utku.cetin Çar, 11/04/2026 - 19:40 Sanayide doktoralı araştırmacı istihdamının teşvik edilmesini amaçlayan 2244-Sanayi Doktora Programı çağrısı açılmıştır. Sanayide ihtiyaç duyulan doktora derecesine sahip nitelikli insan kayn
[2] (TÜBİTAK Duyuruları, tr, 2026-11-03) 2549–Polonya Ulusal Araştırma ve Geliştirme Merkezi (NCBR) ile İkili İşbirliği Programı Başvuru Sonuçları Açıklandı — 2549–Polonya Ulusal Araştırma ve Geliştirme Merkezi (NCBR) ile İkili İşbirliği Programı Başvuru Sonuçları Açıklandı utku.cetin Sa, 11/03/2026 - 10:41 TÜBİTAK ve NCBR (Polonya) arasında açılan çağrı sonucunda 7 projenin desteklenmesine karar verildi. 2549–Polonya Ulusal Araştırma 
[3] (TÜBİTAK Duyuruları, tr, 2026-11-02) 2247-C Stajyer Araştırmacı Burs Programı (STAR) 2026 Yılı 2. Dönem STAR Lisans ve STAR Öğretmen Çağrıları Açıldı — 2247-C Stajyer Araştırmacı Burs Programı (STAR) 2026 Yılı 2. Dönem STAR Lisans ve STAR Öğretmen Çağrıları Açıldı utku.cetin Pzt, 11/02/2026 - 10:05 STAR Programı 2026 yılı 2. dönem çağrısı kapsamında lisans öğrencileri ve öğretmen başvuruları açılmıştır. TÜBİTAK Bilim İnsanı Dest
[4] (TÜBİTAK Duyuruları, tr, 2026-11-02) Bilimfest Samsun — Bilimfest Samsun Bilimfest SAMSUN: Havacılık ve Robot Sistemleri Keşif İstasyonları projesi, 22. yüzyılın dijital dönüşüm sürecine gençlerin ve toplumun etkin bir şekilde uyum sağlamasını hedefleyen kapsamlı bir bilim festivalidir. Havacılık ve uzay ile robotik teknolojilerin gün
[5] (Google Developers Blog, en, 2026-11-06) Agent Distraction — Analysis of over 913,000 coding agent sessions reveals that 13% expose agents to inline TODO(b/...) comments. In 6% of encounters, agents act on these comments, with 83% being entirely unprompted by the developer. These detours result in significant overhead—adding 70% more steps
[6] (Google Developers Blog, en, 2026-11-03) Cost per task: Using cheap classifiers to route across Gemini models and thinking levels — Per-token API prices keep falling, yet engineering bills for autonomous coding agents keep climbing....
[7] (Android Developers Blog, en, 2026-11-06) Build for an expanding lineup of Android XR devices with production-ready tools from Android Developer Summit — From full immersion at home to glanceable experiences on the go, building on Android XR lets you meet users at any moment across the entire spectrum of spatial applications. At Android Developer Summit, we marked an exciting milestone with the launch of XREAL AURA.
[8] (Android Developers Blog, en, 2026-11-05) What’s new in intelligent apps at the Android Developer Summit — In the intelligence era, users are no longer just tapping through apps, they express high-level goals and expect AI agents like Gemini to complete multi-step workflows, sometimes across multiple apps on their devices.
[9] (Android Developers Blog, en, 2026-11-04) Build for every screen with the latest Jetpack Compose updates from Android Developer Summit — The Android ecosystem is a multi-device reality that spans phones, foldables, tablets, wearables, in-car displays, XR, and Googlebook. In this landscape, adaptive development is foundational to reaching users wherever they are.
[10] (Android Developers Blog, en, 2026-11-02) Developing for Today: 50+ New Developer Sessions on Building Apps Today — Over 900 attendees joined our event spaces for a keynote about our outlook on the future, demo sessions, dozens of workshops, a hackathon, and for community discussions focused on ideas and feedback on Android platform.
[11] (GitHub Blog, en, 2026-11-06) Beyond code generation: A developer’s guide to agentic engineering — Writing code got faster. The work around it didn't. See how you can plan, write code, review changes, and investigate production issues with GitHub Copilot, and what work still needs your judgment. The post Beyond code generation: A developer’s guide to agentic engineering appear
[12] (GitHub Blog, en, 2026-11-05) Inside GitHub’s new Git storage architecture — GitHub's new Git storage architecture is built so thousands of agents can push to a single repository at once. Here's how it works. The post Inside GitHub’s new Git storage architecture appeared first on The GitHub Blog .
[13] (GitHub Blog, en, 2026-11-05) Accessibility statements now have a home on GitHub — GitHub now highlights ACCESSIBILITY.md files and helps maintainers document accessibility goals, known barriers, supported environments, contributor expectations, and reporting processes. The post Accessibility statements now have a home on GitHub appeared first on The GitHub Blo
[14] (GitHub Blog, en, 2026-11-03) Arnis turns any place on Earth into a Minecraft world — Louis Erbkamm built the first prototype in his free time. Now GitHub Copilot helps him maintain it alone. The post Arnis turns any place on Earth into a Minecraft world appeared first on The GitHub Blog .
[15] (GitHub Blog, en, 2026-11-01) Game Off 2026: The theme is SHIFT — GitHub’s annual month-long game jam is back for its 14th year! This November, make a game inspired by the theme SHIFT. Change gears, swap perspectives, bend reality, or just press a certain key. The post Game Off 2026: The theme is SHIFT appeared first on The GitHub Blog .
[16] (Google Blog, en, 2026-11-05) Generate longer AI videos with Omni 1.2 Flash in Google Vids at no cost. — Omni 1.2 Flash in Google Vids
[17] (Google Blog, en, 2026-11-05) Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips — Text "Gemini Introducing Gemini Omni 1.2 Flash" surroudned by images of a beehive, animals in conversation, a squid, and a woman walking down a street
[18] (Google Blog, en, 2026-11-05) Investing in Wyoming’s infrastructure, energy and workforce — Community members playing with a pumpkin
[19] (Google Blog, en, 2026-11-05) Transform a quick drawing into a live app with Gemini. — Turn your sketches into functional apps using Gemini. Upload your drawings to the Canvas tool to generate and refine code instantly. Try it now.
[20] (Google Blog, en, 2026-11-05) Check out our free livestream during National Veterans Small Business Week. — Join our November 2026 YouTube livestream for National Veterans Small Business Week. Master AI skills with Gemini and get 1:1 coaching. Register today.
[21] (Google Blog, en, 2026-11-04) Watch Henry Cavill build a video game on his Googlebook — The video shows the making of Henry Cavill's game, “Mustache Protocol."
[22] (Google Blog, en, 2026-11-04) We're sharing our framework for building safer and more helpful AI for health. — Many of us have turned to AI with a health question or received care from a doctor who’s using it. The adoption of technology for health is accelerating and impacts bill…
[23] (Google Blog, en, 2026-11-04) Take a closer look at art with the Courtauld — Experts from the Courtauld discuss their digital partnership with Google Arts & Culture, demonstrating how ultra-high-resolution imagery brings gallery masterpieces into focus. Focusing on works like Paul Cézanne's still life, they explore hidden brushstr
[24] (Google Blog, en, 2026-11-03) Designing responsible AI for learning — A teacher pointing at a student's Chromebook screen while the student observes.
[25] (Google Blog, en, 2026-11-03) New research shows how Guided Learning supports students — Four students huddled in a circle, all looking at a laptop together
[26] (Google Blog, en, 2026-11-03) We’re providing funding for organizations building AI for teachers. — Google.org is funding five organizations to build AI tools for teachers. See how these initiatives support educators and students. Get the details.
[27] (Google Blog, en, 2026-11-03) Working collaboratively to fight scams in Asia Pacific — A woman using her smartphone, surrounded by graphic icons representing online security, privacy, and message alerts.
[28] (Google Blog, en, 2026-11-03) AI in the learning era — Read announcements from Google’s 2026 AI in the Learning Era event.
[29] (Google Blog, en, 2026-11-03) Expanding AI educator training to new countries — An illustration featuring a stylized globe in the center with network lines connecting points across the world to various colorful icon badges, including graduation caps, award ribbons, and stylized figures.
[30] (Google Blog, en, 2026-11-03) Advancing research and partnering with universities in Singapore — A light beam is focused through a lens into thin wires that pass through panels featuring increasingly complex patterns of blue dots, dashes, and other geometric shapes. The Google G is on the bottom left corner.
[31] (Hugging Face Blog, en, 2026-11-06) ToyBlocks: A controlled world for robot learning and evaluation — 
[32] (Hugging Face Blog, en, 2026-11-06) Egyptian and Nigerian English join the Open ASR Leaderboard — 
[33] (Hugging Face Blog, en, 2026-11-05) New NVIDIA Cosmos 3 Open Models for Interactive World Simulation — 
[34] (Hugging Face Blog, en, 2026-11-05) A Closer Look at Phonon TTS. Launching High-Quality On-Device Speech That Tops the Benchmarks. — 
[35] (Hugging Face Blog, en, 2026-11-04) Dharma Field Extractor: Any Document In, Structured Fields in JSON Out — 
[36] (Hugging Face Blog, en, 2026-11-03) Palette: teaching a small model to build decks in your design language — 
[37] (Hugging Face Blog, en, 2026-11-03) CWE-bench v2: More coverage, quality, and transparency — 
[38] (Hugging Face Blog, en, 2026-11-03) Transformers Model Integration Contracts — 
[39] (OpenAI News, en, 2026-11-06) Partnering with Hacktron to find vulnerabilities in OpenAI’s systems — OpenAI is partnering with Hacktron to find vulnerabilities, test connections with third-party services, and strengthen defenses with frontier AI.
[40] (OpenAI News, en, 2026-11-06) Measuring how AI agents handle everyday wet-lab science — OpenAI introduces BioBasicsBench, a 100-task benchmark measuring how well AI agents interpret raw experimental data and handle everyday wet-lab science.
[41] (OpenAI News, en, 2026-11-05) Australian universities are creating AI-native graduates — Australian universities are expanding access to ChatGPT and bringing AI into teaching and learning to prepare students for an AI-enabled workforce.
[42] (OpenAI News, en, 2026-11-05) Cult.fit builds operational muscle with Codex — Cult.fit is using Codex to help teams across functions build tools, move faster, and change how work gets done.
[43] (OpenAI News, en, 2026-11-05) GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents — Introducing GPT‑6 Cyber, OpenAI’s cybersecurity model for finding exploitable vulnerabilities and developing fixes, trained to stay within authorized scope.
[44] (OpenAI News, en, 2026-11-05) Merge builds product and business tools with OpenAI technology — Merge uses GPT-6 Astra, ChatGPT, and Codex to review product code and support marketing. Its teams also use AI to plan executive dinners and prepare sales updates.
[45] (OpenAI News, en, 2026-11-05) Setting a new standard for responsible AI infrastructure — OpenAI introduces its National Community Compact and Compute Campus Policy Blueprint to protect local resources, create jobs, and guide responsible AI infrastructure development.
[46] (OpenAI News, en, 2026-11-05) Flipsnack grows product signups with conversion optimization — Flipsnack focused its ChatGPT Ads campaigns on getting people to try its product, growing registrations while lowering the cost per signup.
[47] (OpenAI News, en, 2026-11-05) Franklin Templeton uses OpenAI to support investment research — Starting with equity research, Franklin Templeton is developing AI workflows to help portfolio managers compare research views and examine investment risks.
[48] (OpenAI News, en, 2026-11-04) OpenAI to acquire Pierre Computer Company, Inc. — OpenAI will acquire Pierre Computer Company, expanding Codex’s tools for building, understanding, and reviewing code.
[49] (OpenAI News, en, 2026-11-04) Daybreak Red is now available in AWS GovCloud (US-East) — Daybreak Red brings GPT-5.6 Cyber to approved customers in AWS GovCloud (US-East) through Amazon Bedrock for authorized cybersecurity work.
[50] (OpenAI News, en, 2026-11-04) A thousand fewer paths to root — OpenAI built an autonomous pipeline that found, validated, and generated patches for 948 local privilege-escalation vulnerabilities in the Linux kernel.
[51] (OpenAI News, en, 2026-11-04) Introducing Images 2.6 — Images 2.6 brings faster image generation, GIF creation, more precise editing, and new API controls across ChatGPT, Codex, and the API.
[52] (OpenAI News, en, 2026-11-04) DevRev delivers autonomous self-service with GPT-6.1 Sol — DevRev uses GPT-6.1 Sol to power Computer and Operator, balancing reasoning, speed, and cost for enterprise service.
[53] (OpenAI News, en, 2026-11-03) Accelerating engineering for the physical world — Discover how ChatGPT and Codex are helping engineers accelerate CAD, PCB design, simulation, and other workflows across the physical world.
[54] (Google DeepMind, en, 2026-11-03) Agentic cheminformatics with Google Antigravity — Learn how Google Antigravity and our Cheminformatics Skills accelerate drug discovery workflows, search compounds, and propose novel rigidified macrocycles.
[55] (Webrazzi, tr, 2026-11-06) Dropbox, Tigris Data'yı 350 milyon dolara satın alıyor — Dropbox, bulut depolama şirketi Tigris Data'yı 350 milyon dolar karşılığında satın almak üzere anlaşmaya vardığını duyurdu. İşlemin 2026'nın dördüncü çeyreğinde tamamlanması bekleniyor. Anlaşma tamaml...
[56] (Webrazzi, tr, 2026-11-06) Shield AI, radar üreticisi Echodyne'i 5,3 milyar dolara satın alıyor — ABD merkezli savunma teknolojisi şirketi Shield AI, insansız hava araçlarını tespit ve takip etmek için radar sistemleri geliştiren Echodyne'i satın almak üzere anlaşmaya vardı. Anlaşma kapsamında işl...
[57] (Webrazzi, tr, 2026-11-06) TikTok, TikTok Shop için bağımsız alışveriş uygulamasını kullanıma sundu — TikTok, alışveriş hizmeti TikTok Shop’u ana uygulamasından ayırarak bağımsız bir mobil uygulama olarak kullanıma sundu. iOS ve Android’de yayınlanan uygulama şu aşamada Singapur, Malezya, Tayland ve F...
[58] (Webrazzi, tr, 2026-11-06) Drone teslimat girişimi Zipline, 1,5 milyar dolar yatırım aldı — Drone teslimat girişimi Zipline, 1,5 milyar dolar yatırım aldı.Yatırım turuna Paradigm, WCM Investment Management ve Layer Global liderlik etti. Yatırım turuna ayrıca Valor Equity Partners, Fidelity M...
[59] (Webrazzi, tr, 2026-11-06) Instagram Edits artık Mac'te kullanılabiliyor — Instagram’ın video düzenleme uygulaması Edits, mobil sürümünün ardından Mac kullanıcıları için de kullanıma açıldı. Daha büyük ekran ve klavye-fare kontrolüyle kapsamlı video projelerini düzenlemeyi h...
[60] (Webrazzi, tr, 2026-11-06) Meta, Muse için gerçek zamanlı sesli sohbet ve hareketli avatar özelliklerini ABD'de kullanıma sundu — Meta, yapay zeka asistanı Muse için gerçek zamanlı sesli sohbet ve hareketli avatar özelliklerini ABD'deki kullanıcıların erişimine açtı. Yeni özellikle birlikte kullanıcılar, Muse'un yapay zeka avata...
[61] (Webrazzi, tr, 2026-11-06) Google, 15 saniyelik video ve yüzde 30 daha düşük fiyatla öne çıkan Gemini Omni 1.2 Flash'i tanıttı — Google, yapay zeka destekli video üretim modeli Gemini Omni 1.2 Flash'i duyurdu. Yeni model; 15 saniyeye kadar video oluşturma, konuşarak video düzenleme, referans görsellere daha yüksek bağlılık ve d...
[62] (Webrazzi, tr, 2026-11-06) The New York Times, Letterboxd'ı 330 milyon dolara satın almak için görüşüyor — The New York Times Company, sinemaseverlere yönelik sosyal ağ Letterboxd'ı yaklaşık 330 milyon dolara satın almak için görüşüyor. The New York Times'ın görüşmelere aşina iki kişiye dayandırdığı haberi...
[63] (Webrazzi, tr, 2026-11-06) Claude, banka hesaplarına bağlanarak harcamaları analiz edecek — Anthropic, yapay zeka asistanı Claude'a banka ve kredi kartı hesaplarını bağlamaya olanak tanıyan Personal Finance özelliğini ekledi. Kullanıcılar, finansal hesaplarını Plaid üzerinden bağladıktan son...
[64] (Webrazzi, tr, 2026-11-05) Akıllı TV işletim sistemi geliştiren Titan OS, 46 milyon dolar yatırım aldı — Barselona merkezli akıllı TV işletim sistemi geliştiricisi Titan OS, 46 milyon dolar finansman sağladığını duyurdu. Öz sermaye yatırımı ve borç finansmanından oluşan tura, BlackRock tarafından yönetil...
[65] (Webrazzi, tr, 2026-11-05) Apple, çalışanlarının yapay zeka kullanım bütçelerini düşürüyor — Apple, çalışanlarının yapay zeka araçları için kullanabildiği günlük bütçeleri azaltmaya başladı. Bloomberg'ün aktardığı bilgilere göre şirket, maliyetleri kontrol altına alma çalışmaları kapsamında b...
[66] (Webrazzi, tr, 2026-11-05) Spotify'ın sesli kitap hizmeti Türkiye'de kullanıma sunuldu — Spotify, sesli kitap hizmetini Türkiye’de kullanıma sundu. Şirketin 350 binden fazla sesli kitaptan oluşan kataloğu, 5 Kasım itibarıyla Türkiye’deki kullanıcıların erişimine açıldı. Türkiye lansmanı, ...
[67] (Webrazzi, tr, 2026-11-05) Apple, MacBook Neo 2 satışlarını ikiye katlamayı hedefliyor — Apple’ın MacBook Neo serisi için 2027 beklentisi, ilk modelin gördüğü talebin ardından yükseliyor. DigiTimes’ın tedarik zinciri kaynaklarına dayandırdığı habere göre Apple, tedarikçileriyle 2027 yılın...
[68] (Webrazzi, tr, 2026-11-05) Revolut'un değerlemesi 115 milyar dolara yükseldi — Fintech şirketi Revolut, yeni bir ikincil hisse satışı sonucunda 115 milyar dolar değerlemeye ulaştı. Şirket, Kasım 2025'te gerçekleştirilen önceki hisse satışında 75 milyar dolar değerleme elde etmiş...
[69] (Webrazzi, tr, 2026-11-05) App Store'da geliştiriciler, aboneliğini iptal etmek isteyen kullanıcılara indirim sunabilecek — Apple, App Store üzerinden aboneliğini iptal etmek isteyen kullanıcılara yönelik yeni bir özelliği kullanıma sundu. Uygulama geliştiricileri, kullanıcılar iptal işlemini tamamlamadan önce aboneliğin a...
[70] (Cloudflare Blog, en, 2026-11-06) The post-quantum future of web privacy — Cryptographic protocols like Privacy Pass help keep web sites safe from abuse while keeping their users private. This post looks at the quantum threat to these protocols, and some new post-quantum cryptography that may help close the gap.
[71] (Cloudflare Blog, en, 2026-11-05) Agents aren’t humans (but they kinda are) — AI agents act for millions, but servers see intermediaries that strip user visibility. This post defines the problem space and introduces a collaborative approach to safely identifying, allowing, and managing this automated traffic.
[72] (Cloudflare Blog, en, 2026-11-04) See the agents, set the terms: new visibility and control for personal agents — Personal AI agents have changed how users interact with the web, blurring the lines between automated and human traffic. Learn how Cloudflare gives site owners visibility and control to manage personal agent access.
[73] (Cloudflare Blog, en, 2026-11-03) Introducing Zero Wire, a hub for investigating critical Internet vulnerabilities — Zero Wire on Cloudflare Radar pairs plain-language briefings with global attack telemetry and remediation steps. Triage critical CVEs faster and decide how to protect your infrastructure.
[74] (Cloudflare Blog, en, 2026-11-02) How we halved DNS build delay and cut memory use by 85% — Zone setting changes used to rebuild entire DNS zones, even ones with tens of millions of records. Here is how we built a planner that picks the smallest safe build, cutting full builds by 40%, peak memory by 85%, and halving build delay.
[75] (Hacker News (100+ puan), en, 2026-11-07) The $8 Linux Computer (2022) — Article URL: http://thelittleengineerthatcould.blogspot.com/2022/12/the-8-linux-computer.html Comments URL: https://news.ycombinator.com/item?id=50404599 Points: 104 # Comments: 46
[76] (Hacker News (100+ puan), en, 2026-11-07) Upload Your RAM — Article URL: https://uploadyourram.org Comments URL: https://news.ycombinator.com/item?id=50403214 Points: 248 # Comments: 229
[77] (Hacker News (100+ puan), en, 2026-11-07) Every Mac comes with an (undocumented) family member classifier — Article URL: https://8rank.ai/game/apple-intelligence-personal-knowledge-graph Comments URL: https://news.ycombinator.com/item?id=50403097 Points: 405 # Comments: 233
[78] (Hacker News (100+ puan), en, 2026-11-07) Running a law firm on Free software — Article URL: https://decoded.legal/blog/2026/11/running-a-law-firm-on-free-software-2026-edition/ Comments URL: https://news.ycombinator.com/item?id=50403066 Points: 131 # Comments: 61
[79] (Hacker News (100+ puan), en, 2026-11-07) Need for Speed Underground 2 online in the browser — Article URL: https://nfsu2.xyz/ Comments URL: https://news.ycombinator.com/item?id=50403052 Points: 486 # Comments: 151
[80] (Hacker News (100+ puan), en, 2026-11-07) The Components of Agent Memory — Article URL: https://www.anthropic.com/research/components-of-agent-memory Comments URL: https://news.ycombinator.com/item?id=50402212 Points: 112 # Comments: 62
[81] (Hacker News (100+ puan), en, 2026-11-07) A barbarian tribe's mythic origin story is true, ancient DNA reveals — Article URL: https://www.science.org/content/article/barbarian-tribe-s-mythic-origin-story-true-ancient-dna-reveals Comments URL: https://news.ycombinator.com/item?id=50401740 Points: 164 # Comments: 146
[82] (Hacker News (100+ puan), en, 2026-11-06) RealPage rent-pricing case wraps with nearly $360M to renters — Article URL: https://www.multifamilydive.com/news/realpage-rent-pricing-case-360m-renters/873553/ Comments URL: https://news.ycombinator.com/item?id=50399991 Points: 162 # Comments: 127
[83] (Hacker News (100+ puan), en, 2026-11-06) Libghostty 1.0 — Article URL: https://mitchellh.com/writing/libghostty-1-0 Comments URL: https://news.ycombinator.com/item?id=50399933 Points: 908 # Comments: 149
[84] (Hacker News (100+ puan), en, 2026-11-06) A Jev that can ask Opus for help gives Opus accuracy at 4x lower cost — Article URL: https://hightouch.com/blog/llm-judges-identity-resolution Comments URL: https://news.ycombinator.com/item?id=50397429 Points: 543 # Comments: 136
[85] (Hacker News (100+ puan), en, 2026-11-06) Firecracker VM Escape: PwnEscape Part 2 — Article URL: https://pwn.ai/blog/firecracker-escape Comments URL: https://news.ycombinator.com/item?id=50397219 Points: 268 # Comments: 115
[86] (Hacker News (100+ puan), en, 2026-11-06) Notes on San Marino — Article URL: https://mattlakeman.org/2026/11/05/notes-on-san-marino/ Comments URL: https://news.ycombinator.com/item?id=50395183 Points: 115 # Comments: 46
[87] (Hacker News (100+ puan), en, 2026-11-06) Tesla to wind down Cybertruck production — Article URL: https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817 Comments URL: https://news.ycombinator.com/item?id=50391456 Points: 1108 # Comments: 1979
[88] (Hacker News (100+ puan), en, 2026-11-06) US FAA says it will phase out floppy disks from air traffic control by 2028 — Article URL: https://www.reuters.com/world/us/us-faa-says-it-will-phase-out-floppy-disks-air-traffic-control-by-2028-2026-11-05/ Comments URL: https://news.ycombinator.com/item?id=50388001 Points: 377 # Comments: 315
[89] (Hacker News (100+ puan), en, 2026-11-04) Greece has its own Pompeii: Thera buried Akrotiri in ash 17th-16th century BCE — Article URL: https://www.smithsonianmag.com/history/greece-has-its-own-pompeii-and-the-ruins-tell-a-captivating-story-of-a-sophisticated-seafaring-bronze-age-society-180989747/ Comments URL: https://news.ycombinator.com/item?id=50360810 Points: 170 # Comments: 25
[90] (Webtekno, tr, 2026-11-07) OMODA ve JAECOO Fiyat Listesi - Kasım 2026 — Kasım 2026 OMODA ve JAECOO fiyat listesi açıklandı. OMODA 7, OMODA 5 ve JAECOO 7 modellerinin güncel fiyatları Webtekno'da!
[91] (Webtekno, tr, 2026-11-07) Audi, Çin'e Özel Otomobillerinde Neden Dört Halkalı Logosunu Kullanmıyor? — Audi, Çin pazarına özel elektrikli otomobillerinde klasik dört halkalı logosu yerine neden AUDI yazısını tercih ediyor? Audi'nin bu stratejisinin arkasındaki nedeni açıklıyoruz.
[92] (Webtekno, tr, 2026-11-07) Epic Games Bir Oyunu Daha Ücretsiz Sunuyor: Hızlı Aksiyon ve Arcade Severler Buraya! — Epic Games, synthwave temalı hızlı aksiyon ve arcade oyunu GMH - Good Morning Human'ı ücretsiz olarak kullanıcılara sunuyor.
[93] (Webtekno, tr, 2026-11-06) Az Sorun Çıkaran 5 Otomatik Şanzıman — Kolay kolay bozulmayan ve arıza yaptığında tamiri daha uygun fiyatlı olan 5 otomatik şanzımanı inceliyoruz.
[94] (Webtekno, tr, 2026-11-06) GTA 6 Ön Siparişleri Rekora Koşuyor: PlayStation Satışları Xbox'ı Katladı! — GTA 6 ön siparişleri 8 milyona yaklaşırken satışların %74'ünü elinde tutan PlayStation, Xbox'a ezici bir üstünlük sağladı.
[95] (Webtekno, tr, 2026-11-06) Motorola’nın Yeni Amiral Gemisi Signature 27 Tanıtıldı: İşte Özellikleri ve Fiyatı — Motorola, yeni amiral gemisi Signature 27 modelini tanıttı. Telefonun özellikleri ve fiyatı belli oldu.
[96] (Webtekno, tr, 2026-11-06) Claude Artık Harcamalarınızı Analiz Edebiliyor: İşte Yeni Kişisel Finans Özelliği! — Anthropic, kullanıcıların banka hesaplarını bağlayarak harcamalarını analiz etmesini sağlayan yeni "Kişisel Finans" aracını duyurdu.
[97] (Webtekno, tr, 2026-11-06) Mercedes Çok Erken Davrandığı Bir Konuda Geri Adım Attı — Mercedes-Benz, sınırlı kalan Seviye 3 otonom sürüşten geri adım atarak odağını gelişmiş Seviye 2 sistemlerine ve 2030 sonrası Seviye 4'e çevirdi.
[98] (Webtekno, tr, 2026-11-06) Tesla Cybertruck İçin Yolun Sonu: Üretim Resmen Sona Eriyor! — Tesla, düşen satışların ardından Cybertruck üretimini durdurarak fabrikada sürücüsüz robotaksi Cybercab için yer açacağını açıkladı.
[99] (Webtekno, tr, 2026-11-06) Samsung’da Prim Gerginliği: Çalışanlar Eyleme Başladı! — Samsung'un cihaz birimi çalışanları, yarı iletken ekibine tanınan tavan sınırlamasız primlerden yararlanma talebiyle eylem başlattı.
[100] (Webtekno, tr, 2026-11-06) Patenti Alındı: Hyundai’den Elektrikli Araçların Menzilini Artıracak Mühendislik Harikası Teknoloji — Hyundai ve Kia, yüksek hızlarda kolları arasındaki boşlukları kapatan bir jant tasarımının patentini aldı. Hareketli kanatçıklarla hava direncini azaltmayı amaçlayan sistem, frenlerin soğutulması gerektiğinde yeniden açılabiliyor.
[101] (Webtekno, tr, 2026-11-06) Tesla’nın Uçan Arabası Roadster’dan Yeni Video Geldi! — Tesla, Roadster’ın iticilerle yerden yükselip takla attığı gösterinin araç içi görüntülerini paylaştı.
[102] (Webtekno, tr, 2026-11-06) Nothing, Yeni Yapay Zekâ Cihazını Duyurdu: İlk Görsel Geldi — Nothing, ekranı olmayan ilk bağımsız yapay zekâ cihazını aralık ayında piyasaya süreceğini duyurdu.
[103] (ShiftDelete.Net, tr, 2026-11-07) Solar Roof davasında Tesla aleyhine karar — Tesla Solar Roof davasında California'daki hakim, delilleri defalarca vermeyen Tesla'yı dolandırıcılıktan sorumlu tuttu. Ev sahibi onarımın 2,5 milyon dolardan fazlaya mal olacağını söylüyor.
[104] (ShiftDelete.Net, tr, 2026-11-07) Instagram Silinen Mesajları Geri Getirme Yolları — Instagram DM için resmi geri yükleme yok ve Son silinenler 30 gün tutsa da mesajları kapsamıyor. Silinen mesaja hangi 3 durumda hala ulaşılabileceğini anlattık.
[105] (ShiftDelete.Net, tr, 2026-11-07) Telefon işlemcisi pazarı yüzde 21 küçüldü — Counterpoint verilerine göre telefon işlemcisi pazarı 2026'nın üçüncü çeyreğinde yüzde 21 küçüldü. MediaTek ve Qualcomm pay kaybederken Apple ile Samsung yükseldi.
[106] (ShiftDelete.Net, tr, 2026-11-07) Jensen Huang'a casus Çin istihbaratından çıktı — Jensen Huang casus iddiasında yeni ayrıntılar geldi. NVIDIA CEO'sunu izlediği öne sürülen Alice Huang'ı Çin'in Devlet Güvenlik Bakanlığı'nın devşirdiği bildirildi.
[107] (ShiftDelete.Net, tr, 2026-11-07) iOS 27'de kilitlenince HDMI görüntüsü kesiliyor — iOS 27 HDMI sorunu, iPhone'u televizyona ya da AR gözlüğe bağlayan kullanıcıları etkiliyor. Ekran kilitlenince YouTube ve Netflix yayını kesiliyor.
[108] (ShiftDelete.Net, tr, 2026-11-07) Instagram Şifre Değiştirme: Telefon ve Bilgisayar — Telefon ve bilgisayarda 2026 adımları değişti: mevcut şifreniz varsa Hesaplar Merkezi, unuttuysanız sıfırlama bağlantısı kullanılmalı. Peki hangi yol doğru?
[109] (ShiftDelete.Net, tr, 2026-11-07) Xbox Cloud Gaming'de telefon kontrolcü olacak — Microsoft, Xbox Cloud Gaming için telefonları kontrolcüye çeviren yeni bir özelliği test ediyor. QR kodla çalışan sistem, ayrı uygulama gerektirmiyor.
[110] (ShiftDelete.Net, tr, 2026-11-07) Starlink kapasitesi üç yılda 100 kat artacak — Elon Musk, Starlink kapasitesinin iki ila üç yıl içinde yaklaşık 100 kat artacağını söyledi. Ağın toplam kapasitesi 800 Tbit/s seviyesinden 80 Pbit/s seviyesine çıkabilir.
[111] (ShiftDelete.Net, tr, 2026-11-07) Epic Games Store Linux desteği geliyor — Epic Games Store Linux desteği için çalışmalara başlandı. Şirket, SteamOS dahil çok sayıda dağıtımı hedefliyor ancak resmi bir çıkış tarihi henüz paylaşılmadı.
[112] (ShiftDelete.Net, tr, 2026-11-07) Çin sıvı hava enerji depolama tesisini açtı — Çin, Qinghai eyaletinde kurduğu 60 MW/600 MWh kapasiteli sıvı hava enerji depolama tesisini 30 Ekim'de şebekeye bağladı. Tesis 10 saat kesintisiz elektrik verebiliyor.
[113] (ShiftDelete.Net, tr, 2026-11-07) WhatsApp Sohbet Önizleme Android'de Testte — Android beta 2.26.44.12 bulgularına göre 5 Kasım'da uzun basınca son mesajlar kartta görünebilir; mavi tik tetiklenmeyebilir. Türkiye'de ne zaman açılır?
[114] (ShiftDelete.Net, tr, 2026-11-07) Honda RN0 elektrikli dağ bisikleti tanıtıldı — Honda RN0, şirketin ilk üst seviye elektrikli dağ bisikleti olarak EICMA 2026'da Milano'da tanıtıldı. Bisiklet, ROTWILD ortaklığıyla geliştirildi.
[115] (ShiftDelete.Net, tr, 2026-11-07) Xbox Series'e FSR 4.1.2 desteği geldi — AMD, makine öğrenimi tabanlı ölçekleyicisi FSR 4.1.2'yi Xbox Series X ve Series S için kullanıma sundu. Geliştiriciler iki farklı model arasından seçim yapabilecek.
[116] (ShiftDelete.Net, tr, 2026-11-07) PS5 neslinin en çok kazandıran 10 oyunu — Alinea Analytics, PS5 neslinin en çok kazandıran oyunları listesini paylaştı. God of War: Ragnarok 1,4 milyar dolarla zirvede, ilk 10 oyun toplam 6,5 milyar dolar getirdi.
[117] (DonanımHaber, tr, 2026-11-07) DJI Matrice 5T, LiDAR ve 176x zoom ile tanıtıldı — DJI Matrice 5T, LiDAR, termal kamera, 176x hibrit zoom ve 59 dakikalık uçuş süresiyle endüstriyel görevleri hedefliyor. İşte yeni nesil drone'un özellikleri ve fiyatı:
[118] (DonanımHaber, tr, 2026-11-07) Google için yapay zeka paradoksa dönüştü — Google yapay zeka aramalarında büyüme kaydederken reklam gelirlerinde yavaşlama yaşıyor. Şirket, yüz milyarlarca dolarlık yatırımlarının karşılığını henüz alamıyor.
[119] (DonanımHaber, tr, 2026-11-07) Samsung Galaxy Buds On, Ocak ayında Türkiye'ye gelebilir — Samsung Galaxy Buds On kulaklıklarının Avrupa ve Türkiye çıkış tarihi için Ocak ayı işaret ediliyor. İşte klipsli tasarım, Bluetooth 6.2 ve 38 saate ulaşan pil ömrüyle yeni modelin ayrıntıları:
[120] (DonanımHaber, tr, 2026-11-07) Sodyum iyon bataryalar maliyette LFP bataryaları yakaladı — Sodyum iyon bataryalar, 2026 sonunda hücre maliyetinde LFP teknolojisini yakalamaya hazırlanıyor. Sodyum iyon bataryaların uzun vadede LFP’ye göre daha avantajlı olduğu bildirildi.
[121] (DonanımHaber, tr, 2026-11-07) Alphabet'ten Qualcomm'a dev yatırım: Hedef yapay zeka veri merkezleri — Alphabet'in Qualcomm'a yaklaşık 548 milyon dolarlık yatırım yaptığı bildirildi. İşte yapay zeka veri merkezlerine yönelirken çip sektöründe yeni bir rekabet alanı oluşturacak yatırımın ayrıntıları:
[122] (DonanımHaber, tr, 2026-11-07) DJI Matrice 5T tanıtıldı: Gece görüşü, termal görüntüleme, 176x zoom — DJI, zifiri karanlıkta gerçekleştirilen kurtarma görevleri için tasarlanmış, her türlü hava koşuluna uygun dronunu tanıttı. DJI Matrice 5T, yaklaşık 10 saniye içinde uçuşa hazır hale geliyor.
[123] (DonanımHaber, tr, 2026-11-07) Akıllı telefon işlemci pazarında Qualcomm ve MediaTek kan kaybediyor — Bellek fiyatlarındaki hızlı yükseliş, akıllı telefon işlemci pazarında yüzde 21'lik sevkiyat düşüşüne neden oldu. MediaTek ve Qualcomm pazar payı kaybederken Apple ve Samsung yükselişe geçti.
[124] (DonanımHaber, tr, 2026-11-07) Android Auto'da sonsuz arama döngüsü: Gemini çıldırttı! — Bazı Android Auto kullanıcıları, kişinin adını belirtmelerine rağmen sistemin sürekli olarak kimi aramak veya kime mesaj göndermek istediğini sorduğunu ifade ediyor. Google, sorunu araştırıyor.
[125] (DonanımHaber, tr, 2026-11-07) Motorola Signature 27, DXOMARK kamera sıralamasında ikinci sıraya yerleşti — Motorola Signature 27, DXOMARK kamera testinden 173 puan alarak küresel sıralamada ikinci oldu. Yeni model, iPhone 18 Pro'yu geride bırakırken Huawei Pura 80 Ultra'nın yalnızca 2 puan gerisinde kaldı.
[126] (DonanımHaber, tr, 2026-11-07) Instagram Edits uygulaması macOS için yayınlandı — Dikey videoları kolay bir şekilde düzenleyerek Instagram platformunda veya başka platformlarda paylaşabildiğiniz Edits uygulaması artık masaüstünde de yerini aldı.
[127] (DonanımHaber, tr, 2026-11-07) One UI 10, Samsung'un en büyük arayüz güncellemesi olabilir — Samsung'un One UI 10 ile arayüzünde şimdiye kadarki en büyük değişiklikleri yapması bekleniyor. Şirketin, önemli yenilikleri One UI 9.5 yerine yeni sürüme sakladığı öne sürülüyor.
[128] (DonanımHaber, tr, 2026-11-07) Razer kablolu oyuncu kulaklığını duyurdu — Razer Hammerhead V3 Chroma kulak içi kulaklık modeli kablolu olmasının yanı sıra aktif gürültü engelleme ve özelleştirilebilir RGB aydınlatma ile dikkat çekiyor.
[129] (DonanımHaber, tr, 2026-11-07) Yenilenen Volkswagen Virtus'un ilk fotoğrafları yayınlandı — Volkswagen, sevilen sedan modeli Virtus’un makyajlı versiyonuna ait ilk görüntüleri paylaştı. 2022’den bu yana ilk kapsamlı güncellemesini alan modelin tazelenen dış tasarımı dikkat çekiyor.
[130] (DonanımHaber, tr, 2026-11-07) BİM marketler Monster oyuncu bilgisayarları satacak — 11 Kasım BİM Aktüel teknoloji ürünleri arasında Monster markasına ait Abra V22.5.3 dizüstü bilgisayar ve Tulpar TD3 V1.2.3.3 oyuncu kasası yer alıyor. Ürünler kasada sipariş veriliyor.

## Yanıt şeması (JSON Schema)

```json
{
 "$defs": {
  "Score": {
   "properties": {
    "id": {
     "title": "Id",
     "type": "integer"
    },
    "score": {
     "description": "0-10: Türk üniversite öğrencileri (özellikle bilgisayar/mühendislik) için ilgi ve fayda",
     "title": "Score",
     "type": "integer"
    },
    "category": {
     "enum": [
      "ai",
      "developer",
      "mobile",
      "web",
      "hardware",
      "security",
      "career",
      "opportunity",
      "science",
      "other"
     ],
     "title": "Category",
     "type": "string"
    },
    "reason": {
     "description": "Puan gerekçesi, Türkçe, en fazla 15 kelime",
     "title": "Reason",
     "type": "string"
    },
    "summary_tr": {
     "description": "Haberin Türkçe özeti, en fazla 30 kelime, yalnızca verilen bilgilere dayan",
     "title": "Summary Tr",
     "type": "string"
    }
   },
   "required": [
    "id",
    "score",
    "category",
    "reason",
    "summary_tr"
   ],
   "title": "Score",
   "type": "object"
  }
 },
 "properties": {
  "scores": {
   "items": {
    "$ref": "#/$defs/Score"
   },
   "title": "Scores",
   "type": "array"
  }
 },
 "required": [
  "scores"
 ],
 "title": "ScoreList",
 "type": "object"
}
```
