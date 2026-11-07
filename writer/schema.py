"""Bölüm senaryosunun şeması. Claude çıktısı bu modellerle doğrulanır; video adımı aynı alanları okur."""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

VisualComponent = Literal["HeadlineCard", "StatCounter", "MiniChart", "CodeBlock", "Terminal", "SourceScreenshot"]


class Visual(BaseModel):
    """Bir haber bloğunda gösterilecek görsel. Yalnızca seçilen component'in alanları doldurulur."""

    component: VisualComponent
    # StatCounter
    stat_value: float | None = Field(None, description="Kaynakta geçen sayı; yalnızca kaynakta varsa")
    stat_prefix: str | None = Field(None, description="ör. '$' veya ''")
    stat_suffix: str | None = Field(None, description="ör. ' milyar $', '%', ' GB'")
    stat_label: str | None = Field(None, description="Sayının ne olduğu, Türkçe, en fazla 6 kelime")
    # MiniChart
    chart_title: str | None = None
    chart_labels: list[str] | None = None
    chart_values: list[float] | None = Field(None, description="Kaynakta geçen değerler; uydurma yok")
    chart_unit: str | None = None
    # CodeBlock / Terminal
    code_language: str | None = Field(None, description="ör. 'bash', 'python', 'kotlin'")
    code_lines: list[str] | None = Field(None, description="En fazla 6 kısa satır; kaynaktaki komut/kod veya kurulum komutu")
    # SourceScreenshot
    screenshot_url: str | None = Field(None, description="Ekran görüntüsü alınacak kaynak URL (sources listesinden)")


class Claim(BaseModel):
    text: str = Field(description="Anlatımdaki tek bir olgusal iddia (rakam, isim, tarih, özellik)")
    source_url: str = Field(description="İddiayı destekleyen kaynak URL; sources listesinden biri olmalı")
    uncertain: bool = Field(description="Kaynak bunu açıkça söylemiyorsa veya yoruma dayanıyorsa true")


class Segment(BaseModel):
    bridge: str = Field("", description="Haberden önce söylenen bağlaç cümlesi, en fazla 7 kelime; önceki habere/izleyiciye bağlar. "
                                        "Yeni olgu içermez. ör. 'Güvenlik demişken, asıl tehlike burada.'")
    headline: str = Field(description="Ekranda görünecek başlık, en fazla 8 kelime")
    narration: str = Field(description="Seslendirilecek haber metni; doğal konuşma Türkçesi, kısa cümleler")
    student_take: str = Field(description="'Bu senin için ne demek?' — somut eylem: başvuru tarihi, kullanılabilecek araç, kariyer etkisi")
    visuals: list[Visual] = Field(description="2-4 görsel; ilk görsel HeadlineCard")
    sources: list[str] = Field(description="Kaynak URL listesi")
    claims: list[Claim] = Field(description="narration ve student_take içindeki tüm olgusal iddialar")


class Script(BaseModel):
    hook: str = Field(description="İlk 2 saniyede ekranda/seste: haftanın en çarpıcı tek cümlesi, en fazla 8 kelime")
    teaser: str = Field("", description="Kancadan hemen sonra merak boşluğu açan cümle, en fazla 12 kelime; "
                                        "sona kalan haberi ima eder, yeni olgu içermez")
    segments: list[Segment]
    question: str = Field("", description="İzleyiciye yorumda cevaplayacağı soru, en fazla 10 kelime")
    outro: str = Field(description="Kapanışta söylenecek kısa cümle, en fazla 8 kelime")


def word_count(script: Script) -> int:
    parts = [script.hook, script.teaser, script.question, script.outro] + [
        p for s in script.segments for p in (s.bridge, s.narration, s.student_take)]
    return sum(len(p.split()) for p in parts)
