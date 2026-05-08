# Numerical Evidence for Prime-Correlated Structure in High Riemann Zero Blocks

## Preprint
**Zenodo:** https://zenodo.org/records/20077673  
**DOI:** 10.5281/zenodo.20077673

## Хураангуй
Riemann zeta функцийн өндөр height-тэй zero block дээр prime-correlated structure-ийн тоон нотолгоо.

### Үндсэн үр дүн

| Dataset | Zeros | r | p-value |
|---------|-------|---|---------|
| zeros2 | 100,000 | 0.9783 | 3.82×10⁻¹⁸⁶ |
| zeros3 | ~10¹² block | 0.9992 | 2.64×10⁻¹⁵ |
| zeros4 | ~10¹³ block | 0.9421 | 5.0×10⁻⁶ |

- ✅ **Prime-location excess:** 12/12 primes дээр бүх dataset-д
- ✅ **BK amplitude law:** r ≥ 0.94 бүх dataset-д
- ❌ **RH proof:** Энэ биш

## Дүгнэлт

Bogomolny–Keating (1996) таамаглалын amplitude law:

```
A(p) ~ C * (log p)² / p
```

3 өөр dataset дээр r ≥ 0.94 корреляцитайгаар батлагдсан.

**Энэ бол RH-н нотолгоо биш — зөвхөн тоон ажиглалт.**

## Өгөгдөл

Odlyzko zero tables:
- zeros2: http://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros2
- zeros3: http://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros3
- zeros4: http://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros4

## Хэрэглэх заавар

```bash
pip install -r requirements.txt
python analyze.py
```

## Лавлагаа

- Bogomolny & Keating (1996): Random matrix theory and the Riemann zeros
- Montgomery (1973): The pair correlation of zeros of the zeta function
- Odlyzko (1992): The 10²⁰-th zero of the Riemann zeta function
- Hiary & Odlyzko (2012): arXiv:1105.4312

## Лиценз

MIT
