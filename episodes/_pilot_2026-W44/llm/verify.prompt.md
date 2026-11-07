# Görev: verify

Yanıtı `episodes/2026-W44/llm/verify.response.json` dosyasına, aşağıdaki JSON şemasına uyan TEK bir JSON nesnesi olarak yaz.

## Sistem talimatı

Sen bağımsız bir doğrulama editörüsün (fact-checker). Bir teknoloji haber videosunun senaryosundaki iddiaları, verilen kaynak metinleriyle karşılaştırırsın.
- Yalnızca verilen kaynak metinlerine dayan; kendi bilgini kullanma. Kaynakta yoksa "not_found" de.
- Rakam, tarih, isim, sürüm numarası birebir eşleşmeli; yuvarlama veya birim farkı varsa "partial".
- evidence alanına kaynaktan birebir alıntı koy.
- Ayrıca anlatım (narration) ve student_take içinde olup claims listesinde bulunmayan olgusal ifadeleri "missed" listesine ekle ve onları da değerlendir.
- Her iddia için tam bir kayıt döndür.

## Girdi

Hook: Siri AI yıl sonuna kadar Türkçe öğreniyor!

<segment no="1">
Başlık: Siri AI'a Türkçe geliyor
Anlatım: Apple, yapay zekâ destekli asistanı Siri AI'ın yıl sonuna kadar Türkçe desteği kazanacağını açıkladı. Asistan eylülde beta olarak yalnızca İngilizceyle başlamıştı. Kesin tarih ise henüz paylaşılmadı.
Öğrenci notu: Uygulama geliştiriyorsan, Türkçe sesli asistan senaryolarını şimdiden planlamaya başla.
İddialar:
  [0] Apple, Siri AI'ın yıl sonuna kadar Türkçe desteği kazanacağını açıkladı  (kaynak: https://webrazzi.com/2026/10/27/siri-ai-yil-sonuna-kadar-turkce-dil-destegi-kazanacak/)
  [1] Siri AI eylülde beta olarak yalnızca İngilizceyle kullanıma açılmıştı  (kaynak: https://webrazzi.com/2026/10/27/siri-ai-yil-sonuna-kadar-turkce-dil-destegi-kazanacak/)
  [2] Türkçe desteğinin kesin tarihi paylaşılmadı  (kaynak: https://webrazzi.com/2026/10/27/siri-ai-yil-sonuna-kadar-turkce-dil-destegi-kazanacak/)
<kaynak url="https://webrazzi.com/2026/10/27/siri-ai-yil-sonuna-kadar-turkce-dil-destegi-kazanacak/">
Apple, yapay zeka destekli asistanı Siri AI'ın yıl sonuna kadar Türkçe dil desteği kazanacağını açıkladı. Türkçe ile birlikte geleneksel Çince, Norveççe ve Vietnamca da desteklenen dillere eklenecek.
Apple'ın açıklamasına göre Siri AI, 27.2 yazılım güncellemeleriyle birlikte Fransızca, İspanyolca, Japonca, Korece ve Portekizce dillerinde de kullanıma sunuldu. Asistan, eylül ayında beta sürümüyle ilk kez kullanıma açıldığında yalnızca İngilizceyi destekliyordu.
Şirket, Türkçe desteğinin hangi tarihte ve hangi yazılım güncellemesiyle sunulacağını ise paylaşmadı. 9to5Mac, yeni dillerin aralık ayında yayımlanması beklenen iOS 27.3 ile gelebileceğini belirtiyor. Ancak bu bilgi Apple tarafından doğrulanmış değil.
Apple Intelligence temel alınarak geliştirilen Siri AI, kullanıcıların mesaj, e-posta ve fotoğraflarındaki bilgileri kişisel bağlamı anlayarak bulmasına yardımcı oluyor. Asistan, uygulamalar arasında işlem yapabiliyor. Örneğin bir e-posta hazırlayabiliyor veya birden fazla fotoğrafı düzenleyip paylaşabiliyor. Ekran farkındalığı sayesinde ekrandaki içerikle ilgili soruları yanıtlayabiliyor ve işlemler gerçekleştirebiliyor.
Siri AI şu anda iOS 27.2, iPadOS 27.2, macOS 27.2, watchOS 27.2 ve visionOS 27.2’de beta sürümüyle kullanılabiliyor. Asistana erişmek için Apple Intelligence'ın etkin olduğu ve desteklenen bir dile ayarlanmış uyumlu bir cihaz gerekiyor. Apple, bazı özelliklerin her bölgede veya her dilde kullanılamayabileceğini de belirtiyor.
Apple Intelligence hâlihazırda Türkçeyi desteklese de bu destek, Siri AI'ın henüz Türkçe kullanılabildiği anlamına gelmiyor. Şirketin son duyurusuyla birlikte, Siri'nin yeni sürümüne yönelik Türkçe desteği için de yıl sonuna kadar bir takvim verilmiş oldu.
Görsel: ChatGPT
</kaynak>
</segment>

<segment no="2">
Başlık: Cloudflare'dan PHP CTF yarışması
Anlatım: Cloudflare, php2shell açıklarına karşı WAF korumasını sınamak için bir Capture the Flag yarışması başlattı. Amaç, korumayı aşıp sunucudaki flag dosyasını ele geçirmek. Yarışma, HackerOne üzerindeki Bug Bounty programıyla yürütülüyor.
Öğrenci notu: Güvenliğe ilgin varsa HackerOne hesabı aç, kuralları oku ve süre dolmadan dene.
İddialar:
  [0] Cloudflare, PHP Capture the Flag yarışması başlattı  (kaynak: https://blog.cloudflare.com/php-ctf/)
  [1] Yarışma php2shell açıklarına karşı WAF korumasını test ediyor  (kaynak: https://blog.cloudflare.com/php-ctf/)
  [2] Amaç WAF'ı aşıp /flag dosyasının içeriğini ele geçirmek  (kaynak: https://blog.cloudflare.com/php-ctf/)
  [3] Yarışma HackerOne üzerindeki Bug Bounty programıyla yürütülüyor ve süreli  (kaynak: https://blog.cloudflare.com/php-ctf/)
  [4] Hedef PHP 8.5.11 ve Apache 2 çalıştırıyor; kapsam yalnızca POST /php/*  (kaynak: https://blog.cloudflare.com/php-ctf/)
<kaynak url="https://blog.cloudflare.com/php-ctf/">
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
</kaynak>
</segment>

<segment no="3">
Başlık: Android'de rehber izni değişiyor
Anlatım: Yeni Android sürümünü hedefleyen uygulamalar, WRITE_CONTACTS izniyle rehbere doğrudan yazamayacak. Bunun yerine izin gerektirmeyen standart rehber intent'leri kullanılacak. Geniş erişim gereken uygulamalar için MANAGE_CONTACTS izni geliyor.
Öğrenci notu: Android uygulaman rehbere yazıyorsa, kodunu ACTION_INSERT intent'ine taşımaya başla.
İddialar:
  [0] Yeni Android sürümünü hedefleyen uygulamalar WRITE_CONTACTS izniyle rehbere doğrudan yazamayacak  (kaynak: https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android)
  [1] Standart rehber intent'leri (ACTION_INSERT, ACTION_EDIT, ACTION_INSERT_OR_EDIT) izin gerektirmeyecek  (kaynak: https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android)
  [2] Geniş erişim gereken uygulamalar için MANAGE_CONTACTS izni geliyor  (kaynak: https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android)
<kaynak url="https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android">
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
</kaynak>
</segment>

<segment no="4">
Başlık: Agent Skills artık bir vakfın
Anlatım: Anthropic, yapay zekâ ajanlarına yetenek kazandıran açık standart Agent Skills'i, Linux Foundation bünyesindeki Agentic AI Foundation'a bağışladı. Standardı ChatGPT, Cursor ve GitHub Copilot dahil 70'ten fazla platform kullanıyor.
Öğrenci notu: Bir SKILL.md dosyasıyla kendi ajan yeteneğini yaz, spesifikasyon agentskills.io'da.
İddialar:
  [0] Anthropic, Agent Skills standardını Agentic AI Foundation'a bağışladı  (kaynak: https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)
  [1] Agentic AI Foundation, Linux Foundation bünyesinde  (kaynak: https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)
  [2] ChatGPT, Cursor ve GitHub Copilot dahil 70'ten fazla platform Agent Skills'i entegre etti  (kaynak: https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)
  [3] Bir skill, SKILL.md dosyası içeren bir klasördür; spesifikasyon agentskills.io'da  (kaynak: https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)
<kaynak url="https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation">
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
