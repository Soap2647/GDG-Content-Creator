# Görev: verify

Yanıtı `episodes/2026-W45/llm/verify.response.json` dosyasına, aşağıdaki JSON şemasına uyan TEK bir JSON nesnesi olarak yaz.

## Sistem talimatı

Sen bağımsız bir doğrulama editörüsün (fact-checker). Bir teknoloji haber videosunun senaryosundaki iddiaları, verilen kaynak metinleriyle karşılaştırırsın.
- Yalnızca verilen kaynak metinlerine dayan; kendi bilgini kullanma. Kaynakta yoksa "not_found" de.
- Rakam, tarih, isim, sürüm numarası birebir eşleşmeli; yuvarlama veya birim farkı varsa "partial".
- evidence alanına kaynaktan birebir alıntı koy.
- Ayrıca anlatım (narration) ve student_take içinde olup claims listesinde bulunmayan olgusal ifadeleri "missed" listesine ekle ve onları da değerlendir.
- Hook, teaser, köprü (bridge), soru ve kapanışta segmentlerde desteklenmeyen bir olgu ya da sonda karşılığı olmayan bir vaat varsa onu da "missed" listesine (ilgili segmente) ekle.
- Her iddia için tam bir kayıt döndür.

## Girdi

Hook: Google hesabınla ayda üç yapay zeka videosu ücretsiz!
Teaser: Dört haber var; sonuncusu lisans öğrencilerine açık bir burs.
Soru: Sen Game Off'a nasıl bir oyunla katılırdın? Yorumlara yaz.
Kapanış: Takip et, haftaya yeni gündemle buradayız.

<segment no="1">
Başlık: Google Vids'te ücretsiz yapay zeka videosu
Köprü: 
Anlatım: Google, yeni video modeli Omni 1.2 Flash'ı Google Vids'e getirdi. Google hesabı olan herkes ayda en fazla 3 adet 15 saniyelik videoyu ücretsiz üretebiliyor. Konuşmalar da artık daha doğal.
Öğrenci notu: Proje tanıtım videon için Google Vids'te hemen deneyebilirsin.
İddialar:
  [0] Google Vids artık Google'ın en yeni video modeli Omni 1.2 Flash ile çalışıyor  (kaynak: https://blog.google/products-and-platforms/products/workspace/omni-1-2-flash-google-vids/)
  [1] Google hesabı olan herkes Vids'te ayda en fazla 3 adet 15 saniyelik videoyu ücretsiz üretebiliyor  (kaynak: https://blog.google/products-and-platforms/products/workspace/omni-1-2-flash-google-vids/)
  [2] Gelişmiş konuşma seslendirmesiyle klipler daha doğal duyuluyor  (kaynak: https://blog.google/products-and-platforms/products/workspace/omni-1-2-flash-google-vids/)
<kaynak url="https://blog.google/products-and-platforms/products/workspace/omni-1-2-flash-google-vids/">
Generate longer AI videos with Omni 1.2 Flash in Google Vids at no cost.
Google Vids, our video creation and editing tool, now runs on Google's newest video generation model: Omni 1.2 Flash. Starting today, anyone with a Google account or Google Workspace subscription can generate up to three 15-second videos per month in Vids at no cost.
With Omni 1.2 in Google Vids, you can now bring your ideas to life in so many more ways:
- Create your product promos in one go. Produce professional, quick-turn social content and promotional materials without a single cut.
- Transform static imagery into engaging videos. Upload reference images from anything — a trip, a school project, or learning materials — and your characters and scenes will stay consistent, from the first frame to the last.
- Make clips that sound more natural. With improved speech narration, your social clips, concept explainers, and teaser videos feel like something you recorded yourself.
If you can describe it, you can make it. Try Google Vids out at vids.new.
</kaynak>
</segment>

<segment no="2">
Başlık: Gemini, kâğıttaki çizimi uygulamaya çeviriyor
Köprü: Videodan sonra sıra uygulamada.
Anlatım: Kâğıda çizdiğin uygulama taslağının fotoğrafını Gemini'ye yükle, Canvas aracını seç ve kodlamasını iste. Gemini çizimi okuyup kodu yazıyor; renkleri ve özellikleri anında değiştirebiliyor.
Öğrenci notu: Proje fikrini önce kâğıda çiz, ilk sürümü Gemini'ye yazdır.
İddialar:
  [0] Uygulama taslağı gibi bir çizimin fotoğrafı Gemini'ye yüklenebiliyor  (kaynak: https://blog.google/innovation-and-ai/products/gemini-app/turn-drawings-into-apps-gemini/)
  [1] Canvas aracı seçilip Gemini'den uygulamayı kodlaması istenebiliyor  (kaynak: https://blog.google/innovation-and-ai/products/gemini-app/turn-drawings-into-apps-gemini/)
  [2] Gemini görseli okuyup kodu yazıyor  (kaynak: https://blog.google/innovation-and-ai/products/gemini-app/turn-drawings-into-apps-gemini/)
  [3] Gemini renkleri, yazı tiplerini ve özellikleri gerçek zamanlı değiştirebiliyor  (kaynak: https://blog.google/innovation-and-ai/products/gemini-app/turn-drawings-into-apps-gemini/)
<kaynak url="https://blog.google/innovation-and-ai/products/gemini-app/turn-drawings-into-apps-gemini/">
Transform a quick drawing into a live app with Gemini.
Great app ideas often start on paper. Turn them into interactive tools with Gemini.
Here’s how.
- Upload a photo of your sketch, like an app mock-up, habit tracker, or game board to Gemini.
- Select the Canvas tool and ask Gemini: "Can you code this app?" Gemini reads your visual and writes the code.
- Test your tool in the preview window. Gemini can adjust colors, fonts, or features in real time.
Next time inspiration strikes, bring it to life with Gemini.
</kaynak>
</segment>

<segment no="3">
Başlık: GitHub Game Off 2026 başladı
Köprü: Kod demişken, bu ay oyun yapsana.
Anlatım: GitHub'ın bir ay süren oyun yarışması Game Off 14. kez başladı. Bu yılın teması SHIFT. Tek başına ya da takımla, istediğin motorla katılabilirsin; son teslim 1 Aralık.
Öğrenci notu: İlk oyununu yapacaksan tek mekanik ve tek bölümle başla.
İddialar:
  [0] GitHub'ın bir ay süren oyun yarışması Game Off 14. kez Kasım'da düzenleniyor  (kaynak: https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/)
  [1] Game Off 2026'nın teması SHIFT  (kaynak: https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/)
  [2] Katılımcılar tek başına ya da takım olarak, istedikleri dil ve oyun motoruyla katılabilir  (kaynak: https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/)
  [3] Oyunların son teslim tarihi 1 Aralık 2026  (kaynak: https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/)
  [4] Kaynak, önce tek bir mekanik ve oynanabilir tek bir bölümle başlamayı tavsiye ediyor  (kaynak: https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/)
<kaynak url="https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/">
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
</kaynak>
</segment>

<segment no="4">
Başlık: TÜBİTAK STAR: Lisans başvuruları açık
Köprü: Ve sona sakladığımız burs geldi.
Anlatım: TÜBİTAK'ın STAR programıyla lisans öğrencileri, araştırma projelerinde bursiyer olarak görev alabiliyor. Başvurular 2 Kasım'da başladı ve 16 Kasım saat 17.30'da kapanıyor.
Öğrenci notu: Projeleri BİDEB sisteminde incele; başvuru TÜBİTAK Yönetim Bilgi Sistemi'nden.
İddialar:
  [0] 2247-C STAR programıyla lisans öğrencileri araştırma projelerinde bursiyer olarak görev alabiliyor  (kaynak: https://tubitak.gov.tr/tr/duyuru/2247-c-stajyer-arastirmaci-burs-programi-star-2026-yili-2-donem-star-lisans-ve-star-ogretmen-cagrilari-acildi)
  [1] Başvurular 2 Kasım 2026'da başladı, 16 Kasım 2026 saat 17.30'da (TSİ) kapanıyor  (kaynak: https://tubitak.gov.tr/tr/duyuru/2247-c-stajyer-arastirmaci-burs-programi-star-2026-yili-2-donem-star-lisans-ve-star-ogretmen-cagrilari-acildi)
  [2] Proje listesine BİDEB Başvuru ve İzleme Sistemi'nden ulaşılıyor, başvurular TÜBİTAK Yönetim Bilgi Sistemi üzerinden alınıyor  (kaynak: https://tubitak.gov.tr/tr/duyuru/2247-c-stajyer-arastirmaci-burs-programi-star-2026-yili-2-donem-star-lisans-ve-star-ogretmen-cagrilari-acildi)
<kaynak url="https://tubitak.gov.tr/tr/duyuru/2247-c-stajyer-arastirmaci-burs-programi-star-2026-yili-2-donem-star-lisans-ve-star-ogretmen-cagrilari-acildi">
TÜBİTAK Bilim İnsanı Destek Programları Başkanlığı (BİDEB) tarafından yürütülen 2247-C Stajyer Araştırmacı Burs Programı’nın (STAR) 2. aşaması olan öğrenci ve öğretmen başvuruları başladı. Program; TÜBİTAK Merkez ve Enstitülerinde yürütülen projeler ile TÜBİTAK tarafından desteklenen araştırma projelerine veya Yükseköğretim Kurulu’nın (YÖK) araştırma üniversitelerine yönelik başlattığı Araştırma Üniversiteleri Destek Programı (ADEP) tarafından desteklenen araştırma projelerine bursiyer olarak dâhil olacak lisans öğrencilerinin (STAR Lisans) bilimsel araştırma projelerinde görev almaları ve öğretmenlerin (STAR Öğretmen) mesleki bilgi ve becerilerinin gelişimini sağlayarak proje kültürü kazanmaları amaçlarını taşıyor.
2026 yılı 2. döneminde aşağıdaki çağrılar kapsamında lisans öğrencileri ile öğretmenlerden başvuru alınacaktır.
- STAR Lisans (Lisans Öğrencisi )
- STAR Öğretmen (Öğretmen)
STAR programının ikinci aşamasında lisans öğrencileri ve öğretmenler, proje yürütücülerinin talepleri doğrultusunda projelerde görev almak üzere 2 Kasım 2026-16 Kasım 2026 (17.30, TSİ) tarihlerinde başvuru yapabileceklerdir.
Başvurular, TÜBİTAK Yönetim Bilgi Sistemiüzerinden alınacaktır. Proje listesine BİDEB Başvuru ve İzleme Sistemi üzerinden, program çağrı metinlerine ise web adresimizden ulaşabilirsiniz.
İletişim: star@tubitak.gov.tr
</kaynak>
</segment>

## Yanıt şeması (JSON Schema)

```json
{
 "$defs": {
  "ClaimCheck": {
   "properties": {
    "segment": {
     "title": "Segment",
     "type": "integer"
    },
    "claim_index": {
     "title": "Claim Index",
     "type": "integer"
    },
    "verdict": {
     "description": "supported: kaynak açıkça söylüyor; partial: kısmen/farklı ifade; unsupported: kaynakla çelişiyor; not_found: kaynakta yok",
     "enum": [
      "supported",
      "partial",
      "unsupported",
      "not_found"
     ],
     "title": "Verdict",
     "type": "string"
    },
    "evidence": {
     "description": "Kaynaktan birebir alıntı, en fazla 30 kelime; yoksa boş",
     "title": "Evidence",
     "type": "string"
    },
    "note": {
     "description": "Kısa açıklama, Türkçe",
     "title": "Note",
     "type": "string"
    }
   },
   "required": [
    "segment",
    "claim_index",
    "verdict",
    "evidence",
    "note"
   ],
   "title": "ClaimCheck",
   "type": "object"
  },
  "MissedClaim": {
   "properties": {
    "segment": {
     "title": "Segment",
     "type": "integer"
    },
    "text": {
     "description": "Anlatımda olup claims listesinde olmayan olgusal ifade",
     "title": "Text",
     "type": "string"
    },
    "verdict": {
     "enum": [
      "supported",
      "partial",
      "unsupported",
      "not_found"
     ],
     "title": "Verdict",
     "type": "string"
    },
    "evidence": {
     "title": "Evidence",
     "type": "string"
    }
   },
   "required": [
    "segment",
    "text",
    "verdict",
    "evidence"
   ],
   "title": "MissedClaim",
   "type": "object"
  }
 },
 "properties": {
  "checks": {
   "items": {
    "$ref": "#/$defs/ClaimCheck"
   },
   "title": "Checks",
   "type": "array"
  },
  "missed": {
   "items": {
    "$ref": "#/$defs/MissedClaim"
   },
   "title": "Missed",
   "type": "array"
  }
 },
 "required": [
  "checks",
  "missed"
 ],
 "title": "Verification",
 "type": "object"
}
```
