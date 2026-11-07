# Görev: write

Yanıtı `episodes/2026-W44/llm/write.response.json` dosyasına, aşağıdaki JSON şemasına uyan TEK bir JSON nesnesi olarak yaz.

## Sistem talimatı

Sen GDG on Campus Kastamonu'nun haftalık, yapay zekâyla üretilen 60-90 saniyelik dikey teknoloji gündemi videosunun senaristisin.
Kitle: Türkiye'deki üniversite öğrencileri. Ton: enerjik ama abartısız, samimi "sen" dili, haber spikeri netliği. Tıklama tuzağı yok.

Görev: Verilen aday haberlerden 3-4 tanesini seç ve senaryoyu şemaya uygun üret.

Seçim:
- Öğrencinin işine yarayan (başvuru, ücretsiz araç, yarışma, açık kaynak sürüm) haberleri öne al; konu çeşitliliği gözet (hepsi aynı şirketten olmasın).
- Kaynak metni boş veya çok kısa olan haberi seçme.

KESİN KURALLAR (ihlal edilirse bölüm yayınlanmaz):
1. Kaynak metinlerde geçmeyen HİÇBİR rakam, isim, tarih, sürüm numarası veya özellik kullanma. Yuvarlama yapma; sayıyı kaynaktaki gibi ver.
2. Anlatımdaki ve "student_take"teki her olgusal ifadeyi `claims` listesine yaz ve kaynağını `source_url` ile bağla. source_url, o segmentin `sources` listesinde olmalı.
3. Kaynağın açıkça söylemediği, çıkarım/yorum içeren her iddiayı `uncertain: true` yap. Emin değilsen kullanma ya da uncertain işaretle.
4. student_take somut olsun: kaynakta bir başvuru tarihi, ücretsiz erişim, indirilebilir araç varsa onu söyle; yoksa genel ama doğru bir öneri ver (ör. "dokümanı incele", "projende dene") ve tarih/rakam uydurma.
5. Uzunluk: hook + tüm narration + tüm student_take + outro toplamı 130-185 kelime (Türkçe ~2.3 kelime/sn → 60-90 sn). Haber başına narration ~22-32 kelime, student_take ~10-16 kelime.
6. Metinlerde rakamları rakamla, İngilizce terimleri orijinal yazımıyla yaz (OpenAI, GPU, %12). Seslendirme için ayrı bir normalizasyon adımı var.
7. Şirket logosu veya gerçek kişi fotoğrafı isteme; görselleri yalnızca şemadaki component'lerle tarif et.

Görseller (her segmentte 2-4, ilk görsel HeadlineCard):
- StatCounter: kaynakta çarpıcı tek bir sayı varsa.
- MiniChart: kaynakta karşılaştırılabilir en az 2 sayı varsa (ör. eski/yeni performans).
- CodeBlock / Terminal: geliştirici haberlerinde kaynaktaki kod/komut veya resmi kurulum komutu varsa (uydurma API çağrısı yazma).
- SourceScreenshot: duyuru sayfasının ekran görüntüsü; screenshot_url = ana kaynak URL. Her segmentte bir tane olması iyi.

hook: haftanın en çarpıcı gelişmesini tek cümlede ver (en fazla 8 kelime), "Merhaba"yla başlama.
outro: kısa kapanış, ör. "Haftaya görüşmek üzere, takipte kal!" (GDG etkinlikleri ekranda ayrıca gösterilecek).

## Girdi

Hafta: 2026-W44

<haber id="c001" puan="7" kaynak="Google Developers Blog" tarih="2026-10-27">
Başlık: Fast, reliable A2UI, with swappable inference formats
URL: https://developers.googleblog.com/fast-reliable-a2ui/
Özet: Google, A2UI için A2UI Express formatını duyurdu; 3 kata kadar daha az token kullanıyor ve gecikmeyi azaltıyor.
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

<haber id="c006" puan="7" kaynak="Android Developers Blog" tarih="2026-10-21">
Başlık: A more reliable way to add and edit contacts on Android
URL: https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android
Özet: Yeni Android sürümünü hedefleyen uygulamalar WRITE_CONTACTS izniyle rehbere doğrudan yazamayacak.
<kaynak_metni>
What's changing
Apps that target the upcoming Android release will no longer be able to directly write to contacts with the WRITE_CONTACTS permission. Instead, you can use the standard contact intents (ACTION_INSERT, ACTION_EDIT, and ACTION_INSERT_OR_EDIT). For a complete reference implementation, see the developer guide on how to modify contacts using intents. 
On devices running the upcoming Android release, these three contact intents will behave consistently and need no permission at all. If your app targets the upcoming Android release or later and attempts to write to contacts directly, those writes will be rejected and result in a SecurityException or permission denial. For the small set of apps which require broad access to create and modify contacts, a new special app access permission, MANAGE_CONTACTS, arrives in Android 17 QPR2 (Q4 2026). Google Play is publishing updated guidelines for contact access, including MANAGE_CONTACTS, today.
Why we're doing this
Currently, if your app needs to save even one contact, you might be requesting WRITE_CONTACTS. But that permission grants broad access, allowing an app to make widespread changes to contacts across the device in the background, even without user interaction. Most apps don’t need such broad permission.
While alternatives exist, we've heard from you that they need to be more standardized across the ecosystem. Previously, the contact intents behaved differently from one device to the next. Some editors dropped the data you passed in, like a contact photo. On some devices, the back button saved the contact without the user meaning to or the "create new contact" option was hard to find. So asking for permission was the rational choice. We're fixing all these issues in the upcoming Android version and requiring devices running it to follow the same standards.
What to use instead
Add or edit a contact: use the contact intents
When you use these intents - ACTION_INSERT, ACTION_EDIT, and ACTION_INSERT_OR_EDIT - the system handles the heavy lifting by presenting a clean,  standardized contact editor experience. It opens a quick half-sheet form for new entries, or allows the user to easily search and add information to an existing contact. Users can seamlessly expand this into a full-page editor to fill out more details, all without your app ever needing direct write permissions. View the tentative UX mocks below: 
Figure 1: Create a New Contact *UX not Final*
Figure 2: Add Info to an Existing Contact *UX not Final*
Note: Different device manufacturers may modify the user experience to match their OS style but the behaviour will remain consistent.
You can further streamline the creation process by passing optional data payloads, known as Extras, alongside your intent:
- EXTRA_ACCOUNT suggests which account the contact saves to, which helps if your app syncs contacts. This extra already existed, but support varied by device. Starting in the upcoming Android release, support is standardized across devices.
- EXTRA_PHOTO_URI passes a photo to pre-fill the contact picture. The editor handles the URI read permission for you. This is new with the upcoming Android release and will be supported across the ecosystem.
| Before: writing directly with WRITE_CONTACTS (Results in a SecurityException or permission denial once your app targets the upcoming Android release.) // Requires android.permission.WRITE_CONTACTS fun saveContactDirectly(context: Context, name: String, phone: String, account: Account) {     val ops = arrayListOf(         ContentProviderOperation.newInsert(ContactsContract.RawContacts.CONTENT_URI)             .withValue(ContactsContract.RawContacts.ACCOUNT_TYPE, account.type)             .withValue(ContactsContract.RawContacts.ACCOUNT_NAME, account.name)             .build(),         ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI)             .withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0)             .withValue(                 ContactsContract.Data.MIMETYPE,                 ContactsContract.CommonDataKinds.StructuredName.CONTENT_ITEM_TYPE             )             .withValue(ContactsContract.CommonDataKinds.StructuredName.DISPLAY_NAME, name)             .build(),         ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI)             .withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0)             .withValue(                 ContactsContract.Data.MIMETYPE,                 ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE             )             .withValue(ContactsContract.CommonDataKinds.Phone.NUMBER, phone)             .build()     )     context.contentResolver.applyBatch(ContactsContract.AUTHORITY, ops) }  | After: opening the contact editor (No permission needed.) fun saveContactWithEditor(     context: Context,     name: String,     phone: String,     account: Account,     photoUri: Uri ) {     val intent = Intent(Intent.ACTION_INSERT, ContactsContract.Contacts.CONTENT_URI).apply {         putExtra(ContactsContract.Intents.Insert.NAME, name)         putExtra(ContactsContract.Intents.Insert.PHONE, phone)         // Suggest which account the contact is saved to         putExtra(ContactsContract.Intents.Insert.EXTRA_ACCOUNT, account)         // New in the upcoming Android release: pre-fill the contact photo         putExtra(ContactsContract.Intents.Insert.EXTRA_PHOTO_URI, photoUri)         clipData = ClipData.newRawUri("", photoUri)         addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)     }     context.startActivity(intent) }  | 
| Before: updating an existing contact directly // Requires android.permission.WRITE_CONTACTS fun addPhoneDirectly(context: Context, rawContactId: Long, phone: String) {     val values = ContentValues().apply {         put(ContactsContract.Data.RAW_CONTACT_ID, rawContactId)         put(ContactsContract.Data.MIMETYPE, ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE)         put(ContactsContract.CommonDataKinds.Phone.NUMBER, phone)     }     context.contentResolver.insert(ContactsContract.Data.CONTENT_URI, values) } | After: letting the user choose a contact to update, or create a new one fun addPhoneWithEditor(context: Context, phone: String) {     val intent = Intent(Intent.ACTION_INSERT_OR_EDIT).apply {         type = ContactsContract.Contacts.CONTENT_ITEM_TYPE         putExtra(ContactsContract.Intents.Insert.PHONE, phone)     }     context.startActivity(intent) } If you already know which contact to update, use ACTION_EDIT with that contact's URI: fun editKnownContact(context: Context, contactUri: Uri, phone: String) {     val intent = Intent(Intent.ACTION_EDIT, contactUri).apply {         putExtra(ContactsContract.Intents.Insert.PHONE, phone)     }     context.startActivity(intent) }  | 
Pick a contact: use the Contact Picker
If you only need to read contacts the user chooses, use the Contact Picker, available since Android 17. It needs no permission.
Calling and messaging apps: use People Directory
Some apps add "Call with…" or "Message with…" actions to contacts so people can start a call or chat from the Phone or Contacts app. If your app does this today by writing extra entries into the user's contacts, move to People Directory, arriving in Android QPR2 (Q4 2026). It's a new system directory where your app publishes how people can reach each other in your app, without editing the user's contacts.
Examples of how apps can migrate
To see how these alternatives work in practice, here are a few examples of how different types of apps can approach contact access:
| Example app type (non-exclusive). | Recommended migration path | 
| Social, P2P Payment, & Ride-Sharing Apps | If your app lets users find friends, split a bill, or share a trip status, you don't need contact permissions at all. Use the Contact Picker for one-time contact selection, and launch ACTION_INSERT with EXTRA_PHOTO_URI when a user taps "Save to Contacts" on a profile. | 
| Business Card Scanners & Event Networking Apps | If your app scans a badge or QR code and saves a new contact – or adds a work phone number to an existing colleague's entry – use ACTION_INSERT or ACTION_INSERT_OR_EDIT. The standardized half-sheet editor pre-fills the parsed fields (name, company, phone, email, and photo) so the user can verify and save in one tap without granting background permissions. | 
| VoIP Calling & Messaging Apps | Rather than requesting WRITE_CONTACTS to inject custom "Call with…" or "Message with…" rows into the user's address book, publish reachability metadata through People Directory and use ACTION_INSERT when users add a new contact from a chat thread. | 
| Enterprise CRM & Cloud Sync Apps | If your app performs continuous, two-way background contact synchronization with a cloud or enterprise account – where prompting the user with an intent UI for every record isn't feasible – your app qualifies to declare MANAGE_CONTACTS  | 
Changes to check for
- Custom data types aren't supported in the editor. If you pass Insert.DATA rows with MIME types other than the standard ContactsContract.CommonDataKinds types, those MIME types will be silently ignored by the editor.
- SHOW_OR_CREATE_CONTACT isn't handled by the system editor. Contacts apps that come with the device can still handle it. For consistent behavior across devices, use ACTION_INSERT_OR_EDIT.
- Writes fail by default. Once you target the upcoming Android release, any direct write without MANAGE_CONTACTS results in a SecurityException or permission denial. Test for it.
Do I need MANAGE_CONTACTS?
Probably not. If your app saves or edits contacts because a user asked it to, the intents above cover you, with no permission and no Play Console declaration.
MANAGE_CONTACTS is for apps whose core purpose is managing contacts, where the intents aren't enough. For example:
| Your app… | Need MANAGE_CONTACTS? | 
| Saves a contact from a chat, business card, or order. | No, use ACTION_INSERT | 
| Adds a number or email to an existing contact. | No, use ACTION_INSERT_OR_EDIT or ACTION_EDIT | 
| Lets users pick contacts to invite, share with, or pay. | No, use the Contact Picker | 
| Adds call or message actions to contacts. | No, use People Directory | 
| Has its own branded contact editing screen. | No, a custom interface alone doesn't qualify | 
| Is a dedicated contact manager or dialer replacement app. | Likely yes | 
| Is a caller ID & spam protection app that mass-updates address book entries. | Likely yes | 
| Syncs contacts with an enterprise or cloud account in the background. | Likely yes | 
| Performs bulk contact backup/restore or device-to-device phone transfer. | Likely yes | 
| Sets custom ringtones for individual contacts. | Likely yes | 
How it works:
- MANAGE_CONTACTS is a special app access permission. It isn't a runtime dialog. Users turn it on under Settings > Special app access > Manage contacts.
// Opens Settings > Apps > Special app access > Manage contacts
val intent = Intent(Settings.ACTION_MANAGE_CONTACTS, Uri.fromParts("package", packageName, null))
context.startActivity(intent)
- It covers reading, adding, editing, and deleting contacts, accounts and People Directory data. You don't need to request READ_CONTACTS as well.
- To publish on Google Play with MANAGE_CONTACTS, you submit a declaration in Play Console explaining why the intents aren't enough for your app's core functionality.
Migration steps
- Find your contact writes. Search your code for WRITE_CONTACTS, ContactsContract.RawContacts.CONTENT_URI, ContactsContract.Data.CONTENT_URI, and applyBatch(ContactsContract.AUTHORITY, …).
- Replace each user-driven write with an intent: ACTION_INSERT for new contacts, and ACTION_EDIT or ACTION_INSERT_OR_EDIT for updates.
- Use only standard data types in Insert.DATA. Move call or message actions to People Directory.
- Decide whether you truly need MANAGE_CONTACTS using the table above. If you do, plan your Play Console declaration.
- Remove WRITE_CONTACTS fro
</kaynak_metni>
</haber>

<haber id="c039" puan="8" kaynak="OpenAI News" tarih="2026-10-26">
Başlık: Introducing GPT-6.1 Terra
URL: https://openai.com/index/introducing-gpt-6-1-terra
Özet: OpenAI, hızlı ve yetenekli bilgisayar kullanımını herkese getiren GPT-6.1 Terra'yı tanıttı.
<kaynak_metni>
(metin alınamadı)
</kaynak_metni>
</haber>

<haber id="c002" puan="6" kaynak="Google Developers Blog" tarih="2026-10-26">
Başlık: Preview, edit, and collaborate on markdown (.md) files natively in Google Docs and Drive
URL: https://developers.googleblog.com/preview-edit-and-collaborate-on-markdown-md-files-natively-in-google-docs-and-drive/
Özet: Google Workspace, Docs ve Drive'da Markdown (.md) dosyalarına yerel destek getirdi.
<kaynak_metni>
Google Workspace is bridging the gap between code and collaboration by providing a familiar, real-time environment where developers and AI agents can seamlessly work together on documentation.
Markdown (.md) is a standard text format widely used by LLMs to preserve structured content—such as tables, headers, and bulleted lists—without the overhead of bulky file formats. Markdown file usage in Google Drive has surged year-over-year, indicating how critical this format has become for modern, fast-paced workflows.
Now, you can natively view, edit, and collaborate in markdown files directly in Google Docs, eliminating the friction of manual file conversions. You can edit without changing file types while ensuring your underlying documentation is preserved for developer tools and git repositories. Plus, with rendered previews in Google Drive, you can easily review formatting with a click.
As AI agents take on larger roles in drafting, planning, and coding, markdown serves as a collaborative common language between humans and AI tools because it is easily readable by both. Google Docs provides a familiar, easy-to-use environment, acting as a shared bridge where team members and autonomous agents work together directly on the same documents. When you open a markdown file in Google Docs, you have:
By combining the simplicity of markdown with the powerful real-time collaboration of Google Docs, teams now have a unified workspace to draft, review, and ship technical content faster.
Anyone with a Google or Workspace account can get started today by uploading an .md file to Google Drive and begin collaborating directly in Google Docs.
</kaynak_metni>
</haber>

<haber id="c005" puan="6" kaynak="Google Developers Blog" tarih="2026-10-21">
Başlık: Powering the Agent Development Lifecycle with any framework, from ADK to LangChain and beyond
URL: https://developers.googleblog.com/powering-the-agent-development-lifecycle-with-any-framework-from-adk-to-langchain-and-beyond/
Özet: Agents CLI eklenti sistemi ADK, LangChain ve LangGraph gibi çerçevelerle ajan geliştirmeyi destekliyor.
<kaynak_metni>
End to end walkthrough of the new Agents CLI Extension System, with a worked LangChain example and a custom deploy policy
When we launched Agents CLI at Google Cloud Next '26, we built it around one strong opinion: going from an idea to a production agent on Google Cloud should take a single unified command surface. For teams building with Agent Development Kit (ADK), that opinionated path has worked. You run agents-cli create, write the agent logic, and ship to Cloud Run with observability and evals wired up, in about thirty minutes.
The agent framework landscape has grown more diverse in the months since. In addition to ADK, developers today pick between LangChain and LangGraph, specialized newcomers like Deep Agents, or in-house frameworks tailored to a specific business domain. Different teams prefer different frameworks, and the right choice for a greenfield prototype is rarely the right choice for a production migration. Enterprise admins may also have governance policies they want to enforce across the ADLC for all of their development teams, such as: a compliance scan, an SSO gate, a Model Risk Management hop.
Can a team benefit from the deployment, evaluation, and observability work in Agents CLI without being forced to adopt ADK, or without being forced to accept the default behavior of every command? Starting with version 1.5.0, the answer is yes. Agents CLI now ships with an Extension System that lets developers override or add commands without forking the tool. Version 1.8.0 ships the first-party LangChain extension, which replaces the framework-coupled commands with their LangChain equivalents and leaves the rest of the lifecycle untouched.
We will walk through two journeys below. First, to show you the ADLC with LangChain agents, we'll show you how you can scaffold, run, deploy, and evaluate a LangChain agent through the Agents CLI lifecycle using the first-party extension. Then we build our own small extension that wraps the deploy command with a Software Bill of Materials (SBOM) scan, demonstrating the pattern enterprise platform teams can use to enforce their own policies across every project. Both journeys use the same mechanism.
Most agent development toolchains available today share a limitation: they are opinionated about one specific framework, and the surrounding capabilities (deployment targets, CI/CD pipelines, evaluation harnesses, observability wiring) assume the developer has adopted that framework. When your framework matches the tool's assumption, the opinionated path works. When it does not, you're left with three bad options.
The first is to fork the CLI, maintaining a divergent copy and re-syncing it on every upstream release. You pay a permanent maintenance tax, and every upstream improvement has to be hand-merged into the fork. The second is to wrap the CLI behind custom scripts, building a parallel command surface that invokes the underlying tool. The problem is that developers (and their coding assistants) forget about the wrapper and call the underlying tool directly, bypassing the intended abstraction. The third is to walk away and build everything from scratch, which can consume several engineer-months of work that the team had not planned for, and which rarely produces tooling as polished as the upstream project.
The problem shows up in two scenarios. One is enterprise customers adopting Agents CLI: in regulated industries, a central platform team often requires that every deploy invocation be wrapped with a compliance check, that login route through corporate single sign-on, or that evaluations flow through a Model Risk Management pipeline. Each of these requirements, implemented today, means either forking the CLI or building a wrapper layer. The other is teams that use ADK most of the time but need to run a non-ADK framework on a specific project. Within the Agents CLI command surface, six commands assume the ADK runtime: playground, run, and four eval subcommands. The other eighteen or so (scaffold, infra, deploy, publish, login, and friends) are framework-agnostic. Without extensions, choosing a non-ADK framework for a single project meant losing access to all twenty-four.
The Extension System handles both with one mechanism.
An Agents CLI extension is a directory in a Git repository that contains a single file called agents-cli-extension.yaml. The file declares which built-in commands the extension overrides and which new commands it adds. From the official documentation:
Extensions are how you adapt agents-cli to a workflow it doesn't ship with — a different agent framework, an org's deploy policy, or a command of your own — without forking the tool.
Extensions take two shapes, described in the Using Extensions page. A command override replaces the behavior of a built-in like playground, deploy, or eval generate. The overridden command receives the user's arguments verbatim, so the user experience stays consistent with the native command. A new command exposes a workflow the CLI does not currently provide as agents-cli <your-command>. Both shapes can coexist in the same extension, and most non-trivial extensions use a combination of the two.
Extensions are distributed through Git repositories rather than through a dedicated package registry. The design draws from the extension model used by the gemini-cli project. There is no central index to publish to, no package format to maintain, and no ownership roster to apply for. Any directory inside any Git repository can serve as an extension, and Git handles the versioning, pinning, and distribution. For enterprise platform teams, this means creating an internal platform-extensions repository and pointing their developers at it, with no external registry to coordinate with.
An extension can be referenced in several ways, depending on where it lives and how the developer wants to use it:
# First-party shorthand, which resolves to the google/agents-cli repository
agents-cli extension add <name>
# Any organization or repository on GitHub, including self-hosted Git servers
agents-cli extension add acme/platform-extensions
agents-cli extension add acme/platform-extensions#soc2-deploy
# A local path, which is typically used during extension development
agents-cli extension add local@../my-extension
The #<name> syntax lets a single Git repository hold multiple extensions, with the fragment identifier selecting one of them. Enterprise platform repositories often bundle together a family of related extensions (one for deploy, one for login, one for scaffold create) under a single repo with shared ownership and release cadence.
Extensions install at two scopes. The default is the project scope, where the extension and its lockfile entry are committed to the project's own repository. Teammates and CI pipelines pick it up on checkout. The alternative is the user scope, enabled via the --global flag, where the extension is stored in the user's home configuration directory and applies to every project on the machine. The user scope is the one you reach for when an extension needs to be available before any project exists, such as a framework bootstrap extension that configures agents-cli create itself.
When both scopes define the same command, the project scope wins, and agents-cli info surfaces the source of each active command. Scoping is deliberately explicit: the Extension System will not silently merge or override extensions, and any conflict surfaces to the developer at install time or in the extension list output.
The Extension System follows the discipline of package managers like uv or npm: it resolves a Git reference to an exact commit SHA at install time, records the resolved SHA in a lockfile, and uses the lockfile to re-materialize the exact reviewed code on every fresh checkout. The agents-cli install command restores the vendored working copy from the pinned SHA without advancing the pin, which guarantees that CI and local development run bit-for-bit identical code. To advance a pin to the latest commit on the tracked reference, the developer runs agents-cli extension update, which re-resolves the reference and re-prompts for third-party trust. The complete lifecycle is in the Using Extensions → Lifecycle section.
The Extension System is marked experimental in v1.8.0. The manifest schema and the command surface may still change in breaking ways before the system is finalized, so teams depending on it should pin their Agents CLI version.
The LangChain first-party extension is a project template: one command scaffolds a working LangChain agent wired into the Agents CLI lifecycle. The resulting project has zero google-adk dependency and deploys to Cloud Run through the same code path an ADK project uses. The template's own description reads:
Run LangChain agents, LangGraph graphs, and Deep Agents through the agents-cli lifecycle.
In modern LangChain (version 1.0 and later), the state management layer is provided by LangGraph, so the three frameworks share a common graph representation. The template serves all three communities with the same code.
Before we begin, we need:
Python 3.11 or later
uv package manager
Google Cloud SDK (gcloud)
A Google Cloud project with billing enabled is also required. If you do not have one yet, it can be created at console.cloud.google.com.
If Agents CLI is not already installed on the development machine, it can be installed in a single command:
uvx google-agents-cli setup
Finally, we authenticate with Google Cloud and enable the APIs the agent will depend on at runtime:
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable aiplatform.googleapis.com run.googleapis.com artifactregistry.googleapis.com
Scaffolding and extension installation are the same operation. Rather than installing an extension first and then scaffolding a project, we point agents-cli create directly at the extension's template, pinned to a specific release tag:
agents-cli create my-agent \
    --agent google/agents-cli/extensions/langchain/template@v1.8.0 \
    -d cloud_run
cd my-agent && agents-cli install
The output confirms the scaffold succeeded:
Agents CLI v1.8.0
Fetching remote template: google/agents-cli/extensions/langchain/template@v1.8.0
> Verifying GCP credentials...
> ✓ Connected to project: your-project
✅ Success! Your agent project is ready.
The scaffolded project already contains an agents-cli-extension.yaml at its root, which is auto-loaded at project scope the next time any command is invoked. There is nothing to install manually, because the project itself is the extension's installation. A developer scaffolding a LangChain project does not need to know the Extension System exists. The command looks and feels like a native agents-cli create invocation that happens to produce a LangChain project instead of an ADK one.
Here's what the scaffolder produced:
my-agent/
├── agents-cli-extension.yaml      # auto-loaded project-scope overrides
├── agents-cli-manifest.yaml       # project configuration (deployment target, etc.)
├── GEMINI.md                      # project's coding-agent guide
├── langgraph.json                 # LangGraph dev-server configuration
├── pyproject.toml                 # langchain, langgraph, langchain-google-genai
├── Dockerfile                     # identical CMD to any ADK project
├── app/
│   ├── agent.py                   # exports root_agent: CompiledStateGraph
│   ├── fast_api_app.py            # exposes `app: FastAPI` on A2A
│   └── app_utils/
│       ├── a2a.py                 # LangGraphAgentExecutor and A2A routes
│       └── telemetry.py           # Cloud Trace and GenAI logging
├── scripts/
│   ├── run.py                     # drop-in replacement for `agents-cli run`
│   ├── eval_generate.py           # drop-in replacement for `agents-cli eval generate`
│   └── publish.py                 # Agent-Runtime-aware refusal wrapper
├── tests/
│   └── eval/datasets/basic-dataset.json
├── 
</kaynak_metni>
</haber>

<haber id="c007" puan="6" kaynak="GitHub Blog" tarih="2026-10-22">
Başlık: How bug bounty sharpens one researcher’s security skills
URL: https://github.blog/security/how-bug-bounty-sharpens-one-researchers-security-skills/
Özet: GitHub Bug Bounty ekibi bir araştırmacının yaklaşımını ve tavsiyelerini paylaştı.
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

<haber id="c008" puan="6" kaynak="GitHub Blog" tarih="2026-10-21">
Başlık: The bridge to agent-scale Git infrastructure
URL: https://github.blog/engineering/architecture-optimization/the-bridge-to-agent-scale-git-infrastructure/
Özet: GitHub, depolarının neredeyse tamamının bir kopyasını Azure'a taşıdığını anlattı.
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

<haber id="c068" puan="8" kaynak="Cloudflare Blog" tarih="2026-10-27">
Başlık: Introducing the Cloudflare PHP Capture the Flag challenge
URL: https://blog.cloudflare.com/php-ctf/
Özet: Cloudflare, Bug Bounty programına bağlı PHP Capture the Flag yarışması başlattı.
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
Awards require a materially distinct bypass method or exploit payload, even for the same PHP CVE. New flags, resets, attempt IDs, or cosmetic changes—including equivalent encodings—do not qualify as unique. Equivalent submissions are duplicates even if unfixed; only the first complete, reproducible HackerOne report is considered. Cloudflare makes final duplicate and reward decisions.
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

<haber id="c034" puan="7" kaynak="OpenAI News" tarih="2026-10-26">
Başlık: Working with academic communities to build scientific understanding
URL: https://openai.com/index/building-scientific-understanding-with-academic-communities
Diğer kaynaklar: https://openai.com/index/building-scientific-understanding-with-academic-communities/
Özet: OpenAI, modellerinin Kakeya sanısı, Üstel Zaman Hipotezi ve kuantum renk dinamiğinde sonuçlar ürettiğini paylaştı.
<kaynak_metni>
(metin alınamadı)
</kaynak_metni>
</haber>

<haber id="c050" puan="7" kaynak="Anthropic News" tarih="2026-10-22">
Başlık: Donating Agent Skills to the Agentic AI Foundation
URL: https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation
Özet: Anthropic, Agent Skills'i Agentic AI Foundation'a bağışladı.
<kaynak_metni>
Today, we’re donating Agent Skills, the open standard that gives AI agents specialized knowledge and workflows, to the Agentic AI Foundation (AAIF). More than 70 agent platforms, including ChatGPT, Cursor, GitHub Copilot, and VS Code, have integrated Agent Skills since we published the standard in December 2025.
Agent interoperability through simplicity
A skill is a folder containing a SKILL.md file that teaches an agent a specific task or domain, along with any scripts or reference material it needs. We developed skills while working on Claude Code. It handled general knowledge work well, but often lacked the procedural knowledge that real business tasks need. Within weeks of our October 2025 launch, developers published thousands of skills on GitHub and wrote loaders for Codex, Cursor, and OpenCode. We then published Agent Skills as an open standard, under its own GitHub organization and domain, so any agent could use it. So far, 1 million skills have been published and nearly 280 million installed.
Donating Agent Skills to AAIF
We’re committed to keeping Agent Skills open, community-driven, and vendor-neutral. Today, we are donating the standard to the Agentic AI Foundation (AAIF) under the Linux Foundation, which we co-founded with Block and OpenAI last year, and to which we donated the Model Context Protocol (MCP). The AAIF will provide a neutral home to the standard going forward, ensuring the community has a say in where Agent Skills go next.
We are donating the Agent Skills name and logo, the GitHub organization, and the agentskills.io domain. You can continue to use the standard or contribute to it without joining the AAIF.
Engineers from Anthropic, Google, OpenAI, and other companies will maintain the standard as individuals, with David Soria Parra and Mahesh Murag as Lead Maintainers.
What comes next
We’ve proposed starting with a roadmap covering versioned releases, a formal proposal process, and security guidance for people who write and install skills. As with MCP, the project will continue to prioritize community input and transparent decision-making. You can join the project’s Discord to give feedback on proposed specification changes.
Thank you to the developers who built with Agent Skills from the start, and to the teams who brought skills into their products. Read the specification at agentskills.io and join the discussion on GitHub.
</kaynak_metni>
</haber>

<haber id="c062" puan="7" kaynak="Webrazzi" tarih="2026-10-27">
Başlık: Siri AI, yıl sonuna kadar Türkçe dil desteği kazanacak
URL: https://webrazzi.com/2026/10/27/siri-ai-yil-sonuna-kadar-turkce-dil-destegi-kazanacak/
Özet: Apple, Siri AI'ın yıl sonuna kadar Türkçe desteği kazanacağını açıkladı.
<kaynak_metni>
Apple, yapay zeka destekli asistanı Siri AI'ın yıl sonuna kadar Türkçe dil desteği kazanacağını açıkladı. Türkçe ile birlikte geleneksel Çince, Norveççe ve Vietnamca da desteklenen dillere eklenecek.
Apple'ın açıklamasına göre Siri AI, 27.2 yazılım güncellemeleriyle birlikte Fransızca, İspanyolca, Japonca, Korece ve Portekizce dillerinde de kullanıma sunuldu. Asistan, eylül ayında beta sürümüyle ilk kez kullanıma açıldığında yalnızca İngilizceyi destekliyordu.
Şirket, Türkçe desteğinin hangi tarihte ve hangi yazılım güncellemesiyle sunulacağını ise paylaşmadı. 9to5Mac, yeni dillerin aralık ayında yayımlanması beklenen iOS 27.3 ile gelebileceğini belirtiyor. Ancak bu bilgi Apple tarafından doğrulanmış değil.
Apple Intelligence temel alınarak geliştirilen Siri AI, kullanıcıların mesaj, e-posta ve fotoğraflarındaki bilgileri kişisel bağlamı anlayarak bulmasına yardımcı oluyor. Asistan, uygulamalar arasında işlem yapabiliyor. Örneğin bir e-posta hazırlayabiliyor veya birden fazla fotoğrafı düzenleyip paylaşabiliyor. Ekran farkındalığı sayesinde ekrandaki içerikle ilgili soruları yanıtlayabiliyor ve işlemler gerçekleştirebiliyor.
Siri AI şu anda iOS 27.2, iPadOS 27.2, macOS 27.2, watchOS 27.2 ve visionOS 27.2’de beta sürümüyle kullanılabiliyor. Asistana erişmek için Apple Intelligence'ın etkin olduğu ve desteklenen bir dile ayarlanmış uyumlu bir cihaz gerekiyor. Apple, bazı özelliklerin her bölgede veya her dilde kullanılamayabileceğini de belirtiyor.
Apple Intelligence hâlihazırda Türkçeyi desteklese de bu destek, Siri AI'ın henüz Türkçe kullanılabildiği anlamına gelmiyor. Şirketin son duyurusuyla birlikte, Siri'nin yeni sürümüne yönelik Türkçe desteği için de yıl sonuna kadar bir takvim verilmiş oldu.
Görsel: ChatGPT
</kaynak_metni>
</haber>

<haber id="c010" puan="6" kaynak="Google Blog" tarih="2026-10-27">
Başlık: 8 examples of Gemini 4 Argon in action
URL: https://blog.google/products-and-platforms/products/gemini/gemini-4-argon-in-action/
Özet: Google, Gemini 4 Argon'un 8 kullanım örneğini paylaştı.
<kaynak_metni>
8 examples of Gemini 4 Argon in action
Our newest model, Gemini 4 Argon, was built to solve your hardest problems. By tackling complex, real-world tasks and taking on high-stakes work that used to require months of manual effort, it's fundamentally changing the way we work and build at Google — and it can do the same for you. Go ahead and hand over dense research materials, raw photos, and multi-step projects. Argon will reason, code, and coordinate tools to deliver what you need.
From deep research to interactive 3D design, here are eight examples of what our most intelligent model yet can do.
Handling complex tasks
Using advanced reasoning and multimodal capabilities, Gemini 4 Argon excels in deep comprehension and long-horizon workflows. From a short prompt and with zero assets or libraries, Argon wrote 5,000 lines of math to render a 3D sunlit library from scratch — and then made a video about the process.
Making interactive tools and playable 3D games
Googlers have used Argon to prototype complex 3D visualizations, high-fidelity games, and interactive animations. When prompted to build an app to overlay shapes across videos, Gemini 4 Argon in the Gemini app generated a custom audiovisual tool that traces musical scale lines from frame to frame. The motion of the video triggers musical notes, creating a dynamic audio composition.
To turn your world into an interactive game, start with photos of a physical space and our AI Studio how-to. We used Argon in Antigravity to orchestrate subagents, Blender MCP, and Nano Banana to transform pictures of a real desk into a playable 3D track.
Optimizing workflows
Argon combines frontier reasoning, deep visual perception, expanded knowledge, and stronger writing capabilities to help with high-stakes professional workflows. Given a custom slides template and more than 80,000 raw files from NASA — including weather logs and engineering, health, and science data accumulated across 72 flights on Mars — Gemini 4 Argon in Antigravity was able to parse information, organize insights, and turn it all into an executive-ready deck with clear visual narratives.
Building engaging visuals
Gemini 4 Argon is especially strong when work requires visual understanding. When prompted to make dense academic chapters come alive, Argon used Nano Banana and Veo to transform the scientific concepts in a PDF into an illustrated animation of key moments in the Gemini app.
To create an unforgettable science explainer in Antigravity, Argon generated a self-navigating 3D periodic table with animated atoms choreographed with frame-accurate audio timing to the rapid-fire lyrics of “The Elements” by Tom Lehrer.
Generating lifelike textures
Argon brings a deeper understanding of real-time 3D rendering, lighting and shading, and interactive physics simulation. This allows Argon in Antigravity to code a custom “fur engine” with studio-grade hair dynamics, generating visually rich fur that grows and moves as a character does.
We also used Argon in Antigravity to create an interactive musical “G” with fluid physics and reactive sound.
Gemini 4 Argon is now globally available for developers and enterprises via the API in AI Studio and Gemini platform, for Google AI Ultra and Pro subscribers in Google Antigravity, and Google AI Ultra and Pro subscribers in the Gemini app and AI Mode in Search.
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
  "segments": {
   "items": {
    "$ref": "#/$defs/Segment"
   },
   "title": "Segments",
   "type": "array"
  },
  "outro": {
   "description": "Kapanışta söylenecek kısa cümle, en fazla 10 kelime",
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
