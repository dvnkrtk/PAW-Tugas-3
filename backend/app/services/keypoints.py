def extract_key_points(text: str) -> str:
    text_lower = text.lower()
    points = []

    # Produk
    if "bagus" in text_lower or "baik" in text_lower or "berkualitas" in text_lower:
        points.append("Produk berkualitas")
    if "jelek" in text_lower or "buruk" in text_lower:
        points.append("Produk kurang memuaskan")

    # Pengiriman
    if "cepat" in text_lower:
        points.append("Pengiriman cepat")
    if "lama" in text_lower or "lambat" in text_lower:
        points.append("Pengiriman lambat")

    # Harga
    if "murah" in text_lower:
        points.append("Harga terjangkau")
    if "mahal" in text_lower:
        points.append("Harga mahal")

    if not points:
        points.append("Tidak ada poin penting terdeteksi")

    return "\n".join(f"- {p}" for p in points)
