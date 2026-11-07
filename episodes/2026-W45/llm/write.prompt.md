# Görev: write

Yanıtı `episodes/2026-W45/llm/write.response.json` dosyasına, aşağıdaki JSON şemasına uyan TEK bir JSON nesnesi olarak yaz.

## Sistem talimatı

Sen GDG on Campus Kastamonu'nun haftalık, yapay zekâyla üretilen 80-105 saniyelik dikey teknoloji gündemi videosunun senaristisin.
Kitle: Türkiye'deki üniversite öğrencileri. Ton: enerjik ama abartısız, samimi "sen" dili, haber spikeri netliği. Tıklama tuzağı yok.

Görev: Verilen aday haberlerden 4-4 tanesini seç ve senaryoyu şemaya uygun üret.

Seçim:
- Öğrencinin işine yarayan (başvuru, ücretsiz araç, yarışma, açık kaynak sürüm) haberleri öne al; konu çeşitliliği gözet (hepsi aynı şirketten olmasın).
- Kaynak metni boş veya çok kısa olan haberi seçme.

KESİN KURALLAR (ihlal edilirse bölüm yayınlanmaz):
1. Kaynak metinlerde geçmeyen HİÇBİR rakam, isim, tarih, sürüm numarası veya özellik kullanma. Yuvarlama yapma; sayıyı kaynaktaki gibi ver.
2. Anlatımdaki ve "student_take"teki her olgusal ifadeyi `claims` listesine yaz ve kaynağını `source_url` ile bağla. source_url, o segmentin `sources` listesinde olmalı.
3. Kaynağın açıkça söylemediği, çıkarım/yorum içeren her iddiayı `uncertain: true` yap. Emin değilsen kullanma ya da uncertain işaretle.
4. student_take somut olsun: kaynakta bir başvuru tarihi, ücretsiz erişim, indirilebilir araç varsa onu söyle; yoksa genel ama doğru bir öneri ver (ör. "dokümanı incele", "projende dene") ve tarih/rakam uydurma.
5. Uzunluk: seslendirilen her şeyin (hook, teaser, bridge'ler, narration'lar, student_take'ler, question, outro) toplamı 155-195 kelime (Türkçe ~1.9 kelime/sn). Haber başına narration ~20-26 kelime, student_take ~8-12 kelime; kısa ve vurucu tut.
6. Metinlerde rakamları rakamla, İngilizce terimleri orijinal yazımıyla yaz (OpenAI, GPU, %12). Seslendirme için ayrı bir normalizasyon adımı var.
7. Şirket logosu veya gerçek kişi fotoğrafı isteme; görselleri yalnızca şemadaki component'lerle tarif et.

Akış ve izleyiciyi tutma (Instagram Reels; ilk 3 saniye ve "sona kadar izlenme" belirleyici):
- Sıra: en çarpıcı haber ilk sırada (hook onu anlatır), öğrencinin en çok işine yarayan haber EN SONDA.
- hook: haftanın en çarpıcı gelişmesi, tek cümle, en fazla 8 kelime; "Merhaba"yla veya "Bu hafta"yla başlama. Soru ya da şaşırtıcı bir olgu olabilir.
- teaser: hook'tan hemen sonra, en fazla 12 kelime. Kaç haber olduğunu ve sondaki haberin izleyiciyi doğrudan ilgilendirdiğini ima ederek merak boşluğu aç (ör. "Dört haber var; sonuncusu doğrudan senin bilgisayarını ilgilendiriyor."). Sonda gerçekten karşılığı olmalı; tıklama tuzağı yok.
- bridge: her haberin önünde, en fazla 7 kelime. Önceki haberden bir sonrakine anlamlı bir köprü kur ya da izleyiciye seslen ("Güvenlik demişken, asıl risk telefonunda.", "Şimdi sıra söz verdiğim habere."). Klişe "İkinci haberimiz..." kullanma. İlk haberin bridge'i boş olabilir. Son haberin bridge'i teaser'daki sözü hatırlatsın.
- narration içinde de kısa cümleler; her habere bir "neden önemli" anı koy.
- question: kapanıştan önce izleyiciye yorumda cevaplayacağı, kişisel ve kolay bir soru (en fazla 10 kelime; ör. "Sen Siri'yi Türkçe kullanır mıydın? Yorumlara yaz.").
- outro: en fazla 8 kelime, takip çağrısı (ör. "Takip et, haftaya yeni gündemle buradayız.").
- teaser, bridge, question ve outro YENİ olgu (rakam, isim, tarih) içermez; yalnızca segmentlerde geçen bilgilere atıf yapar.

Görseller (her segmentte 2-4, ilk görsel HeadlineCard):
- StatCounter: kaynakta çarpıcı tek bir sayı varsa.
- MiniChart: kaynakta karşılaştırılabilir en az 2 sayı varsa (ör. eski/yeni performans).
- CodeBlock / Terminal: geliştirici haberlerinde kaynaktaki kod/komut veya resmi kurulum komutu varsa (uydurma API çağrısı yazma).
- SourceScreenshot: duyuru sayfasının ekran görüntüsü; screenshot_url = ana kaynak URL. Her segmentte bir tane olması iyi.

## Girdi

Hafta: 2026-W45

<haber id="c003" puan="9" kaynak="TÜBİTAK Duyuruları" tarih="2026-11-02">
Başlık: 2247-C Stajyer Araştırmacı Burs Programı (STAR) 2026 Yılı 2. Dönem STAR Lisans ve STAR Öğretmen Çağrıları Açıldı
URL: https://tubitak.gov.tr/tr/duyuru/2247-c-stajyer-arastirmaci-burs-programi-star-2026-yili-2-donem-star-lisans-ve-star-ogretmen-cagrilari-acildi
Özet: TÜBİTAK 2247-C Stajyer Araştırmacı Burs Programı (STAR) 2026 2. dönem lisans ve öğretmen çağrıları açıldı.
<kaynak_metni>
TÜBİTAK Bilim İnsanı Destek Programları Başkanlığı (BİDEB) tarafından yürütülen 2247-C Stajyer Araştırmacı Burs Programı’nın (STAR) 2. aşaması olan öğrenci ve öğretmen başvuruları başladı. Program; TÜBİTAK Merkez ve Enstitülerinde yürütülen projeler ile TÜBİTAK tarafından desteklenen araştırma projelerine veya Yükseköğretim Kurulu’nın (YÖK) araştırma üniversitelerine yönelik başlattığı Araştırma Üniversiteleri Destek Programı (ADEP) tarafından desteklenen araştırma projelerine bursiyer olarak dâhil olacak lisans öğrencilerinin (STAR Lisans) bilimsel araştırma projelerinde görev almaları ve öğretmenlerin (STAR Öğretmen) mesleki bilgi ve becerilerinin gelişimini sağlayarak proje kültürü kazanmaları amaçlarını taşıyor.
2026 yılı 2. döneminde aşağıdaki çağrılar kapsamında lisans öğrencileri ile öğretmenlerden başvuru alınacaktır.
- STAR Lisans (Lisans Öğrencisi )
- STAR Öğretmen (Öğretmen)
STAR programının ikinci aşamasında lisans öğrencileri ve öğretmenler, proje yürütücülerinin talepleri doğrultusunda projelerde görev almak üzere 2 Kasım 2026-16 Kasım 2026 (17.30, TSİ) tarihlerinde başvuru yapabileceklerdir.
Başvurular, TÜBİTAK Yönetim Bilgi Sistemiüzerinden alınacaktır. Proje listesine BİDEB Başvuru ve İzleme Sistemi üzerinden, program çağrı metinlerine ise web adresimizden ulaşabilirsiniz.
İletişim: star@tubitak.gov.tr
</kaynak_metni>
</haber>

<haber id="c015" puan="9" kaynak="GitHub Blog" tarih="2026-11-01">
Başlık: Game Off 2026: The theme is SHIFT
URL: https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/
Özet: GitHub'ın yıllık oyun yarışması Game Off 14. kez başladı; Kasım boyunca SHIFT temasından ilham alan oyunlar yapılacak.
<kaynak_metni>
Senior Program Manager, GitHub Developer Relations. Open source hype man, AI whisperer, hackathon and game jam wrangler. I write && manage programs, support dev communities, and occasionally ship something.
It’s time to make Shift happen.
Game Off, GitHub’s annual month-long game jam, returns for its 14th year this November. Thousands of developers have joined us over the years to make everything from polished platformers to wonderfully weird experiments.
Whether you’re making your first game or your fiftieth, we’d love for you to join us.
The theme for Game Off 2026 is SHIFT!
Shift gears. Shift perspectives. Shift dimensions. Shift bits. Work the night shift. Or make a game where the only buttons are the Shift keys.
How you interpret the theme is entirely up to you.
You have until December 1, 2026, at 13:37 PST to build and submit a game inspired by SHIFT. Strong or loose inspirations apply!
Need inspiration? Here are a few concept ideas
- A one-button (or two-button) game where the Shift keys are is your only control.
- A racing game where shifting gears changes more than your speed. Second gear reverses gravity, third slows time, and fourth removes the brakes.
- A perspective puzzler where rotating the camera turns walls into floors and shifts shadows into platforms.
- A puzzle-platformer where you shift between two overlapping realities. That broken bridge might exist in the other world. Unfortunately, so might the monster standing on it.
- A shapeshifting adventure where you transform into creatures and objects, inheriting their abilities and weaknesses.
- A night-shift horror game set in a convenience store where the customers get progressively stranger, and whatever’s in aisle seven definitely isn’t covered by your training.
- A comedy detective game where you committed the crime and must shift the blame onto increasingly unlikely suspects without contradicting the evidence.
- A programming puzzler: Use bitwise shifts to manipulate the world. Shift left to double an object’s size, shift right to halve it, and discover what happens when you run out of bits.
- An adventure game about convincing somebody to cover your shift so you can attend the final boss battle.
Of course, you could also build a game about shifting tectonic plates, shape-shifting aliens, shifting alliances, shifting sands, or a particularly ambitious stick shift.
Don’t overthink it. Pick an interpretation that interests you and see where it takes you.
Pro tip: Start with one mechanic and one playable level. Get those working before adding the multiverse. Future you (and your bug tracker) will thank you.
Need another perspective? Try brainstorming with GitHub Copilot. Give it the theme, a few constraints, and see what it comes up with:
Act as an indie game designer. Suggest 10 original game concepts inspired by SHIFT, each with a unique core mechanic, genre, and technical twist. Prioritize ideas a solo developer could prototype in a weekend.
How to participate
Work alone or form a team. Use whichever programming languages, game engines, frameworks, libraries, and tools make sense for your game.
- Create a free GitHub account if you don’t already have one.
- Join the jam. Head to the Game Off 2026 page on itch.io. If you don’t have an itch.io account, you can sign in with your GitHub account.
- Create a public repository. Store your game’s source code on GitHub. Push your game before December 1, 2026, at 13:37 PST.
- Submit your game on itch.io before December 1, 2026, at 13:37 PST. Pushing your code to GitHub does not submit your entry to the jam. After submissions close, you’ll be able to play other entries and cast your votes.
Voting
Here’s the fun part: you decide who wins.
Once submissions close, it’s your turn to play and rate the games your fellow developers have created. Every vote helps determine which games take home the bragging rights.
Entries will be evaluated in the following categories:
- Overall
- Gameplay
- Graphics
- Audio
- Innovation
- Theme interpretation
Voting will end on January 1, 2027, at 13:37 PST. Winners will be announced on the GitHub Blog and GitHub social channels shortly thereafter.
Light rules
Game Off is intentionally relaxed, but there are a few guidelines to help keep it fair and fun:
- Your game must live in a GitHub repository. You should begin the project during the jam, although templates and starter projects are welcome. The vast majority of the work should take place during the Game Off submission period.
- License it however you like. Open source is encouraged but not required.
- Fly solo or join a team. Work in whichever way makes you most comfortable.
- Use any tools and assets you prefer. Open source, commercial, commissioned, and original assets are all welcome.
- AI-assisted development is allowed. We recognize that AI use in game development is a sensitive subject, and participants have different perspectives. When submitting your game, you’ll be asked about your use of AI so others can better understand how it was made.
That’s it. Keep it creative, respectful, and fun… and make sure your final code is pushed before the deadline.
Help
New to game development?
You don’t need to be an expert to participate. Many Game Off participants create their first game during the jam.
Some use established engines. Some build their own. Others make games for old consoles, unusual hardware, terminals, calculators, or platforms we assumed had been lost to time.
However you build your game, there’s no single correct way to play.
Here are a few engines and frameworks you might want to explore:
- Godot (GDScript, C#, C++): Open source, lightweight, beginner-friendly, and excellent for both 2D and 3D games.
- Unity (C#): A popular option for 2D, 3D, mobile, and XR games, with a large ecosystem of tutorials and assets.
- Unreal Engine (C++, Blueprints): A strong choice for cinematic visuals, complex 3D environments, and high-end experiences.
- Phaser (JavaScript, TypeScript): Great for browser-based 2D games, arcade games, and platformers.
- Pygame (Python): A friendly way to learn game development fundamentals or prototype an idea quickly.
- Bevy (Rust): A modern, data-driven engine built around an entity component system.
- LÖVE (Lua): Lightweight, fast, and well suited to 2D games and creative experiments.
- Flame (Dart, Flutter): A useful option for developers interested in mobile-first 2D games.
- Ebitengine (Go): A straightforward, cross-platform 2D game engine for Go developers.
- Defold (Lua): A compact, cross-platform engine with built-in development tools.
- libGDX (Java): A familiar option for developers coming from Java or Android development.
- HaxeFlixel (Haxe): A good fit for retro-inspired 2D games, platformers, and fast-paced jam projects.
- raylib (C, plus bindings for other languages): A simple, code-first library for developers who want to work closer to the metal.
- PICO-8 (Lua): A fantasy console with deliberate constraints, ideal for tiny games with distinctive pixel-art aesthetics.
- TIC-80 (multiple languages): Another fantasy computer for making, playing, and sharing small games.
Looking for teammates or a place to share progress? The Game Off 2026 Community is a great place to ask questions, share progress, and look for teammates. There’s also a friendly community-run Discord server.
New to Git or GitHub?
Game Off is the perfect opportunity to check it out. Version control pun fully intended.
- Git documentation: Learn the fundamentals of version control and get started with Git.
- GitHub Docs: Explore tutorials, guides, and documentation for building and collaborating on GitHub.
- GitHub Community: Ask questions, share your work, and connect with other developers.
Whether you spend November shifting pixels, shifting bits, shifting timelines, or shifting unfinished tasks into the final 24 hours, you’ll be part of a global community making games together.
So take a different perspective, change the rules, and see what happens when you press ⇧.
Good luck and have fun! Can’t wait to play, err, test all your games! <3
Tags:
Written by
Related posts
GitHub now highlights ACCESSIBILITY.md files and helps maintainers document accessibility goals, known barriers, supported environments, contributor expectations, and reporting processes.
</kaynak_metni>
</haber>

<haber id="c016" puan="8" kaynak="Google Blog" tarih="2026-11-05">
Başlık: Generate longer AI videos with Omni 1.2 Flash in Google Vids at no cost.
URL: https://blog.google/products-and-platforms/products/workspace/omni-1-2-flash-google-vids/
Özet: Google Vids'te Omni 1.2 Flash ile daha uzun yapay zeka videoları ücretsiz oluşturulabiliyor.
<kaynak_metni>
Generate longer AI videos with Omni 1.2 Flash in Google Vids at no cost.
Google Vids, our video creation and editing tool, now runs on Google's newest video generation model: Omni 1.2 Flash. Starting today, anyone with a Google account or Google Workspace subscription can generate up to three 15-second videos per month in Vids at no cost.
With Omni 1.2 in Google Vids, you can now bring your ideas to life in so many more ways:
- Create your product promos in one go. Produce professional, quick-turn social content and promotional materials without a single cut.
- Transform static imagery into engaging videos. Upload reference images from anything — a trip, a school project, or learning materials — and your characters and scenes will stay consistent, from the first frame to the last.
- Make clips that sound more natural. With improved speech narration, your social clips, concept explainers, and teaser videos feel like something you recorded yourself.
If you can describe it, you can make it. Try Google Vids out at vids.new.
</kaynak_metni>
</haber>

<haber id="c050" puan="8" kaynak="OpenAI News" tarih="2026-11-04">
Başlık: A thousand fewer paths to root
URL: https://openai.com/index/a-thousand-fewer-paths-to-root
Özet: OpenAI'ın otonom hattı, Linux çekirdeğinde 948 yerel yetki yükseltme açığını bulup doğruladı ve yamalarını üretti.
<kaynak_metni>
(metin alınamadı)
</kaynak_metni>
</haber>

<haber id="c000" puan="6" kaynak="TÜBİTAK Duyuruları" tarih="2026-11-05">
Başlık: TÜBİTAK Bilim Söyleşileri 2026 Yılı Başvurularının Süresi Uzatıldı
URL: https://tubitak.gov.tr/tr/duyuru/tubitak-bilim-soylesileri-2026-yili-basvurularinin-suresi-uzatildi
Özet: TÜBİTAK Bilim ve Toplum Başkanlığı'nın yürüttüğü Bilim Söyleşileri'nin 2026 başvuru süresi uzatıldı.
<kaynak_metni>
TÜBİTAK Bilim ve Toplum Başkanlığı tarafından yürütülen Bilim Söyleşileri programı, alanında uzman bilim insanlarını ilkokul, ortaokul ve lise düzeyindeki öğrenciler başta olmak üzere bilime ilgi duyan tüm vatandaşlarla buluşturmayı amaçlamaktadır. Bu etkinliklerle ayrıca toplum ve bilim dünyası arasındaki bağın güçlendirilmesi, bilimsel bilgiye erişimin kolaylaştırılması ve bilim okuryazarlığının artırılması hedeflenmektedir.
Bilim Söyleşileri 2026 Yılı Çağrısı yayımlanmış olup yeni dönem başvuruları uzatılmıştır. Yeni döneme ilişkin bazı güncellemeler ise şöyledir:
- TÜBİTAK Bilim Söyleşileri başvuru sayfası ve sunum şablonu güncellendi.
- Bilim söyleşisinin gerçekleştirileceği okulda TÜBİTAK Bilim Fuarı da düzenlenecekse iki etkinliğin aynı gün yapılması önerilmektedir.
TÜBİTAK Bilim Söyleşileri’ne ilişkin ayrıntılı bilgi ve başvuru şartları için lütfen tıklayınız.
Son Başvuru Tarihi: 13 Kasım 2026 (17.30, TSİ)
Başvuru için lütfen tıklayınız.
</kaynak_metni>
</haber>

<haber id="c001" puan="6" kaynak="TÜBİTAK Duyuruları" tarih="2026-11-04">
Başlık: 2244–Sanayi Doktora Programı 2026 Yılı Çağrısı Açıldı
URL: https://tubitak.gov.tr/tr/duyuru/2244-sanayi-doktora-programi-2026-yili-cagrisi-acildi-0
Özet: Sanayide doktoralı araştırmacı istihdamını teşvik eden 2244-Sanayi Doktora Programı'nın 2026 çağrısı açıldı.
<kaynak_metni>
Sanayide ihtiyaç duyulan doktora derecesine sahip nitelikli insan kaynağının üniversite-sanayi iş birliğiyle yetiştirilmesi ve sanayide doktoralı araştırmacı istihdamının teşvik edilmesini amaçlayan, TÜBİTAK Bilim İnsanı Destek Programları Başkanlığı (BİDEB) tarafından yürütülen 2244–Sanayi Doktora Programı çağrısı açılmıştır.
2244–Sanayi Doktora Programı’na başvurular çevrim içi olarak TÜBİTAK Yönetim Bilgi Sistemi (TYBS) üzerinden 22 Aralık 2026 tarihine kadar alınacaktır.
2244–Sanayi Doktora Programı hakkında bilgi almak ve çağrı duyurusuna ulaşmak için tıklayınız.
</kaynak_metni>
</haber>

<haber id="c017" puan="7" kaynak="Google Blog" tarih="2026-11-05">
Başlık: Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips
URL: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/
Diğer kaynaklar: https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/
Özet: Google, hızlı ve uygun maliyetli, daha uzun klipler üreten video modeli Gemini Omni 1.2 Flash'i tanıttı.
<kaynak_metni>
Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips
Today, we’re rolling out Gemini Omni 1.2 Flash, and making it generally available across the Gemini API and Gemini for business. Gemini Omni 1.2 Flash introduces native 15-second video creation, multi-turn conversational editing capabilities, and enhanced reference following. We have dropped the price 30% from Gemini Omni 1.1 making it available at $0.07 per second for 720p video.
Here’s an overview of what’s new:
Fast and cost-effective at scale
Beyond the lower price, the workflow keeps costs down: you can draft fast at 360p or 720p, fix a detail with a follow-up edit instead of re-generating the entire clip, and then upscale your best creations to 1080p or 4K.
Longer clips up to 15 seconds
You can now generate and edit videos natively up to 15 seconds long, up from 10 seconds with Omni 1.1. You can also specify duration in one-second increments from 3 to 15 seconds, giving you room to tell complete stories, create product explainers, or produce full social ad spots in a single generation.
Better reference adherence
You can guide generation combining character, product, or style images, short motion clips (up to three seconds), and audio cues — and Omni 1.2 Flash holds onto those details from start to finish. Faces, garments, packaging typography, and brand colors stay consistent across camera angles, making it easy to turn existing product photography or character sheets into virtual try-on clips, catalog spins, and branded video ads.
Combining one model photo with front-and-back product shots of three outfits, Gemini Omni 1.2 Flash generates a 15-second virtual try-on sequence across 360-degree turns and match cuts while keeping the model’s identity and each garment’s cut, drape, and back details consistent.
More consistent results
You can maintain stronger character, object, and scene consistency from the first to the last frame, with less visual drift or morphing across motion and camera transitions. Whether you’re interpolating between a first and last keyframe, or extending a clip to build a longer sequence, products, characters, props, and environments stay consistent from shot to shot.
Given the same static studio lighting exhibition poster and five-layer animation prompt, Gemini Omni 1.1 Flash does not match the reference image as closely as 1.2 does. Gemini Omni 1.2 Flash builds the poster sequentially layer by layer on the dusty-pink cyclorama rising the hexagonal plinth, assembling the ribbed glass, warm filament, faceted crystal, and coiled-cord letterforms for HALO, GLOW, and LUMEN, and locking every material, shadow, and typographic detail consistently through the final frame.
Easier editing in conversation
You can refine the same clip turn by turn — such as swapping a product or background, changing the lighting or weather, or switching the aspect ratio — instead of starting over from scratch. Multi-turn conversational editing works across full 15-second clips, making it easy to produce ad variants for different audiences and placements without re-briefing or re-generating.
Starting from one generated clip, multi-turn conversational prompts swap the background turn by turn — from a striped pavilion tent to an oak forest, a stable with a white horse, a market fair, and a stone castle — while keeping both characters’ performances, armor reflections, and camera framing intact.
More natural speech
You can generate scenes with more fluid, natural-sounding dialogue, clearer lip-sync, and distinct multi-speaker conditioning. This will show up whether you’re directing multi-character dialogue in Flow, creating video explainers in Gemini for business, or creating polished, pro videos with avatars, music and narration in Google Vids.
Conditioned on one conservatory scene image alongside four character, mouth, and one-second voice references, Gemini Omni 1.2 Flash routes each sampled voice to the right character with expressive lip-sync and natural comedic timing across a 15-second animated scene.
More controllable, cinematic look
You can direct complex, continuous camera movements like sweeping FPV flythroughs to dramatic zoom-outs and orbits with significantly fewer unwanted jump cuts, steadier scale, and a more polished, cinematic look.
Guided by two architectural reference photos, Gemini Omni 1.2 Flash directs one continuous FPV drone flight across the piazza, through the bronze doors, and up through the Pantheon’s coffered dome to the oculus with zero jump cuts.
Longer clips with smoother motion and tighter consistency
Gemini Omni 1.2 Flash generates clips up to 15 seconds long that hold references together better than before. You can scroll through to see characters, text, and camera moves stay consistent across longer shots, multiple turns and transitions with no cuts.
Real-world results, from creatives to global brands
Businesses, startups, and creatives are already using Gemini Omni 1.2 Flash in their workflows. And for the first time, Gemini Omni is now generally available, backed by Google Cloud’s enterprise-grade infrastructure and security. Provisioned Throughput is available, and outputs carry an imperceptible SynthID watermark.
Get started with Gemini Omni 1.2 Flash
While development is ongoing to further improve things like fast sports action, rapid script changes and complex physics, Gemini Omni 1.2 Flash is ideal for businesses, developers, and creators producing videos at scale. You can get started with Gemini Omni 1.2 Flash today as it rolls out across Google’s products and developer platforms:
- For developers using the Gemini API: Prototype in Google AI Studio, explore interactive starter apps, and check out the developer documentation and pricing.
- For businesses: Try it in the Google Cloud console, and build enterprise solutions with the API.
- For everyone using Google apps: Direct scenes and multi-turn edits in Flow, generate 15-second clips at no additional cost in Google Vids with a Google account or Google Workspace subscription, create 15-second videos in the Gemini app (rolling out to Google AI Ultra subscribers), and scale video campaigns in Google Ads.
</kaynak_metni>
</haber>

<haber id="c019" puan="7" kaynak="Google Blog" tarih="2026-11-05">
Başlık: Transform a quick drawing into a live app with Gemini.
URL: https://blog.google/innovation-and-ai/products/gemini-app/turn-drawings-into-apps-gemini/
Özet: Gemini Canvas'a yüklenen çizimler çalışan uygulamalara dönüştürülebiliyor; kod anında üretilip düzenlenebiliyor.
<kaynak_metni>
Transform a quick drawing into a live app with Gemini.
Great app ideas often start on paper. Turn them into interactive tools with Gemini.
Here’s how.
- Upload a photo of your sketch, like an app mock-up, habit tracker, or game board to Gemini.
- Select the Canvas tool and ask Gemini: "Can you code this app?" Gemini reads your visual and writes the code.
- Test your tool in the preview window. Gemini can adjust colors, fonts, or features in real time.
Next time inspiration strikes, bring it to life with Gemini.
</kaynak_metni>
</haber>

<haber id="c005" puan="6" kaynak="Google Developers Blog" tarih="2026-11-06">
Başlık: Agent Distraction
URL: https://developers.googleblog.com/agent-distraction/
Özet: 913 binden fazla kodlama ajanı oturumunun analizi, ajanların koddaki TODO yorumlarına istenmeden yöneldiğini ve fazladan adım attığını gösteriyor.
<kaynak_metni>
What is easy for humans to skim past in code, agents see as a call to action. They do not know better, latching on to that which is littered across the files read during the planning and research phase of the coding journey.
As agents' agency through tools and skills grows the ability for side-quests scales proportionally. Obsolete specs, long resolved bugs, and lagging documentation no longer rest in long forgotten corners of the codebase, but rather are unintentionally ingested as context indirecting and misdirecting the next wave of coders - the agents. This indirection is not free: in the best case it only costs tokens, steps, and time - in the worst case it distracts and grounds the agent on falsehoods leading to incorrect logic and decisions during implementation.
Measuring how often agents fall into these traps across millions of monthly sessions is impossible with manual human review - we need an objective signal derivable from the code itself. Inline TODO(bug/...) comments provide the perfect proxy. TODOs tend to be left behind long after the underlying bug is resolved or abandoned, while the linked bug ticket acts as the canonical record. By cross-referencing every TODO an agent encounters against the TODO's bug status and the user's prompt, we can automatically separate valid work from wasted detours at scale.
By leveraging the distributed traces of agent interactions across thousands of engineers and over hundreds of millions of individual agent steps, we quantify the impact of TODO distractions in the codebase and how agents act on them:
Controlling for developer, codebase complexity, task type, model tier, number of files read, initial prompt length, and the step where the bug reference appeared, using a multi-way fixed-effects regression with developer-clustered standard errors, we see that unprompted bug detours add substantial overhead (all stat sig p<0.0001). Per session:
The Obsolete Detour: In the following trajectory we can observe how this drift plays out. During an investigation into an unrelated bug The agent views SurfaceControlTest.java and sees // TODO(bug/XXX)
This bug, while fixed in 2023, remains lingering in the codebase leading to subsequent investigation distraction across Steps with the agent digging into the bug to learn more.
The Eager Agent: In the trajectory the agent encountered a TODO in the bug it was investigating and decided (unprompted) to "fix" the code
The agent executed multiple Code Search and internal knowledge search queries for the bug ultimately resulting in the agent changing the ModelDownloaderV1 code. Later in the trajectory the human challenged the scope creep.
With the model when admitting it was an incorrect increase in scope:
While in both of these cases they were only trivial to minor detours - they were real distractions costing time, tokens, and human intervention.
As part of addressing this finding at scale we created agents that scrubbed the totality of our codebases, finding bug references in the code that were marked as fixed or obsolete for cleanup. That step alone however was not enough to determine if the TODOs in the codebase were load-bearing or not. The agents had to go further looking at the history of the bug, the file, and changes to the codebase, at times spanning years of history. Only in cases where the agent was able to confirm that the TODO and the intent behind the TODO was obsolete did our agent send a change for review to delete it from the codebase. As a result of this multi-layer approach, our todo cleaner has been able to remove thousands of actually obsolete references over the last 6 months exceeding 95% acceptance from human reviewers.
In recap, as we task agents on more and more ambitious problems, "agent friendly codebases" require more than just the code in the hotpath being healthy. The forgotten corners of the codebase now more than ever carry a significant tax levied against agents.
Tooling like presubmit analyzers, entire corpus scanners, and automated coding agents to remediate dead-todos offer out of the box ready to scale solutions to address the tax enabling a healthier and distraction free codebase for agents to thrive.
Projects that once were on the backburner to cleanup lingering debt but deprioritized due to perceived low value need to be reevaluated with the new agents acting at scale on your codebase.
</kaynak_metni>
</haber>

<haber id="c007" puan="6" kaynak="Android Developers Blog" tarih="2026-11-06">
Başlık: Build for an expanding lineup of Android XR devices with production-ready tools from Android Developer Summit
URL: https://developer.android.com/blog/posts/build-android-xr-devices-tools
Özet: Android Developer Summit'te Android XR için üretime hazır araçlar ve XREAL AURA cihazının çıkışı duyuruldu.
<kaynak_metni>
From full immersion at home to glanceable experiences on the go, building on Android XR lets you meet users wherever they are. At Android Developer Summit, we marked an exciting milestone with the launch of XREAL AURA, the first wired XR glasses powered by Android XR. Designed for lightweight comfort at under 95 grams with a portable compute puck, XREAL AURA leverages a shared Android foundation so your existing apps work out of the box on day one, giving you the perfect starting point to expand into richer spatial interactions.
To help you build for this expanding hardware landscape, we're delivering production-grade tools across the entire platform stack. We've graduated core Jetpack XR libraries and device emulators to stable, added real-world anchoring in ARCore for Jetpack XR, streamlined 3D engine workflows across Unity, Godot, and Unreal Engine.
Read the highlights of our announcements here, and head over to the Android Developer Summit XR Session Playlist to watch all technical walkthroughs on demand.
Stabilizing core Jetpack XR foundations and developer tooling
For developers building native experiences with Kotlin and Compose, production readiness begins at the platform layer. The core Jetpack XR SDK libraries have officially graduated to stable, providing long-term API stability and production performance. This stable release includes Jetpack SceneCore for building and manipulating the Android XR scene graph with 3D content, ARCore for Jetpack XR to handle environment perception, and XR Runtime for standardized session management. Alongside these libraries, Android XR emulators in Android Studio are now stable, letting you build, iterate, and visually validate layouts across XR devices directly from your laptop without needing physical hardware.
To see how these foundation APIs translate into real-world applications, watch Moving beyond 2D with custom 3D geometry in the Jetpack XR SDK. Discover how to animate glTF models, manipulate subnodes, use custom PBR materials at runtime, and generate real-time procedural 3D meshes in Kotlin using Jetpack SceneCore.
Anchoring digital experiences to the physical world
The Geospatial APIs in ARCore for Jetpack XR are now stable, enabling you to anchor digital content to real-world coordinates with high precision and robust local tracking. These capabilities unlock contextual, location-aware experiences across wired XR glasses by combining visual positioning services with local device perception.
In Build world anchored experiences for XREAL AURA wired XR glasses, you will learn how to design glanceable optical see-through UIs with Jetpack Compose Glimmer and anchor them to real-world locations. For teams building in game engines, Architecting Spatial Content on Android XR with Unity explores how to map physical spaces, persist 3D placements across sessions, and synchronize shared multi-user experiences in Unity using Spatial Entities, Cloud Anchors, and ARCore Geospatial APIs.
Scaling across familiar 3D engines
Android XR meets developers wherever they already build, including rich interactive environments crafted in dedicated real-time engines. The Android XR Engine Hub is now stable, streamlining setup, configuration, and optimization pipelines across Unity, Godot, and Unreal Engine. The Engine Hub simplifies project scaffolding with pre-configured OpenXR extensions and validated project settings so you can start creating immediately. It also delivers native profiling workflows to help you capture and inspect system traces, thermal limits, and frame budgets across CPU and GPU cores directly within your engine interface.
To see how these runtime systems connect directly with Android UI, watch Elevate immersive experiences with 3D Engines in Jetpack Compose for XR and see how to embed Godot and Unity as libraries inside native Jetpack Compose apps using OpenXR Spatial Containers.
Supporting familiar engines makes it seamless to adapt existing 3D titles for Android XR form factors. Teams like Contract XR are already leveraging this pipeline with their ported Unity game, Jigsaw Night, on XREAL AURA, creating a collaborative space where players can walk around, pass pieces, and solve puzzles together, demonstrating how lightweight XR glasses and engine workflows unlock natural, multi-user mixed reality experiences.
Designing multimodal interactions with on-device audio
As the device lineup expands into audio interactions, we are introducing new tools to architect lightweight, multimodal experiences. Developers can now leverage the ML Kit Gen AI Text to Speech API to generate natural-sounding voices powered by on-device AI. We have launched new design guidance around best practices for sound, including Earcons, to guide users through audio-first and augmented environments. To see these pieces in action, watch Building audio-first experiences for intelligent eyewear with Gemini Nano 4 to learn how to combine Jetpack Projected, ML Kit, and on-device Gemini Nano into hands-free, conversational apps.
Get started with the latest tools
With these updates to our core SDKs, emulators, and engine tools, you have the foundation to build immersive and augmented experiences across the Android XR ecosystem. Update to the latest stable release of Android Studio today to set up and test Android XR virtual devices for glasses form factors, add the stable Jetpack XR dependencies to your build files, or install the Android XR Engine Hub plugin for your preferred 3D engine. With new devices like XREAL AURA now available now, it’s the perfect time to build for Android XR. Head over to our Android XR Developer Site for the stable libraries, tools, and guides you need to get started today.
To explore all of our technical sessions and deep dives from the Android Dev Summit, check out the complete Android XR Session Playlist.
</kaynak_metni>
</haber>

<haber id="c008" puan="6" kaynak="Android Developers Blog" tarih="2026-11-05">
Başlık: What’s new in intelligent apps at the Android Developer Summit
URL: https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads
Özet: Android Developer Summit'te Gemini gibi ajanların uygulamalar arasında çok adımlı işleri tamamlamasına yönelik akıllı uygulama yenilikleri anlatıldı.
<kaynak_metni>
In the intelligence era, users are no longer just tapping through apps, they express high-level goals and expect AI agents like Gemini to complete multi-step workflows, sometimes across multiple apps on their devices. To help you meet users where they are, we’re unlocking new ways to build intelligent, agentic experiences in your Android apps:
- Connect with the Android intelligence system: Share your app’s capabilities with Android MCP. To let users connect directly with your app through the Gemini app and Google Search on Android, join the Connected Apps Platform preview program.
- Bring intelligence into your app: Build smart features and agents on-device with ML Kit GenAI APIs, bring your custom ML model with LiteRT in Google Play services. Leverage Gemini models on the Cloud with Firebase AI Logic, and enable your agent to build native Compose UI with the A2UI Compose renderer.
You’ve already seen some of these new APIs and developer tools at the Android Developer Summit keynote. Now, learn with our new deep-dive resources to help you build intelligent apps, including 10 new on-demand sessions around new intelligent experiences.
Connect with the Android intelligence system
The Android intelligence system is the system foundation designed to protect users while connecting AI agents with apps on Android devices. It provides users with both prompted assistance and proactive assistance across the Android ecosystem of devices spanning phones, wearables, XR glasses, TVs, and automobiles.
- Prompted assistance: When the user actively asks an agent to fulfill a goal (for example, "check my calendar, book a ride, and message Jingyu my ETA"), the agent orchestrates tools across apps to get it done. For the fastest, most reliable execution, you can use a remote MCP server or local Android MCP. Agents can also fall back to using Android’s Computer Control framework to complete actions without requiring any app-side integration.
- Proactive assistance: The system anticipates the user's needs and surfaces contextual suggestion chips directly on lock screens, notifications, virtual keyboards, and within apps.
We give you control over how your apps integrate with the Android intelligence system by providing APIs and tools based on the familiar MCP standard. Android MCP, powered by the AppFunctions Jetpack library, is our unified tool-calling framework. It lets you connect with AI agents right on the device.
Remote MCP server provides you with cross-platform reach. Android MCP complements remote MCP as an Android native solution and is the recommended integration path when your user journey uses end-to-end encryption or sensitive local device data, requires device sensors and hardware, needs to execute locally, or when there’s no server endpoint available.
You can integrate your app with Gemini using remote MCP, Android MCP or both depending on your use case. Learn more below:
Bring intelligence into your apps: from on-device agent to A2UI Compose renderer
With new capabilities available in Gemini Nano 4 like function calling, we are expanding the ML Kit GenAI APIs to build agentic workflows entirely on-device. We provide you the building blocks directly with ML Kit’s direct model access with Prompt API and the new Agentic API that auto-executes functions for you, saves conversation history, manages the orchestration loop, and includes automatic guardrails. Check out the Jetpacker code sample on GitHub and watch this video for a deep dive into how you can unlock agentic capabilities in your app with ML Kit GenAI APIs:
Besides the new Agentic APIs, we are bringing a suite of new capabilities on-device:
- Get an overview of on-device ML Kit GenAI APIs, from Prompt API features like thinking mode and system instructions to new alpha APIs like the Embeddings API, powered by EmbeddingGemma 2. You'll also learn about under-the-hood Android system optimizations and see common on-device GenAI use cases already in production.
- Take a deep dive into the model architecture of Gemini Nano 4, built on Gemma 4. Powered by per-layer embeddings, quantization-aware training, and multi-token prediction, Gemini Nano 4 delivers to 3x inference speedup while cuts memory usage by up to 4x compared to the previous version of Gemini Nano model under internal testing benchmarks.
- You can run your custom ML models with faster GPU performance using LiteRT in Google Play services which removes the runtime from your APK making your APK about 8 MB smaller. Now also available on Wear OS and Android Automotive OS. Whether you are using the turn-key ML Kit APIs or bring your own custom edge model, read the announcement and check out this talk.
- See how these APIs come together in real-world apps, from an XR language teacher using the ML Kit speech recognition, speech translation, and text-to-speech APIs on phones and smart glasses, to a Formula E AI co-driver built with Gemini Nano, ML Kit direct model access, and the Agent Development Kit (ADK).
For workflows that span cloud and local processing, Firebase AI Logic offers a straightforward hybrid solution. You can call advanced cloud models like Gemini 4 while using on-device inference with Gemini Nano when available. To protect your app and manage costs in production, use Firebase App Check, the new server prompt templates, and Firebase spend caps.
As showcased in the keynote demo with Jetpacker's live booking assistant, the Jetpack Compose A2UI renderer is now available in alpha to help your agents "speak UI". Your agents can stream rich, interactive native Compose UIs directly from a JSON protocol. Get started with the A2UI Compose renderer and give us your feedback. Watch this talk to see how to implement it in your app.
Reach across Gemini and Search with Connected Apps Platform
Across Google surfaces, users are shifting from asking questions to taking action. We introduced the Connected Apps Platform so you can reach high-intent users across Gemini and Search, combining Android MCP for native on-device execution with remote MCP servers for cross-platform reach. You can start building and testing locally today with Gemini Apps Developer Mode. When you're ready for production, join the preview waitlist; preview capacity is currently limited to selected production-ready apps in supported categories, with broader self-serve access coming later.
To walk you through building, testing, and publishing your first Connected App, watch Extend your app to Gemini and Search with the Connected Apps Platform.
Start building intelligent apps with the latest updates
To start building, create on-device agents with ML Kit agentic workflows alongside direct model access with new Android skills. Make sure you opt in to the AIcore Developer Preview program when testing with new capabilities in preview models. Bring intelligent features to your app with ML Kit APIs and run custom ML models with LiteRT in Google Play Services. Run Inference with Gemini models in the cloud with Firebase AI Logic directly and stream native Compose UIs from JSON using the Jetpack Compose A2UI renderer. Finally, integrate with the Android intelligence system, prototype with Android MCP using the AppFunctions skill and sample agent and sign up for the Connected Apps Platform developer preview.
We can't wait to see what you build!
- 
  Product News At Google I/O 2026, we introduced Android’s shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google’s AI into your apps.
- 
  Product News From full immersion at home to glanceable experiences on the go, building on Android XR lets you meet users at any moment across the entire spectrum of spatial applications. At Android Developer Summit, we marked an exciting milestone with the launch of XREAL AURA.
- 
  Product News Today, at the Android Dev Summit, we are announcing the broad availability of many tools and APIs designed to remove everyday friction and give you more flexibility to build great Android apps.
</kaynak_metni>
</haber>

<haber id="c009" puan="6" kaynak="Android Developers Blog" tarih="2026-11-04">
Başlık: Build for every screen with the latest Jetpack Compose updates from Android Developer Summit
URL: https://developer.android.com/blog/posts/build-for-every-screen-jetpack-compose-updates
Özet: Android Developer Summit'te telefondan XR'a farklı ekranlar için Jetpack Compose güncellemeleri duyuruldu.
<kaynak_metni>
The Android ecosystem is a multi-device reality that spans phones, foldables, tablets, wearables, in-car displays, XR, and Googlebook. In this landscape, adaptive development is foundational to reaching users wherever they are.
Jetpack Compose is the standard for building all UI across Android. Moving beyond the legacy View system gives you a single, unified development target that eliminates the friction of maintaining fragmented codebases across different form factors. But building adaptive layouts is only half the picture. When screens fold, windows resize, or apps transition across form factors, traditional layout assumptions may break down, and it is easy for apps to lose state or feel disjointed.
At the Android Developer Summit, we shared how we are advancing app foundations across both UI and architecture by bringing Compose deeper into your data layer with Jetpack AppState, while giving you adaptive building blocks like FlexBox and Grid, and agent-ready tooling to scale across screens every screen.
Check out some highlights of our recent announcements below or also head to our Android Developer site to catch over 50 on-demand sessions, including best practices for app foundations.
Advancing core foundations and bringing Compose beyond the UI
The upcoming Compose 1.13 stable release is expanding the toolkit with built-in support for adaptive layouts through Grid and Flexbox and new functionality like Progressive Blur and Formatted Text. To see the latest features with Graphics like mesh gradients and progressive blurs without sacrificing battery life or frame rates, watch Elevate your apps with the latest graphics features in Jetpack Compose and Android.
Alongside visual rendering, Compose text editing now features a completely rewritten BasicTextField with a buffer-driven architecture and TextFieldState, eliminating IME race conditions and supporting rich text formatted editing mechanics. Watch Building reliable text editing experiences in Compose, to learn more about this shift. 
As you introduce these rich visual and interactive experiences, maintaining smooth frame rates and low startup latency is critical. Check out Outperform yourself in Compose to explore how to profile with Perfetto and recomposition tracing, identify costly anti-patterns, and keep your UI running smoothly.
Compose is also expanding into the architecture layer with Jetpack AppState, now in alpha. AppState brings Compose's snapshot system into your app's architecture: Transform lets you derive reactive state from State and Flow inputs using automatic read tracking and plain Kotlin control flow, while StateStore gives you a keyed container to share observable state across activities, background services, widgets, and App Functions—with optional DataStore persistence. Watch Taking Compose State Beyond the UI with Jetpack AppState to see how moving Compose state up your stack simplifies complex state pipelines and keeps every surface of your app in sync.
Designing robust navigation and input systems for across form factors
As apps grow more modular, navigation and user input need to stay predictable across every entry point and screen size. With version 1.2, Jetpack Navigation 3 brings built-in, type-safe deep linking to its developer-owned back stack. Using Kotlin Serialization, you can map incoming URIs and intents directly to strongly typed navigation keys, customize how complex arguments are parsed, and lazily build synthetic back stacks so back navigation always feels natural. To see these APIs in action, check out Building type-safe deep links with Jetpack Navigation 3.
Input handling has also evolved to support multi-modal interactions across devices. Compose's layered input system extends seamlessly beyond touch to support trackpads, mice, and physical controls. To see how to manage pointer lifecycles, hover states, and hardware events across form factors, watch Scaling input interactions beyond the touchscreen with Jetpack Compose.
Scaling interfaces across large screens, desktop, and beyond
When moving across foldables, tablets, and laptops, interfaces must adapt naturally rather than simply stretching content to fill larger displays. Building adaptively with Compose development combines Navigation 3, WindowManager, and agentic workflows to help you refactor mobile layouts into responsive multi-pane experiences with minimal manual overhead. For developers looking to take their existing layouts further, Scale your app for every screen with Compose walks through these multi-pane architecture patterns and demonstrates how to optimize navigation flows as window sizes change.
Expanding beyond mobile form factors also unlocks new opportunities like with Googlebook. Building desktop-class experiences requires physical peripheral support, windowing environments and more. In Inside the first wave on Googlebook with Notability and Logitech, early partners share practical engineering strategies on optimizing for pointer interactions, external hardware, and desktop-grade workflows.
Get started with our Android skills
To help you implement these patterns even faster, you can leverage Android skills to help your coding agents. Whether you use Gemini in Android Studio or run the Android CLI with other agents, these skills handle the heavy lifting for you and be compliant with the Adaptive Quality Guidelines. For Compose we currently have:
- The updated Adaptive skill helps agents transform compact screens into responsive multi-pane layouts and handle state and configuration change. It now adds foldable and desktop support, automatically handling windowing, keyboard shortcuts, tooltips, and trackpad hover states.
- New Compose performance skill to help optimize your codebase
- XML to Compose migration skill
- New Ink skill
Beyond core architecture and adaptive layouts, you can explore technical deep dives covering Media3 playback, CameraX pipelines, in-car experiences, rich graphics, and lessons from migrating Google Play to Compose at scale. Check out the full collection of technical walkthroughs in the Android Developer Summit App Foundations session playlist to explore the architectures, code walkthroughs, and practical guidance.
- 
  Events & Programs We’re opening applications for the Android XR Developer Catalyst Program, a dedicated initiative to accelerate the development of Android XR apps ready to launch within the next year.
</kaynak_metni>
</haber>

## Yanıt şeması (JSON Schema)

```json
{
 "$defs": {
  "Claim": {
   "properties": {
    "text": {
     "description": "Anlatımdaki tek bir olgusal iddia (rakam, isim, tarih, özellik)",
     "title": "Text",
     "type": "string"
    },
    "source_url": {
     "description": "İddiayı destekleyen kaynak URL; sources listesinden biri olmalı",
     "title": "Source Url",
     "type": "string"
    },
    "uncertain": {
     "description": "Kaynak bunu açıkça söylemiyorsa veya yoruma dayanıyorsa true",
     "title": "Uncertain",
     "type": "boolean"
    }
   },
   "required": [
    "text",
    "source_url",
    "uncertain"
   ],
   "title": "Claim",
   "type": "object"
  },
  "Segment": {
   "properties": {
    "bridge": {
     "default": "",
     "description": "Haberden önce söylenen bağlaç cümlesi, en fazla 7 kelime; önceki habere/izleyiciye bağlar. Yeni olgu içermez. ör. 'Güvenlik demişken, asıl tehlike burada.'",
     "title": "Bridge",
     "type": "string"
    },
    "headline": {
     "description": "Ekranda görünecek başlık, en fazla 8 kelime",
     "title": "Headline",
     "type": "string"
    },
    "narration": {
     "description": "Seslendirilecek haber metni; doğal konuşma Türkçesi, kısa cümleler",
     "title": "Narration",
     "type": "string"
    },
    "student_take": {
     "description": "'Bu senin için ne demek?' — somut eylem: başvuru tarihi, kullanılabilecek araç, kariyer etkisi",
     "title": "Student Take",
     "type": "string"
    },
    "visuals": {
     "description": "2-4 görsel; ilk görsel HeadlineCard",
     "items": {
      "$ref": "#/$defs/Visual"
     },
     "title": "Visuals",
     "type": "array"
    },
    "sources": {
     "description": "Kaynak URL listesi",
     "items": {
      "type": "string"
     },
     "title": "Sources",
     "type": "array"
    },
    "claims": {
     "description": "narration ve student_take içindeki tüm olgusal iddialar",
     "items": {
      "$ref": "#/$defs/Claim"
     },
     "title": "Claims",
     "type": "array"
    }
   },
   "required": [
    "headline",
    "narration",
    "student_take",
    "visuals",
    "sources",
    "claims"
   ],
   "title": "Segment",
   "type": "object"
  },
  "Visual": {
   "description": "Bir haber bloğunda gösterilecek görsel. Yalnızca seçilen component'in alanları doldurulur.",
   "properties": {
    "component": {
     "enum": [
      "HeadlineCard",
      "StatCounter",
      "MiniChart",
      "CodeBlock",
      "Terminal",
      "SourceScreenshot"
     ],
     "title": "Component",
     "type": "string"
    },
    "stat_value": {
     "anyOf": [
      {
       "type": "number"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "description": "Kaynakta geçen sayı; yalnızca kaynakta varsa",
     "title": "Stat Value"
    },
    "stat_prefix": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "description": "ör. '$' veya ''",
     "title": "Stat Prefix"
    },
    "stat_suffix": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "description": "ör. ' milyar $', '%', ' GB'",
     "title": "Stat Suffix"
    },
    "stat_label": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "description": "Sayının ne olduğu, Türkçe, en fazla 6 kelime",
     "title": "Stat Label"
    },
    "chart_title": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Chart Title"
    },
    "chart_labels": {
     "anyOf": [
      {
       "items": {
        "type": "string"
       },
       "type": "array"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Chart Labels"
    },
    "chart_values": {
     "anyOf": [
      {
       "items": {
        "type": "number"
       },
       "type": "array"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "description": "Kaynakta geçen değerler; uydurma yok",
     "title": "Chart Values"
    },
    "chart_unit": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Chart Unit"
    },
    "code_language": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "description": "ör. 'bash', 'python', 'kotlin'",
     "title": "Code Language"
    },
    "code_lines": {
     "anyOf": [
      {
       "items": {
        "type": "string"
       },
       "type": "array"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "description": "En fazla 6 kısa satır; kaynaktaki komut/kod veya kurulum komutu",
     "title": "Code Lines"
    },
    "screenshot_url": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "description": "Ekran görüntüsü alınacak kaynak URL (sources listesinden)",
     "title": "Screenshot Url"
    }
   },
   "required": [
    "component"
   ],
   "title": "Visual",
   "type": "object"
  }
 },
 "properties": {
  "hook": {
   "description": "İlk 2 saniyede ekranda/seste: haftanın en çarpıcı tek cümlesi, en fazla 8 kelime",
   "title": "Hook",
   "type": "string"
  },
  "teaser": {
   "default": "",
   "description": "Kancadan hemen sonra merak boşluğu açan cümle, en fazla 12 kelime; sona kalan haberi ima eder, yeni olgu içermez",
   "title": "Teaser",
   "type": "string"
  },
  "segments": {
   "items": {
    "$ref": "#/$defs/Segment"
   },
   "title": "Segments",
   "type": "array"
  },
  "question": {
   "default": "",
   "description": "İzleyiciye yorumda cevaplayacağı soru, en fazla 10 kelime",
   "title": "Question",
   "type": "string"
  },
  "outro": {
   "description": "Kapanışta söylenecek kısa cümle, en fazla 8 kelime",
   "title": "Outro",
   "type": "string"
  }
 },
 "required": [
  "hook",
  "segments",
  "outro"
 ],
 "title": "Script",
 "type": "object"
}
```
