# Bai 4: Mo phong quy trinh Hotfix & Gitflow thuc te

## Muc tieu

Ap dung mo hinh phan nhanh **Gitflow** chuan de xu ly tinh huong hotfix khan cap tren he thong dang chay o moi truong production.

---

## Boi canh tinh huong

| Yeu to | Chi tiet |
|--------|---------|
| **Loi phat hien** | Lo du lieu nhay cam nguoi dung (password, credit card, SSN) - CVE-2026-0001 |
| **Nhanh production** | `main` - dang chay **v1.0.0** on dinh |
| **Nhanh phat trien** | `develop` - co tinh nang WIP (notifications), **khong the deploy ngay** |
| **Giai phap** | Tao nhanh `hotfix/v1.0.1` tach thang tu `main`, va loi, release `v1.0.1` |

---

## Mo hinh phan nhanh Gitflow da su dung

```
main        --- [v1.0.0] --------------------- [MERGE hotfix] --- [v1.0.1 TAG]
                    \                                /
hotfix/v1.0.1        +---- [FIX bao mat] ----------+
                    \                                \
develop              +---- [WIP feature] ------------ [MERGE hotfix]
```

### Nguyen tac Gitflow ap dung:
- `main` -> luon la code production on dinh, chi nhan merge tu `hotfix/` hoac `release/`
- `develop` -> code dang phat trien, tich hop feature branches
- `hotfix/*` -> tach tu `main`, sau khi xong phai merge **ca hai** vao `main` va `develop`

---

## Cac buoc thuc hien

### 1. Khoi tao moi truong

```bash
git init
git add app.py config.py
git commit -m "feat: khoi tao he thong quan ly nguoi dung v1.0.0"
git branch -m master main
git tag -a v1.0.0 -m "Release v1.0.0 - Phien ban production on dinh"
```

### 2. Tao nhanh `develop` voi tinh nang WIP

```bash
git checkout -b develop
# Them notifications.py (WIP - chua hoan thien)
git add notifications.py
git commit -m "feat(WIP): them module thong bao email va push notification [chua hoan thien]"
```

### 3. Tao nhanh `hotfix/v1.0.1` tu `main`

```bash
git checkout main
git checkout -b hotfix/v1.0.1
```

> Bat buoc tach tu `main`, KHONG tu `develop` - vi `develop` co code chua san sang.

### 4. Sua loi bao mat tren nhanh hotfix

**Loi goc (app.py v1.0.0):**
```python
# LOI: Tra ve toan bo du lieu ke ca password, credit card, SSN
return users.get(user_id)
```

**Ban va (app.py v1.0.1):**
```python
# FIX: Chi tra ve cac truong an toan
return {
    "id": user["id"],
    "name": user["name"],
    "email": user["email"]
    # password_hash, credit_card, ssn KHONG duoc tra ve!
}
```

```bash
git add app.py config.py
git commit -m "hotfix: va lo hong bao mat - ngan chan lo du lieu nhay cam nguoi dung (CVE-2026-0001)"
```

### 5. Merge hotfix vao `main` + tao tag release

```bash
git checkout main
git merge hotfix/v1.0.1 --no-ff -m "Merge branch 'hotfix/v1.0.1' into main"
git tag -a v1.0.1 -m "Release Hotfix v1.0.1 - Va lo hong bao mat lo du lieu nguoi dung"
```

### 6. Merge hotfix vao `develop` (dong bo ban va)

```bash
git checkout develop
git merge hotfix/v1.0.1 --no-ff -m "Merge branch 'hotfix/v1.0.1' into develop"
```

> Buoc nay **bat buoc** de tranh "troi loi" - dam bao code tuong lai cung duoc va.

### 7. Don dep nhanh hotfix

```bash
git branch -d hotfix/v1.0.1
```

---

## Ket qua kiem tra

### `git branch -a`
```
* develop
  main
```

### `git tag`
```
v1.0.0
v1.0.1
```

### `git log --graph --oneline --all`
```
*   0b672ef Merge branch 'hotfix/v1.0.1' into develop
|\
* | fdf2ca2 feat(WIP): them module thong bao email va push notification [chua hoan thien]
| | * c190aa1 Merge branch 'hotfix/v1.0.1' into main
| |/|
|/|/
| * 609b22f hotfix: va lo hong bao mat - ngan chan lo du lieu nhay cam nguoi dung (CVE-2026-0001)
|/
* 74db977 feat: khoi tao he thong quan ly nguoi dung v1.0.0
```

---

## So do merge bang ASCII

```
THOI GIAN ---------------------------------------------------------------->

main      (v1.0.0)                              (Merge) [TAG v1.0.1]
           [A]-------------------------------------------[D]
              \                                 /|
               \                               / |
hotfix/v1.0.1   [B]----[FIX CVE-2026-0001]--[C] |
                                                  |
develop   [A]---[WIP notifications]-----------[E]
                                           (Merge hotfix)

A = feat: khoi tao he thong v1.0.0
B = Tach nhanh hotfix/v1.0.1 tu main
C = hotfix: va lo hong bao mat CVE-2026-0001
D = Merge hotfix vao main + TAG v1.0.1
E = Merge hotfix vao develop (dong bo ban va)
```

---

## Tai sao phai dung `--no-ff` khi merge?

| Tuy chon | Ket qua | Khi dung |
|----------|---------|----------|
| `git merge` (fast-forward) | Lich su thang, khong ro nguon goc | Khong nen cho hotfix |
| `git merge --no-ff` | Tao merge commit rieng, giu nguyen lich su nhanh | Dung cho hotfix/release |

Voi `--no-ff`, do thi lich su ro rang: nhanh hotfix ton tai, duoc merge vao ca main lan develop - de audit va rollback.

---

## Ly do phai merge hotfix ve ca `develop`?

Neu **khong** merge hotfix ve `develop`:
- Developer tiep tuc lam viec tren `develop` voi code loi cu
- Khi release v2.0.0, loi bao mat se **tai xuat hien** (regression bug)
- Phai va lai lan nua - ton cong, rui ro cao

Day goi la hien tuong **"loi troi" (bug drift)** - ngan chan bang cach luon merge hotfix ve `develop` ngay sau khi release.

---

## Cau truc file trong repository

```
SS05-Bai04/
|-- app.py            # Module chinh - da va loi CVE-2026-0001
|-- config.py         # Cau hinh he thong (version: 1.0.1 tren main)
|-- notifications.py  # Module WIP - chi co tren nhanh develop
+-- README.md         # Bao cao nay
```
