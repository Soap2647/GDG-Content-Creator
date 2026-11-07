# Görev: score

Yanıtı `episodes/2026-W44/llm/score.response.json` dosyasına, aşağıdaki JSON şemasına uyan TEK bir JSON nesnesi olarak yaz.

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

[0] (TÜBİTAK Duyuruları, tr, 2026-10-27) 2508 TÜBİTAK – Slovenya Araştırma ve Yenilik Ajansı (ARIS) İkili İş Birliği Programı 2026 Yılı Çağrısı Açıldı — 2508 TÜBİTAK – Slovenya Araştırma ve Yenilik Ajansı (ARIS) İkili İş Birliği Programı 2026 Yılı Çağrısı Açıldı utku.cetin Sa, 10/27/2026 - 20:42 TÜBİTAK ve Slovenya Araştırma ve Yenilik Ajansı (Slovenian Research and Innovation Agency–ARIS) arasındaki iş birliği kapsamında, ortak 
[1] (TÜBİTAK Duyuruları, tr, 2026-10-27) Bütünleşik Algılama ve Haberleşme Kış Okulu 2026 Yılı Başvuruları Başladı — Bütünleşik Algılama ve Haberleşme Kış Okulu 2026 Yılı Başvuruları Başladı utku.cetin Sa, 10/27/2026 - 19:38 TÜBİTAK Temel Bilimler Araştırma Enstitüsü (TBAE) tarafından açılan Bütünleşik Algılama ve Haberleşme Kış Okulu’nun 2026 yılı başvuruları başladı. TÜBİTAK Temel Bilimler Ar
[2] (TÜBİTAK Duyuruları, tr, 2026-10-26) Eureka Network Türkiye-İspanya 2026 Yılı Çağrısı Açıldı — Eureka Network Türkiye-İspanya 2026 Yılı Çağrısı Açıldı utku.cetin Pzt, 10/26/2026 - 16:38 Türkiye ve İspanya arasındaki iş birliğini güçlendirmek ve her iki ülkedeki firmaların ortak Ar-Ge faaliyetlerini EUREKA Network aracı kapsamında desteklemek amacıyla Türkiye ve İspanya İki
[3] (Google Developers Blog, en, 2026-10-27) Fast, reliable A2UI, with swappable inference formats — A2UI now supports swappable inference formats, introducing A2UI Express which uses up to 3x fewer tokens and cuts latency by compiling compact Python-style syntax into standard A2UI JSON via Agent SDKs. Developers can also use controlled generation with TypeSafe's Jev system-deci
[4] (Google Developers Blog, en, 2026-10-27) Building Conversational Commerce with Multi-Agent Swarms on GCP: A Working Prototype — This document provides a publication template and metadata structure for a technical blog post focused on building Conversational User Interfaces (CUIs) using AI. It outlines key developer focus areas, product stacks, and approval workflows required for publishing technical conte
[5] (Google Developers Blog, en, 2026-10-26) Preview, edit, and collaborate on markdown (.md) files natively in Google Docs and Drive — Google Workspace now offers native support for Markdown (.md) files, allowing developers and AI agents to seamlessly collaborate on documentation directly in Google Docs without manual file conversions. This integration preserves native file fidelity for use with Git repositories
[6] (Google Developers Blog, en, 2026-10-22) Architecting Governed, Self-Evolving AI Agents on Google Cloud — Learn how Project Chrysalis combines Google Cloud's Gemini Enterprise Agent Platform, Agent Development Kit (ADK), BigQuery, and a four-gate defense-in-depth security stack (Model Armor, Cloud KMS, Binary Authorization, and OPA) to build governed, self-evolving AI agents that rem
[7] (Google Developers Blog, en, 2026-10-22) Streaming comes to API Gateway: real-time and AI-ready APIs, without changing your spec — API Gateway now supports real-time streaming—including Server-Sent Events, WebSockets, gRPC, and chunked transfer encoding—in Public Preview without requiring changes to your existing API specifications. This update allows developers to route long-lived, bi-directional streams an
[8] (GitHub Blog, en, 2026-10-22) How bug bounty sharpens one researcher’s security skills — As Cybersecurity Awareness Month continues, the GitHub Bug Bounty team spotlights @r31n, diving into their research approach, favorite bug classes, and advice for aspiring hackers. The post How bug bounty sharpens one researcher’s security skills appeared first on The GitHub Blog
[9] (GitHub Blog, en, 2026-10-21) The bridge to agent-scale Git infrastructure — We moved a copy of 99.99999% of GitHub's repositories to Azure. Here's how per-reference quorums will bring over the rest, and how object storage lets reads scale independently. The post The bridge to agent-scale Git infrastructure appeared first on The GitHub Blog .
[10] (Google Blog, en, 2026-10-27) We’re announcing Genie 4, our new world model for real-time interactive simulation. — Today, we’re announcing our research on Genie 4, our new world model that brings unprecedented realism and native audio to real-time interactive simulation.The Genie 4 m…
[11] (Google Blog, en, 2026-10-27) 8 examples of Gemini 4 Argon in action — Collage of various uses of Gemini 4 Argon
[12] (Google Blog, en, 2026-10-27) Fitbit Edge: Premium design for an active life — TBD
[13] (Google Blog, en, 2026-10-26) 15 college students share their favorite Gemini features — Three young adults gathered around a laptop looking at its screen
[14] (Google Blog, en, 2026-10-26) Our newest AI Quest: Mapping the human brain — An illustration of a planet rotating to show various cartoon figures waving. At the top is the text "AI Quests"
[15] (Google Blog, en, 2026-10-26) Powering sub-Saharan Africa beyond the grid — A person holding up a solar panel
[16] (Google Blog, en, 2026-10-26) We’re helping farmers around the world connect to essential services online. — Google.org is investing $2.5M to help 1 million farmers access AI-powered agricultural services via the World Bank's ONA. See how it works.
[17] (Google Blog, en, 2026-10-26) How Google Beam connects military families globally — Several military families communicating with Google Beam
[18] (Google Blog, en, 2026-10-23) See what 5 builders are making with Gemini 4 Argon — Collage showing five builds with Gemini 4 Argon
[19] (Google Blog, en, 2026-10-22) Explore new ways to drive your best ROI with the first Google Marketing Platform Drop. — Google Marketing Platform Drops, a new monthly series, delivers our latest news to help you get your best ROI across the full customer journey. We’ll cover everything fr…
[20] (Google Blog, en, 2026-10-22) We are working with Voltus to build a 1-gigawatt virtual power plant. — Google and Voltus are building a 1-gigawatt virtual power plant to boost grid reliability for 67 million people. See how this expansion works.
[21] (Google Blog, en, 2026-10-21) Recreating the lost studios of women sculptors with Prune Nourry — Recreating the lost studios of women sculptors with Prune Nourry YouTube video
[22] (Hugging Face Blog, en, 2026-10-27) Build specialized multimodal models with LFM3 — 
[23] (Hugging Face Blog, en, 2026-10-27) Can we trust LLMs to judge whether a research idea is novel? — 
[24] (Hugging Face Blog, en, 2026-10-23) Does Your Model Run on AWS Trainium? Look It Up — 
[25] (Hugging Face Blog, en, 2026-10-22) Turning Database Grading into RL Rewards: Post-Training Agents with ThinkingBox — 
[26] (Hugging Face Blog, en, 2026-10-22) Ensemble forecasting with IBM Granite time-series models — 
[27] (Hugging Face Blog, en, 2026-10-21) NVIDIA Kumo Relational Outperforms Supervised Machine Learning on Relational Data, No Training Required — 
[28] (Hugging Face Blog, en, 2026-10-21) How Specializing the Vocabulary of SLMs Can Cut Inference Cost by 77% in Real Applications — 
[29] (Hugging Face Blog, en, 2026-10-21) Profiling TorchNeuron (Part 1): System-level profiling on AWS Trainium. — 
[30] (Hugging Face Blog, en, 2026-10-21) Granite Speech 5.0: Transcribe, Translate, and Attribute more Accurately and Faster — 
[31] (OpenAI News, en, 2026-10-28) Legora is building the agentic operating system for legal work — See how Legora uses OpenAI models, ChatGPT, and Codex to accelerate legal workflows, expand contract analysis, and free lawyers to focus on higher-value work.
[32] (OpenAI News, en, 2026-10-27) Retell uses OpenAI models to help power 100M monthly calls — GPT-6 Astra tops Retell’s voice agent benchmark, while Codex helps it reach a $1.6M annual revenue run rate per employee.
[33] (OpenAI News, en, 2026-10-27) OpenAI expands partnership with Oracle to bring its apps to ChatGPT — OpenAI and Oracle are expanding their partnership to bring business applications and AI agents into ChatGPT and power new Oracle offerings.
[34] (OpenAI News, en, 2026-10-27) How Check Point accelerates vulnerability research with Daybreak — With OpenAI Daybreak, Check Point speeds up the research behind new security protections, enabling its analysts to turn vulnerability intelligence into customer defenses faster.
[35] (OpenAI News, en, 2026-10-26) Greptile takes bug detection beyond code review with GPT-6 Astra — How Greptile uses GPT-6 Astra to test user workflows, Daybreak to strengthen security, and Codex to reduce rework.
[36] (OpenAI News, en, 2026-10-26) Working with academic communities to build scientific understanding — OpenAI shares model results on the Kakeya conjecture, Exponential Time Hypothesis, and quantum chromodynamics—and how researchers can verify and build on them.
[37] (OpenAI News, en, 2026-10-26) GPT-6.1 Sol helps CodeRabbit strengthen security across complex codebases — CodeRabbit uses GPT-6.1 Sol to investigate security risks across complex codebases. Its security agent helps developers review findings and proposed fixes.
[38] (OpenAI News, en, 2026-10-26) ChatGPT’s expanding world of work — Explore OpenAI Signals data on 165 work activities across nearly 100 countries, revealing how people use ChatGPT for work and how usage changes over time.
[39] (OpenAI News, en, 2026-10-26) How Fanatics and OpenAI streamline the fan experience — Fanatics uses OpenAI to help fans complete their game-day outfits with Shop the Look. Testing across roughly 30,000 MLB products showed 10% higher engagement.
[40] (OpenAI News, en, 2026-10-26) How Ultrafast cut incident investigation from hours to minutes at OpenAI — See how OpenAI engineers use Codex Ultrafast to investigate incidents in minutes. Explore faster security analysis, code refactoring, and daily workflows.
[41] (OpenAI News, en, 2026-10-26) Introducing GPT-6.1 Terra — Bringing fast and capable computer use to everyone
[42] (OpenAI News, en, 2026-10-23) Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II) — Learn how OpenAI scaled Habitat with reliable multi-tenancy, global caching, and Azure Cosmos DB to deliver 12× faster reads for ChatGPT.
[43] (OpenAI News, en, 2026-10-23) Securing our frontier model training environment — OpenAI explains how we strengthened containment for frontier model training and evaluation, including offline environments and high-compute red-teaming.
[44] (OpenAI News, en, 2026-10-23) Anima helps clinics cut call waits by 75% with GPT-6 and GPT-Live — Anima expands what care teams can do with OpenAI models, giving them more capacity to respond to patients.
[45] (OpenAI News, en, 2026-10-23) OpenAI and Poland’s NASK partner to advance AI safety and security — OpenAI and Poland’s NASK are partnering on AI safety, security, and technical research to strengthen safeguards and support a more resilient digital ecosystem.
[46] (Google DeepMind, en, 2026-10-27) Genie 4: A new generation of world simulation — Genie 4: our new world model unlocking unprecedented realism in real-time simulation.
[47] (Google DeepMind, en, 2026-10-22) Beyond tree cover: mapping the world’s forest types — A global map categorizing every 10-meter patch of land on Earth into distinct forest types.
[48] (Anthropic News, en, 2026-10-26) Anthropic files S-1 with the SEC for proposed initial public offering — Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.
[49] (Anthropic News, en, 2026-10-27) Expanding our partnership with GSA to bring Claude to all levels of government — Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.
[50] (Anthropic News, en, 2026-10-27) Partnerships — Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.
[51] (Anthropic News, en, 2026-10-22) Donating Agent Skills to the Agentic AI Foundation — Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.
[52] (Anthropic News, en, 2026-10-22) Open call for guest investigators in the life sciences — Today, we’re inviting members of the life sciences community to apply to work with us on special projects.
[53] (Webrazzi, tr, 2026-10-28) Guidewire, yapay zeka girişimi Hyperexponential'ı 1,7 milyar dolara satın alıyor — Sigorta teknolojileri şirketi Guidewire, sigorta şirketlerinin riskleri değerlendirmesine ve fiyat belirlemesine yardımcı olan Hyperexponential'ı 1,7 milyar dolara satın alıyor. Guidewire, satın almay...
[54] (Webrazzi, tr, 2026-10-28) AIOps: Tech ekibinin 20 yıllık kıdemli mimarı — Berkay Özuygur, Parny'nin kurucu ortağı ve CEO'sudur. Bu yazı Webrazzi'de konuk yazar olarak yayınlanmıştır.Yapay zekâ döneminde DevOps kavramı da değişiyor. Yazılımı geliştirenlerle onu güvenilir biç...
[55] (Webrazzi, tr, 2026-10-28) Yapay zeka için bulut bilişim altyapısı geliştiren General Compute, 100 milyon dolar yatırım aldı — Yapay zeka teknolojisi için bulut bilişim altyapısı geliştiren General Compute, 100 milyon dolar yatırım aldı. Şirketin 100 milyon dolarlık A serisi yatırım turuna Blackbird Ventures ve Abstract Ventu...
[56] (Webrazzi, tr, 2026-10-28) Martı, sürücüsüz araçları paylaşımlı yolculuğa taşıyacak RoboMartı’yı tanıttı — Martı, yapay zekâ destekli sürücüsüz araçları paylaşımlı yolculuk modeliyle buluşturmayı hedefleyen RoboMartı projesini duyurdu. Şirketin kurucusu Oğuz Alper Öktem, projeye ilişkin test sürüşlerinin b...
[57] (Webrazzi, tr, 2026-10-28) Üretim teknolojilerine odaklanan Re:Build, 2,1 milyar dolar yatırım aldı — ABD merkezli Re:Build Manufacturing, ileri aşama yatırım turunda 2,1 milyar dolar yatırım aldı. Turun liderliğini General Catalyst ve JPMorganChase’in Strategic Investment Group birimi üstlendi. Gener...
[58] (Webrazzi, tr, 2026-10-28) ChatGPT, iCloud Mail ve Takvim entegrasyonlarını kullanıma sundu — OpenAI, ChatGPT’ye Apple’ın e-posta ve takvim hizmetleri için iki yeni eklenti eklediğini X hesabında paylaşarak duyurdu. iCloud Mail ve iCloud Takvim entegrasyonları sayesinde kullanıcılar, sohbet ro...
[59] (Webrazzi, tr, 2026-10-28) Google, ses üretebilen ve gerçek zamanlı yönlendirilebilen dünya modeli Genie 4'ü tanıttı — Google DeepMind, gerçek zamanlı etkileşimli simülasyonlar oluşturan yeni dünya modeli Genie 4’ü duyurdu. Araştırma ön izlemesi kapsamında sınırlı bir test grubuna açılan model, daha gerçekçi görseller...
[60] (Webrazzi, tr, 2026-10-28) Nvidia ve AMD, Meta'ya toplam 4 milyar dolar yatırım yapacak — Nvidia ve AMD, Meta ile yapay zeka alanındaki iş birliklerini genişletirken şirkete toplam 4 milyar dolarlık yatırım yapmaya hazırlanıyor. Nvidia, 3 milyar dolarlık Meta hissesi satın almayı planlarke...
[61] (Webrazzi, tr, 2026-10-27) OpenAI, matematik ve fizikte sınırları zorluyor: Üç yeni çözüm iddiası — OpenAI, geliştirdiği modellerin üç bilimsel problemde yeni sonuçlar ürettiğini açıkladı. Şirket, bu çıktıları ham araştırma verisi olarak tanımlarken bilimsel bilgiye dönüştürülmeleri için farklı yayı...
[62] (Webrazzi, tr, 2026-10-27) Apple yeni iMac'i tanıttı: Fiyatı ve teknik özellikleri — Apple, 28 Ekim’de düzenleyeceği Pro and Tell etkinliği öncesinde yeni iMac modelini tanıttı. M6 işlemcisinden güç alan bilgisayar, 24 inçlik 4.5K Retina ekranıyla geliyor. İnce tasarımını koruyan yeni...
[63] (Webrazzi, tr, 2026-10-27) Apple, M6 çipli MacBook Pro'yu tanıttı: Yapay zeka ve grafik performansı artıyor — Apple, MacBook Pro ailesini M6 çipli 14 inç modeliyle güncelledi. Yeni cihaz, özellikle bilgisayar üzerinde çalışan yapay zeka uygulamalarında ve grafik işlemlerinde performans artışına odaklanıyor. M...
[64] (Webrazzi, tr, 2026-10-27) Apple'ın katlanabilir telefonu iPhone Duo, ekran çatlaması şikayetleriyle gündemde — Apple’ın ilk katlanabilir telefonu iPhone Duo, satışa sunulmasının ardından ekran sorunlarıyla gündeme geldi. Reddit üzerinden deneyimlerini paylaşan bazı kullanıcılar, cihazlarının iç ekranında kulla...
[65] (Webrazzi, tr, 2026-10-27) Bedrock Robotics, 4,1 milyar dolar değerleme üzerinden 600 milyon dolar yatırım aldı — Sürücüsüz araç teknolojileri geliştiren Bedrock Robotics, 600 milyon dolar yatırım aldı. Şirketin 600 milyon dolarlık C serisi yatırım turuna CapitalG ve Emergence Capital ortaklaşa liderlik etti. ABD...
[66] (Webrazzi, tr, 2026-10-27) Intel, kuantum bilişim girişimi Classiq'i 2,2 milyar dolara satın alıyor — Intel, kuantum bilgisayarlar için yazılım geliştiren Classiq'i 2,2 milyar dolara satın almak üzere anlaşmaya vardı. Satın alma, Intel'in kuantum bilişim alanındaki yazılım ve donanım çalışmalarını bir...
[67] (Webrazzi, tr, 2026-10-27) Instagram, 90 dakikaya kadar yatay videoları test ediyor — Sosyal medya platformu Instagram, dün duyurusunu yaptığı yeni özelliklerle uzun videolara ve televizyon ekranlarına yönelik çalışmalarını genişletiyor. “Features” adı verilen yeni format, içerik üreti...
[68] (Cloudflare Blog, en, 2026-10-27) Introducing the Cloudflare PHP Capture the Flag challenge — We are launching a PHP Capture the Flag challenge integrated with our Bug Bounty program to test our WAF protections. Security researchers are invited to bypass our defenses and capture the flag to help make the Internet safer.
[69] (Cloudflare Blog, en, 2026-10-27) What took the Internet offline in Q3 2026 — An examination of global Internet disruptions observed by Cloudflare Radar during the third quarter of 2026. This review analyzes how power failures, natural disasters, and government shutdowns impacted network connectivity and traffic.
[70] (Cloudflare Blog, en, 2026-10-26) Cross-request KV cache exposure in the GLM-5.3 Workers AI model, and our remediation with SGLang — A configuration mismatch in GLM 5.3 on Workers AI triggered an SGLang bug that exposed KV cache pages across requests. Here is how we addressed the issue.
[71] (Cloudflare Blog, en, 2026-10-23) Origin Range Requests: Serving large files without range-request tuning — Naive byte-range caching can waste gigabytes of origin bandwidth on small requests. We rebuilt our cache architecture in Pingora to coordinate partial fetches automatically, cutting R2 p99 latency in half.
[72] (Cloudflare Blog, en, 2026-10-23) Bringing post-quantum cryptography to geographically fenced key management — Cloudflare's new post-quantum GeoKey Manager protects geographically fenced decryption keys from harvest now, decrypt later attacks. Learn how we redesigned our cryptography stack to support strict data sovereignty in a post-quantum world.
[73] (Cloudflare Blog, en, 2026-10-22) Localizing compliance at scale: achieving South Korea’s ISMS certification — Cloudflare has achieved South Korea's ISMS certification following an audit across 80 controls. Learn how we localized user consent flows, adapted social sign-up paths at the edge, and validated our global security program.
[74] (Cloudflare Blog, en, 2026-10-21) Introducing full transaction detection for Cloudflare WAF — Cloudflare's web application firewall can now correlate an HTTP request with its response. Full transaction detection helps every customer find successful exploits, data exposure, and risky misconfigurations that request-only inspection can miss.
[75] (Cloudflare Blog, en, 2026-10-21) Cloudflare deploys protections against php2shell vulnerability — Cloudflare has deployed default web application firewall (WAF) protections for newly disclosed PHP vulnerabilities before public disclosure. The rules use request and response signals to stop exploit attempts and prevent exposed data from reaching attackers.
[76] (Hacker News (100+ puan), en, 2026-10-28) Ten days later, Git on macOS still trusts the compromised eMudhra certificates — Article URL: https://emudhra.we-have-a-problem.com/apple.html Comments URL: https://news.ycombinator.com/item?id=50271640 Points: 241 # Comments: 100
[77] (Hacker News (100+ puan), en, 2026-10-28) Git for the US Code — Article URL: https://lexifina.com/blog/git-for-the-us-code Comments URL: https://news.ycombinator.com/item?id=50268380 Points: 324 # Comments: 173
[78] (Hacker News (100+ puan), en, 2026-10-27) Early progress on accelerating drug development with Claude — Article URL: https://www.anthropic.com/research/early-progress-drug-development Comments URL: https://news.ycombinator.com/item?id=50265609 Points: 258 # Comments: 254
[79] (Hacker News (100+ puan), en, 2026-10-27) Raspberry Pi Zero 3W and Pi 4 Model A spotted in device trees — Article URL: https://bret.dk/raspberry-pi-zero-3-w-pi-4-model-a/ Comments URL: https://news.ycombinator.com/item?id=50265594 Points: 186 # Comments: 108
[80] (Hacker News (100+ puan), en, 2026-10-27) Code-execution flaw in UEFI firmware threatens most servers on planet Earth — Article URL: https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/ Comments URL: https://news.ycombinator.com/item?id=50265393 Points: 192 # Comments: 126
[81] (Hacker News (100+ puan), en, 2026-10-27) Four Months of Zig — Article URL: https://gracefulliberty.com/articles/four-months-of-zig/ Comments URL: https://news.ycombinator.com/item?id=50265128 Points: 153 # Comments: 106
[82] (Hacker News (100+ puan), en, 2026-10-27) Tailscale SSH: Investigation and remediation update — Article URL: https://tailscale.com/ssh-investigation-update Comments URL: https://news.ycombinator.com/item?id=50264857 Points: 319 # Comments: 170
[83] (Hacker News (100+ puan), en, 2026-10-27) Survival LLM: AI assistant and emergency library that runs on your own computer — Article URL: https://www.brangus.io/survival-llm Comments URL: https://news.ycombinator.com/item?id=50264853 Points: 405 # Comments: 154
[84] (Hacker News (100+ puan), en, 2026-10-27) Ghostty 1.4 — Article URL: https://ghostty.org/docs/install/release-notes/1-4-0 Comments URL: https://news.ycombinator.com/item?id=50261998 Points: 1120 # Comments: 359
[85] (Hacker News (100+ puan), en, 2026-10-27) Classification of Finite Simple Groups Formalized in Lean — Article URL: https://cfsg.axiommath.ai/ Comments URL: https://news.ycombinator.com/item?id=50261647 Points: 221 # Comments: 68
[86] (Hacker News (100+ puan), en, 2026-10-27) New 14‑inch MacBook Pro with M6 — Article URL: https://www.apple.com/in/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/ Comments URL: https://news.ycombinator.com/item?id=50261352 Points: 384 # Comments: 529
[87] (Hacker News (100+ puan), en, 2026-10-27) US Government is hiding a secret court ruling about how it spies on Americans — Article URL: https://www.wired.com/story/the-us-government-is-hiding-a-secret-court-ruling-about-how-it-spies-on-americans/ Comments URL: https://news.ycombinator.com/item?id=50259604 Points: 998 # Comments: 381
[88] (Hacker News (100+ puan), en, 2026-10-27) New iMac with M6 — Article URL: https://www.apple.com/imac/ Comments URL: https://news.ycombinator.com/item?id=50258538 Points: 350 # Comments: 442
[89] (Hacker News (100+ puan), en, 2026-10-27) Python's experimental JIT to be removed — Article URL: https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/ Comments URL: https://news.ycombinator.com/item?id=50257419 Points: 537 # Comments: 294
[90] (Webtekno, tr, 2026-10-28) Konsiyon, Yapay Zekâ ile Güçlendi — İstanbul merkezli yerli bir site yönetim yazılımı olan Konsiyon, yapay zekâ özellikleri ile artık daha kullanışlı.
[91] (Webtekno, tr, 2026-10-28) Mobil Fotoğrafçılıkta Yeni Dönem: vivo X500 Pro Max Tanıtıldı! — vivo X500 Pro Max, 200 MP ZEISS telefoto kamerası, 400 mm lens desteği ve Türkiye'ye özel avantajlı lansman fırsatlarıyla tanıtıldı.
[92] (Webtekno, tr, 2026-10-28) OpenAI'a Ağır Suçlama: "ChatGPT Kızımıza İlacı Bıraktırdı ve Ölümüne Yol Açtı" — OpenAI'a açılan davada, ChatGPT'nin epilepsi hastası genç kadına ilacını bıraktırarak ölümüne yol açtığı öne sürüldü.
[93] (Webtekno, tr, 2026-10-28) Toyota’dan Ezber Bozan Hamle: Yeni Nesil Benzinli Motorlarını Rakiplerine Satacak! — Toyota, geliştirdiği yeni nesil benzinli ve hibrit motorları diğer üreticilere satarak 2032’ye kadar milyarlarca euro gelir hedefliyor.
[94] (Webtekno, tr, 2026-10-28) Samsung, Performansa Yönelik Dev Davayı Kaybetti (Bilerek Oyun Performansını mı Kısıtlıyor?) — Güney Kore mahkemesi, Galaxy S21 ve S22 serilerinde oyun performansını kısıtlayan GOS yazılımını gizlediği gerekçesiyle Samsung'a para cezası verdi.
[95] (Webtekno, tr, 2026-10-28) BMW'nin En Büyük Elektrikli SUV Modeli iX7 Sızdırıldı: 2027'de Tanıtılacak! — BMW'nin 2027'de tanıtılması beklenen yeni elektrikli SUV modeli iX7, sızdırılan bilgilerle şimdiden merak uyandırıyor.
[96] (Webtekno, tr, 2026-10-28) İndirim Diye Aldanmayın: Ticaret Bakanlığı Kasım Ayı Denetimlerini Sıkılaştırdı! — Ticaret Bakanlığı, kasım indirimleri döneminde tüketiciyi yanıltan kampanyaları ve haksız ticari uygulamaları mercek altına alıyor. İhlalin niteliğine göre işletmelere yaklaşık 40 milyon TL'ye varan idari para cezaları uygulanabilecek.
[97] (Webtekno, tr, 2026-10-28) Bazı Audi Araçlar İçin Kritik Uyarı Yapıldı: Sakın %80'in Üzerinde Şarj Etmeyin! — Bataryada yangın riski taşıyan binlerce Audi elektrikli araç için geri çağırma kararı çıktı.
[98] (Webtekno, tr, 2026-10-28) Amazon'da Bu Haftanın En Avantajlı Ürünleri — Amazon'da fiyatı 500 TL ve altında olan ürünler arasından işinize yarayabilecek olanları sizler için seçtik.
[99] (Webtekno, tr, 2026-10-28) 10.000 mAh Batarya, 165 Hz Ekran! Redmi K100 Tanıtıldı — Redmi, ekranından bataryasına ve işlemcisine kadar her konuda çok iddialı yeni modeli K100’ü duyurdu.
[100] (Webtekno, tr, 2026-10-28) ChatGPT Artık iCloud Hesabınıza Bağlanabiliyor: İşte Yapabildikleri! — OpenAI, ChatGPT'nin iCloud Mail ve Apple Takvim ile bağlantı kurmasını sağlayan yeni özelliğini kullanıma sundu.
[101] (Webtekno, tr, 2026-10-28) Steam Türkiye'de En Çok Satan Oyunlar Açıklandı [20-27 Ekim 2026] — Steam, Türkiye'de geçen hafta boyunca en çok satan oyunları açıkladı.
[102] (Webtekno, tr, 2026-10-28) Uygun Fiyatlı MacBook Neo 2’nin Ne Zaman Tanıtılacağı Ortaya Çıktı — Apple’ın uygun fiyatlı yeni MacBook Neo modelinin yeni neslini ne zaman tanıtacağına dair bilgler geldi.
[103] (Webtekno, tr, 2026-10-28) İncecik Tasarımı Gelişmiş Özelliklerle Buluşturan Xiaomi Redmi Book 2027 Laptop Modelleri Tanıtıldı — Xiaomi, gelişmiş özellikleri incecik tasarıma sığdıran yeni Redmi Book 2027 laptop modellerini tanıttı.
[104] (Webtekno, tr, 2026-10-28) Tavanı Açıkken 349 km/s Hız Yapabilen Aston Martin Valhalla Spider Tanıtıldı — Aston Martin, 1064 beygirlik hibrit süper otomobili Valhalla Spider’ı tanıttı.
[105] (ShiftDelete.Net, tr, 2026-10-28) Dijital T.C. Kimlik Kartı Geliyor: İlk Testler 2027’de Başlıyor — e-Devlet ile kamu hizmetlerinde başlayan dijital dönüşüm hamlesi, fiziksel cüzdanları tamamen rafa kaldıracak yeni bir aşamaya geçiyor. Cumhurbaşkanlığı Yıllık Programı’nda yer alan bilgilere göre, ulusal dijital kimlik cüzdanının ilk prototipi 2027 yılında hayata geçiyor. Sistem
[106] (ShiftDelete.Net, tr, 2026-10-28) PSN Hesaplarında Yeni Tehlike: Parola Değişimi Yetersiz Kalıyor — PSN hesaplarında parola değiştirilse bile passkey anahtarlarının aktif kalması ciddi bir güvenlik riski yaratıyor. İşte korunmak için yapmanız gerekenler.
[107] (ShiftDelete.Net, tr, 2026-10-28) Xiaomi Robot Vacuum 6 Türkiye’de: Fiyatı, özellikleri ve rakipleri — Xiaomi Robot Vacuum 6 Türkiye'de satışa çıktı. Rulo mop, 30.000 Pa emiş gücü ve yapay zeka kamerası sunan model, rakipleri karşısında nerede duruyor?
[108] (ShiftDelete.Net, tr, 2026-10-28) Huawei Pura 90 Plus Tanıtıldı – İşte Özellikleri ve Fiyatı — Huawei, Pura 90 serisinin yeni üyesi Pura 90 Plus'ı Çin'de tanıttı. Kirin 9025 işlemci, 1 inç tipi ana kamera sensörü ve değişken diyaframla gelen telefonun fiyatı 5.499 CNY'den başlıyor.
[109] (ShiftDelete.Net, tr, 2026-10-28) ASELSAN’ın Finansal Performansı ve Borsadaki Durumu — ASELSAN, 2026’nın ilk dokuz ayına ait finansal sonuçlarını dün akşam KAP’ta açıkladı. Rakamları tek tek okuduğumda akla gelen ilk cümle şu: Büyüme hızını artıran bir şirketin bilançosu… Öte yandan aynı şirketin hissesi son üç ayda yerinde sayıyor, hatta geriliyor. Bu yazıda ikisi
[110] (ShiftDelete.Net, tr, 2026-10-28) Nintendo Switch 2 Oyunu Mario Kart World iPhone’da Çalıştı — Nintendo Switch 2'nin kırılmasının ardından Mario Kart World oyunu macOS ve iPhone 18 Pro cihazlarında çalıştırıldı. İşte emülasyon dünyasındaki son gelişmeler.
[111] (ShiftDelete.Net, tr, 2026-10-28) iPhone 18e Özellikleri Ortaya Çıktı — Apple'ın merakla beklenen iPhone 18e modeli hakkında ilk teknik detaylar sızdı. 2027 başında çıkması beklenen telefonun özellikleri ve stratejik önemi hakkında detaylı bilgiler.
[112] (ShiftDelete.Net, tr, 2026-10-28) Huawei Enjoy 100 Pro Modelini HarmonyOS 7 ile Tanıttı — Huawei, 6.100mAh bataryalı ve HarmonyOS 7 işletim sistemine sahip yeni akıllı telefonu Enjoy 100 Pro'yu tanıttı. İşte tüm teknik detaylar ve fiyat bilgisi.
[113] (ShiftDelete.Net, tr, 2026-10-28) Pixel Kullanıcılarının Alarm Kabusu: Alarmlar Sessizce Kapanıyor — Pixel telefonlarda yaşanan Pixel alarm otomatik sessize alındı hatası kullanıcıları mağdur ediyor. Google, sorunu incelemeye aldı.
[114] (ShiftDelete.Net, tr, 2026-10-28) ChatGPT’ye iCloud Takvim ve E-posta Desteği Geldi — ChatGPT iCloud takvim entegrasyonu ile e-postalarınızı ve takvim etkinliklerinizi doğrudan yönetin. OpenAI'ın yeni eklentileri hakkında detaylar.
[115] (ShiftDelete.Net, tr, 2026-10-28) Türkiye’de Kritik Altyapılarda 1071 ve 1453 Şifreleri Kullanılıyor – Risk Büyük — Türkiye'deki kritik altyapı tesislerinde 1071 ve 1453 gibi zayıf şifrelerin kullanıldığı ortaya çıktı. 430 tesisin siber güvenlik zafiyetlerine dair detaylar haberimizde.
[116] (ShiftDelete.Net, tr, 2026-10-28) Motorola Signature 27 ve Razr Flex Özellikleri Sızdı — Motorola Signature 27 özellikleri ve Razr Flex modeli Avrupa'daki bir perakendecide listelendi. Yeni cihazların teknik detayları ve fiyatları belli oldu.
[117] (ShiftDelete.Net, tr, 2026-10-28) Donald Trump Yapay Zeka Yerine Süper Zeka Terimini Zorunlu Kılıyor — ABD Başkanı Donald Trump, yapay zeka (AI) yerine süper zeka (SI) teriminin kullanılması gerektiğini savunuyor. İşte tartışmalı kararın detayları.
[118] (ShiftDelete.Net, tr, 2026-10-28) Redmi İlk Açık Kulaklığı Clip Neo’yu Tanıttı — Redmi, ilk açık yapılı kablosuz kulaklığı Clip Neo'yu duyurdu. 32 saate varan pil ömrü, Bluetooth 5.4 ve uygun fiyatıyla dikkat çeken modelin tüm detayları burada.
[119] (ShiftDelete.Net, tr, 2026-10-28) Anthropic: Yapay Zeka Felakete Neden Olabilir — Anthropic, halka arz öncesi sunduğu S-1 dosyasında yapay zeka modelleriyle ilgili varoluşsal ve ticari riskleri detaylıca açıkladı.
[120] (DonanımHaber, tr, 2026-10-28) Türkiye, İHA ve SİHA’lar için görünmez kalkan geliştiriliyor — Sivas Bilim ve Teknoloji Üniversitesi, “Görünmez Kalkan Projesi” kapsamında İHA ve SİHA’ları elektromanyetik girişimlerden korurken görüntü almayı sürdürecek şeffaf bir kaplama geliştiriyor.
[121] (DonanımHaber, tr, 2026-10-28) Tiggo 7’nin daha maceracı kardeşi tanıtıldı: İşte yeni Chery Tiggo X7 — Chery Tiggo X7, hibrit motorları ve dört tekerlekten çekiş seçeneğiyle geliyor. Yeni SUV, 700 mm sudan geçiş kapasitesi ve altı arazi moduyla aile kullanımını doğa yolculuklarıyla birleştiriyor.
[122] (DonanımHaber, tr, 2026-10-28) Fiat'tan sürpriz hamle: Efsane model Punto geri dönüyor — Fiat, 2018'de üretimi biten efsane Punto modelini geri döndürmeye hazırlanıyor. Yeni Punto hem içten yanmalı hem de elektrikli seçenekleriyle Renault'nun pazar hakimiyetine meydan okuyacak.
[123] (DonanımHaber, tr, 2026-10-28) Yeni MacBook Pro Dynamic Island ile geliyor: Çentikli ekrana veda! — Dokunmatik ekranlı MacBook Pro'nun tanıtılmasına saatler kala dizüstü bilgisayarın bir özeliği daha ortaya çıktı. Yeni MacBook Pro, çentikli ekran yerine Dynamic Island özellikli ekranla gelecek.
[124] (DonanımHaber, tr, 2026-10-28) Çinli GWM, Avrupa üretimi için Bulgaristan’ı seçti — GWM, Avrupa’da üretim için Bulgaristan’ı seçti. Ora 5’in montajı 2027’nin ilk çeyreğinde başlayacak. Yıllık 50 bin araç kapasiteli tesis, markanın Avrupa’da 300 bin adetlik üretim hedefinin ilk adımı.
[125] (DonanımHaber, tr, 2026-10-28) Bellek bulmak daha da zorlaşabilir: SK Hynix 2030’u işaret etti — SK Hynix, yapay zeka belleklerine yönelik talep nedeniyle üretim kapasitesini artırıyor. Şirket, tüm yatırımlara rağmen bellek piyasasındaki arz sıkıntısının 2030’a kadar sürmesini bekliyor.
[126] (DonanımHaber, tr, 2026-10-28) Çin'den internet hızında rekor: Fiber üzerinden 3,2 petabit — Çinli araştırmacılar, tek bir fiber optik kablo üzerinden saniyede 3,2 petabit veri aktararak yeni bir rekora imza attı. Bu hız, veri merkezlerinin geleceğini değiştirebilir.
[127] (DonanımHaber, tr, 2026-10-28) Tesla Roadster’ın gösterişli özelliğinin bedeli: 5 saniye itiş, saatlerce dolum — Tesla Roaster’ın gazlı itiş sistemi, 5 saniyelik kullanımın ardından 2 ila 6 saatlik dolum gerektiriyor. Şirket, azot tankının dolum süresini 30 dakikanın altına indirmeyi hedefliyor.
[128] (DonanımHaber, tr, 2026-10-28) Apple, selfie ile yaş doğrulama özelliğini kullanıma sundu — Apple, iOS 27.2 ile birlikte kullanıcıların yetişkin olduklarını doğrulamaları için yeni bir yöntem sundu. Bu yöntem, kullanıcıların selfie çekerek yaşlarını kanıtlamalarına olanak tanıyor.
[129] (DonanımHaber, tr, 2026-10-28) Samsung'a Galaxy S21 ve S22 için oyun performansı cezası — Samsung, Galaxy S21 ve S22 serilerinde oyun performansını sınırlayan GOS özelliğini yeterince açıklamadığı gerekçesiyle Güney Kore'de para cezasına çarptırıldı.
[130] (DonanımHaber, tr, 2026-10-28) Cyberpunk 2 için açılan yeni ilan multiplayer moduna işaret ediyor — Cyberpunk 2077'nin devma oyunu için hazırlıkların hız kazansmasıyla birlikte yeni detaylar da ortaya çıkmaya başladı. Gelen son haberlere bakılırsa Cyberpunk 2'de bir multiplayer modu da olacak.
[131] (DonanımHaber, tr, 2026-10-28) Oyunlarda tersine mühendislik dönemi başlıyor: Battlefield 2'nin oyun motoru açık kaynak oldu — Battlefield 2'nin oyun motorunu tersine mühendislikle yeniden oluşturan OpenBF2, kaynak kodlarını GitHub'da yayımlandı. Yapay zekâ alanında yaşanan gelişmeler, benzer projelerin sayısını artırıyor.
[132] (DonanımHaber, tr, 2026-10-28) MacBook Neo 2 için çıkış tarihi ortaya çıktı: A19 Pro ve 12 GB RAM geliyor — Apple'ın uygun fiyatlı dizüstü bilgisayarı MacBook Neo 2'nin 2027'nin ilk yarısında tanıtılması bekleniyor. Yeni model, A19 Pro işlemci ve 12 GB RAM ile gelebilir.

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
