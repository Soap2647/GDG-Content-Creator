# Görev: write

Yanıtı `episodes/2026-W44/llm/write.response.json` dosyasına, aşağıdaki JSON şemasına uyan TEK bir JSON nesnesi olarak yaz.

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

Hafta: 2026-W44

<haber id="c001" puan="8" kaynak="TÜBİTAK Duyuruları" tarih="2026-10-27">
Başlık: Bütünleşik Algılama ve Haberleşme Kış Okulu 2026 Yılı Başvuruları Başladı
URL: https://tubitak.gov.tr/tr/duyuru/butunlesik-algilama-ve-haberlesme-kis-okulu-2026-yili-basvurulari-basladi
Özet: TÜBİTAK TBAE'nin Bütünleşik Algılama ve Haberleşme Kış Okulu 2026 başvuruları başladı.
<kaynak_metni>
TÜBİTAK Temel Bilimler Araştırma Enstitüsü (TBAE), temel bilimin çeşitli dallarında ve disiplinler arası alanlarda oldukça geniş bir yelpazede nitelikli bilgi üretmek, uluslararası düzeyde bilimsel etkinlikler gerçekleştirmek ve Türkiye’ye bilimsel rekabet gücü kazandırmak yönündeki çabalarını arttırmak amacıyla önemli adımlar atmaya devam ediyor. Bu kapsamda 23–25 Kasım 2026 tarihlerinde “Bütünleşik Algılama ve Haberleşme” (TBAE ISAC) Kış Okulu düzenlenecektir. 
Bütünleşik Algılama ve Haberleşme (ISAC) ortak spektrum, donanım ve dalga biçimlerini kullanarak kablosuz sistemlerin hem haberleşme hem de algılama gerçekleştirmesini sağlayan, 6G ağları için kilit bir teknoloji olarak öne çıkmakta, çevresel farkındalık ve konum belirleme için yeni fırsatlar sunmaktadır.
TBAE ISAC Kış Okulu, radar ve kablosuz algılama temellerini, OFDM ve MIMO sistemlerini, ISAC mimarilerini, dalga biçimi ve huzme biçimlendirme tasarımını, algılama konfigürasyonlarını, performans sınırlarını ve algılama ile haberleşme arasındaki ödünleşimleri kapsamayı amaçlamaktadır. Ek konular arasında kanal modellemesi, 5G-Advanced ve 6G standardizasyon faaliyetleri ile araç algılama ve İHA tespiti gibi uygulama alanları da yer alabilir. Okulda ayrıca ISAC alanındaki güncel araştırmaları ve açık problemleri ele alan konuşmalar yer alacaktır.
Yüz yüze katılım kontenjan 50 kişiyle sınırlıdır. İlgili alanlardaki yüksek lisans ile doktora öğrencileri ve doktora sonrası araştırmacılara yüz yüze katılım için öncelik verilecektir. Seçilen tüm katılımcılara ücretsiz konaklama ve Türkiye içi (otobüs/tren) ulaşım desteği sağlanacaktır.
Çağrı Takvimi:
Son Başvuru Tarihi: 12 Kasım 2026
Kış Okulu Tarihleri: 23 – 25 Kasım 2026
Yer: Gebze, Türkiye
Başvuru:
Bütünleşik Algılama ve Haberleşme Kış Okulu’na yüz yüze veya Zoom üzerinden çevrim içi katılmak için başvuru yapabilirsiniz. Yüz yüze katılım sınırlı olup yapılan başvurular arasından seçilecektir.
Başvuru için tıklayınız.
</kaynak_metni>
</haber>

<haber id="c005" puan="7" kaynak="Google Developers Blog" tarih="2026-10-26">
Başlık: Preview, edit, and collaborate on markdown (.md) files natively in Google Docs and Drive
URL: https://developers.googleblog.com/preview-edit-and-collaborate-on-markdown-md-files-natively-in-google-docs-and-drive/
Özet: Google Docs ve Drive, Markdown dosyalarını dönüştürmeden önizleme, düzenleme ve ortak çalışma desteği sunuyor.
<kaynak_metni>
Google Workspace is bridging the gap between code and collaboration by providing a familiar, real-time environment where developers and AI agents can seamlessly work together on documentation.
Markdown (.md) is a standard text format widely used by LLMs to preserve structured content—such as tables, headers, and bulleted lists—without the overhead of bulky file formats. Markdown file usage in Google Drive has surged year-over-year, indicating how critical this format has become for modern, fast-paced workflows.
Now, you can natively view, edit, and collaborate in markdown files directly in Google Docs, eliminating the friction of manual file conversions. You can edit without changing file types while ensuring your underlying documentation is preserved for developer tools and git repositories. Plus, with rendered previews in Google Drive, you can easily review formatting with a click.
As AI agents take on larger roles in drafting, planning, and coding, markdown serves as a collaborative common language between humans and AI tools because it is easily readable by both. Google Docs provides a familiar, easy-to-use environment, acting as a shared bridge where team members and autonomous agents work together directly on the same documents. When you open a markdown file in Google Docs, you have:
By combining the simplicity of markdown with the powerful real-time collaboration of Google Docs, teams now have a unified workspace to draft, review, and ship technical content faster.
Anyone with a Google or Workspace account can get started today by uploading an .md file to Google Drive and begin collaborating directly in Google Docs.
</kaynak_metni>
</haber>

<haber id="c010" puan="7" kaynak="Google Blog" tarih="2026-10-27">
Başlık: We’re announcing Genie 4, our new world model for real-time interactive simulation.
URL: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/
Diğer kaynaklar: https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/
Özet: Google, gerçek zamanlı etkileşimli simülasyon için yerel ses üreten yeni dünya modeli Genie 4'ü duyurdu.
<kaynak_metni>
We’re announcing Genie 4, our new world model for real-time interactive simulation.
Today, we’re announcing our research on Genie 4, our new world model that brings unprecedented realism and native audio to real-time interactive simulation.
The Genie 4 model incorporates and builds on capabilities from the Gemini family: Gemini Omni anchors simulations in real-world appearance and behavior, while other Gemini models provide the complex reasoning needed to help maintain a simulation’s coherence and continuity.
With Genie 4, you can set an event in motion and steer scenes in real time using natural language, like moving the camera, changing the weather, or introducing new characters. Every world also generates native audio on the fly, including ambient sounds, music, and interactive dialogue.
Simulating the world is a crucial step toward AGI, enabling safe training environments for robots and agents, and amplifying creative tools across industries like filmmaking, journalism, gaming, and manufacturing.
We have started rolling out Genie 4 to a limited group of trusted testers. It’s coming soon to Google AI Ultra subscribers in Project Genie and early access partners in the Gemini API and AI Studio.
Explore the demos on the Google DeepMind blog.
</kaynak_metni>
</haber>

<haber id="c003" puan="6" kaynak="Google Developers Blog" tarih="2026-10-27">
Başlık: Fast, reliable A2UI, with swappable inference formats
URL: https://developers.googleblog.com/fast-reliable-a2ui/
Özet: A2UI, takas edilebilir çıkarım formatları ve 3 kata kadar daha az token kullanan A2UI Express'i getirdi.
<kaynak_metni>
We've heard your concerns about the speed of A2UI and generative UI experiences: people wait while the model generates each screen. This release gives you levers to make that faster, so you can choose the trade-off that fits each screen.
With this release, we’re happy to introduce swappable inference formats and share examples on leveraging decision models with A2UI, which help building faster and more reliable generative UI experiences. Using our new A2UI Express as an inference format you can reduce latency by up to 3x, and up-to 80x using decision models like Jev to make layout decisions. Express requires up to 3x fewer tokens to generate the same kinds of UI compared to Direct JSON. We'll dive into the details in this blog post.
A2UI is an agent-optimized protocol for generative UI, where a client advertises a catalog of trusted components as a contract, an agent sends A2UI messages describing a bespoke user interface composed from that catalog, and the client's renderer draws the UI (see Introducing A2UI).
Initially agents generated A2UI JSON transport messages directly, every curly brace and nested element. It turns out that generating JSON trees constrained by a complex JSON schema is slow and error-prone for LLMs. This coupled A2UI to LLMs, which output text, and made it difficult to integrate faster System One decision models.
Now agents can generate A2UI Express, an intermediate format optimized for inference speed and accuracy, and rely on deterministic code in A2UI's Agent SDKs to translate it into the JSON-based transport protocol. Agent builders are also free to swap in any other DSL and its associated compiler for any special use-cases, and our A2UI Agent SDK(s) make it compatible with transports and renders.
The format the model generates is what we call inference_format. You set it with one argument when you create the generator. The SDK generates the prompt instructions for that format and compiles the model's reply into standard A2UI messages. This post covers how the swap works, why we developed A2UI Express as the new default inference format, and how a decision model can build screens from layouts you define in advance.
An inference format has two parts, and the SDK generates both from your catalog's JSON schema. A prompt section teaches the model the format's syntax, and a compiler compiles the model's reply into validated A2UI messages. Because both come from the schema, a format can't describe a component or property that your catalog lacks.
You choose the format with one argument when you create the generator:
from a2ui.processor import A2uiGenerator, CatalogConfig
from a2ui.inference_formats import ExpressFormatFactory
catalog = CatalogConfig.from_path("catalog.json")
generator = A2uiGenerator(
    [catalog],
    examples=few_shot_examples,  # written once as A2UI JSON
    inference_format_factory=ExpressFormatFactory(),
)
processor = generator.create_processor(renderer_capabilities)
system_prompt = f"{instructions}\n\n{processor.prompt_snippet}"
parts = processor.parse_response(model_reply)  # text parts + validated A2UI messages
A2UI Express is available in the Python agent SDK (a2ui-agent-sdk 0.9.0 on PyPI), in the TypeScript agent SDK (@a2ui/agent on npm), and in the Dart SDK (a2ui_agent 0.0.1-wip004 on pub.dev). In TypeScript, you pass new ExpressFormatFactory() as the generator's third argument. The Python and TypeScript SDKs can both stream Direct JSON chunk by chunk, and they compile Express from the complete reply.
Express writes one statement per line, in a style close to Python. Each line assigns a component to a variable, and the variable name becomes the component ID. Arguments are positional: the compiler maps them to property names in the order your catalog schema declares them, and _ skips one. $/title binds a value to the data model, and Event("accept") declares a server action. This is the A2UI gallery's notification card in Express:
surface("gallery-notification-permission")
$/description="Get alerts for order status changes"
$/icon="check"
$/title="Enable notification"
root=Card(main_column)
main_column=Column([icon, title, description, actions], _, "center")
icon=Icon($/icon)
title=Text($/title)
description=Text($/description, "body")
actions=Row([yes_btn, no_btn], "center")
yes_btn_text=Text("Yes")
yes_btn=Button(yes_btn_text, _, Event("accept", {}))
no_btn_text=Text("No")
no_btn=Button(no_btn_text, _, Event("decline", {}))
Swappable Inference formats including A2UI Express also work with macros in the Python agent SDK, which help when a screen shows data your systems already hold. The model writes a call with only an ID, such as OrderStatus("ord_42"), and your macro fetches the order and fills in the values, so every value on screen comes straight from your data. The macros README shows the setup.
Customer feedback uncovered latency and accuracy issues with direct JSON generation. To fix this, we started devising a new inference format. We experimented with four options:
We ran all four formats through the same 51-task eval on gemini-3.5-flash and compared them for thinking modes: on and off.
We observed that Express inference format works just as well even with thinking off; which can give you the fastest inference times when working with A2UI Express.
Some screens have a known shape, such as a settings page, a checkout or a confirmation. For those, the model doesn't need to design a layout. It needs to choose among layouts you have already defined, and a different kind of model is built for that. For this, you would not need the full expressivity provided by A2UI Express.
Jev, from TypeSafe, is what is called a System One model, built to make fast, structured decisions that code can use directly. Jev doesn't generate text or JSON. You send it a state and a set of typed questions, and it answers each one with calibrated probabilities. A question can ask whether a statement is true (Noul), which option from a list fits (Choice), or how something scores on a rubric (Score). Jev answers many questions in one request, in roughly 100 to 300 ms.
Apparite(jev2ui), an open-source design tool, shows one way to connect a System One model to A2UI. Jev decides the structure of each screen, code builds the A2UI components from those decisions, and a small model, gemini-3.5-flash-lite, writes only the text. The questions live in a Markdown grammar written ahead of time. A blockquote asks a question, and the bullets are its options, each with criteria. This block from grammar/screen.md decides which control a settings row gets:
#### row_control (of each row in rows, within each group in groups)
Material: a switch for one on/off setting that takes effect at once. HIG: a disclosure indicator for a row that opens another page.
> `{row}` is a row in the supplied screen and section. Grouped rows can represent content, navigation, settings or actions; use their actual text and context to decide.
>
> What kind of row is {row}?
- **switch** — A setting that is simply on or off and takes effect at once: notifications, dark mode, autoplay, sync.
- **value** — A setting with one current value picked from several, changed on another page: language, quality, theme, frequency, units.
- **nav** — A link to another page: a content item, details, account, privacy, help, about, or managing something. Its text and section identify what it opens.
- **check** — One of several alternative options listed together, of which one is chosen: the choices of a single setting, such as '10 seconds', '30 seconds', 'High', 'Low'.
- **danger** — A final or destructive account action: sign out, delete account, clear data, reset.
On a podcast app's settings screen, Jev answers Skip forward → value, Auto-download → switch and Log out → danger, each at p ≈ 1.00. Apparite builds a whole screen in three steps:
createSurface and updateComponents at about 200 ms, with placeholders where the text will go.updateDataModel. As each part arrives, small follow-up Jev requests settle what depends on it, such as the row controls above.
In one run of 11 prompts, the component tree was on screen in 92 to 298 ms and each screen was complete in 0.8 to 1.7 s. The text writer generated 101 to 341 tokens per screen, and both of Apparite's Jev pipelines produced valid A2UI on all 11 prompts. The project treats these numbers as a first look, since the sample is small.
Controlled generation can only produce the layouts its grammar describes. Apparite's grammar covers nine screen archetypes and twelve blocks, so screens without a known shape are a better fit for Express. A2UI Agent SDKs, don’t include a decision model inference format yet; apparite(jev2ui) project is an example on how A2UI messages could be assembled given a batch of independent decisions from a decision model.
A2UI Express is fast and keeps the full expressivity of A2UI, but a decision model making multiple independent decisions is still faster. Choose by how much of the screen you can define ahead of time:
Use Express in your agent. Install the Python SDK with pip install a2ui-agent-sdk or the TypeScript SDK with npm install @a2ui/agent, pass ExpressFormatFactory() when you create the generator, and run the model with thinking off. Your catalog and renderers stay as they are, and the Express specification documents the syntax.
To teach Gemini, or any other model that loads skills, to write Express with only your components, generate skills from your catalog with the Python SDK's SkillGenerator:
import json
from a2ui.core import Catalog
from a2ui.inference_formats.express import ExpressFormat
from a2ui.skill import SkillGenerator
catalog = Catalog.from_json(json.load(open("catalog.json")))
skills = SkillGenerator(ExpressFormat([catalog])).generate_skillset()
skills.export_to_directory("skills")  # a2ui-core plus one skill per catalog
Try controlled generation. Clone the example jev2ui repository, and follow the instructions there to get started. A hosted version of Apparite(jev2ui) runs at apparite.cnfg.ai.
Earlier A2UI posts: Introducing A2UI (December 2025), A2UI v0.9 (April 2026) and A2UI + MCP Apps (June 2026).
</kaynak_metni>
</haber>

<haber id="c068" puan="8" kaynak="Cloudflare Blog" tarih="2026-10-27">
Başlık: Introducing the Cloudflare PHP Capture the Flag challenge
URL: https://blog.cloudflare.com/php-ctf/
Özet: Cloudflare, WAF korumalarını aşmaya davet eden ve Bug Bounty programına bağlı bir PHP Capture the Flag yarışması başlattı.
<kaynak_metni>
Last week was one for the Internet security history books. First, eight eMudhra intermediate certificates were compromised, creating the possibility of forged certificates that could be used to impersonate servers. Then came php2shell: serious vulnerabilities in PHP, the runtime behind a large portion of the Web.
Cloudflare worked around the clock as these events unfolded to protect our customers and help protect the Internet. We shipped client updates and multiple mitigations, updated our web application firewall (WAF) with new rules to block attackers from exploiting the PHP vulnerabilities, and introduced a new feature called full transaction detection.
As always in situations like this, these new capabilities were made available on all plans, including Free.
Put our WAF to the test
Protecting systems from vulnerabilities like these is always an ongoing process, not a one-time event. The widespread adoption of AI allows attackers to discover new vectors with unprecedented speed and efficiency, so collecting real-world data to test our assumptions and strengthen defenses is essential.
That’s why today we're launching the Cloudflare PHP Capture the Flag challenge, run through our Bug Bounty program. We've put a deliberately vulnerable PHP installation behind our WAF, and we're inviting security researchers on HackerOne to try to bypass the protections and capture a flag.
How this Capture the Flag (CTF) works
We are keeping this simple. The challenge focuses on CVE-2026-109618 and CVE-2026-109619, the two PHP vulnerabilities behind php2shell. The target runs stock PHP 8.5.11 (with standard PHP extensions), Apache 2 (via mod_php), and an empty index.php inside a Cloudflare Container, with our default WAF protection rules for these vulnerabilities enabled in front of it. Inside the sandbox is a file called /flag.
The sandbox is reset every few minutes, including the flag file.
Your mission, should you choose to accept it: bypass the WAF protections, exploit the PHP sandbox, and recover the contents of /flag. You can use your own research tools. The challenge page has the environment details, scope, and flag verification form.
Challenge requirements
This limited-time challenge is run via Cloudflare's Bug Bounty program on HackerOne. All aspects of this challenge are subject to HackerOne terms and the Cloudflare HackerOne program rules the (“Bounty Terms”). If you find an eligible bypass, you must follow these requirements in order to claim the bounty:
- All participants must sign up for a HackerOne account and review and agree to the Bounty Terms before participating in the CTF.
- Demonstrate attacker-controlled PHP code or command execution inside the sandbox through an authorized POST request.
- Use that remote code execution (RCE) to recover the current contents of /flag, then successfully verify the flag through the CTF user interface (UI). Verify promptly before a reset; retain the successful result for later review.
- Submit a private report to Cloudflare on HackerOne. Include PHP CTF in the title and provide:
  - The endpoint, complete payload, and request sequence, preserving relevant headers, encoding, and body bytes.
  - Raw request/response captures or a readable proof of concept sufficient to reproduce the full chain.
  - An explanation of the WAF bypass, executed code or command, and how that execution recovered /flag.
  - The attempt ID, successful UI verification result, and exploit/verification UTC timestamps. Include the flag privately if needed for verification.
  - What makes the method or payload materially distinct, and related submissions you know about.
UI verification does not submit a HackerOne report or establish reporting priority. File disclosure without RCE, RCE without successful flag recovery and UI verification, local-only exploits, rediscovery of the known PHP vulnerabilities, and WAF detection differences or partial chains without the full objective are not eligible.
Awards require a materially distinct Firewall (WAF) bypass method, even for the same PHP CVE. Reports using the same Firewall-bypass mechanism are duplicates, regardless of differences in the PHP exploit, payload, RCE technique, or flag-recovery method. New flags, resets, attempt IDs, or cosmetic changes—including equivalent encodings—do not qualify as unique. Equivalent submissions are duplicates even if unfixed; only the first complete, reproducible HackerOne report is considered. Cloudflare makes final duplicate and reward decisions.
We record attempted metadata and request payloads to help analyze reports, so please use test data only. Do not send credentials, personal information, or anything else you would not want included in a research record. Read Cloudflare’s privacy notice before testing.
Testing is authorized only against the challenge hostname's WAF-protected /php/* endpoints (POST method only). Other Cloudflare services, direct access to the underlying infrastructure, the upstream PHP project, and third-party systems are out of scope. No denial of service, high-volume scanning, persistence, social engineering, or attacks on other participants. If you get a 429 or 503, back off.
In the event of any conflict between this blog post and the Bounty Terms, the Bounty Terms shall prevail.
Cloudflare reserves the right to suspend or terminate this challenge at any time. Once the competition is removed from HackerOne, it is officially terminated, so please refer to the Cloudflare HackerOne page for the most up-to-date information on whether this challenge remains open.
Not a substitute for patching
Our WAF protects you, but it is not a replacement for fixing vulnerable software. Response blocking can prevent exposed data from reaching an attacker, but it cannot undo actions already performed at the origin. If you run PHP, follow the latest PHP security advisories and apply the relevant updates.
Last week was a reminder that helping build a better Internet often takes many people—researchers, maintainers, and teams across the industry—doing difficult, urgent work together.
We hope this challenge gives everyone a useful way to join in. Head over to php-rce.cloudflare.app if you want to participate: the flag is there, and we'd like to know if you can get it.
</kaynak_metni>
</haber>

<haber id="c041" puan="7" kaynak="OpenAI News" tarih="2026-10-26">
Başlık: Introducing GPT-6.1 Terra
URL: https://openai.com/index/introducing-gpt-6-1-terra
Özet: OpenAI, hızlı ve yetenekli bilgisayar kullanımını herkese getiren GPT-6.1 Terra'yı tanıttı.
<kaynak_metni>
(metin alınamadı)
</kaynak_metni>
</haber>

<haber id="c000" puan="5" kaynak="TÜBİTAK Duyuruları" tarih="2026-10-27">
Başlık: 2508 TÜBİTAK – Slovenya Araştırma ve Yenilik Ajansı (ARIS) İkili İş Birliği Programı 2026 Yılı Çağrısı Açıldı
URL: https://tubitak.gov.tr/tr/duyuru/2508-tubitak-slovenya-arastirma-ve-yenilik-ajansi-aris-ikili-birligi-programi-2026-yili-cagrisi-acildi
Özet: TÜBİTAK ile Slovenya ARIS arasındaki 2508 ikili iş birliği programının 2026 çağrısı açıldı.
<kaynak_metni>
TÜBİTAK 1071 Programı kapsamında, Slovenya Araştırma ve Yenilik Ajansı (ARIS) ile imzalanan iş birliği protokolü çerçevesinde açılan çağrıyla iki ülkenin bilim insanları arasında; “Sağlık”, “Bilgi ve İletişim Teknolojileri”, “Gıda ve Tarım”, “İnşaatta İleri Malzemeler ve Teknolojiler” ve “Temel Bilimler” alanlarında gerçekleştirilecek olan ortak araştırma projeleri desteklenecektir. Çağrının alt tematik alanlarına ilişkin bilgiler çağrı metninde sunulmaktadır.
Çağrı kapsamında, Türkiye ve Slovenya'daki araştırmacıların ortaklaşa yürütecekleri projeler kapsamında karşılıklı seyahat desteği sağlanacaktır. TÜBİTAK tarafından seyahat giderlerinin yanı sıra bursiyer ve temsil-tanıtma giderleri de desteklenebilecektir.
Ortak araştırma projesi önermek isteyen Türkiye'deki bilim insanlarının, projeyi birlikte gerçekleştirecekleri Slovenya’daki bilim insanları ile proje ortağı olarak anlaşmaları gerekmektedir. Tek taraflı proje başvuruları kabul edilmemektedir.
TÜBİTAK'a yapılacak proje başvurularının elektronik başvuru sistemi üzerinden gerçekleştirilmesi gerekmektedir.
Son başvuru tarihi: 21 Aralık 2026 (23:59, TSİ)
E-imza sürecinin tamamlanması için son tarih: 28 Aralık 2026 (23:59, TSİ)
Çağrıya ilişkin ayrıntılı bilgiye aşağıdaki çağrı metni üzerinden ulaşılabilmektedir.
</kaynak_metni>
</haber>

<haber id="c089" puan="7" kaynak="Hacker News (100+ puan)" tarih="2026-10-27">
Başlık: Python's experimental JIT to be removed
URL: https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/
Özet: Python'un deneysel JIT derleyicisinin kaldırılacağı bildirildi.
<kaynak_metni>
Python's experimental JIT to be removed
[LWN subscriber-only content]
| Welcome to LWN.net The following subscription-only content has been made available to you by an LWN subscriber. Thousands of subscribers depend on LWN for the best news from the Linux and free software communities. If you enjoy this article, please consider accepting the trial offer on the right. Thank you for visiting LWN.net! |  | 
| Free trial subscription Try LWN for free for 1 month: no payment or credit card required. Activate your trial subscription now and see why thousands of readers subscribe to LWN.net. | 
Python's experimental just-in-time (JIT) compiler, which was added to CPython in 2024 for the 3.13 release, is on its way out. In June, the Python steering council announced that it was pausing work on the JIT in CPython's main branch until there was an accepted Python Enhancement Proposal (PEP) that addressed concerns about maintenance, compatibility, and set clear success metrics as well as a timeline for completion. After creating PEP 836 ("JIT Go Brrr: The Path to a Supported JIT Compiler for CPython") to try to meet the council's request, and after months of discussion, the JIT maintainers have withdrawn the PEP. For now, it appears that development on the once-promising project has come to an end.
The JIT was added to CPython by Brandt Bucher in early 2024. Generally, such a major feature would be expected to land only after the council had approved a standards-track PEP. Bucher had given a talk (YouTube video, slides) about the JIT at a Python core developer sprint, and announced his intent to merge the feature—but he had not taken the step of authoring or submitting a PEP for its approval. He was prodded into doing so by steering council member Thomas Wouters, who was also serving as the release manager for Python 3.13.
Bucher and Savannah Ostrowski drafted PEP 744 ("JIT Compilation"), which was an informational PEP—meaning it only provides information to the Python community and does not represent formal consensus to proceed on a feature or project. LWN covered the discussion of PEP 744 in April 2024, and later covered Bucher's talk on the JIT at PyCon US 2024, as well as the follow-up talk at PyCon US 2025.
PEP it up
Work on the JIT had been proceeding on the basis of PEP 744 until this
June, when the council had put forward its formal request for the JIT maintainers to
create a standards-track PEP. One might wonder, as
Antoine Pitrou did, why the council had decided that it was time to speak up
and ask for a new PEP. Wouters said
that there was no "
single triggering event for this request
", but that
the council had been discussing the topic for a while and indicated that it was
looking to ensure the JIT work did not interfere with other projects. "
There's been work
trying to get the JIT to play nice with instrumentation, debugging, and
profiling. There's also external JITs (like CinderX), JIT-adjacent things (like
Numba and PyTorch's compile), and discussions about a tier 3 JIT.
" The
council had waited until after the Python 3.15 beta release "
to be clear
that we're OK with the status quo for 3.15
".
The council asked for a PEP that would make the case for the JIT "
as a supported,
non-experimental part of CPython: its guarantees, its maintenance commitments,
and its impact on redistributors
". The council set a deadline of six months
for the PEP to be submitted and accepted; failing that, the council would
require the JIT code to be removed from the CPython main branch.
Bucher, Ostrowski, and Ken Jin drafted PEP 836 and published it on the Python forum for community feedback on July 3. It generated quite a bit of discussion, some favorable and some critical. One of the key themes in the comments, such as this one by Wouters, and this comment by Mark Shannon, was that the draft felt like it should be two separate PEPs. Shannon, for example, thought that the PEP should only cover goals for accepting the JIT work and felt that it should leave out implementation details. There were also quite a few calls for additional information.
Bucher pushed
back a bit on the suggestion that it should be two PEPs, and Ostrowski defended
the structure of the PEP as it was. "
Outlining goals like we have in the PEP
without being able to share the plan and everything we've thought through
alongside it would make me uncomfortable. To me, goals without plans behind them
aren't really goals at all.
"
When we last looked at this
topic in September, the discussion about the PEP had slowed down without a
commitment to develop new PEPs or a formal statement from the council. The last
word from the council at that time, in the form of a summary
of its August 6 meeting, was that it had met with the PEP authors and
was "
discussing the state of the PEP and whether it answered the questions
the SC asked in its request for a PEP
".
Experimentation in main
On September 21, Wouters posted
a statement from the steering council, minus Ostrowski (who is currently a
member of the steering council but did not participate since she is a co-author
of the PEP), that summarized its position. The statement
said that PEP did answer all of the questions that were highlighted in the
council's request, "
although perhaps some less convincingly than
others
".
The council wished to make clear that it was not looking for the criteria that the JIT should meet to be a supported feature, or whether it should be considered such. Instead, the council was evaluating whether the JIT should continue as an experiment in CPython's main branch.
Part of the problem with allowing experimentation in main is the lack of unified
design, and the uncertainty that core developers, package maintainers and users
face as the experimentation changes behaviours and API surfaces.
The council said that the PEP was not specific enough about support plans, performance
criteria, and too vague or too optimistic about a number of other areas. The
statement included a ten-point list of items that the council wanted "
to see
either spelled out in the PEP, or at least discussed and rejected
". The
council's list expressed concerns ranging from memory impact to security. For
example, on the topic of platform parity, the council wanted to ensure that the
JIT was designed to be easily adopted for new platforms. It wanted assurance
that the JIT's design would not be tied to specific platform or require
platform-specific knowledge to maintain.
Another area that the council called out was user impact. It said that the
PEP was "
overly optimistic
" about user-visible differences with the JIT
enabled. There were many cases where users depend on idiosyncrasies in the
interpreter design, "
as we've seen with other Python implementations or even
just between major Python versions
", and it wanted clarification on how
those differences would be handled. Would they be considered bugs, how would
situations be handled if a difference in behavior was unavoidable, and so
on.
Security was "
an underserved area in the PEP
", according to the
council; it suggested that a discussion with the Python security response
team was in order and that a security review should be part of the criteria
for supported status as well.
PEP 836 specified a compatibility
review milestone to correspond with the first Python 3.17 release
candidate—which would be expected sometime in August 2028—that
would involve running the test suites of the top PyPI packages to see if the JIT
broke them. The council wanted that timeline moved up significantly. "
We
think that's way, way too late, and the compatibility review should be an
ongoing and continuous process starting as soon as possible
".
The council also worried about the JIT's design decisions being made
"
without critical review by the larger group of developers ultimately
responsible for [CPython] development, maintenance and support
". The bottom
line, it said, was that PEP 836 "
mostly answers the questions we
asked
" with no missing pieces, but it wanted more discussion on those topics
so it could "
gauge community support and consensus before we're asked to
pronounce on this PEP
".
Jin replied a few days later to thank the council for its detailed feedback and said that the group would work on its suggestions.
Withdrawn
After some consideration, it appears, the PEP's authors have decided not to continue pursing the council's approval. On October 19, Ostrowski (who is also release manager for Python 3.16 and 3.17) announced that the PEP was being withdrawn:
The Steering Council rightly sets a high bar for a proposal of this scope, and
we don't feel we have the personal bandwidth to carry the current version
forward. We continue to believe in the technical direction outlined in the PEP,
including free-threaded support and a method-based frontend, and remain
optimistic about the JIT's potential in CPython. We'll make the reference
implementation available and link it from the withdrawn PEP so others who are
interested can explore and build on that.
Barry Scott asked
if that meant that work on the JIT was stopped. Brett Cannon replied
that the work would be stopped in the main repository, but it would be up to the
community whether the work would continue elsewhere. Dunc Graham suggested
that there might be time for an alternative PEP to be submitted before the
council's deadline. Cannon said
that was not likely, "
as all the people actively driving the JIT were either
authors on that PEP or contributors to it
".
With the PEP withdrawn, the JIT will likely be removed from CPython main fairly soon to ensure that any problems caused by its removal can be addressed early in the Python 3.16 development cycle. It is unclear whether the original drivers of the JIT work intend to continue working on it at all, or if it will simply be left for others to pick up if there is enough community interest. I have emailed the PEP authors for clarification, but have not yet received a reply.
Did you like this article? Please accept our trial subscription offer to be able to see more content like it and to participate in the discussion.
</kaynak_metni>
</haber>

<haber id="c115" puan="7" kaynak="ShiftDelete.Net" tarih="2026-10-28">
Başlık: Türkiye’de Kritik Altyapılarda 1071 ve 1453 Şifreleri Kullanılıyor – Risk Büyük
URL: https://shiftdelete.net/turkiyede-kritik-altyapilarda-1071-ve-1453-sifreleri-kullaniliyor-risk-buyuk
Özet: Türkiye'deki kritik altyapı tesislerinde 1071 ve 1453 gibi zayıf şifreler kullanıldığı ortaya çıktı.
<kaynak_metni>
Türkiye’de Kritik Altyapılarda 1071 ve 1453 Şifreleri Kullanılıyor – Risk Büyük
Türkiye’deki çeşitli kritik altyapı tesislerinin siber güvenlik zafiyetleri, bağımsız bir siber güvenlik araştırmacısının yaptığı çalışma ile gün yüzüne çıktı. Araştırmacı, sistemlerin giriş şifrelerinde ‘1071’ ve ‘1453’ gibi tahmin edilmesi oldukça kolay ve yaygın parolaların kullanıldığını tespit etti.
Bu zafiyet nedeniyle su pompaları ve atık su arıtma tesislerini de içeren 430 kritik sisteme kolaylıkla erişim sağlandığı bildirildi. Söz konusu durum, ulusal altyapı güvenliğinin mevcut koruma standartlarının yetersizliğini ve dijital dönüşüm süreçlerinde parola yönetiminin ne denli hayati bir öneme sahip olduğunu bir kez daha kanıtladı.
- Siber güvenlik araştırmacıları 430 farklı kritik tesise ait sistemlere zayıf parolalar üzerinden erişim sağladı.
- Erişilen sistemler arasında su yönetimi ve atık su arıtma gibi hayati öneme sahip altyapılar yer alıyor.
- Kritik altyapı yöneticilerinin şifreleme protokollerinde tarihsel sembolleri kullanması büyük bir güvenlik açığı oluşturuyor.
Siber Güvenlik Açıkları Ulusal Güvenliği Tehdit Ediyor
Modern dünyada kritik altyapılar artık sadece fiziksel değil, dijital varlıklarla da korunmaktadır. Ancak yapılan son araştırmalar, Türkiye’deki bazı tesislerin dijital kapılarının oldukça savunmasız olduğunu gösteriyor. Araştırmacı tarafından paylaşılan veriler, profesyonel sistemlerdeki parola politikalarının ne kadar özensiz uygulandığını gözler önüne seriyor.
Özellikle 1071 ve 1453 gibi toplumsal hafızada yer eden ancak tahmin edilmesi çok kolay olan şifrelerin tercih edilmesi, saldırganların işini kolaylaştıran temel unsurlar arasında yer alıyor.
Kritik Tesislerin Yönetiminde Yeni Standartlar Belirlenmeli
Su pompaları gibi doğrudan halk sağlığını ve şehir yaşamını ilgilendiren altyapıların bu denli basit yöntemlerle ele geçirilebilmesi, siber güvenlik stratejilerinin acilen gözden geçirilmesi gerektiğini gösteriyor. Uzmanlar, çok faktörlü kimlik doğrulama (MFA) sistemlerinin kritik tesislerde zorunlu hale getirilmesi gerektiğinin altını çiziyor.
Sadece parola kullanımı ile sınırlı kalan güvenlik duvarları, günümüzün sofistike siber saldırı yöntemleri karşısında etkisiz kalmaktadır. Kurumların, sistemlerini daha güvenli hale getirmek için sürekli izleme ve düzenli siber güvenlik denetimleri yapması kritik bir gereklilik haline geldi.
Siber Savunma Stratejileri Geliştirilmeye Devam Ediliyor
Bu olay, dijitalleşen dünyada sadece teknolojiye yatırım yapmanın yeterli olmadığını, aynı zamanda güvenlik kültürünün de tesis edilmesi gerektiğini gösteriyor. Şifreleme standartlarının oluşturulması ve çalışanların siber hijyen konusunda eğitilmesi, olası saldırıların önlenmesinde ilk savunma hattını oluşturuyor.
Yetkili kurumların, söz konusu zafiyetlerin giderilmesi için gerekli çalışmaları başlatması ve kritik altyapıların siber saldırılara karşı daha dayanıklı hale getirilmesi için gerekli güncellemeleri yapması bekleniyor. Dijital altyapıların güvenliği, ulusal güvenliğin ayrılmaz bir parçası olarak kabul edilmelidir.
Sizce kritik altyapı tesislerimizde dijital güvenlik önlemleri yeterli mi? Bu tür zafiyetlerin önlenmesi için kurumlar hangi adımları atmalıdır, yorumlarınızı aşağıda bizimle paylaşabilirsiniz.
</kaynak_metni>
</haber>

<haber id="c007" puan="5" kaynak="Google Developers Blog" tarih="2026-10-22">
Başlık: Streaming comes to API Gateway: real-time and AI-ready APIs, without changing your spec
URL: https://developers.googleblog.com/streaming-comes-to-api-gateway-real-time-and-ai-ready-apis-without-changing-your-spec/
Özet: API Gateway, SSE, WebSocket ve gRPC akışını önizlemede, API tanımı değiştirmeden destekliyor.
<kaynak_metni>
For most of the last decade, an API call looked like a transaction. A client sent a request, waited, and got a complete response back in one piece. That model is exactly what most API management tooling — including API Gateway — was built to handle, and it still describes a huge amount of production traffic.
But that no longer describes all traffic types. A model generating a response emits tokens as it produces them, not in one batch at the end. An agent working through a multi-step task reports progress as it goes. A dashboard, a collaborative editor, a live inference endpoint — these all need a connection that stays open and carries data in both directions.
Until now, developers building those experiences in API Gateway had to make an uncomfortable choice: put API Gateway in front of their APIs and give up streaming, or route streaming endpoints around the gateway and give up the authentication, API key enforcement, and observability that made the gateway essential in the first place. Teams ended up with a split estate — governed APIs on one path, ungoverned streaming traffic on another.
We're announcing that streaming support in API Gateway is available in Public Preview. Your streaming endpoints can now sit behind the same gateway, with the same policies, as everything else you serve.
For AI applications, streaming also strengthens API Gateway's connection to Gemini platform. A gateway that uses model routing now streams responses from Gemini, Claude and OpenAI gpt-oss models in model garden in Gemini platform as they're generated, and streaming backends you host anywhere else work the same way. Alongside Apigee and Agent Gateway in Gemini platform, API Gateway is the lightweight entry point to Google Cloud's AI gateway capabilities.
API Gateway now supports the full range of streaming patterns modern APIs rely on:
Streams can stay open for up to one hour. As with any long-lived connection, clients should implement reconnection logic so that a session survives the end of a stream — a well-behaved WebSocket or SSE client should be doing this anyway.
This is the part we are most pleased with: there is nothing new to learn.
Streaming is not a different product, a different resource type, or a different way of describing your API. There are no new extensions to add, no streaming-specific annotations, no separate spec for streaming operations. The same document that describes your existing API describes your streaming API.
Everything you already rely on continues to work exactly as before:
During Public Preview, you opt-in when creating the gateway:
gcloud api-gateway gateways create GATEWAY_ID \
  --api=API_ID \
  --api-config=CONFIG_ID \
  --location=REGION \
  --enable-streaming
That single flag is the entire difference. At GA, it is planned that streaming will simply be how API Gateway behaves, with no opt-in required and, as during Preview, no changes to your API config.
Alongside streaming, gateways get a deterministic default hostname:
GATEWAY_ID-PROJECT_NUMBER.REGION.gateway.dev
(Example: streaming-test-12345.us-central1.gateway.dev)
Previously the default gateway.dev hostname included a generated hash, which meant you could not know your gateway's URL until after you had created it. That is a small thing that causes a lot of friction: you can't write the endpoint into a client config, a Terraform module, a CI pipeline, a firewall allowlist, or a partner integration doc until the resource exists — and if you tear the environment down and rebuild it, the URL changes underneath you.
Now the hostname is a pure function of values you already chose. You can generate it, template it, document it, and commit it to source control before the gateway exists, and you get the same URL every time you rebuild the same gateway in the same project and region. For anyone managing environments as code, or promoting a configuration from dev to staging to prod, this removes an entire category of bootstrapping problem.
Streaming isn't a niche feature for AI applications — it's the expected interaction pattern.
Users expect to see a model's response appear as it's generated, not after a thirty-second pause. Agents need to report intermediate steps. Tool-calling protocols and remote MCP servers depend on long-lived, incrementally-delivered connections. An API management layer that can't stream severely limits the user experience of AI applications.
With streaming, API Gateway becomes a viable front door for that agentic traffic — and the value of a front door is exactly the same as it's always been, only more urgent. AI endpoints are expensive, they consume quota, they need per-consumer authentication and rate limiting, and they need to be observable. These are the governance problems that an AI gateway is intended to solve. The alternative — every team standing up its own proxy in front of its own model endpoint — is how organizations end up unable to answer basic questions about who is calling what.
Model routing in API Gateway lets you expose a single OpenAI-compatible endpoint and dispatch requests to Gemini, Claude, or OpenAI gpt-oss models based on the model field in the request payload. Model routing plus streaming means clients get a familiar, standards-based streaming interface, while you retain centralized control over which models are reachable, by whom, and under what policy.
Streaming, model routing and MCP support are all features within API Gateway that provide a lightweight on-ramp to AI gateway capabilities within Google Cloud. These AI gateway capabilities allow teams to monitor, secure and control agentic traffic of tools, models and agents in their ecosystem, and they're delivered as a composable suite so you can choose the right gateway for each use case. For more expansive AI policies and full lifecycle management, use Apigee. To manage and secure agent connectivity, use Agent Gateway in Gemini platform. You can also combine these gateways: API Gateway or Apigee can sit in front of your agents and APIs, or behind Agent Gateway so your agents can reach models, tools, and MCP servers. For example, you can route your agent's egress through Agent Gateway for strict security governance, and then pass the request to API Gateway to handle model routing.
A few things to plan around while the feature is in Preview:
If you're already using API Gateway, the fastest way to see this working is to point a new streaming-enabled gateway at an existing backend that emits SSE and watch the events arrive incrementally. No spec changes needed.
</kaynak_metni>
</haber>

<haber id="c008" puan="5" kaynak="GitHub Blog" tarih="2026-10-22">
Başlık: How bug bounty sharpens one researcher’s security skills
URL: https://github.blog/security/how-bug-bounty-sharpens-one-researchers-security-skills/
Özet: GitHub Bug Bounty ekibi bir araştırmacının yaklaşımını ve yeni başlayanlara tavsiyelerini paylaştı.
<kaynak_metni>
As Cybersecurity Awareness Month continues, the GitHub Bug Bounty team is excited to spotlight another top-performing security researcher from the GitHub Security Bug Bounty Program: @r31n!
As home to the world’s developers, GitHub is dedicated to the security and reliability of the code behind millions of projects, and our Bug Bounty Program remains a cornerstone of that commitment. Collaboration with external researchers is one of the most effective ways to improve security, and every year, the community helps us identify and fix vulnerabilities that make the platform safer for everyone.
The security research landscape is changing rapidly. AI has lowered the barrier to entry and become a genuine force multiplier. We use it across our own internal security programs, and we welcome researchers who do the same. However, what separates great research has not changed: validation, a working proof of concept, and a clear demonstration of real security impact. The tools do not matter; the quality of the work does. The researchers we spotlight this month exemplify exactly that standard through findings that are verified, reproducible, and demonstrate that a security boundary has been crossed rather than simply theorizing that one exists.
Researchers who consistently work at that level can earn an invitation to our permanent VIP program, which offers higher payouts, faster response times, and early previews of beta products and features. Learn more about how to qualify on our public bounty site.
As we wrap up our Cybersecurity Awareness Month celebration, we interview @r31n, a researcher renowned for their work on GitHub Enterprise Server, where they have repeatedly uncovered high-impact issues. Their reports consistently include working proofs of concept and clear reproduction steps, helping our engineering teams move from triage to remediation more quickly.
How did you get started in security and bug bounty, and what keeps you coming back to GitHub’s program?
I got into bug bounty because I wanted a way to keep developing my security skills outside the environments I work with every day. It exposes me to different products, technologies, and architectures I probably wouldn’t run into otherwise. GitHub is one of those programs I keep coming back to because there’s just so much surface area. It’s large, complex, and constantly changing. New features ship all the time, so it never really feels like a finished target. They also work closely with researchers, the bounty structure is competitive, and the swag is a nice bonus. It’s simply a program I enjoy spending time on.
What are your favorite classes of bugs to research and why?
I don’t really have one favorite bug class. What interests me more are exploit chains, especially cases where a few things that seem relatively harmless on their own come together and create something much more serious. An open redirect is a simple example. By itself, the impact might be limited. But if you find an allowlisted-domain SSRF that follows redirects, suddenly that open redirect can become a useful part of a much bigger chain. That’s probably the part of vulnerability research I enjoy most: finding those connections, looking at two or three separate bugs and realizing they can be combined in a way that wasn’t intended. It takes some technical knowledge, but also quite a bit of creativity.
How do you keep your skills sharp and stay on top of new vulnerability trends?
It’s actually a mix of different things. Security blogs, vulnerability write-ups, conference talks, proof of concepts, research papers, courses. I try to learn from wherever useful work is being shared. But most of it only really sticks once I try it myself. I can read a vulnerability write-up, but working through it myself gives me a much deeper understanding. If I actually reproduce the technique, play around with it, break it, and figure out why it behaves the way it does, that’s when it really stays with me. And later, when I see a similar pattern on a real target, it’s much easier to recognize.
What tools or workflows have been gamechangers for your research? Any lesser-known utilities you’d recommend?
I tend to prefer manual investigation and small, purpose-built scripts over large automated toolchains. If I notice I’m repeating the same task during research, I’ll usually automate that specific part. AI has probably impacted my way of working more than any individual security tool.
Even then, I think mindset matters more than tooling. You can become extremely good with a particular tool and still miss interesting bugs because you’re only looking at the target through the lens that tool gives you. Sometimes relying too heavily on tooling actually narrows the way you think. Tools change. Techniques change. Curiosity and persistence tend to age much better. So, I don’t really have one tool I’d recommend to everyone. The most useful tool is usually the one that helps answer the specific question I’m investigating.
Walk us through your general approach. How do you pick a target area, and how do you go from “interesting feature” to a confirmed finding?
I usually start by mapping out the application and getting a feel for how its different parts fit together. I tend to spend more time on complex functionality, integrations, trust boundaries, and anything that behaves a little differently from the rest. Experience and intuition matter too. Some areas simply look more likely to expose interesting security behavior. From there, I often think in terms of sources and sinks rather than starting with a specific vulnerability class. A source is a point where attacker-controlled data enters the application.
Think of a request parameter, uploaded file, API input, or data coming from another service. A sink can be a security-sensitive operation that consumes this data, for example, a network request, file access, process execution, database query, or authorization decision. The interesting part is tracing the path between the two. I look at how the data is transformed, validated, or passed across trust boundaries, and whether those controls are sufficient before it reaches the sink.
I like this approach because it lets me reason about attack paths without forcing my investigation into a predefined bug class. Sometimes the vulnerability only becomes obvious once you understand how a particular source can influence a security-sensitive operation. I consider a finding confirmed once I understand the attack path, can produce a working PoC, and can explain the impact.
Do you use AI in your research? Where does it genuinely help and where does it fall short?
Yes. Quite a lot, actually, but mostly as an accelerator. I use it for navigating unfamiliar code, finding call sites, tracing data through the codebase, and understanding how a system is structured and how its components interact. I also find it helpful for writing PoC scripts once I’ve identified the vulnerability.
Where it works best is when the question is specific. “Is this application vulnerable?” usually isn’t a very useful prompt. Give it the right context, explain what you already know, and ask a narrow question, and the quality goes up dramatically. There’s a bit of a paradox there. AI becomes more useful as you understand the problem better yourself. And I never treat its conclusions as facts. Hallucinations, false positives, bad assumptions, and confidently wrong answers are all common. Everything should still be manually verified. AI makes my work faster. However, it doesn’t replace understanding the application, developing intuition, or proving that something actually works.
What’s your guidance on using AI responsibly in bug bounty?
Use it to improve your research, not to outsource responsibility for it. If AI tells you it found a vulnerability, that doesn’t mean you found a real vulnerability. You still need to reproduce it yourself. You should understand exactly what’s happening, which security boundary or control is being violated, and what the real impact is. Ideally, you should understand the issue well enough that you could write the report without AI at all. Build a clear PoC. Make sure the security team can follow it. Know why every step matters.
AI has lowered the barrier to doing security research, which is great in a lot of ways. But you can also see the downside in the number of unverified reports teams now have to deal with. AI should make research better. Not just make more reports.
As the industry ships more AI-powered features, does testing them require a different mindset than traditional web bugs?
Yes. Conventional vulnerabilities still matter, but attackers may also be able to influence a probabilistic decision-making component through the data, instructions, or context it receives. But getting a model to say or do something unexpected isn’t necessarily the interesting part. The more important question is what that influence allows an attacker to achieve. Can they access something they should not or cause the system to act with privileges the attacker does not have? That’s why I don’t think model-level guardrails should ever be treated as the only or primary security boundary. You still need deterministic controls around the model. This includes proper authorization, least-privilege access, isolation, and validation. The surrounding systems matter just as much as the model itself. And traditional application security doesn’t disappear just because AI is involved. Model output should still be treated as untrusted input. If that output ends up in a browser, database query, shell command, web request, or another downstream system without the right controls, you can still end up with very familiar vulnerabilities: XSS, SQL injection, command injection, SSRF, and so on. I think the model is new. A lot of the dangerous sinks aren’t.
What’s one thing you wish you’d known when you first started?
Learn systems, not checklists. When I started, I was tempted to collect huge lists of techniques, payloads, tools, and bypasses and then work through them one by one. Those lists can be useful.
I still use them. But understanding how a system works has been far more valuable. Its internal logic. The data flows. Trust relationships. Assumptions. Why one component is allowed to talk to another. Why a particular restriction exists in the first place. I also learned not to assume something is secure because it looks secure, or because plenty of researchers have already tested it.
A lot of interesting research begins with: “Why does this work this way?” rather than “Which payload should I try next?” There’s some luck involved too. Sometimes you spend days following something that goes absolutely nowhere. Then you notice one tiny detail almost by accident and it turns into a high-impact finding. You can’t control that part. You can control whether you keep questioning things long enough to notice it.
What advice or resources would you recommend to researchers trying to land their first valid report?
Get comfortable with the fundamentals, then pick one program and one target and stick with them for a while. Constantly jumping between targets makes it difficult to build a real mental model of any of them. Use the application. Explore weird flows. Test different roles and permission levels. Read the documentation. Watch the requests and responses. Look at the APIs. Labs, courses, public write-ups, disclosed bug bounty reports, and intentionally vulnerable applications are all useful too. They teach you where bugs tend to hide and, over time, help build the intuition to recognize similar situations elsewhere.
One mistake I see a lot is relying on tools too early. Another is giving up because the obvious tests didn’t find anything. Tools help. They don’t build the mental model for you. And when you finally do find something, spend the extra time validating it properly. Create a working PoC. Make reproduction easy for the security team. Und
</kaynak_metni>
</haber>

<haber id="c009" puan="5" kaynak="GitHub Blog" tarih="2026-10-21">
Başlık: The bridge to agent-scale Git infrastructure
URL: https://github.blog/engineering/architecture-optimization/the-bridge-to-agent-scale-git-infrastructure/
Özet: GitHub, depolarının neredeyse tamamının bir kopyasını Azure'a taşıdığını ve kalanının nasıl taşınacağını anlattı.
<kaynak_metni>
Senior Software Engineer
Over the past year, while Git traffic grew exponentially, 99.99999% of the Git repositories on GitHub began living in two places at once: our own data centers and Azure. The rest are among the busiest on the platform, and they’re held back by just one thing: a 25ms round trip.
In an earlier blog post, we laid out the two principles behind our next-generation storage architecture:
- Minimize coordination
- Decouple storage from compute
In this post, we’ll look at the immediate bridge between our old design and our new one. We’ll talk about how a change to the way our quorum serializes writes gets the busiest repositories into Azure, and how that same step opens the door to replicas that keep no persistent state of their own.
How we got here
The timing and shape of the move were driven by the agentic shift: rapidly growing traffic, a hard ceiling on the power capacity of our data centers and the surrounding geographical region, and physical supply chain constraints. At the beginning of our migration, the remaining capacity with all possible expansion gave us enough time to migrate safely, but not enough to do it slowly.
While we had prototyped new architectural approaches for scaling Git on cloud infrastructure, changing the storage architecture and the hosting platform at the same time, under that growth, carried too much risk. Given our scale and how critical the service is to the community, we needed to sequence the work carefully: move the data first, then evolve the architecture once it arrived.
Git operations are a Tier 0 service: they’re a core function of GitHub, and nearly everything in GitHub depends on the repository data. That meant the data, services, and every dependency had to move first. The first copy of a repository landed in Azure’s Central US region in August 2025. Today, most repositories have two of their five replicas in Azure, and Azure serves about half of Git traffic. For most of that time, Azure absorbed our growth while our own data centers held steady.
During the migration, traffic follows the data. Most repositories have five replicas to balance durability, availability, and scale. To minimize read latency, Spokes uses preferential routing to direct traffic to a replica in the same region and availability zone as the request. As replicas move to Azure, the share of the traffic that can be served from Azure grows with each one, until the last replica arrives and the old region stops receiving requests entirely. Every repository goes through this process:
No repository left behind
So, what about the remaining 0.00001% of repositories?
In our current architecture, a repository hosted in more than one region has a lower write throughput ceiling. Spokes’ quorum only needs a majority to commit a write, but it waits for every healthy replica to respond (up to a timeout) before moving on, so slow replicas delay every write rather than falling behind. In practice, that means the slowest healthy replica sets the latency of every write, and because each write holds a repository-wide lock until it commits, it also sets the throughput ceiling. Once a replica lives in the target Azure region, it’s about 1,000 miles from our data centers, making each network round trip around 25ms, and a write requires multiple round trips. A repository already near its throughput ceiling can’t absorb that on every serialized write; it would fall further behind with every push.
This is where our first principle, minimizing coordination, comes into play. Specifically for this case: don’t serialize what doesn’t need to be. Git’s consistency requirements apply to each reference individually. Once the server accepts an update to a reference, no client should see an older value afterward, only that value or a newer one. That holds whether the update is a fast-forward, a force push, or a delete. But in most cases, updates to different references don’t depend on each other and can be applied independently.
So, we’re changing the scope of the quorum from the whole repository to individual references.
Holding a repository-wide lock for the entire reference update, round trips included, turns the quorum into a single, unordered request queue with one write in flight at a time. Each write in that queue takes as long as the slowest healthy replica. As the write rate grows, so does the queue, and each write waits longer than the one before it.
With per-reference serialization, only writes that contend on a shared reference must wait for each other. In practice, most writes to a repository touch different references—for example, agents and developers pushing to their own branches—so they no longer wait on each other. Each write still experiences the cross-region latency but writes to different references can be in flight at the same time. That removes the single bottleneck on the repository. We can visualize how queueing and timeouts build up by comparing the two approaches side by side under similar load:
These changes raise a repository’s write throughput ceiling roughly in proportion to how many references are being written at once, and get the last remaining repositories into Azure. In internal testing with realistic traffic, writes to different references consistently saw 3–4x higher throughput at lower latency.
Scaling reads on their own
Most repositories are heavily read-skewed, with somewhere between 100 and 1,000 reads for every write. Today, reads and writes hit the same replicas, so they compete for the same resources and can’t be scaled independently.
Decoupling storage from compute changes that. Once repository data is durably stored in Azure Blob Storage and updated with each incoming write, we can begin to decouple read traffic from the write quorum, and independently scale the compute needed for each. For example, reads would benefit from far more in-memory cache than we give them today, but that memory is also needed for compaction. Once they’re separated, each gets its own configuration.
The first step is making object storage a member of the quorum, but a special one that we call a virtual replica. The compute that represents it is our first fully ephemeral node. It serves as a bridge to object storage, streaming incoming writes and serving no reads. Because it’s a member of the quorum, a write isn’t acknowledged until it’s durable in object storage.
That adds a little latency to each write, but just like the cross-region round trip, per-reference serialization keeps it from becoming a throughput bottleneck. The virtual write replica also coalesces transactions on disjoint references into a single set of network I/Os to object storage, so a busy repository pays for one round trip across many concurrent writes instead of one per write. For now, the virtual write replica also handles compaction, and read replicas inherit the compacted state.
With the virtual write replica in place, we can scale out as many virtual read replicas as a repository needs, on demand. Each read replica warms its cache from Azure Blob Storage and starts taking read traffic without joining the quorum, using object storage as the source of truth and reconciling its local state against it in the background.
This step unlocks significant read scale. In internal testing, our distributed load testing harness routinely found ceilings in the current architecture. Against virtual read replicas, the harness hit its own limits first. It also comes with a few challenges that are solved in subsequent steps:
- Virtual read replicas start out reconciling with object storage in the background, which makes them a good fit for some read workloads but not all of them. Serving every kind of read requires moving that reconciliation in-line, fetching only the reference state and data that changed since the replica last caught up.
- While we’ve incrementally increased write throughput by shifting to a per-reference model, the quorum remains the bounding factor for increasing further.
How can we push write throughput further?
What comes next
The GitHub of today was built on the Spokes quorum, and over the years Spokes has become much more than a quorum coordinator. It’s also an intelligent routing and load balancing layer, a unified API that internal clients use to access and transact repository data at well over 100 billion operations per day, and a collection of background systems we call “sweepers” that handle repository placement, repair, and rebalancing between storage nodes.
The vast majority of what lives under the Spokes service umbrella applies just as well to the new architecture as it does to the existing one. But we also recognize that the commit protocol that has taken GitHub to a billion repositories won’t take it to the next billion and beyond.
We’re not done yet. With these steps in place, the next limit is write throughput. Every write still waits on replicas that each hold a full copy of the repository, yet very little of a write actually needs to be ordered. Git objects are immutable and named by their contents, so they can be stored without anyone agreeing on them. What’s left is small, and the hard part is ordering it as fast as possible without moving the bottleneck somewhere else. Designing for that on a whiteboard is one thing. Doing it underneath a billion repositories that developers and agents are writing to around the clock is another. Getting there forced us to rethink the second-order effects too, like where durable reference state lives and how compaction and garbage collection scale.
Agent traffic isn’t slowing down, and each of these steps gives repositories more headroom as it lands, without waiting for the end state.
Coming next week: At GitHub Universe and in the final post in this series, we’ll take a tour through that end state, what it does for write throughput, the second-order problems we had to solve to get there, and why there’s still a (small) consensus group somewhere in the stack.
Thanks to Brian Celenza for their contributions to this post.
Tags:
Written by
Related posts
Our new repo star history API now provides trends without returning individual identities or requiring unbounded database work. These are the engineering tradeoffs we made.
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
