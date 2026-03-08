# Contribution Guide

Terima kasih atas minat kontribusi ke Python Knowledge Universe.

## Jenis Kontribusi

- perbaikan typo dan kejelasan bahasa
- penambahan materi atau contoh kode
- perbaikan struktur dokumen
- pembaruan referensi resmi Python

## Standar Penulisan

- gunakan bahasa yang jelas, ringkas, dan konsisten
- prioritaskan akurasi berdasarkan sumber resmi
- sertakan contoh kode yang mudah diuji
- gunakan penamaan file snake_case

## Struktur Pull Request

Setiap pull request sebaiknya berisi:

1. ringkasan perubahan
2. alasan perubahan
3. dampak ke bagian lain (jika ada)
4. checklist validasi sederhana

## Checklist Sebelum PR

- [ ] tautan internal tidak rusak
- [ ] format markdown rapi
- [ ] istilah konsisten dengan `glossary.md`
- [ ] referensi teknis valid
- [ ] `CHANGELOG.md` yang relevan sudah diperbarui

## Konvensi Konten Core

- satu folder mewakili satu buku/topik besar
- setiap folder punya `README.md` sebagai peta materi
- materi turunan menggunakan urutan numerik (`01_`, `02_`, dst)
- setiap buku Core wajib punya `CHANGELOG.md`

## Konvensi Konten Specialization

- setiap specialization punya README sendiri
- setiap domain specialization berada di `specializations/<domain>/`
- buku di dalam domain menggunakan folder bernomor, contoh `specializations/ai-engineering/01_llm_fundamentals/`
- setiap folder buku wajib punya `README.md` sebagai peta isi buku
- setiap folder buku wajib punya `CHANGELOG.md`
- urutan buku menggunakan prefix numerik (`01_`, `02_`, dst)
- jelaskan prasyarat Core yang dibutuhkan
- bedakan materi konsep, praktik, dan project

## Konvensi Kode Buku

Gunakan kode unik per buku agar tracking perubahan konsisten.

- Core: `CORE-01`, `CORE-02`, ..., `CORE-15`
- Specialization Web: `SPEC-WEB-01`, `SPEC-WEB-02`, ...
- Specialization Data Science: `SPEC-DS-01`, `SPEC-DS-02`, ...
- Specialization Machine Learning: `SPEC-ML-01`, `SPEC-ML-02`, ...
- Specialization AI Engineering: `SPEC-AI-01`, `SPEC-AI-02`, ...
- Specialization Automation: `SPEC-AUTO-01`, `SPEC-AUTO-02`, ...

## Aturan CHANGELOG Bertingkat

Level log yang dipakai:

1. Sub-rak utama:
- `core/CHANGELOG.md`
- `specializations/CHANGELOG.md`

2. Sub-rak domain specialization:
- `specializations/<domain>/CHANGELOG.md`

3. Buku:
- `core/<book>/CHANGELOG.md`
- `specializations/<domain>/<book>/CHANGELOG.md`

Aturan update:

- perubahan isi buku: update `CHANGELOG.md` buku
- perubahan struktur domain: update `CHANGELOG.md` domain
- perubahan lintas domain/arsitektur: update `core/CHANGELOG.md` atau `specializations/CHANGELOG.md`

## Format Entry CHANGELOG Buku

Setiap `CHANGELOG.md` buku minimal berisi:

- `Book Code`
- `Version`
- `Last Updated`
- daftar entry perubahan dengan format:
  - `Date`
  - `Changed`
  - `Reason`
  - `Impact`

Contoh singkat:

```md
# CHANGELOG

Book Code: CORE-01
Version: v0.1.0
Last Updated: 2026-03-08

## 2026-03-08
- Changed: Menambahkan struktur awal buku.
- Reason: Menetapkan fondasi sebelum penulisan detail.
- Impact: Navigasi materi lebih jelas.
```
