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

[0] (TÜBİTAK Duyuruları, tr, 2026-10-26) Eureka Network Türkiye-İspanya 2026 Yılı Çağrısı Açıldı — Eureka Network Türkiye-İspanya 2026 Yılı Çağrısı Açıldı utku.cetin Pzt, 10/26/2026 - 16:38 Türkiye ve İspanya arasındaki iş birliğini güçlendirmek ve her iki ülkedeki firmaların ortak Ar-Ge faaliyetlerini EUREKA Network aracı kapsamında desteklemek amacıyla Türkiye ve İspanya İki
[1] (Google Developers Blog, en, 2026-10-27) Fast, reliable A2UI, with swappable inference formats — A2UI now supports swappable inference formats, introducing A2UI Express which uses up to 3x fewer tokens and cuts latency by compiling compact Python-style syntax into standard A2UI JSON via Agent SDKs. Developers can also use controlled generation with TypeSafe's Jev system-deci
[2] (Google Developers Blog, en, 2026-10-26) Preview, edit, and collaborate on markdown (.md) files natively in Google Docs and Drive — Google Workspace now offers native support for Markdown (.md) files, allowing developers and AI agents to seamlessly collaborate on documentation directly in Google Docs without manual file conversions. This integration preserves native file fidelity for use with Git repositories
[3] (Google Developers Blog, en, 2026-10-22) Architecting Governed, Self-Evolving AI Agents on Google Cloud — Learn how Project Chrysalis combines Google Cloud's Gemini Enterprise Agent Platform, Agent Development Kit (ADK), BigQuery, and a four-gate defense-in-depth security stack (Model Armor, Cloud KMS, Binary Authorization, and OPA) to build governed, self-evolving AI agents that rem
[4] (Google Developers Blog, en, 2026-10-22) Streaming comes to API Gateway: real-time and AI-ready APIs, without changing your spec — API Gateway now supports real-time streaming—including Server-Sent Events, WebSockets, gRPC, and chunked transfer encoding—in Public Preview without requiring changes to your existing API specifications. This update allows developers to route long-lived, bi-directional streams an
[5] (Google Developers Blog, en, 2026-10-21) Powering the Agent Development Lifecycle with any framework, from ADK to LangChain and beyond — The Agents CLI Extension System enables developers to use frameworks like LangChain, LangGraph, or custom enterprise stacks while retaining a unified deployment and evaluation workflow. It details a first-party LangChain template that scaffolds, runs, and deploys agents without r
[6] (Android Developers Blog, en, 2026-10-21) A more reliable way to add and edit contacts on Android — Apps that target the upcoming Android release will no longer be able to directly write to contacts with the WRITE_CONTACTS permission.
[7] (GitHub Blog, en, 2026-10-22) How bug bounty sharpens one researcher’s security skills — As Cybersecurity Awareness Month continues, the GitHub Bug Bounty team spotlights @r31n, diving into their research approach, favorite bug classes, and advice for aspiring hackers. The post How bug bounty sharpens one researcher’s security skills appeared first on The GitHub Blog
[8] (GitHub Blog, en, 2026-10-21) The bridge to agent-scale Git infrastructure — We moved a copy of 99.99999% of GitHub's repositories to Azure. Here's how per-reference quorums will bring over the rest, and how object storage lets reads scale independently. The post The bridge to agent-scale Git infrastructure appeared first on The GitHub Blog .
[9] (GitHub Blog, en, 2026-10-20) How 3 Java Champions are using GitHub Copilot for increased productivity — Three Java Champions share how they use GitHub Copilot to solve problems, accelerate development, and keep humans responsible for the results. The post How 3 Java Champions are using GitHub Copilot for increased productivity appeared first on The GitHub Blog .
[10] (Google Blog, en, 2026-10-27) 8 examples of Gemini 4 Argon in action — Collage of various uses of Gemini 4 Argon
[11] (Google Blog, en, 2026-10-27) Fitbit Edge: Premium design for an active life — TBD
[12] (Google Blog, en, 2026-10-26) 15 college students share their favorite Gemini features — Three young adults gathered around a laptop looking at its screen
[13] (Google Blog, en, 2026-10-26) Our newest AI Quest: Mapping the human brain — An illustration of a planet rotating to show various cartoon figures waving. At the top is the text "AI Quests"
[14] (Google Blog, en, 2026-10-26) Powering sub-Saharan Africa beyond the grid — A person holding up a solar panel
[15] (Google Blog, en, 2026-10-26) We’re helping farmers around the world connect to essential services online. — Google.org is investing $2.5M to help 1 million farmers access AI-powered agricultural services via the World Bank's ONA. See how it works.
[16] (Google Blog, en, 2026-10-26) How Google Beam connects military families globally — Several military families communicating with Google Beam
[17] (Google Blog, en, 2026-10-23) See what 5 builders are making with Gemini 4 Argon — Collage showing five builds with Gemini 4 Argon
[18] (Google Blog, en, 2026-10-22) Explore new ways to drive your best ROI with the first Google Marketing Platform Drop. — Google Marketing Platform Drops, a new monthly series, delivers our latest news to help you get your best ROI across the full customer journey. We’ll cover everything fr…
[19] (Google Blog, en, 2026-10-22) We are working with Voltus to build a 1-gigawatt virtual power plant. — Google and Voltus are building a 1-gigawatt virtual power plant to boost grid reliability for 67 million people. See how this expansion works.
[20] (Google Blog, en, 2026-10-21) Recreating the lost studios of women sculptors with Prune Nourry — Recreating the lost studios of women sculptors with Prune Nourry YouTube video
[21] (Google Blog, en, 2026-10-21) New bidding and budgeting tools can transform your upcoming holiday ad strategy. — Get actionable insights on bidding and budgeting tools in the latest episode of Google's "Ads Decoded" podcast.
[22] (Google Blog, en, 2026-10-21) Drive with “The Cat in the Hat” on Waze. — Cat in the hat
[23] (Google Blog, en, 2026-10-21) Southeast Asia’s digital economy to hit $368 billion — Cover image for the e-Conomy SEA 2026 report titled Building the intelligent economy by Google, Temasek, and Bain and Company. A 3D illustration features a glowing yellow star surrounded by miniature scenes representing digital sectors, including data cen
[24] (Google Blog, en, 2026-10-20) Get hands-free personalized help on the road with Gemini — Center of image is a photo of a 1st-person point of view of driving a car. On the circumference of the circle are the Gemini logo and various prompts. The bottom of the image has the text "Personal Intelligence hits the road".
[25] (Hugging Face Blog, en, 2026-10-23) LitPivot: Developing research ideas through dynamic contextualization within the literature landscape — 
[26] (Hugging Face Blog, en, 2026-10-23) Does Your Model Run on AWS Trainium? Look It Up — 
[27] (Hugging Face Blog, en, 2026-10-22) Turning Database Grading into RL Rewards: Post-Training Agents with ThinkingBox — 
[28] (Hugging Face Blog, en, 2026-10-22) Ensemble forecasting with IBM Granite time-series models — 
[29] (Hugging Face Blog, en, 2026-10-21) NVIDIA Kumo Relational Outperforms Supervised Machine Learning on Relational Data, No Training Required — 
[30] (Hugging Face Blog, en, 2026-10-21) How Specializing the Vocabulary of SLMs Can Cut Inference Cost by 77% in Real Applications — 
[31] (Hugging Face Blog, en, 2026-10-21) Profiling TorchNeuron (Part 1): System-level profiling on AWS Trainium. — 
[32] (Hugging Face Blog, en, 2026-10-21) Granite Speech 5.0: Transcribe, Translate, and Attribute more Accurately and Faster — 
[33] (OpenAI News, en, 2026-10-26) Greptile takes bug detection beyond code review with GPT-6 Astra — How Greptile uses GPT-6 Astra to test user workflows, Daybreak to strengthen security, and Codex to reduce rework.
[34] (OpenAI News, en, 2026-10-26) Working with academic communities to build scientific understanding — OpenAI shares model results on the Kakeya conjecture, Exponential Time Hypothesis, and quantum chromodynamics—and how researchers can verify and build on them.
[35] (OpenAI News, en, 2026-10-26) GPT-6.1 Sol helps CodeRabbit strengthen security across complex codebases — CodeRabbit uses GPT-6.1 Sol to investigate security risks across complex codebases. Its security agent helps developers review findings and proposed fixes.
[36] (OpenAI News, en, 2026-10-26) ChatGPT’s expanding world of work — Explore OpenAI Signals data on 165 work activities across nearly 100 countries, revealing how people use ChatGPT for work and how usage changes over time.
[37] (OpenAI News, en, 2026-10-26) How Fanatics and OpenAI streamline the fan experience — Fanatics uses OpenAI to help fans complete their game-day outfits with Shop the Look. Testing across roughly 30,000 MLB products showed 10% higher engagement.
[38] (OpenAI News, en, 2026-10-26) How Ultrafast cut incident investigation from hours to minutes at OpenAI — See how OpenAI engineers use Codex Ultrafast to investigate incidents in minutes. Explore faster security analysis, code refactoring, and daily workflows.
[39] (OpenAI News, en, 2026-10-26) Introducing GPT-6.1 Terra — Bringing fast and capable computer use to everyone
[40] (OpenAI News, en, 2026-10-23) Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II) — Learn how OpenAI scaled Habitat with reliable multi-tenancy, global caching, and Azure Cosmos DB to deliver 12× faster reads for ChatGPT.
[41] (OpenAI News, en, 2026-10-23) Securing our frontier model training environment — OpenAI explains how we strengthened containment for frontier model training and evaluation, including offline environments and high-compute red-teaming.
[42] (OpenAI News, en, 2026-10-23) OpenAI and Poland’s NASK partner to advance AI safety and security — OpenAI and Poland’s NASK are partnering on AI safety, security, and technical research to strengthen safeguards and support a more resilient digital ecosystem.
[43] (OpenAI News, en, 2026-10-22) Build more responsive apps with the Decisions API — Fast, focused, low-cost decisions for any application.
[44] (OpenAI News, en, 2026-10-22) What FDE means at OpenAI — What forward deployed engineering means at OpenAI
[45] (OpenAI News, en, 2026-10-22) Uber brings ChatGPT Work to all employees with OpenAI — Uber is rolling out ChatGPT Work to more than 30,000 employees, helping teams research, analyze data, create presentations, and complete complex workflows.
[46] (OpenAI News, en, 2026-10-21) How AT&T is rethinking in-house legal work with OpenAI — AT&T is working with OpenAI to make legal knowledge easier to access. Learn how its LegalEdge team is rethinking intake and scaling legal judgment.
[47] (OpenAI News, en, 2026-10-21) Broad access through consistent standards — How OpenAI works with distribution partners to uphold consistent safeguards, support responsible access, and clarify expectations in our Usage Policies.
[48] (Google DeepMind, en, 2026-10-22) Beyond tree cover: mapping the world’s forest types — A global map categorizing every 10-meter patch of land on Earth into distinct forest types.
[49] (Anthropic News, en, 2026-10-26) Anthropic files S-1 with the SEC for proposed initial public offering — Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.
[50] (Anthropic News, en, 2026-10-22) Donating Agent Skills to the Agentic AI Foundation — Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.
[51] (Anthropic News, en, 2026-10-22) Open call for guest investigators in the life sciences — Today, we’re inviting members of the life sciences community to apply to work with us on special projects.
[52] (Anthropic News, en, 2026-10-21) Physicist Christopher Stubbs joins Anthropic's Long-Term Benefit Trust — Dr. Christopher Stubbs, an experimental physicist and former Dean of Science at Harvard University, has joined Anthropic’s Long-Term Benefit Trust. He brings to the Trust decades of scientific expertise across observational cosmology and precision measurement. He has also advised
[53] (Webrazzi, tr, 2026-10-27) OpenAI, matematik ve fizikte sınırları zorluyor: Üç yeni çözüm iddiası — OpenAI, geliştirdiği modellerin üç bilimsel problemde yeni sonuçlar ürettiğini açıkladı. Şirket, bu çıktıları ham araştırma verisi olarak tanımlarken bilimsel bilgiye dönüştürülmeleri için farklı yayı...
[54] (Webrazzi, tr, 2026-10-27) Apple yeni iMac'i tanıttı: Fiyatı ve teknik özellikleri — Apple, 28 Ekim’de düzenleyeceği Pro and Tell etkinliği öncesinde yeni iMac modelini tanıttı. M6 işlemcisinden güç alan bilgisayar, 24 inçlik 4.5K Retina ekranıyla geliyor. İnce tasarımını koruyan yeni...
[55] (Webrazzi, tr, 2026-10-27) Apple, M6 çipli MacBook Pro'yu tanıttı: Yapay zeka ve grafik performansı artıyor — Apple, MacBook Pro ailesini M6 çipli 14 inç modeliyle güncelledi. Yeni cihaz, özellikle bilgisayar üzerinde çalışan yapay zeka uygulamalarında ve grafik işlemlerinde performans artışına odaklanıyor. M...
[56] (Webrazzi, tr, 2026-10-27) Apple'ın katlanabilir telefonu iPhone Duo, ekran çatlaması şikayetleriyle gündemde — Apple’ın ilk katlanabilir telefonu iPhone Duo, satışa sunulmasının ardından ekran sorunlarıyla gündeme geldi. Reddit üzerinden deneyimlerini paylaşan bazı kullanıcılar, cihazlarının iç ekranında kulla...
[57] (Webrazzi, tr, 2026-10-27) Bedrock Robotics, 4,1 milyar dolar değerleme üzerinden 600 milyon dolar yatırım aldı — Sürücüsüz araç teknolojileri geliştiren Bedrock Robotics, 600 milyon dolar yatırım aldı. Şirketin 600 milyon dolarlık C serisi yatırım turuna CapitalG ve Emergence Capital ortaklaşa liderlik etti. ABD...
[58] (Webrazzi, tr, 2026-10-27) Intel, kuantum bilişim girişimi Classiq'i 2,2 milyar dolara satın alıyor — Intel, kuantum bilgisayarlar için yazılım geliştiren Classiq'i 2,2 milyar dolara satın almak üzere anlaşmaya vardı. Satın alma, Intel'in kuantum bilişim alanındaki yazılım ve donanım çalışmalarını bir...
[59] (Webrazzi, tr, 2026-10-27) Instagram, 90 dakikaya kadar yatay videoları test ediyor — Sosyal medya platformu Instagram, dün duyurusunu yaptığı yeni özelliklerle uzun videolara ve televizyon ekranlarına yönelik çalışmalarını genişletiyor. “Features” adı verilen yeni format, içerik üreti...
[60] (Webrazzi, tr, 2026-10-27) OpenAI, bilgisayar kullanımına odaklanan GPT-6.1 Terra modelini tanıttı — OpenAI, görsel anlama, bilgisayar kullanımı ve metin üretimi yeteneklerini bir araya getiren GPT-6.1 Terra’yı duyurdu. GPT-5.6 Terra’nın yerini alan model; teklif hazırlama, teknik çizimleri yorumlama...
[61] (Webrazzi, tr, 2026-10-27) Microsoft, 60 bin çalışanına gönüllü işten ayrılma teklifinde bulunuyor — Teknoloji şirketleri, yapay zeka yatırımlarına ağırlık verirken maliyetlerini azaltmak için çalışan sayısını da gözden geçiriyor. Microsoft da bu kapsamda yaklaşık 60 bin çalışanına gönüllü işten ayrı...
[62] (Webrazzi, tr, 2026-10-27) Siri AI, yıl sonuna kadar Türkçe dil desteği kazanacak — Apple, yapay zeka destekli asistanı Siri AI'ın yıl sonuna kadar Türkçe dil desteği kazanacağını açıkladı. Türkçe ile birlikte geleneksel Çince, Norveççe ve Vietnamca da desteklenen dillere eklenecek.A...
[63] (Webrazzi, tr, 2026-10-26) Anthropic halka arz dosyasını yayımladı: 16,3 milyar dolar gelir, dev altyapı anlaşmaları ve kurucuların kontrolü — Claude’un geliştiricisi Anthropic, halka arz başvurusunu 26 Ekim’de ABD Menkul Kıymetler ve Borsa Komisyonu (SEC) üzerinden kamuya açtı. Haziran ayında gizli başvuru yapan şirket, A sınıfı hisselerini...
[64] (Webrazzi, tr, 2026-10-26) AWS, yapay zeka talebiyle 2027'ye kadar bulut kapasitesinin büyük bölümünü sattı — Yapay zeka teknolojilerinin gelişmesi, şirketlerin bulut bilişim altyapısına yönelik talebini artırıyor. Bu talep, teknoloji şirketlerinin mevcut altyapılarını genişletme ihtiyacını da beraberinde get...
[65] (Webrazzi, tr, 2026-10-26) Apple, OLED ekran ve A20 Pro çipli yeni iPad mini'yi tanıttı — Apple, iPad mini’nin yenilenen modelini web sitesinde paylaştı. Super Retina XDR OLED ekrana geçiş yapan cihaz, önceki modele kıyasla yüzde 14 daha ince ve yüzde 13 daha hafif bir tasarımla karşımıza ...
[66] (Webrazzi, tr, 2026-10-26) Commonwealth Fusion Systems, 85 milyon dolarlık destek için ABD ile anlaştı — Füzyon enerjisi alanında çalışan Commonwealth Fusion Systems (CFS), füzyon santrallerinde kullanılacak yarı iletken teknolojilerini geliştirmek için ABD Ticaret Bakanlığı (Department of Commerce) ile ...
[67] (Webrazzi, tr, 2026-10-26) Paribu Kripto Para Bilinirlik ve Algı Araştırması 2026'dan öne çıkanlar — Paribu, FutureBright Group iş birliğiyle hazırladığı Kripto Para Bilinirlik ve Algı Araştırması 2026’nın sonuçlarını yayımladı. Yedinci kez gerçekleştirilen araştırma; yatırımcı profilindeki değişimi,...
[68] (Cloudflare Blog, en, 2026-10-27) Introducing the Cloudflare PHP Capture the Flag challenge — We are launching a PHP Capture the Flag challenge integrated with our Bug Bounty program to test our WAF protections. Security researchers are invited to bypass our defenses and capture the flag to help make the Internet safer.
[69] (Cloudflare Blog, en, 2026-10-27) What took the Internet offline in Q3 2026 — An examination of global Internet disruptions observed by Cloudflare Radar during the third quarter of 2026. This review analyzes how power failures, natural disasters, and government shutdowns impacted network connectivity and traffic.
[70] (Cloudflare Blog, en, 2026-10-26) Cross-request KV cache exposure in the GLM-5.3 Workers AI model, and our remediation with SGLang — A configuration mismatch in GLM 5.3 on Workers AI triggered an SGLang bug that exposed KV cache pages across requests. Here is how we addressed the issue.
[71] (Cloudflare Blog, en, 2026-10-23) Origin Range Requests: Serving large files without range-request tuning — Naive byte-range caching can waste gigabytes of origin bandwidth on small requests. We rebuilt our cache architecture in Pingora to coordinate partial fetches automatically, cutting R2 p99 latency in half.
[72] (Cloudflare Blog, en, 2026-10-23) Bringing post-quantum cryptography to geographically fenced key management — Cloudflare's new post-quantum GeoKey Manager protects geographically fenced decryption keys from harvest now, decrypt later attacks. Learn how we redesigned our cryptography stack to support strict data sovereignty in a post-quantum world.
[73] (Cloudflare Blog, en, 2026-10-22) Localizing compliance at scale: achieving South Korea’s ISMS certification — Cloudflare has achieved South Korea's ISMS certification following an audit across 80 controls. Learn how we localized user consent flows, adapted social sign-up paths at the edge, and validated our global security program.
[74] (Cloudflare Blog, en, 2026-10-21) Introducing full transaction detection for Cloudflare WAF — Cloudflare's web application firewall can now correlate an HTTP request with its response. Full transaction detection helps every customer find successful exploits, data exposure, and risky misconfigurations that request-only inspection can miss.
[75] (Cloudflare Blog, en, 2026-10-21) Cloudflare deploys protections against php2shell vulnerability — Cloudflare has deployed default web application firewall (WAF) protections for newly disclosed PHP vulnerabilities before public disclosure. The rules use request and response signals to stop exploit attempts and prevent exposed data from reaching attackers.
[76] (Cloudflare Blog, en, 2026-10-21) How Commerce.com and Cloudflare are getting storefronts ready for AI agents — Almost 100,000 Commerce.com domains now give AI agents real shopping tools through WebMCP on Cloudflare. Here's how we turned it on across every store at once, while keeping each merchant in control.
[77] (Cloudflare Blog, en, 2026-10-20) 8 eMudhra certificates are compromised. Here's what you need to know — Following the discovery that eight eMudhra intermediate certificates use weak keys, Cloudflare is deploying mitigations and releasing client updates. We explain the impact, our response, and what customers and developers should do next.
[78] (Hacker News (100+ puan), en, 2026-10-27) The US Government Is Hiding Secret Court Ruling About How It Spies on Americans — Article URL: https://www.wired.com/story/the-us-government-is-hiding-a-secret-court-ruling-about-how-it-spies-on-americans/ Comments URL: https://news.ycombinator.com/item?id=50259604 Points: 166 # Comments: 31
[79] (Hacker News (100+ puan), en, 2026-10-27) Software may be getting worse, but it used to be horrible — Article URL: https://www.bitlog.com/2026/10/27/software-may-be-getting-worse-but-it-used-to-be-horrible/ Comments URL: https://news.ycombinator.com/item?id=50257548 Points: 205 # Comments: 156
[80] (Hacker News (100+ puan), en, 2026-10-27) Python's experimental JIT to be removed — Article URL: https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/ Comments URL: https://news.ycombinator.com/item?id=50257419 Points: 218 # Comments: 119
[81] (Hacker News (100+ puan), en, 2026-10-27) Wikipedia's Cleanup of AI-Generated Content — Article URL: https://spectrum.ieee.org/wikipedia-wikiproject-ai-writing-cleanup Comments URL: https://news.ycombinator.com/item?id=50257326 Points: 209 # Comments: 86
[82] (Hacker News (100+ puan), en, 2026-10-27) AI promised less work. I've never worked more — Article URL: https://oioannou.com/blog/ai-promised-less-work/ Comments URL: https://news.ycombinator.com/item?id=50257325 Points: 425 # Comments: 380
[83] (Hacker News (100+ puan), en, 2026-10-27) Roblox downloaded 145GB models from us (including adult content) without asking — Article URL: https://open3dlab.com/news/roblox-downloaded-145-gb-of-models-from-our-sites/ Comments URL: https://news.ycombinator.com/item?id=50256985 Points: 381 # Comments: 224
[84] (Hacker News (100+ puan), en, 2026-10-27) The Mythical Man-Month in the Age of AI — Article URL: https://j11g.com/the-mythical-man-month-in-the-age-of-ai Comments URL: https://news.ycombinator.com/item?id=50255298 Points: 330 # Comments: 208
[85] (Hacker News (100+ puan), en, 2026-10-27) I still teach OpenGL ES 3.0 — Article URL: https://eliasfarhan.ch/graphics/cpp/2026/01/27/why-i-teach-opengles.html Comments URL: https://news.ycombinator.com/item?id=50253939 Points: 118 # Comments: 72
[86] (Hacker News (100+ puan), en, 2026-10-26) The Exponential Time Hypothesis Is False [pdf] — See also: Announcing three new discoveries in mathematics, computer science, and physics - https://news.ycombinator.com/item?id=50251344 Comments URL: https://news.ycombinator.com/item?id=50251661 Points: 731 # Comments: 261
[87] (Hacker News (100+ puan), en, 2026-10-26) Type Server Protocol — Article URL: https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md Comments URL: https://news.ycombinator.com/item?id=50248371 Points: 262 # Comments: 172
[88] (Hacker News (100+ puan), en, 2026-10-26) Oldest GUI application that still runs on Windows 11 — Article URL: https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/ Comments URL: https://news.ycombinator.com/item?id=50248055 Points: 499 # Comments: 298
[89] (Hacker News (100+ puan), en, 2026-10-26) CSS-Tricks has a new owner — Article URL: https://css-tricks.com/css-tricks-has-a-new-owner/ Comments URL: https://news.ycombinator.com/item?id=50245831 Points: 528 # Comments: 109
[90] (Hacker News (100+ puan), en, 2026-10-26) Solar power is becoming bigger than nuclear — Article URL: https://www.bbc.com/future/article/20261023-how-solar-became-bigger-than-nuclear Comments URL: https://news.ycombinator.com/item?id=50245385 Points: 466 # Comments: 651
[91] (Webtekno, tr, 2026-10-27) Sony, PS5’te Güvenlik Açığı Keşfeden Kişiye 50 Bin Dolar Ödül Verdi! — Bir hacker, PS5’te güvenlik açığı keşfetti. Sony, bu açık nedeniyle ona 50 bin dolar ödül verdi.
[92] (Webtekno, tr, 2026-10-27) vivo X500s'in Ekran Özellikleri Sızdırıldı — vivo’nun X500 serisine dahil edeceği yeni amiral gemisi modeli X500s’in ekran özellikleri sızdırıldı.
[93] (Webtekno, tr, 2026-10-27) OnePlus, İlk Açık Kulaklığı Buds Clip’i Duyurdu: Sağ-Sol Ayrımı Olmayan Kulaklık! — OnePlus, kulağın hangi tarafta olduğunu sensörleriyle anlayıp stereo kanallarını otomatik ayarlayan ilk klipsli açık kulaklığı Buds Clip modelini duyurdu.
[94] (Webtekno, tr, 2026-10-27) iPhone 18e'nin Özellikleri Ortaya Çıktı: Neler Değişecek? — Yeni uygun fiyatlı iPhone modeli olacak iPhone 18e'nin özellikleri sızdırıldı.
[95] (Webtekno, tr, 2026-10-27) 94 Binden Fazla Range Rover Modeli Geri Çağrıldı: İyi de Neden? — Jaguar Land Rover, geri görüş kamerasıyla ilgili bir sorun yüzünden 94 bine yakın Range Rover’ı geri çağırdı.
[96] (Webtekno, tr, 2026-10-27) OpenAI, 3 Büyük Bilimsel Keşif Yaptığını Açıkladı — OpenAI; matematik, bilgisayar bilimi ve fizikte üç büyük teorik kırılma gerçekleştirdiğini öne sürdü.
[97] (Webtekno, tr, 2026-10-27) Instagram YouTube’a Rakip Oluyor! Uzun Videolar Geliyor — Instagram, YouTube’a ciddi rakip olmasını sağlayacak “Features” isimli yeni özellik test ediyor. Bu özellik, 90 dakikaya kadar videoları platforma getirecek.
[98] (Webtekno, tr, 2026-10-27) Microsoft, 60 Bin Çalışanı İçin Gönüllü İşten Ayrılma Programı Başlattı — Microsoft, maliyetleri kısmak için toplu işten çıkarma yerine farklı bir alternatif deniyor.
[99] (Webtekno, tr, 2026-10-27) Apple, iPhone Duo’daki Ekran Çatlaması Problemiyle Açıklama Yaptı — Apple, iPhone Duo satın alan kullanıcıların ilk günden yaşadığı ekran çatlaması problemi hakkında açıklama yaptı.
[100] (Webtekno, tr, 2026-10-27) Casper NevoPro P40 vs Casper Nirvana X100: Hangisi Kime Uygun? — Yapay zeka destekli donanımlar, yüksek pil ömrü ve taşınabilirlik: Casper'ın en yeni nesil iş ve ofis bilgisayarları arasında doğru seçimi yapmak için tüm özellikleri, bütçeleri ve performans puanlarını masaya yatırıyoruz.
[101] (Webtekno, tr, 2026-10-27) Fiat Doblo, Opel Combo, Peugeot Rifter Gibi Modellerin Bursa’daki Üretimi Resmen Başladı — 4 farklı markanın toplam 5 modelinin Bursa’da üretilmesini sağlayacak Tofaş, Koç ve Stellantis ortaklığının 300 milyon dolarlık K9 projesi seri üretime geçti.
[102] (Webtekno, tr, 2026-10-27) GTA 6 Temalı DualSense Kontrolcünün Türkiye Fiyatı Belli Oldu — GTA 6 temalı özel tasarım PS5 DualSense oyun kumandasının Türkiye fiyatı belli oldu.
[103] (Webtekno, tr, 2026-10-27) Türkiye'deki iPad Fiyatlarına Yine Zam Geldi: İşte Yeni Fiyatlar — Apple, yeni iPad mini duyurusunun ardından Türkiye'deki iPad modellerine zam yaptı.
[104] (Webtekno, tr, 2026-10-27) OpenAI, Bilgisayarınızı Sizin Yerinize Kullanacak GPT-6.1 Terra'yı Tanıttı — OpenAI, rutin bilgisayar işlerini devralacak orta segment yapay zekâ modeli GPT-6.1 Terra’yı tanıttı.
[105] (Webtekno, tr, 2026-10-27) Apple Müjdeyi Verdi: Siri AI'a Yakında Türkçe Geliyor! — Apple, Siri AI'a yakında Türkçe geleceğini açıkladı. Tarihi konusunda da bilgi verildi.
[106] (ShiftDelete.Net, tr, 2026-10-27) Mini LED mi OLED mi? Hangi TV Alınmalı? (Büyük Ekran Rehberi) — Yeni bir televizyon satın alma kararı, telefon gibi sık değiştirilmeyen ve evin baş köşesinde ortalama 8 ila 10 yıl boyunca bize eşlik eden bir yatırımı temsil ediyor. Bu süreçte doğru paneli ve ekran boyutunu seçmek uzun vadeli seyir zevki açısından kritik önem taşırken, son dön
[107] (ShiftDelete.Net, tr, 2026-10-27) Apple Türkiye Tüm Mac Modellerine Zam Yaptı: İşte Güncel Fiyat Listesi — Apple, Türkiye pazarındaki ürün gamında kapsamlı bir fiyat güncellemesine gitti. Giriş seviyesi dizüstü bilgisayarlardan profesyonel masaüstü sistemlerine kadar neredeyse tüm Mac ailesi zam dalgasından nasibini aldı. Yapılan son güncellemeyle birlikte hem popüler MacBook Air seri
[108] (ShiftDelete.Net, tr, 2026-10-27) Apple Creator Studio Güncellendi: Final Cut Pro, Logic Pro ve Pixelmator Pro İçin Yapay Zeka Hamlesi — Apple; video kurgu, ses prodüksiyonu ve görsel tasarım araçlarını tek çatı altında toplayan Apple Creator Studio paketini yapay zeka odaklı yeni özelliklerle güncelledi. Yapılan duyuruyla birlikte Final Cut Pro doğrudan yerleşik MotionVFX eklentilerine ve Pixelmator Pro entegrasy
[109] (ShiftDelete.Net, tr, 2026-10-27) Apple M6 Çipli Yeni iMac Tanıtıldı: Yapay Zeka Odaklı Performans — Apple, hepsi bir arada (all-in-one) masaüstü bilgisayar serisinin en yeni üyesi olan M6 işlemcili iMac modelini resmi olarak duyurdu. İnce tasarım çizgisini ve yedi farklı renk seçeneğini koruyan yeni nesil iMac; 12 çekirdeğe kadar ölçeklenen M6 çipi, çift Neural Engine mimarisi,
[110] (ShiftDelete.Net, tr, 2026-10-27) Apple M6 Çipli 14 İnç MacBook Pro Tanıtıldı: Yapay Zeka ve 24 Saatlik Pil Ömrü — Apple, profesyonel dizüstü bilgisayar ailesinin en popüler üyelerinden olan 14 inç MacBook Pro modelini yeni nesil M6 işlemcisiyle güncelledi. Donanım tarafında doğrudan cihaz içi yapay zeka işlem gücüne, yüksek grafik verimliliğine ve pil tasarrufuna odaklanan model, tek şarjla 
[111] (ShiftDelete.Net, tr, 2026-10-27) KKB Hackathon 2026 Sona Erdi: Genç Geliştiriciler Yapay Zekayla Yarıştı — Kredi Kayıt Bürosu (KKB) tarafından düzenlenen KKB Hackathon, bu yıl ikinci kez kapılarını açarak genç yetenekleri veri ve yapay zeka odaklı projelerde buluşturdu. MEXT Teknoloji Merkezi’nde gerçekleşen final maratonunda, “Agentic Data Analytics” teması kapsamında yarışan ünivers
[112] (ShiftDelete.Net, tr, 2026-10-27) Acer Predator Atlas 8 Fiyatı Belli Oldu! PC mi Alıyoruz El Konsolu mu? — Acer'ın yeni Intel Arc destekli el konsolu Predator Atlas 8, 1 Kasım'da 1.300 dolar fiyatla piyasaya çıkıyor. İşte cihazın özellikleri ve detayları.
[113] (ShiftDelete.Net, tr, 2026-10-27) Microsoft’tan Kritik Uyarı: Yapay Zeka Ajanlarına Güvenilmemeli — Microsoft, yapay zeka ajanlarının tahmin edilemez doğası nedeniyle kurumlar için risk oluşturduğunu ve bu sistemlere tam güvenilmemesi gerektiğini açıkladı.
[114] (ShiftDelete.Net, tr, 2026-10-27) X’in Yeni Ürün Sorumlusu Peter Sellis Oldu: Nikita Bier Görevi Devretti — Elon Musk’ın sahibi olduğu sosyal medya platformu X, tepe yönetiminde kritik bir bayrak değişimine imza atıyor. Yaklaşık bir yıldır X’in ürün geliştirme süreçlerini yöneten Nikita Bier görevinden ayrılırken, platformun yeni ürün sorumlusu koltuğuna sektörün deneyimli isimlerinden
[115] (ShiftDelete.Net, tr, 2026-10-27) Uygun Fiyatlı iPhone 18e Özellikleri ile Sızdı: Ekran Kaç Hz Olacak? — Apple’ın uygun fiyatlı ve kompakt akıllı telefon serisinde yeni bir dönem kapıda. Standart iPhone 18 ve iPhone Air 2 modelleriyle birlikte 2027 yılının ilk çeyreğinde resmiyet kazanması beklenen iPhone 18e modeline dair ilk teknik veriler gün yüzüne çıktı. Güvenilir sızıntı kayna
[116] (ShiftDelete.Net, tr, 2026-10-27) Fiat Doblo Yeniden Türkiye’de Üretilecek — Türk otomotiv sektörünün simge modellerinden Fiat Doblo, üç yıllık ayrılığın ardından yeniden Bursa’daki Tofaş fabrikasında banttan inmeye başlıyor. Koç Holding ve Stellantis ortaklığında hayata geçirilen yaklaşık 300 milyon dolarlık dev K9 projesi kapsamında Doblo’nun yanı sıra 
[117] (ShiftDelete.Net, tr, 2026-10-27) IT şirketleri ve dijital ajanslarda proje yönetimi: Otomasyon iş süreçlerini nasıl değiştiriyor? — IT şirketleri ve dijital ajanslar, aynı anda birden fazla müşteriyle çalışırken farklı projeleri, teslim tarihlerini ve ekiplerin iş yükünü yönetmek zorunda kalıyor. Yazılım geliştirme, web tasarımı, dijital pazarlama ve içerik üretimi gibi süreçlerde müşteri taleplerinin doğru k
[118] (ShiftDelete.Net, tr, 2026-10-27) Hastanelerde Islak İmza Dönemi Sona Erdi: SMS ve e-Nabız ile Onay Devri Başladı — Sağlık Bakanlığı, sağlık kuruluşlarındaki bürokrasiyi azaltacak ve dijitalleşmeyi hızlandıracak kritik bir adımı devreye aldı. Resmi Gazete’de yayımlanarak yürürlüğe giren yeni yönetmelikle birlikte tıbbi müdahaleler öncesinde hastalardan alınan bilgilendirilmiş onam (rıza) forml
[119] (ShiftDelete.Net, tr, 2026-10-27) Alibaba’nın Qwen Modeli için Güvenlik Uyarısı: Çin’e Veri Gönderiyordu — Alibaba'nın Qwen3.8-Flash-Next modeli, Cohere'in güvenlik testinde Pekin'e veri göndermeye çalıştı. Olayın detayları ve uzman görüşleri haberimizde.
[120] (ShiftDelete.Net, tr, 2026-10-27) En İyi Laptop Soğutucular (5 Tavsiye) — Özellikle oyun oynarken karşılaşılan laptop ısınma sorunu, aynı zamanda video düzenlerken veya uzun süre bilgisayar başında çalışırken de kullanıcıların canını sıkabilmektedir. Cihazın hava akışını desteklemek için tercih edilen soğutucular, laptopun alt kısmında hava dolaşımını 
[121] (DonanımHaber, tr, 2026-10-27) ABD'de toplu konutlara kurulacak jeotermal ısı pompaları, hem ısıtmayı hem soğutmayı yapacak — Yer altındaki sıcaklıktan yararlanan jeotermal ısı pompaları, ABD'deki yeni bir konut projesinde kullanılacak. Sistemin kurulum maliyetini ise yerel bir doğal gaz şirketi karşılayacak.
[122] (DonanımHaber, tr, 2026-10-27) OpenAI GPT-6.1 Terra duyuruldu: Maliyette radikal ilerleme — OpenAI, GPT-6.1 Terra modelini duyurdu. GPT-6 Astra seviyesinde performans sunan model, daha düşük maliyet, yüksek hız ve gelişmiş kodlama yetenekleriyle öne çıkıyor.
[123] (DonanımHaber, tr, 2026-10-27) Volkswagen, Avrupa’da Çin yazılımına geçebilir: Dev tasarruf planı — Volkswagen, Çin’de geliştirdiği elektronik mimariyi Avrupa’daki elektrikli modellerine taşımayı değerlendiriyor. Bu plan gruba 4 ila 5 milyar euro arasında geliştirme tasarrufu sağlayabilir.
[124] (DonanımHaber, tr, 2026-10-27) Microsoft'tan yapay zeka uyarısı: "AI modellere güvenilemez" — Microsoft Security yöneticisi Hayete Gallot, güncel yapay zeka modellerinin güvenilmez olduğunu ve AI ajanlarının şirket sistemlerinde gereğinden fazla yetkiyle hareket ettiğini söyledi.
[125] (DonanımHaber, tr, 2026-10-27) Uygun fiyatlı MacBook Neo artık uygun değil: MacBook Neo ve Air zamlandı — Apple bugün MacBook modellerinde fiyat artışına gitti. Şirketin uygun fiyatlı dizüstü bilgisayarı MacBook Neo 50 bin TL sınırına dayandı, MacBook Air ise 100 bin TL'ye yükseldi.
[126] (DonanımHaber, tr, 2026-10-27) Ağaca ve direğe çarpıp devrildi, hava yastıkları açılmadı: Xpeng’den açıklama — Çin’de kaza yapan Xpeng X9’un sahibi, araç pert olmasına rağmen hava yastıklarının açılmadığını söyledi. Markaya göre çarpışma, hava yastıklarını devreye sokacak tetikleme koşullarını karşılamadı.
[127] (DonanımHaber, tr, 2026-10-27) Anthropic halka arz için başvurdu: Değerlemesi 2 trilyon dolara ulaşabilir — Anthropic, Nasdaq borsasına halka arz için başvurdu. Yılık ilk altı ayında 16,3 milyar dolar gelir elde eden şirketin değerlemesinin 2 trilyon dolara ulaşabileceği belirtiliyor.
[128] (DonanımHaber, tr, 2026-10-27) Apple, M6 işlemcili yeni iMac modelini tanıttı: İşte Türkiye fiyatı ve özellikleri — Apple, yeni M6 işlemcili iMac modelini tanıttı. Yapay zeka performansında 5 kata kadar artış vadeden bilgisayar, yedi renk seçeneği ve dikkat çeken yeniliklerle geliyor.
[129] (DonanımHaber, tr, 2026-10-27) M6 çipli 14 inç MacBook Pro tanıtıldı: İşte Türkiye fiyatı ve özellikleri — Apple, yeni M6 iMac'in yanı sıra M6 çipiyle güçlendirilmiş yeni 14 inç MacBook Pro'yu tanıttı. M6 çipli MacBook Pro Türkiye fiyatı 138 bin TL'den başlıyor ve 28 Ekim'de ön satışa sunulacak.
[130] (DonanımHaber, tr, 2026-10-27) Otomobillere yeni ışık geliyor: Turkuaz ışık ne işe yarayacak? — Otomotiv dünyasında araç aydınlatma teknolojileri için yeni bir dönemin kapısı aralanıyor. ABD'de gündeme gelen son öneri, otonom araçlara özel turkuaz ışıkların entegre edilmesini öngörüyor.
[131] (DonanımHaber, tr, 2026-10-27) Yapay zeka para kazandırmıyor: Teknoloji sektörü dışında getiri sıfır — Apollo ekonomistine göre yapay zeka, teknoloji sektörü dışındaki büyük şirketlere henüz finansal katkı sağlamadı. Çalışan başına gelir ve kâr marjlarında artış görülmüyor.
[132] (DonanımHaber, tr, 2026-10-27) Intel Nova Lake-S çıkmadan test edildi! İşte ilk detaylar — Intel'in yeni nesil Nova Lake-S işlemcilerine ait olduğu düşünülen benchmark sonuçları ortaya çıktı. 28 çekirdekli model, tek çekirdekte Core Ultra 9 285K'yı geride bıraktı.
[133] (DonanımHaber, tr, 2026-10-27) Türkiye’nin petrol ve doğal gaz bağımlılığını azaltacak fırsat: Elektrik — Ember raporuna göre Türkiye’nin enerji tüketiminin yüzde 85’i mevcut teknolojilerle elektrikle karşılanabilir. Ancak 2035 hedefi için ulaşım, sanayi ve binalarda dönüşümün hızlanması gerekiyor.
[134] (DonanımHaber, tr, 2026-10-27) Instagram, YouTube'a meydan okuyor: 90 dakikalık videolar geliyor — Instagram, 90 dakikaya kadar uzun süreli yatay video formatını test etmeye başladı. Features olarak adlandırılan yeni format, belirli içerik üreticilerine sunuldu. İşte ayrıntılar:
[135] (DonanımHaber, tr, 2026-10-27) Sceye'nin uçan baz istasyonu, ABD'den Japonya'ya 30 bin km yol katetti — ABD merkezli Sceye, gökyüzünden mobil bağlantı sağlayan uçan baz istasyonuyla ABD-Japonya arasında 30 bin kilometre yol katetti. Bu süre boyunca standart telefonlara bağlantı sundu.

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
