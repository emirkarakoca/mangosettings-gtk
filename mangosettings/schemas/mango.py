GROUPS=[ #thanks claude!

    {"title": "Blur", "items": [
        {"key": "blur", "type": "bool", "label": "Blur",
         "subtitle": "Pencerelerin saydam bölgelerine buzlu cam efekti uygular. Performans etkisi görecelidir, zayıf donanımda önerilmez.",
         "default": False},

        {"key": "blur_layer", "type": "bool", "label": "Katman (Layer) Blur",
         "subtitle": "Bar, panel, dock gibi katman yüzeylerinde blur uygular.",
         "default": False},

        {"key": "blur_optimized", "type": "bool", "label": "Optimize Blur",
         "subtitle": "Duvar kağıdını önbelleğe alır, GPU kullanımını ciddi oranda azaltır. Kapatılması GPU yükünü artırır. (Önerilir: açık)",
         "default": True},

        {"key": "blur_params_num_passes", "type": "int", "label": "Geçiş Sayısı",
         "subtitle": "Daha fazla geçiş = daha yumuşak blur, daha düşük performans.",
         "min": 1, "max": 10, "step": 1, "default": 2},

        {"key": "blur_params_radius", "type": "int", "label": "Yarıçap (Radius)",
         "subtitle": "Blur gücü / bulanıklık şiddeti.",
         "min": 0, "max": 50, "step": 1, "default": 5},

        {"key": "blur_params_noise", "type": "float", "label": "Gürültü Seviyesi",
         "subtitle": "Daha yüksek değer daha fazla görsel gren (grain) oluşturur.",
         "min": 0, "max": 1, "step": 0.01, "digits": 2, "default": 0.02},

        {"key": "blur_params_brightness", "type": "float", "label": "Parlaklık",
         "subtitle": "Blur arka planının parlaklık ayarı.",
         "min": 0, "max": 2, "step": 0.1, "digits": 1, "default": 0.9},

        {"key": "blur_params_contrast", "type": "float", "label": "Kontrast",
         "subtitle": "Blur arka planının kontrast ayarı.",
         "min": 0, "max": 2, "step": 0.1, "digits": 1, "default": 0.9},

        {"key": "blur_params_saturation", "type": "float", "label": "Doygunluk",
         "subtitle": "Blur arka planının renk doygunluğu ayarı.",
         "min": 0, "max": 2, "step": 0.1, "digits": 1, "default": 1.2},
    ]},

    {"title": "Gölgeler", "items": [
        {"key": "shadows", "type": "bool", "label": "Gölgeler",
         "subtitle": "Yüzen (floating) pencereleri arka plandan ayırt etmek için gölge ekler.",
         "default": False},

        {"key": "layer_shadows", "type": "bool", "label": "Katman Gölgeleri",
         "subtitle": "Bar, panel gibi katman yüzeylerine gölge ekler.",
         "default": False},

        {"key": "shadow_only_floating", "type": "bool", "label": "Sadece Yüzen Pencerelerde",
         "subtitle": "Gölgeyi yalnızca yüzen pencerelerde çizer, performanstan tasarruf sağlar.",
         "default": True},

        {"key": "shadows_size", "type": "int", "label": "Gölge Boyutu",
         "subtitle": "Gölgenin yayılma büyüklüğü.",
         "min": 0, "max": 50, "step": 1, "default": 10},

        {"key": "shadows_blur", "type": "int", "label": "Gölge Bulanıklığı",
         "subtitle": "Gölge kenarlarının yumuşaklık miktarı.",
         "min": 0, "max": 50, "step": 1, "default": 15},

        {"key": "shadows_position_x", "type": "int", "label": "Gölge X Konumu",
         "subtitle": "Gölgenin yatay eksende kayma miktarı.",
         "min": -50, "max": 50, "step": 1, "default": 0},

        {"key": "shadows_position_y", "type": "int", "label": "Gölge Y Konumu",
         "subtitle": "Gölgenin dikey eksende kayma miktarı.",
         "min": -50, "max": 50, "step": 1, "default": 0},

        {"key": "shadowscolor", "type": "color", "label": "Gölge Rengi",
         "subtitle": "Gölgenin rengi (ARGB, 0xRRGGBBAA formatında).",
         "default": "0x000000ff"},
    ]},

    {"title": "Opaklık ve Köşe Yarıçapı", "items": [
        {"key": "border_radius", "type": "int", "label": "Köşe Yarıçapı",
         "subtitle": "Pencere köşelerinin piksel cinsinden yuvarlaklık miktarı.",
         "min": 0, "max": 50, "step": 1, "default": 6},

        {"key": "border_radius_location_default", "type": "choice", "label": "Köşe Yarıçapı Konumu",
         "subtitle": "Yuvarlaklığın uygulanacağı köşe(ler).",
         "options": [
             {"value": 0, "label": "Tüm köşeler"},
             {"value": 1, "label": "Sol üst"},
             {"value": 2, "label": "Sağ üst"},
             {"value": 3, "label": "Sol alt"},
             {"value": 4, "label": "Sağ alt"},
             {"value": 5, "label": "En yakın köşe"},
         ], "default": 0},

        {"key": "no_radius_when_single", "type": "bool", "label": "Tekil Pencerede Köşe Yarıçapını Kapat",
         "subtitle": "Ekranda tek pencere varken köşe yuvarlaklığını devre dışı bırakır.",
         "default": False},

        {"key": "focused_opacity", "type": "float", "label": "Odaklı Pencere Opaklığı",
         "subtitle": "Aktif pencerenin saydamlık seviyesi.",
         "min": 0, "max": 1, "step": 0.05, "digits": 2, "default": 1.0},

        {"key": "unfocused_opacity", "type": "float", "label": "Odaksız Pencere Opaklığı",
         "subtitle": "Odaklanılmayan pencerelerin saydamlık seviyesi.",
         "min": 0, "max": 1, "step": 0.05, "digits": 2, "default": 1.0},
    ]},

    {"title": "Animasyonlar", "items": [
        {"key": "animations", "type": "bool", "label": "Animasyonlar",
         "subtitle": "Pencere açma/kapama/taşıma ve etiket geçiş animasyonlarını etkinleştirir.",
         "default": True},

        {"key": "layer_animations", "type": "bool", "label": "Katman Animasyonları",
         "subtitle": "Bar, panel gibi katman yüzeyleri için animasyon uygular.",
         "default": False},

        {"key": "animation_type_open", "type": "choice", "label": "Açılış Animasyon Türü",
         "subtitle": "Pencere açılırken kullanılacak animasyon.",
         "options": [
             {"value": "zoom", "label": "Yakınlaştırma (Zoom)"},
             {"value": "slide", "label": "Kayma (Slide)"},
             {"value": "fade", "label": "Solma (Fade)"},
             {"value": "none", "label": "Yok"},
         ], "default": "slide"},

        {"key": "animation_type_close", "type": "choice", "label": "Kapanış Animasyon Türü",
         "subtitle": "Pencere kapanırken kullanılacak animasyon.",
         "options": [
             {"value": "zoom", "label": "Yakınlaştırma (Zoom)"},
             {"value": "slide", "label": "Kayma (Slide)"},
             {"value": "fade", "label": "Solma (Fade)"},
             {"value": "none", "label": "Yok"},
         ], "default": "slide"},

        {"key": "layer_animation_type_open", "type": "choice", "label": "Katman Açılış Animasyonu",
         "subtitle": "Katman yüzeyi (bar, launcher vb.) açılırken kullanılacak animasyon.",
         "options": [
             {"value": "slide", "label": "Kayma (Slide)"},
             {"value": "zoom", "label": "Yakınlaştırma (Zoom)"},
             {"value": "fade", "label": "Solma (Fade)"},
             {"value": "none", "label": "Yok"},
         ], "default": "slide"},

        {"key": "layer_animation_type_close", "type": "choice", "label": "Katman Kapanış Animasyonu",
         "subtitle": "Katman yüzeyi kapanırken kullanılacak animasyon.",
         "options": [
             {"value": "slide", "label": "Kayma (Slide)"},
             {"value": "zoom", "label": "Yakınlaştırma (Zoom)"},
             {"value": "fade", "label": "Solma (Fade)"},
             {"value": "none", "label": "Yok"},
         ], "default": "slide"},

        {"key": "animation_fade_in", "type": "bool", "label": "Solarak Açılma (Fade-in)",
         "subtitle": "Pencere açılışında solma efektini etkinleştirir.",
         "default": True},

        {"key": "animation_fade_out", "type": "bool", "label": "Solarak Kapanma (Fade-out)",
         "subtitle": "Pencere kapanışında solma efektini etkinleştirir.",
         "default": True},

        {"key": "tag_animation_direction", "type": "choice", "label": "Etiket Animasyon Yönü",
         "subtitle": "Etiketler (tag) arası geçiş animasyonunun yönü.",
         "options": [
             {"value": 1, "label": "Yatay"},
             {"value": 0, "label": "Dikey"},
         ], "default": 1},

        {"key": "zoom_initial_ratio", "type": "float", "label": "Başlangıç Yakınlaştırma Oranı",
         "subtitle": "Zoom animasyonunun başladığı ölçek oranı.",
         "min": 0, "max": 1, "step": 0.05, "digits": 2, "default": 0.3},

        {"key": "zoom_end_ratio", "type": "float", "label": "Bitiş Yakınlaştırma Oranı",
         "subtitle": "Zoom animasyonunun bittiği ölçek oranı.",
         "min": 0, "max": 1, "step": 0.05, "digits": 2, "default": 0.8},

        {"key": "fadein_begin_opacity", "type": "float", "label": "Solma Başlangıç Opaklığı (Açılış)",
         "subtitle": "Fade-in animasyonunun başladığı opaklık seviyesi.",
         "min": 0, "max": 1, "step": 0.05, "digits": 2, "default": 0.5},

        {"key": "fadeout_begin_opacity", "type": "float", "label": "Solma Başlangıç Opaklığı (Kapanış)",
         "subtitle": "Fade-out animasyonunun başladığı opaklık seviyesi.",
         "min": 0, "max": 1, "step": 0.05, "digits": 2, "default": 0.8},

        {"key": "animation_duration_move", "type": "int", "label": "Taşıma Animasyonu Süresi",
         "subtitle": "Pencere taşınırken animasyon süresi (ms).",
         "min": 0, "max": 2000, "step": 10, "default": 500},

        {"key": "animation_duration_open", "type": "int", "label": "Açılış Animasyonu Süresi",
         "subtitle": "Pencere açılış animasyonu süresi (ms).",
         "min": 0, "max": 2000, "step": 10, "default": 400},

        {"key": "animation_duration_tag", "type": "int", "label": "Etiket Animasyonu Süresi",
         "subtitle": "Etiketler arası geçiş animasyonu süresi (ms).",
         "min": 0, "max": 2000, "step": 10, "default": 350},

        {"key": "animation_duration_close", "type": "int", "label": "Kapanış Animasyonu Süresi",
         "subtitle": "Pencere kapanış animasyonu süresi (ms).",
         "min": 0, "max": 2000, "step": 10, "default": 800},

        {"key": "animation_duration_focus", "type": "int", "label": "Odak Değişimi Animasyon Süresi",
         "subtitle": "Odak değişiminde opaklık geçiş animasyonunun süresi (ms).",
         "min": 0, "max": 2000, "step": 10, "default": 0},

        {"key": "animation_curve_open", "type": "text", "label": "Açılış Eğrisi (Bezier)",
         "subtitle": "Açılış animasyonu için cubic-bezier eğrisi (x1,y1,x2,y2).",
         "default": "0.46,1.0,0.29,1"},

        {"key": "animation_curve_move", "type": "text", "label": "Taşıma Eğrisi (Bezier)",
         "subtitle": "Taşıma animasyonu için cubic-bezier eğrisi.",
         "default": "0.46,1.0,0.29,1"},

        {"key": "animation_curve_tag", "type": "text", "label": "Etiket Eğrisi (Bezier)",
         "subtitle": "Etiket geçiş animasyonu için cubic-bezier eğrisi.",
         "default": "0.46,1.0,0.29,1"},

        {"key": "animation_curve_close", "type": "text", "label": "Kapanış Eğrisi (Bezier)",
         "subtitle": "Kapanış animasyonu için cubic-bezier eğrisi.",
         "default": "0.08,0.92,0,1"},

        {"key": "animation_curve_focus", "type": "text", "label": "Odak Eğrisi (Bezier)",
         "subtitle": "Odak değişimi animasyonu için cubic-bezier eğrisi.",
         "default": "0.46,1.0,0.29,1"},

        {"key": "animation_curve_opafadein", "type": "text", "label": "Solma Eğrisi (Açılış)",
         "subtitle": "Fade-in opaklık animasyonu için cubic-bezier eğrisi.",
         "default": "0.46,1.0,0.29,1"},

        {"key": "animation_curve_opafadeout", "type": "text", "label": "Solma Eğrisi (Kapanış)",
         "subtitle": "Fade-out opaklık animasyonu için cubic-bezier eğrisi.",
         "default": "0.5,0.5,0.5,0.5"},
    ]},

    {"title": "Scroller Düzeni", "items": [
        {"key": "scroller_structs", "type": "int", "label": "Kenar Boşluğu",
         "subtitle": "Pencere oranı 1 iken ekranın iki yanında bırakılan boşluk.",
         "min": 0, "max": 200, "step": 1, "default": 20},

        {"key": "scroller_default_proportion", "type": "float", "label": "Varsayılan Pencere Oranı",
         "subtitle": "Scroller düzeninde pencerenin varsayılan genişlik oranı.",
         "min": 0.1, "max": 1.0, "step": 0.05, "digits": 2, "default": 0.8},

        {"key": "scroller_focus_center", "type": "bool", "label": "Odağı Her Zaman Ortala",
         "subtitle": "Odaklanılan pencereyi her zaman ekranın ortasına getirir.",
         "default": False},

        {"key": "scroller_prefer_center", "type": "bool", "label": "Ortalamayı Tercih Et",
         "subtitle": "Son odaklanılan pencere ekran içindeyse ortalamaz; değilse odaklanılan pencereyi ortalar.",
         "default": False},

        {"key": "edge_scroller_pointer_focus", "type": "bool", "label": "Kenardaki Pencereyi Fare ile Odakla",
         "subtitle": "Pencere ekrana tam sığmasa bile fare hareketiyle odaklanılabilir.",
         "default": True},

        {"key": "scroller_ignore_proportion_single", "type": "bool", "label": "Tekil Pencerede Oranı Sabitle",
         "subtitle": "Etikette tek pencere varken otomatik boyut ayarını devre dışı bırakır.",
         "default": True},

        {"key": "scroller_default_proportion_single", "type": "float", "label": "Tekil Pencere Oranı",
         "subtitle": "Etikette tek pencere olduğunda kullanılan varsayılan oran.",
         "min": 0.1, "max": 1.0, "step": 0.05, "digits": 2, "default": 1.0},

        {"key": "scroller_proportion_preset", "type": "text", "label": "Oran Ön Ayarları",
         "subtitle": "Geçiş yapılabilecek pencere oranı ön ayarları (virgülle ayrılmış).",
         "default": "0.5,0.8,1.0"},
    ]},

    {"title": "Master-Stack Düzeni", "items": [
        {"key": "new_is_master", "type": "bool", "label": "Yeni Pencere Master Olsun",
         "subtitle": "Yeni açılan pencere otomatik olarak master alana geçer.",
         "default": True},

        {"key": "default_mfact", "type": "float", "label": "Master Alan Oranı",
         "subtitle": "Master alanın ekrana oranı.",
         "min": 0.1, "max": 0.9, "step": 0.05, "digits": 2, "default": 0.55},

        {"key": "default_nmaster", "type": "int", "label": "Master Pencere Sayısı",
         "subtitle": "Master alanda gösterilecek varsayılan pencere sayısı.",
         "min": 0, "max": 10, "step": 1, "default": 1},

        {"key": "smartgaps", "type": "bool", "label": "Akıllı Boşluklar",
         "subtitle": "Tek pencere varken kenar boşluklarını kaldırır.",
         "default": False},

        {"key": "center_master_overspread", "type": "bool", "label": "Master'ı Yayarak Ortala",
         "subtitle": "Stack'te pencere yokken master penceresini tüm ekrana yayar (yalnızca center_tile düzeninde).",
         "default": False},

        {"key": "center_when_single_stack", "type": "bool", "label": "Tekil Stack'te Ortala",
         "subtitle": "Stack'te tek pencere varken master'ı ortalar (yalnızca center_tile düzeninde).",
         "default": True},
    ]},

    {"title": "Genel Görünüm (Overview)", "items": [
        {"key": "enable_hotarea", "type": "bool", "label": "Sıcak Bölgeyi Etkinleştir",
         "subtitle": "Fare ekranın sol alt köşesine geldiğinde overview modunu açar/kapatır.",
         "default": True},

        {"key": "hotarea_size", "type": "int", "label": "Sıcak Bölge Boyutu",
         "subtitle": "Overview modunu tetikleyen köşe alanının piksel boyutu.",
         "min": 1, "max": 100, "step": 1, "default": 10},

        {"key": "ov_tab_mode", "type": "bool", "label": "Tab Modu",
         "subtitle": "Overview'da sıradan odak değiştirme ve mod tuşu bırakılınca çıkma davranışı.",
         "default": False},

        {"key": "overviewgappi", "type": "int", "label": "İç Boşluk",
         "subtitle": "Overview modunda pencereler arası iç boşluk.",
         "min": 0, "max": 100, "step": 1, "default": 5},

        {"key": "overviewgappo", "type": "int", "label": "Dış Boşluk",
         "subtitle": "Overview modunda ekran kenarındaki dış boşluk.",
         "min": 0, "max": 200, "step": 1, "default": 30},
    ]},

    {"title": "Çeşitli Ayarlar", "items": [
        {"key": "xwayland_persistence", "type": "bool", "label": "XWayland Kalıcılığı",
         "subtitle": "XWayland oturumunun kalıcılığını etkinleştirir (etkinleştirmek için oturumu yeniden başlatın).",
         "default": True},

        {"key": "syncobj_enable", "type": "bool", "label": "DRM SyncObj",
         "subtitle": "drm_syncobj zaman çizelgesi desteğini etkinleştirir, bazı oyunlardaki takılmaları azaltabilir (oturum yeniden başlatma gerektirir).",
         "default": False},

        {"key": "adaptive_sync", "type": "bool", "label": "Değişken Yenileme Hızı (VRR)",
         "subtitle": "Adaptive Sync / VRR desteğini etkinleştirir.",
         "default": False},

        {"key": "allow_shortcuts_inhibit", "type": "bool", "label": "Kısayolların Bastırılmasına İzin Ver",
         "subtitle": "Uygulamaların (örn. sanal makineler) kısayol tuşlarını geçici olarak devre dışı bırakmasına izin verir.",
         "default": True},

        {"key": "allow_tearing", "type": "choice", "label": "Ekran Yırtılmasına (Tearing) İzin Ver",
         "subtitle": "VSync kapalıymış gibi davranarak gecikmeyi azaltır (oyun modu).",
         "options": [
             {"value": 0, "label": "Kapalı"},
             {"value": 1, "label": "Açık"},
             {"value": 2, "label": "Sadece Tam Ekran"},
         ], "default": 0},

        {"key": "allow_lock_transparent", "type": "bool", "label": "Şeffaf Kilit Ekranı",
         "subtitle": "Kilit ekranının saydam olmasına izin verir.",
         "default": False},

        {"key": "axis_bind_apply_timeout", "type": "int", "label": "Kaydırma Algılama Aralığı",
         "subtitle": "Ardışık fare tekerleği hareketlerinin algılanma aralığı (ms).",
         "min": 0, "max": 1000, "step": 10, "default": 100},

        {"key": "axis_scroll_factor", "type": "float", "label": "Kaydırma Hız Çarpanı",
         "subtitle": "Fare tekerleği ile kaydırma hızı çarpanı.",
         "min": 0.1, "max": 10.0, "step": 0.1, "digits": 1, "default": 1.0},

        {"key": "focus_on_activate", "type": "bool", "label": "Etkinleşince Odaklan",
         "subtitle": "Uygulama 'activate' isteği gönderdiğinde pencereyi odaklar.",
         "default": True},

        {"key": "idleinhibit_ignore_visible", "type": "bool", "label": "Görünmez Pencereler Boşta Kalmayı Engelleyebilsin",
         "subtitle": "Görünür olmayan istemcilerin de ekranın kararmasını engellemesine izin verir.",
         "default": False},

        {"key": "sloppyfocus", "type": "bool", "label": "Fareyi Takip Eden Odak",
         "subtitle": "Fare imleci üzerine geldiğinde pencereyi otomatik odaklar.",
         "default": True},

        {"key": "warpcursor", "type": "bool", "label": "Odak Değişince İmleci Taşı",
         "subtitle": "Odak değiştiğinde fare imlecini yeni pencereye taşır.",
         "default": True},

        {"key": "drag_corner", "type": "choice", "label": "Sürükleme Köşesi",
         "subtitle": "Yüzen pencere yeniden boyutlandırılırken tutulacak köşe.",
         "options": [
             {"value": 0, "label": "Sol Üst"},
             {"value": 1, "label": "Sağ Üst"},
             {"value": 2, "label": "Sol Alt"},
             {"value": 3, "label": "Sağ Alt"},
             {"value": 4, "label": "En Yakın Köşe"},
         ], "default": 3},

        {"key": "drag_warp_cursor", "type": "bool", "label": "Sürüklerken İmleci Köşeye Taşı",
         "subtitle": "Yüzen pencere sürüklenirken imleci köşeye ışınlar.",
         "default": True},

        {"key": "focus_cross_monitor", "type": "bool", "label": "Monitörler Arası Odaklanma",
         "subtitle": "Odak değiştirme komutlarının başka monitördeki pencerelere de geçmesine izin verir.",
         "default": False},

        {"key": "exchange_cross_monitor", "type": "bool", "label": "Monitörler Arası Pencere Değişimi",
         "subtitle": "İki farklı monitördeki pencerelerin yer değiştirmesine izin verir.",
         "default": False},

        {"key": "scratchpad_cross_monitor", "type": "bool", "label": "Ortak Scratchpad",
         "subtitle": "Tüm monitörlerin aynı scratchpad'i paylaşmasını sağlar.",
         "default": False},

        {"key": "focus_cross_tag", "type": "bool", "label": "Etiketler Arası Odaklanma",
         "subtitle": "Odak değiştirme komutlarının farklı etiketlerdeki pencerelere de geçmesine izin verir.",
         "default": False},

        {"key": "view_current_to_back", "type": "bool", "label": "Mevcut Etikete Otomatik Dönüş",
         "subtitle": "Mevcut etiketi tekrar görüntülemek, önceki görüntülenen etikete otomatik döner.",
         "default": True},

        {"key": "enable_floating_snap", "type": "bool", "label": "Yüzen Pencere Yapışması",
         "subtitle": "Yüzen pencerelerin kenarlara/diğer pencerelere yapışmasını etkinleştirir.",
         "default": False},

        {"key": "snap_distance", "type": "int", "label": "Yapışma Mesafesi",
         "subtitle": "Yapışmayı tetikleyen maksimum piksel mesafesi.",
         "min": 0, "max": 200, "step": 1, "default": 30},

        {"key": "cursor_size", "type": "int", "label": "İmleç Boyutu",
         "subtitle": "Fare imlecinin piksel boyutu.",
         "min": 8, "max": 128, "step": 1, "default": 24},

        {"key": "cursor_theme", "type": "text", "label": "İmleç Teması",
         "subtitle": "Kullanılacak imleç temasının adı (boş bırakılırsa sistem varsayılanı kullanılır).",
         "default": ""},

        {"key": "no_border_when_single", "type": "bool", "label": "Tekil Pencerede Kenarlığı Kaldır",
         "subtitle": "Etikette tek pencere varken kenarlığı çizmez.",
         "default": False},

        {"key": "cursor_hide_timeout", "type": "int", "label": "İmleci Otomatik Gizleme Süresi",
         "subtitle": "Belirtilen saniye boyunca hareket olmazsa imleci gizler (0: devre dışı).",
         "min": 0, "max": 9999, "step": 1, "default": 0},

        {"key": "drag_tile_to_tile", "type": "bool", "label": "Döşenmiş Pencereleri Sürükleyerek Takas Et",
         "subtitle": "Döşenmiş bir pencereyi başka bir döşenmiş pencerenin üzerine sürükleyerek yerlerini değiştirir.",
         "default": False},

        {"key": "single_scratchpad", "type": "bool", "label": "Tek Seferde Tek Scratchpad",
         "subtitle": "Aynı anda yalnızca bir scratchpad'in (isimli ya da normal) görünmesine izin verir.",
         "default": True},

        {"key": "circle_layout", "type": "text", "label": "Döngü Düzenleri",
         "subtitle": "switch_layout komutuyla geçiş yapılacak düzenler, virgülle ayrılmış (örn. tile,grid,scroller). Boşsa tüm düzenler arasında geçiş yapılır.",
         "default": ""},
    ]},

    {"title": "Klavye", "items": [
        {"key": "repeat_rate", "type": "int", "label": "Tekrar Hızı",
         "subtitle": "Tuş basılı tutulduğunda saniyedeki tekrar sayısı.",
         "min": 1, "max": 100, "step": 1, "default": 25},

        {"key": "repeat_delay", "type": "int", "label": "Tekrar Gecikmesi",
         "subtitle": "Tuş tekrarının başlamasından önceki gecikme (ms).",
         "min": 0, "max": 2000, "step": 10, "default": 600},

        {"key": "numlockon", "type": "bool", "label": "Başlangıçta Num Lock",
         "subtitle": "Mango başlarken Num Lock durumu.",
         "default": True},
    ]},

    {"title": "Touchpad ve Fare", "items": [
        {"key": "disable_trackpad", "type": "bool", "label": "Touchpad'i Devre Dışı Bırak",
         "subtitle": "Dahili touchpad'i tamamen devre dışı bırakır.",
         "default": False},

        {"key": "tap_to_click", "type": "bool", "label": "Dokunarak Tıklama",
         "subtitle": "Touchpad'e dokunarak tıklama yapılmasını sağlar.",
         "default": True},

        {"key": "tap_and_drag", "type": "bool", "label": "Dokun ve Sürükle",
         "subtitle": "Dokunarak öğe seçip sürüklemeyi etkinleştirir.",
         "default": True},

        {"key": "drag_lock", "type": "bool", "label": "Sürükleme Kilidi",
         "subtitle": "Parmağı kaldırdıktan sonra kısa süre sürüklemeye devam etmeyi sağlar.",
         "default": True},

        {"key": "trackpad_natural_scrolling", "type": "bool", "label": "Touchpad'de Doğal Kaydırma",
         "subtitle": "Kaydırma yönünü tersine çevirir (içerik parmakla aynı yönde hareket eder).",
         "default": False},

        {"key": "disable_while_typing", "type": "bool", "label": "Yazarken Touchpad'i Devre Dışı Bırak",
         "subtitle": "Klavyeden yazarken touchpad'i geçici olarak devre dışı bırakır.",
         "default": True},

        {"key": "left_handed", "type": "bool", "label": "Solak Modu",
         "subtitle": "Fare düğmelerini solak kullanım için ters çevirir.",
         "default": False},

        {"key": "middle_button_emulation", "type": "bool", "label": "Orta Tuş Emülasyonu",
         "subtitle": "Sol ve sağ tuşa aynı anda basarak orta tık simüle edilmesini sağlar.",
         "default": False},

        {"key": "swipe_min_threshold", "type": "int", "label": "Minimum Kaydırma Eşiği",
         "subtitle": "Bir kaydırma hareketinin algılanması için gereken minimum eşik değeri.",
         "min": 0, "max": 100, "step": 1, "default": 20},

        {"key": "mouse_natural_scrolling", "type": "bool", "label": "Farede Doğal Kaydırma",
         "subtitle": "Harici farenin kaydırma yönünü tersine çevirir.",
         "default": False},

        {"key": "accel_profile", "type": "choice", "label": "İmleç Hızlanma Profili",
         "subtitle": "Fare/touchpad imleç hızlanma davranışı.",
         "options": [
             {"value": 0, "label": "Hızlanma Yok"},
             {"value": 1, "label": "Sabit (Flat)"},
             {"value": 2, "label": "Uyarlanabilir (Adaptive)"},
         ], "default": 2},

        {"key": "accel_speed", "type": "float", "label": "Hızlanma Miktarı",
         "subtitle": "İmleç hızlanma seviyesi.",
         "min": -1.0, "max": 1.0, "step": 0.05, "digits": 2, "default": 0.0},

        {"key": "scroll_method", "type": "choice", "label": "Kaydırma Yöntemi",
         "subtitle": "Touchpad üzerinde kaydırmanın nasıl algılanacağı.",
         "options": [
             {"value": 0, "label": "Yok"},
             {"value": 1, "label": "İki Parmak"},
             {"value": 2, "label": "Kenar"},
             {"value": 4, "label": "Tuşla"},
         ], "default": 1},

        {"key": "click_method", "type": "choice", "label": "Tıklama Yöntemi",
         "subtitle": "Touchpad üzerinde tıklamanın nasıl tetikleneceği.",
         "options": [
             {"value": 0, "label": "Yok"},
             {"value": 1, "label": "Buton Alanları"},
             {"value": 2, "label": "Parmak Sayısı (Clickfinger)"},
         ], "default": 1},

        {"key": "send_events_mode", "type": "choice", "label": "Olay Gönderme Modu",
         "subtitle": "Cihazdan olay gönderilme davranışı.",
         "options": [
             {"value": 0, "label": "Etkin"},
             {"value": 1, "label": "Devre Dışı"},
             {"value": 2, "label": "Harici Fare Varken Devre Dışı"},
         ], "default": 0},

        {"key": "button_map", "type": "choice", "label": "Parmak-Tuş Eşleşmesi",
         "subtitle": "1/2/3 parmakla dokunmanın hangi fare tuşuna karşılık geleceği.",
         "options": [
             {"value": 0, "label": "Sol / Sağ / Orta"},
             {"value": 1, "label": "Sol / Orta / Sağ"},
         ], "default": 0},
    ]},

    {"title": "Görünüm", "items": [
        {"key": "gappih", "type": "int", "label": "Yatay İç Boşluk",
         "subtitle": "Pencereler arasındaki yatay boşluk.",
         "min": 0, "max": 100, "step": 1, "default": 5},

        {"key": "gappiv", "type": "int", "label": "Dikey İç Boşluk",
         "subtitle": "Pencereler arasındaki dikey boşluk.",
         "min": 0, "max": 100, "step": 1, "default": 5},

        {"key": "gappoh", "type": "int", "label": "Yatay Dış Boşluk",
         "subtitle": "Ekran kenarı ile pencereler arasındaki yatay boşluk.",
         "min": 0, "max": 100, "step": 1, "default": 10},

        {"key": "gappov", "type": "int", "label": "Dikey Dış Boşluk",
         "subtitle": "Ekran kenarı ile pencereler arasındaki dikey boşluk.",
         "min": 0, "max": 100, "step": 1, "default": 10},

        {"key": "scratchpad_width_ratio", "type": "float", "label": "Scratchpad Genişlik Oranı",
         "subtitle": "Scratchpad penceresinin ekran genişliğine oranı.",
         "min": 0.1, "max": 1.0, "step": 0.05, "digits": 2, "default": 0.8},

        {"key": "scratchpad_height_ratio", "type": "float", "label": "Scratchpad Yükseklik Oranı",
         "subtitle": "Scratchpad penceresinin ekran yüksekliğine oranı.",
         "min": 0.1, "max": 1.0, "step": 0.05, "digits": 2, "default": 0.9},

        {"key": "borderpx", "type": "int", "label": "Kenarlık Kalınlığı",
         "subtitle": "Pencere kenarlığının piksel cinsinden kalınlığı.",
         "min": 0, "max": 20, "step": 1, "default": 4},

        {"key": "rootcolor", "type": "color", "label": "Arka Plan Rengi",
         "subtitle": "Kök pencere (masaüstü) arka plan rengi.",
         "default": "0x201b14ff"},

        {"key": "bordercolor", "type": "color", "label": "Kenarlık Rengi",
         "subtitle": "Odaklanılmayan pencerelerin kenarlık rengi.",
         "default": "0x444444ff"},

        {"key": "focuscolor", "type": "color", "label": "Odak Rengi",
         "subtitle": "Odaklanılan pencerenin kenarlık rengi.",
         "default": "0xad741fff"},

        {"key": "maximizescreencolor", "type": "color", "label": "Tam Ekran Kenarlık Rengi",
         "subtitle": "Ekranı kaplamış (maximize) pencerenin kenarlık rengi.",
         "default": "0x89aa61ff"},

        {"key": "urgentcolor", "type": "color", "label": "Acil Pencere Rengi",
         "subtitle": "Dikkat isteyen (urgent) pencerenin kenarlık rengi.",
         "default": "0xad401fff"},

        {"key": "scratchpadcolor", "type": "color", "label": "Scratchpad Rengi",
         "subtitle": "Scratchpad penceresinin kenarlık rengi.",
         "default": "0x516c93ff"},

        {"key": "globalcolor", "type": "color", "label": "Global Pencere Rengi",
         "subtitle": "Global (tüm etiketlerde görünen) pencerenin kenarlık rengi.",
         "default": "0xb153a7ff"},

        {"key": "overlaycolor", "type": "color", "label": "Overlay Pencere Rengi",
         "subtitle": "En üstte sabit kalan (overlay) pencerenin kenarlık rengi.",
         "default": "0x14a57cff"},
    ]},

    {"title": "Klavye Düzeni ve Giriş Yöntemi", "items": [
        {"key": "xkb_rules_rules", "type": "text", "label": "XKB Kural Seti",
         "subtitle": "Klavye eşleme kural setinin adı (örn. evdev, base). Genelde sistem tarafından otomatik algılanır, elle değiştirmeye gerek yoktur.",
         "default": ""},

        {"key": "xkb_rules_model", "type": "text", "label": "Klavye Modeli",
         "subtitle": "Fiziksel klavye donanım modeli (örn. pc104, macbook).",
         "default": ""},

        {"key": "xkb_rules_layout", "type": "text", "label": "Klavye Düzeni",
         "subtitle": "Ülke/bölge klavye kodu (örn. us, tr, de). Birden fazla düzen virgülle ayrılarak yazılabilir.",
         "default": "us"},

        {"key": "xkb_rules_variant", "type": "text", "label": "Düzen Varyantı",
         "subtitle": "Düzen varyantı (örn. dvorak, colemak, intl, f klavye için 'f').",
         "default": ""},

        {"key": "xkb_rules_options", "type": "text", "label": "XKB Seçenekleri",
         "subtitle": "Ek klavye seçenekleri (örn. ctrl:nocaps, grp:lalt_lshift_toggle - düzenler arası geçiş tuşu).",
         "default": ""},
    ]},
]