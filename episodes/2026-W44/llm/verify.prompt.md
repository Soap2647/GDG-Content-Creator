# Görev: verify

Yanıtı `episodes/2026-W44/llm/verify.response.json` dosyasına, aşağıdaki JSON şemasına uyan TEK bir JSON nesnesi olarak yaz.

## Sistem talimatı

Sen bağımsız bir doğrulama editörüsün (fact-checker). Bir teknoloji haber videosunun senaryosundaki iddiaları, verilen kaynak metinleriyle karşılaştırırsın.
- Yalnızca verilen kaynak metinlerine dayan; kendi bilgini kullanma. Kaynakta yoksa "not_found" de.
- Rakam, tarih, isim, sürüm numarası birebir eşleşmeli; yuvarlama veya birim farkı varsa "partial".
- evidence alanına kaynaktan birebir alıntı koy.
- Ayrıca anlatım (narration) ve student_take içinde olup claims listesinde bulunmayan olgusal ifadeleri "missed" listesine ekle ve onları da değerlendir.
- Hook, teaser, köprü (bridge), soru ve kapanışta segmentlerde desteklenmeyen bir olgu ya da sonda karşılığı olmayan bir vaat varsa onu da "missed" listesine (ilgili segmente) ekle.
- Her iddia için tam bir kayıt döndür.

## Girdi

Hook: Kritik tesislerde 1071 ve 1453 şifreleri bulundu!
Teaser: Dört haber var; sonuncusu senin başvurabileceğin bir fırsat.
Soru: Genie 4'le nasıl bir dünya kurardın? Yorumlara yaz.
Kapanış: Takip et, haftaya yeni gündemle buradayız.

<segment no="1">
Başlık: Kritik tesislerde şifre: 1071 ve 1453
Köprü: 
Anlatım: Bağımsız bir araştırmacı, Türkiye'deki kritik altyapılarda 1071 ve 1453 gibi şifreler kullanıldığını tespit etti. Bu zayıf parolalarla su pompaları dahil 430 sisteme erişildiği bildirildi.
Öğrenci notu: Kendi hesaplarında tahmin edilebilir şifre kullanma, iki adımlı doğrulamayı aç.
İddialar:
  [0] Bağımsız bir siber güvenlik araştırmacısı Türkiye'deki kritik altyapılarda zafiyet tespit etti  (kaynak: https://shiftdelete.net/turkiyede-kritik-altyapilarda-1071-ve-1453-sifreleri-kullaniliyor-risk-buyuk)
  [1] Sistemlerin giriş şifrelerinde 1071 ve 1453 gibi parolalar kullanılıyordu  (kaynak: https://shiftdelete.net/turkiyede-kritik-altyapilarda-1071-ve-1453-sifreleri-kullaniliyor-risk-buyuk)
  [2] Zayıf parolalarla su pompaları dahil 430 kritik sisteme erişim sağlandığı bildirildi  (kaynak: https://shiftdelete.net/turkiyede-kritik-altyapilarda-1071-ve-1453-sifreleri-kullaniliyor-risk-buyuk)
<kaynak url="https://shiftdelete.net/turkiyede-kritik-altyapilarda-1071-ve-1453-sifreleri-kullaniliyor-risk-buyuk">
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
</kaynak>
</segment>

<segment no="2">
Başlık: Cloudflare'den PHP CTF yarışması
Köprü: Peki savunmayı sen test etmek istersen?
Anlatım: Cloudflare, kasıtlı olarak açık bırakılmış bir PHP kurulumunu güvenlik duvarının arkasına koydu. Görev: korumayı aşıp flag dosyasını ele geçirmek. Yarışma sınırlı süreli, HackerOne'daki ödül programı üzerinden yürüyor.
Öğrenci notu: Katılmak için HackerOne hesabı gerekiyor; önce kuralları dikkatlice oku.
İddialar:
  [0] Cloudflare, kasıtlı olarak savunmasız bir PHP kurulumunu WAF'ının arkasına koydu  (kaynak: https://blog.cloudflare.com/php-ctf/)
  [1] Görev WAF korumalarını aşıp /flag dosyasının içeriğini ele geçirmek  (kaynak: https://blog.cloudflare.com/php-ctf/)
  [2] Yarışma sınırlı süreli ve Cloudflare'in HackerOne'daki Bug Bounty programı üzerinden yürüyor  (kaynak: https://blog.cloudflare.com/php-ctf/)
  [3] Katılımcıların HackerOne hesabı açması ve Bounty kurallarını kabul etmesi gerekiyor  (kaynak: https://blog.cloudflare.com/php-ctf/)
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
Awards require a materially distinct Firewall (WAF) bypass method, even for the same PHP CVE. Reports using the same Firewall-bypass mechanism are duplicates, regardless of differences in the PHP exploit, payload, RCE technique, or flag-recovery method. New flags, resets, attempt IDs, or cosmetic changes—including equivalent encodings—do not qualify as unique. Equivalent submissions are duplicates even if unfixed; only the first complete, reproducible HackerOne report is considered. Cloudflare makes final duplicate and reward decisions.
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
Başlık: Genie 4: Sesli ve yönetilebilir sanal dünyalar
Köprü: Güvenlikten çıkıp sanal dünyalara geçelim.
Anlatım: Google DeepMind, yeni dünya modeli Genie 4'ü duyurdu. Doğal dille sahneyi gerçek zamanlı yönetebiliyor, havayı değiştirip yeni karakter ekleyebiliyorsun. Her dünya kendi sesini de anında üretiyor.
Öğrenci notu: Şimdilik sınırlı test grubunda; geniş erişim için Google duyurularını takip et.
İddialar:
  [0] Google DeepMind yeni dünya modeli Genie 4'ü duyurdu  (kaynak: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/)
  [1] Genie 4'te sahneler doğal dille gerçek zamanlı yönlendirilebiliyor; hava değiştirilebiliyor, yeni karakterler eklenebiliyor  (kaynak: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/)
  [2] Her dünya ortam sesi, müzik ve diyalog dahil sesini anında üretiyor  (kaynak: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/)
  [3] Genie 4 şimdilik sınırlı bir güvenilir test grubuna açılıyor  (kaynak: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/)
<kaynak url="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/">
We’re announcing Genie 4, our new world model for real-time interactive simulation.
Today, we’re announcing our research on Genie 4, our new world model that brings unprecedented realism and native audio to real-time interactive simulation.
The Genie 4 model incorporates and builds on capabilities from the Gemini family: Gemini Omni anchors simulations in real-world appearance and behavior, while other Gemini models provide the complex reasoning needed to help maintain a simulation’s coherence and continuity.
With Genie 4, you can set an event in motion and steer scenes in real time using natural language, like moving the camera, changing the weather, or introducing new characters. Every world also generates native audio on the fly, including ambient sounds, music, and interactive dialogue.
Simulating the world is a crucial step toward AGI, enabling safe training environments for robots and agents, and amplifying creative tools across industries like filmmaking, journalism, gaming, and manufacturing.
We have started rolling out Genie 4 to a limited group of trusted testers. It’s coming soon to Google AI Ultra subscribers in Project Genie and early access partners in the Gemini API and AI Studio.
Explore the demos on the Google DeepMind blog.
</kaynak>
<kaynak url="https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/">
Acknowledgements
Genie 4 was made possible by core contributions from Hang Qi, Diego Rivas, Aleksander Hołyński, Inbar Mosseri, Jack Parker-Holder, Shlomi Fruchter, Tejas Kulkarni, James Assiene, Philip Ball, Jakob Bauer, Eddie Cao, Lucy Chai, Harris Chan, Kleopatra Chatziprimou, Hao Chen, Yoni Choukroun, Mark Collier, Enric Corona, Kurtis David, Ariel Ephrat, Maxime Gazeau, Ruiqi Gao, Chelsee Glover-Odom, Liangke Gui, Swaroop Guntupalli, Shan Han, Tingbo Hou, Jiri Hron, Hui Huang, Drew A. Hudson, Zhouyuan Huo, Linyi Jin, Christos Kaplanis, Dhrupad Karwa, Eunyoung Kim, Congtao Kuang, Eliot Laidlaw, José Lezama, Hao Li, Shuang Li, Yuchen Liu, Hanzi Mao, Mark Matthews, Matt McGill, Kay McKinney, Ricardo Monti, Mark Murphy, Joseph Ortiz, Roni Paiss, Frank Perbet, Ben Poole, Tal Reiss, Konstantinos Rematas, Guy Scully, Jeremy Shar, Shashank Shastry, Sri S, Omer Tov, Ruben Villegas, Andrey Voynov, Hongjie Wang, Luyu Wang, Kaustubh Sridhar, Mo Samsami, Stephen Spencer, Yufei Wang, Will Whitney, Rundi Wu, Joyce (Jingjing) Xie, Jesse Yin, Shiran Zada, Serena Zhang, Xiaofan Zhang, Zhengqi Li, Zhixing Zhang, Yuan Zhong, Shuo-yiin Chang, Dmitry Lagun, Ronny Huang, Yao Su, Ankush Gupta, Genzhi Ye, Haolin Jia, Weiqin Wang, Xi Xiong, Salah Zaiem, Carol Zheng, .
Genie 4 also required close collaborations across partner teams, we thank all our cross-functional partners that made this launch possible: Dina Bashkirova, Emil Bergner, Greta Borisko, Irina Blok, Melissa Byun, Gabe Clapper, Viral Carpenter, Michael Y. Chang, Maximo Cudich-Sieburger, Chloe Doan, Alisa Fortin, Shivani Ghanta, Vikram Gopali, Ezra Gorman, Khyatti Gupta, Sam Hasinoff, Philipp Henzler, Hector Hinestroza, Ed Hirst, Tyler Holland, Kristian Holsheimer, Tiffany Hu, Kapil Joshi, Randeep Katari, Pavan Kumar, Vikhyat Kumeria, Sam Kvaalen, Matthew Levine, Yinxiao Li, Yuchi Liu, Miao Luo, Nick Matarese, Kangfu Mei, Signe Nørly, Moises Oliveira, Eric Paskie, Manika Puri, Susanna Ricco, Andrey Ryabtsev, Cai Schumann, Nicole Brichtova, Andy Sekyere, Grace Shih, Melissa Smith, Duncan Noble Smith, Kenda Stewart, Rod Strougo, Jenn Sturgeon, Amy Zeng, Gaby Pearl, Eleanor Tomlinson, Kenyon Watson, Inês Ayer, Luke Talbot, Han-Yun Tsao, Guillaume Vernade, Karen Wang, Changchang Wu, Ian Wilkinson, Weijuan Xi, Jennifer Yick, Yunhan Zhao, Eric Zhang, Jason Zhang, Annie Zhou, James Zhou, Chris Walker, Alan Yam, Alex Chen, Cliff Lungaretti, Dan Motzenbecker, Kaloyan Kolev, Matthew Carey, Nate Zucker, Sam Lawton, Shashwath Santosh, Suz Chambers, Agrim Gupta.
Thanks to Raia Hadsell, Aäron van den Oord, Josh Woodward, Steve Seitz, Carlos Hernandez, Elias Roman, Jung E. Kim, Abhishek Bapna, Eli Collins, Tulsee Doshi, Carolina Parada, Jie Tan, Koray Kavukcuoglu and Demis Hassabis for their insightful guidance and support throughout the research process.
Lastly, we thank our trusted tester and early access users that have provided feedback to help guide our research forward.
</kaynak>
</segment>

<segment no="4">
Başlık: TÜBİTAK kış okulu: Başvurular açık
Köprü: Ve sona sakladığımız fırsat geldi.
Anlatım: TÜBİTAK, 6G ağları için kilit teknoloji olan Bütünleşik Algılama ve Haberleşme üzerine kış okulu düzenliyor. 23 ile 25 Kasım arasında Gebze'de; seçilenlere ücretsiz konaklama ve Türkiye içi ulaşım desteği var.
Öğrenci notu: Son başvuru 12 Kasım; yüz yüze öncelik lisansüstünde, çevrim içi katılıma da başvurabilirsin.
İddialar:
  [0] TÜBİTAK TBAE, Bütünleşik Algılama ve Haberleşme Kış Okulu düzenliyor  (kaynak: https://tubitak.gov.tr/tr/duyuru/butunlesik-algilama-ve-haberlesme-kis-okulu-2026-yili-basvurulari-basladi)
  [1] Bütünleşik Algılama ve Haberleşme 6G ağları için kilit bir teknoloji  (kaynak: https://tubitak.gov.tr/tr/duyuru/butunlesik-algilama-ve-haberlesme-kis-okulu-2026-yili-basvurulari-basladi)
  [2] Kış okulu 23-25 Kasım 2026'da Gebze'de  (kaynak: https://tubitak.gov.tr/tr/duyuru/butunlesik-algilama-ve-haberlesme-kis-okulu-2026-yili-basvurulari-basladi)
  [3] Seçilen katılımcılara ücretsiz konaklama ve Türkiye içi ulaşım desteği sağlanacak  (kaynak: https://tubitak.gov.tr/tr/duyuru/butunlesik-algilama-ve-haberlesme-kis-okulu-2026-yili-basvurulari-basladi)
  [4] Son başvuru tarihi 12 Kasım 2026  (kaynak: https://tubitak.gov.tr/tr/duyuru/butunlesik-algilama-ve-haberlesme-kis-okulu-2026-yili-basvurulari-basladi)
  [5] Yüz yüze katılımda yüksek lisans, doktora öğrencileri ve doktora sonrası araştırmacılara öncelik veriliyor  (kaynak: https://tubitak.gov.tr/tr/duyuru/butunlesik-algilama-ve-haberlesme-kis-okulu-2026-yili-basvurulari-basladi)
  [6] Zoom üzerinden çevrim içi katılım için de başvuru yapılabiliyor  (kaynak: https://tubitak.gov.tr/tr/duyuru/butunlesik-algilama-ve-haberlesme-kis-okulu-2026-yili-basvurulari-basladi)
  [7] Yüz yüze katılım kontenjanı 50 kişi  (kaynak: https://tubitak.gov.tr/tr/duyuru/butunlesik-algilama-ve-haberlesme-kis-okulu-2026-yili-basvurulari-basladi)
<kaynak url="https://tubitak.gov.tr/tr/duyuru/butunlesik-algilama-ve-haberlesme-kis-okulu-2026-yili-basvurulari-basladi">
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
