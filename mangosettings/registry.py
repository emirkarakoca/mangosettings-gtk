PAGES = [
    {
        "id": "general",
        "name": "Genel",
        "icon": "preferences-system-symbolic",
        "category": "Sistem",
        "kind": "static"
    },
    {
        "id": "apps",
        "name": "Uygulamalar",
        "icon": "view-grid-symbolic",
        "category": "Sistem",
        "kind": "service"
    },
    {
        "id": "bluetooth",
        "name": "Bluetooth",
        "icon": "bluetooth-symbolic",
        "category": "Sistem",
        "kind": "service"
    },
    {
        "id": "sound",
        "name": "Ses",
        "icon": "audio-volume-high-symbolic",
        "category": "Sistem",
        "kind": "service"
    },
    {
        "id": "power",
        "name": "Güç",
        "icon": "battery-symbolic",
        "category": "Sistem",
        "kind": "service"
    },
    {
        "id": "display",
        "name": "Ekran",
        "icon": "video-display-symbolic",
        "category": "Sistem",
        "kind": "schema"
    },
    {
        "id": "keyboard",
        "name": "Klavye",
        "icon": "input-keyboard-symbolic",
        "category": "Sistem",
        "kind": "schema"
    },
    {
        "id": "shortcuts",
        "name": "Kısayollar",
        "icon": "preferences-desktop-keyboard-shortcuts-symbolic",
        "category": "Sistem",
        "kind": "schema"
    },
    {
        "id": "mouse",
        "name": "Fare",
        "icon": "input-mouse-symbolic",
        "category": "Sistem",
        "kind": "schema"
    },
    {
        "id": "appearance",
        "name": "Görünüm",
        "icon": "preferences-desktop-appearance-symbolic",
        "category": "Kişiselleştirme",
        "kind": "schema"
    },
    {
        "id": "animations",
        "name": "Animasyonlar",
        "icon": "preferences-other-symbolic",
        "category": "Kişiselleştirme",
        "kind": "schema"
    },
    {
        "id": "wallpaper",
        "name": "Duvar Kağıdı",
        "icon": "preferences-desktop-wallpaper-symbolic",
        "category": "Kişiselleştirme",
        "kind": "service"
    },
    {
        "id": "layout",
        "name": "Pencere Düzeni",
        "icon": "view-grid-symbolic",
        "category": "Pencere Yönetimi",
        "kind": "schema"
    },
    {
        "id": "overview",
        "name": "Genel Görünüm",
        "icon": "view-fullscreen-symbolic",
        "category": "Pencere Yönetimi",
        "kind": "schema"
    },
    {
        "id": "window-rules",
        "name": "Pencere Kuralları",
        "icon": "preferences-other-symbolic",
        "category": "Pencere Yönetimi",
        "kind": "schema"
    },
    {
        "id": "layer-rules",
        "name": "Layer Kuralları",
        "icon": "preferences-other-symbolic",
        "category": "Pencere Yönetimi",
        "kind": "schema"
    },
    {
        "id": "tag-rules",
        "name": "Tag Kuralları",
        "icon": "preferences-other-symbolic",
        "category": "Pencere Yönetimi",
        "kind": "schema"
    },
    {
        "id": "misc",
        "name": "Çeşitli Ayarlar",
        "icon": "applications-engineering-symbolic",
        "category": "Gelişmiş",
        "kind": "schema"
    },
    {
        "id": "about",
        "name": "Hakkında",
        "icon": "info-outline-symbolic",
        "category": "Bilgi",
        "kind": "service"
    }
]

def get_categories():
    categories = {}
    for page in PAGES:
        category = page["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(
            (
                page["id"],
                page["name"],
                page["icon"]
            )
        )
    return list(categories.items())